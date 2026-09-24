"""
Unit tests for encryption utilities.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import pytest

from utils.encryption import (
    decrypt_data,
    derive_key_from_password,
    encrypt_data,
    generate_key,
    get_key_from_env,
)


def test_generate_key_produces_valid_fernet_key():
    key = generate_key()
    assert isinstance(key, bytes)
    assert len(key) == 44


def test_encrypt_and_decrypt_roundtrip():
    key = generate_key()
    plaintext = "UNCLASSIFIED // FOUO - sensitive operational data"

    token = encrypt_data(plaintext, key)
    assert token != plaintext
    assert decrypt_data(token, key) == plaintext


def test_decrypt_with_wrong_key_raises():
    key = generate_key()
    token = encrypt_data("classified payload", key)

    with pytest.raises(ValueError, match="Decryption failed"):
        decrypt_data(token, generate_key())


def test_derive_key_from_password_is_deterministic():
    salt = b"fixed-test-salt-16b"
    key_a = derive_key_from_password("DoD-Framework-Key!", salt)
    key_b = derive_key_from_password("DoD-Framework-Key!", salt)

    assert key_a == key_b
    token = encrypt_data("payload", key_a)
    assert decrypt_data(token, key_b) == "payload"


def test_get_key_from_env(monkeypatch):
    key = generate_key()
    monkeypatch.setenv("ENCRYPTION_KEY", key.decode())

    assert get_key_from_env() == key


def test_get_key_from_env_returns_none_when_unset(monkeypatch):
    monkeypatch.delenv("ENCRYPTION_KEY", raising=False)
    assert get_key_from_env() is None

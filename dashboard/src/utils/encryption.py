"""
Encryption utilities for sensitive data protection.

Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)
"""

import base64
import os
from typing import Optional

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key() -> bytes:
    """Generate a new Fernet encryption key."""
    return Fernet.generate_key()


def get_key_from_env(env_var: str = "ENCRYPTION_KEY") -> Optional[bytes]:
    """Load a Fernet key from an environment variable."""
    value = os.environ.get(env_var)
    if not value:
        return None
    return value.encode()


def derive_key_from_password(password: str, salt: bytes, iterations: int = 480000) -> bytes:
    """Derive a Fernet-compatible key from a password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_data(plaintext: str, key: bytes) -> str:
    """Encrypt a string and return a URL-safe token."""
    return Fernet(key).encrypt(plaintext.encode()).decode()


def decrypt_data(token: str, key: bytes) -> str:
    """Decrypt a token produced by encrypt_data."""
    try:
        return Fernet(key).decrypt(token.encode()).decode()
    except InvalidToken as exc:
        raise ValueError("Decryption failed: invalid key or corrupted data") from exc

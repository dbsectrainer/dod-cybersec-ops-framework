#!/bin/sh

# Wait for Vault to start
sleep 5

# Export Vault address and token (sourced from the container environment,
# which docker-compose populates from .env and requires to be set — see
# docker-compose.yml). Fail closed rather than falling back to a known
# default if this script is ever invoked without that environment set.
export VAULT_ADDR='http://127.0.0.1:8200'
if [ -z "${VAULT_DEV_ROOT_TOKEN_ID}" ]; then
    echo "VAULT_DEV_ROOT_TOKEN_ID is not set; refusing to initialize Vault with a default token." >&2
    exit 1
fi
export VAULT_TOKEN="${VAULT_DEV_ROOT_TOKEN_ID}"

# Enable audit logging
vault audit enable file file_path=/vault/logs/audit.log

# Enable KV secrets engine
vault secrets enable -path=secret kv-v2

# Create sample secrets
vault kv put secret/application/database \
    username="app_user" \
    password="sample_password_123" \
    host="db.example.com" \
    port="5432" \
    database="appdb"

vault kv put secret/application/api \
    key="sample_api_key_xyz" \
    endpoint="https://api.example.com" \
    timeout="30s"

vault kv put secret/application/smtp \
    host="smtp.example.com" \
    port="587" \
    username="notifications@example.com" \
    password="sample_smtp_pass"

# Enable PKI secrets engine
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

# Generate root CA
vault write pki/root/generate/internal \
    common_name="example.com" \
    ttl=87600h

# Configure PKI URLs
vault write pki/config/urls \
    issuing_certificates="http://vault:8200/v1/pki/ca" \
    crl_distribution_points="http://vault:8200/v1/pki/crl"

# Create PKI role
vault write pki/roles/example-dot-com \
    allowed_domains="example.com" \
    allow_subdomains=true \
    max_ttl="72h"

# Create sample policy
vault policy write sample-policy /vault/config/policies/sample_policy.hcl

# Enable userpass auth method for testing
vault auth enable userpass

# Create a test user. Fail closed rather than falling back to a known
# default password if this script is ever invoked without VAULT_TEST_USER_PASSWORD set.
if [ -z "${VAULT_TEST_USER_PASSWORD}" ]; then
    echo "VAULT_TEST_USER_PASSWORD is not set; refusing to create testuser with a default password." >&2
    exit 1
fi
vault write auth/userpass/users/testuser \
    password="${VAULT_TEST_USER_PASSWORD}" \
    policies="sample-policy"

echo "Vault initialization completed successfully"

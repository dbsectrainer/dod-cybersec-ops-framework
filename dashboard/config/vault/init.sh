#!/bin/sh

# Wait for Vault to start
sleep 5

# Export Vault address and token
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='dev-only-token'

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

# Create a test user
vault write auth/userpass/users/testuser \
    password="testpass123" \
    policies="sample-policy"

echo "Vault initialization completed successfully"

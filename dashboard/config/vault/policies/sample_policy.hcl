# Sample policy for application access
path "secret/data/application/*" {
  capabilities = ["read", "list"]
}

# Sample policy for database credentials
path "database/creds/readonly" {
  capabilities = ["read"]
}

# Sample policy for PKI
path "pki/*" {
  capabilities = ["read", "list"]
}

# Allow tokens to look up their own properties
path "auth/token/lookup-self" {
  capabilities = ["read"]
}

# Allow tokens to renew themselves
path "auth/token/renew-self" {
    capabilities = ["update"]
}

# Allow tokens to revoke themselves
path "auth/token/revoke-self" {
    capabilities = ["update"]
}

# Allow checking the status of PKI backends
path "sys/mounts" {
  capabilities = ["read"]
}

# Allow health checks
path "sys/health" {
  capabilities = ["read", "sudo"]
}

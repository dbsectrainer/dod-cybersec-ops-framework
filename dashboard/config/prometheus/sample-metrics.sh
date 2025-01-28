#!/bin/sh

# Function to generate random CPU usage between 0-100
generate_cpu_usage() {
    echo $((RANDOM % 100))
}

# Function to generate random memory usage between 0-16GB (in bytes)
generate_memory_usage() {
    echo $((RANDOM % 16 * 1024 * 1024 * 1024))
}

# Create metrics directory if it doesn't exist
mkdir -p /prometheus/metrics

while true; do
    # Generate metrics
    cat > /prometheus/metrics/sample_metrics.prom << EOF
# HELP node_cpu_seconds_total Seconds the CPUs spent in each mode
# TYPE node_cpu_seconds_total counter
node_cpu_seconds_total{cpu="0",mode="idle"} $(generate_cpu_usage)

# HELP node_memory_MemTotal_bytes Memory information field MemTotal_bytes
# TYPE node_memory_MemTotal_bytes gauge
node_memory_MemTotal_bytes 17179869184

# HELP node_memory_MemFree_bytes Memory information field MemFree_bytes
# TYPE node_memory_MemFree_bytes gauge
node_memory_MemFree_bytes $(generate_memory_usage)

# HELP node_memory_Buffers_bytes Memory information field Buffers_bytes
# TYPE node_memory_Buffers_bytes gauge
node_memory_Buffers_bytes 204800

# HELP node_memory_Cached_bytes Memory information field Cached_bytes
# TYPE node_memory_Cached_bytes gauge
node_memory_Cached_bytes 1024000
EOF

    sleep 5
done

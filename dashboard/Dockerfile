# DoD Cybersecurity Operations Dashboard Dockerfile
# Classification: UNCLASSIFIED // FOR OFFICIAL USE ONLY (FOUO)

# Use Iron Bank's hardened Python image
FROM registry1.dso.mil/ironbank/opensource/python/python39:latest

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    STREAMLIT_SERVER_PORT=8501

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN adduser --system --group appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Set Python path
ENV PYTHONPATH=/app/src

# Create necessary directories with correct permissions
RUN mkdir -p /app/data/metrics /app/data/reports /app/logs && \
    chmod -R 750 /app/data /app/logs

# Security headers and classification banner
ENV STREAMLIT_SERVER_HEADERS='{"X-Frame-Options": "DENY", "X-Content-Type-Options": "nosniff", "X-XSS-Protection": "1; mode=block", "Content-Security-Policy": "default-src '\''self'\''"}'

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Expose port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "src/app.py", \
     "--server.address=0.0.0.0", \
     "--server.port=8501", \
     "--server.baseUrlPath=/dashboard", \
     "--server.enableCORS=false", \
     "--server.enableXsrfProtection=true", \
     "--server.maxUploadSize=5"]

# Security Labels
LABEL org.opencontainers.image.title="DoD Cybersecurity Operations Dashboard" \
      org.opencontainers.image.description="Dashboard for DoD Cybersecurity Operations Framework" \
      org.opencontainers.image.vendor="Department of Defense" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.created="2025-01-27" \
      org.opencontainers.image.documentation="https://github.com/your-repo/dashboard/README.md" \
      org.opencontainers.image.source="https://github.com/your-repo/dashboard" \
      org.opencontainers.image.licenses="DoD-OSA-1.0" \
      mil.dod.classification="UNCLASSIFIED" \
      mil.dod.distribution="FOUO" \
      mil.dod.sensitivity="SENSITIVE"

# ---------- Build stage ----------
FROM python:3.11-slim AS builder

WORKDIR /build

# System deps (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# ---------- Runtime stage ----------
FROM python:3.11-slim

# Create non-root user
RUN useradd --create-home --shell /usr/sbin/nologin appuser

WORKDIR /app

# Copy Python deps
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* \
    && rm -rf /wheels

# Copy application code
COPY . .

# Set ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Production-ready command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

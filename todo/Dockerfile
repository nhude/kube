# syntax=docker/dockerfile:1.7
############################
# Builder: install deps into a venv using pinned requirements
############################
FROM python:3.10-slim AS builder

ENV VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps for building some wheels (keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Create virtualenv
RUN python -m venv "$VIRTUAL_ENV" && pip install --upgrade pip

# Copy only the pinned requirements first for better caching
WORKDIR /app
COPY pyproject.toml /app/pyproject.toml
COPY requirements.lock.txt /app/requirements.lock.txt

# Install runtime deps into the venv (fully pinned)
# Export runtime requirements without editable local project (-e .)
RUN sed '/^-e /d' /app/requirements.lock.txt > /app/requirements.runtime.txt \
  && pip install --no-cache-dir -r /app/requirements.runtime.txt

# Copy app source (kept separate for cache efficiency)
# Bring in package files and the app module
COPY src/todo /app/todo
COPY app.py /app/todo/app.py

############################
# Final: slim runtime, non-root
############################
FROM python:3.10-slim AS runtime

ENV VIRTUAL_ENV=/opt/venv \
    PATH=/opt/venv/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Create non-root user
RUN useradd -u 10001 -ms /bin/bash appuser

# Copy venv and app from builder
COPY --from=builder /opt/venv /opt/venv
WORKDIR /app
COPY src/todo /app/todo
COPY app.py /app/todo/app.py

USER appuser
EXPOSE 8000

# Exec-form CMD with shell to expand ${PORT:-8000}
CMD ["sh", "-c", "uvicorn todo.app:app --host 0.0.0.0 --port ${PORT:-8000}"]

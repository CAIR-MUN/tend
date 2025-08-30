FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set work directory
WORKDIR /app

# Copy uv files
COPY pyproject.toml ./

# Install Python dependencies
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -e ".[dev]"

# Copy project
COPY . .

# Make sure we use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Expose port
EXPOSE 8000

# Default command
CMD ["python", "tend_project/manage.py", "runserver", "0.0.0.0:8000"]
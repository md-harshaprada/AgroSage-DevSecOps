# Use a smaller base image
FROM python:3.8-slim as builder

# Copy only requirements file to install dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Set working directory
WORKDIR /app

# Build the application (if required)

# Final stage, use a lightweight base image
FROM python:3.8-slim

# Copy dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=builder /app /app

# Set working directory
WORKDIR /app

# Expose port for Flask app
EXPOSE 5000

# Command to run on container start
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

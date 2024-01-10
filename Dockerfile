# Base image for Python application
FROM python:3.8.8

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Expose port for Flask app
EXPOSE 5000

# Command to run on container start
CMD ["flask", "run", "--host=0.0.0.0"]  # Start Flask app with external access

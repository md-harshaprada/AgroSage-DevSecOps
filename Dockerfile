# Base image for Python application
FROM python:3.8.8

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn  # Install Gunicorn

# Copy project files
COPY . /app

# Set working directory
WORKDIR /app

# Expose port for Flask app
EXPOSE 5000

# Command to run on container start (using Gunicorn WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"] 
# Assuming your app's entry point is in app.py

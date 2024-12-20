# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app
CMD ["python", "app/app.py"]

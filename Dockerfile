# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /automation

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY recursive.py .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "recursive.py"]

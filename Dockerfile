# Use an official lightweight Python runtime
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . /app/

# Prevent Python from writing .pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port 8000 and start Django
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

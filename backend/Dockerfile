# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Grant execute permission to setup.sh (if needed)
RUN chmod +x setup.sh

# Command to start the Django server when the container starts
CMD ["python manage.py makemigrations && python manafe.py migrate &&",  "python", "manage.py", "runserver", "0.0.0.0:8000"]

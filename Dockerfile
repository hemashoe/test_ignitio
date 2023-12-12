# Using Python image
FROM python:3.10

WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set the entry point to run the Flask app
CMD ["python", "app/main.py"]


FROM python:3.10-slim

WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src folder (app.py, Dockerfile, and other files) into the container's /app directory
COPY . /app/

# Expose the port for the application (assuming FastAPI runs on 8000)
EXPOSE 8000

# Set the PYTHONPATH environment variable so that Python can locate 'src'
ENV PYTHONPATH=/app/src

# Command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

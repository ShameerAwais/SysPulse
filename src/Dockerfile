# Start with a slim Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first to take advantage of Docker layer caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the backend and frontend code into the container
# This step includes both your backend (app.py) and frontend files (index.html, app.js, style.css)
COPY . /app/

# Copy templates and static files into the correct location
COPY syspulse/templates /app/syspulse/templates
COPY syspulse/static /app/syspulse/static

# Expose the port where FastAPI will run (default is 8000)
EXPOSE 8000

# Set the PYTHONPATH environment variable so that Python can find 'src'
ENV PYTHONPATH=/app/src

# Serve the static files from the 'frontend' directory via FastAPI
# This will allow serving HTML, CSS, JS under the '/static' route
RUN mkdir -p /app/src/frontend && cp -r /app/frontend /app/src/

# Command to run the application (uvicorn is the ASGI server for FastAPI)
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

# Use Python 3.10 slim image as the base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the syspulse package (including static and templates)
COPY syspulse /app/syspulse

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "syspulse.server:app", "--host", "0.0.0.0", "--port", "8000"]

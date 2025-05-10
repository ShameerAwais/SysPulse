# Use Python 3.10 slim image as the base
FROM python:3.10-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY syspulse /app/syspulse

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

EXPOSE 8000

CMD ["uvicorn", "syspulse.server:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed for psutil
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your scripts and dashboard
COPY monitor.py .
COPY server.py .
COPY dashboard.html .

# Startup script to run both processes
RUN echo '#!/bin/bash\npython3 monitor.py &\nsleep 2\npython3 server.py' > /app/start.sh && chmod +x /app/start.sh

EXPOSE 8080

CMD ["/app/start.sh"]
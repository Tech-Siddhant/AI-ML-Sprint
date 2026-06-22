# 1. Base OS
FROM python:3.11-slim

# 2. Isolated Workspace
WORKDIR /app

# 3. Cache the Blueprint
COPY requirements.txt .

# 4. Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. The Surgical Payload
COPY projects/ ./projects/

# --- THE FIX: Teleport inside the projects folder before ignition ---
WORKDIR /app/projects

# 6. The Trigger
CMD ["python", "week01_log-aggregator.py"]
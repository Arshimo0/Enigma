# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container to /app
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install Flask (and any other dependencies)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all your code (app.py, logic.py, templates/) into the container
COPY . .

# 6. Tell Docker we are going to use port 5000
EXPOSE 5000

# 7. The command to run your app when the container starts
CMD ["python", "app.py"]
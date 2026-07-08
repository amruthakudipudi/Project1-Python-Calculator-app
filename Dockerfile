FROM  python:3.10.20-slim
WORKDIR /app
COPY . .
CMD ["python", "server.py"]
EXPOSE 5000

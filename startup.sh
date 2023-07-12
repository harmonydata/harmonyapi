java -jar /tmp/tika-server.jar &
uvicorn main:app_fastapi --host 0.0.0.0 --port 8000


run locally:
uvicorn main:app --reload

run from docker:
docker build -t my-fastapi-server .
docker run -p 8000:8000 -e HOST=0.0.0.0 my-fastapi-server
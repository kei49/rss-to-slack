import uvicorn

from src.scripts.main import run

def app():
    run()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, log_level="info") # , reload=True)

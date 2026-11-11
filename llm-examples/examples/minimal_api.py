import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"hello": "世界"}


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()

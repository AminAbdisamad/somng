from fastapi import FastAPI


app = FastAPI(
    title="Somnog", description="Somnog Event management app", version="1.0.0"
)


@app.get("/")
def index() -> None:
    return {"Name": "Somnog"}


def greating(message):
    return "hello" + message




from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello FastAPI!"


@app.get("/property")
def property():
    return "This is a property page"


@app.get("/movies")
def movies():
    return {"movie list": ["Movie_1, Movie_2"]}
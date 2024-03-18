from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello FastAPI!"


@app.get("/property/{id}")
def property(id):
    return f"This is a property page for property {id}"


@app.get("/movies")
def movies():
    return {"movie list": ["Movie_1, Movie_2"]}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello FastAPI!"


@app.get("/property/{id}")
def property(id: int):
    return f"This is a property page for property {id}"


@app.get("/user/admin")
def admin():
    return "This is admin page"


@app.get("/movies")
def movies():
    return {"movie list": ["Movie_1, Movie_2"]}


@app.get("/user/{username}")
def profile(username: str):
    return f"This is a profile page for user: {username}"


@app.get("/products")
def products(id: int = None, price: float = None):
    return f"Product with an id: {id} and price {price}"


@app.get("/profile/{user_id}/comments")
def profile(user_id: int, comment_id: int):
    return (
        f"Profile page for user with user id {user_id} and comment with id {comment_id}"
    )


@app.post("/adduser")
def add_user():
    return "user data"

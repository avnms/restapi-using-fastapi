from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import Set


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Image(BaseModel):
    name: HttpUrl
    url: str


class Product(BaseModel):
    name: str
    price: float = Field(
        title="Price of the item",
        description="This would be the price of the item being added",
        gt=0,
    )
    discount: float
    discounted_price: float
    tags: Set[str] = []
    image: Image


class User(BaseModel):
    name: str
    email: str


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
def add_user(profile: Profile):
    return profile


@app.post("/addproduct/{product_id}")
def add_product(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {
        "product_id": product_id,
        "product": product,
        "category": category,
    }


@app.post("/purchse")
def purchase(user: User, product: Product):
    return {
        "user": user,
        "product": product,
    }

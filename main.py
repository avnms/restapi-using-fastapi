from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set
from uuid import UUID
from datetime import date, time, datetime, timedelta


class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    execute_after: timedelta


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Image(BaseModel):
    name: HttpUrl
    url: str


class Product(BaseModel):
    name: str = Field(example="Phone")
    price: float = Field(
        title="Price of the item",
        description="This would be the price of the item being added",
        gt=0,
    )
    discount: float
    discounted_price: float
    tags: Set[str] = Field(example='["Electronics", "Phone"]')
    images: List[Image]

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "name": "Phone",
    #             "price": 100,
    #             "discount": 10,
    #             "discounted_price": 0,
    #             "tags": ["Electronics", "Computers"],
    #             "images": [
    #                 {
    #                     "name": "Phone image",
    #                     "url": "www.google.com",
    #                 },
    #                 {
    #                     "name": "Phone image side view",
    #                     "url": "www.google.com",
    #                 },
    #             ],
    #         }
    #     }


class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]


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


@app.post("/addoffer")
def add_offer(offer: Offer):
    return offer


@app.post("/addevent")
def add_event(event: Event):
    return event

from typing import Optional, List
from fastapi import FastAPI, Path,Query

from pydantic import BaseModel

app = FastAPI(
    title="Aadhar App",
    description="This is the app for creating And Store the Aadhar details",
    summary="Appaani Said Aadhar app is Good ",
    version="0.0.1",
    contact={
        "name": "LogeshBharathi",
        "url": "https://www.linkedin.com/in/freshbye/",
        "email": "Logeshb889@gmail.com",
    },
    license_info={
        "name": "JarvisLabs.ai",
        "url": "https://cloud.jarvislabs.ai/",
    },
)

users = []


class User(BaseModel):
    name: str
    age: int
    mobile_no: str
    aadhar_no: str
    email: str
    district: str


@app.get("/get_users")
async def get_users():
    return users


@app.post("/post_user")
async def add_user(user: User):
    users.append(user)
    return f"Hello Mr/Ms. {user.name}, your Account is Successfully Created"


@app.get("/getUserById/{age}")
async def get_user_details(age: int = Path(..., description="Enter the User Age to retrieve the user details",gt=2),q:str=Query(None,max_length=3)):
    if age < 0 or age >= len(users):
        return "User not found"
    return {"User":users[age],"query":q}

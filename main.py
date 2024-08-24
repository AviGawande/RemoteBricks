from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from passlib.hash import bcrypt
from bson import ObjectId
import logging

from models import UserRegistration, UserLogin, LinkID
from database import users_collection, ids_collection

app = FastAPI()

# Registration Endpoint
@app.post("/register")
async def register_user(user: UserRegistration):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = bcrypt.hash(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
    }
    users_collection.insert_one(new_user)
    return {"message": "User registered successfully"}

# Login Endpoint
@app.post("/login")
async def login_user(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not bcrypt.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful"}

# Linking ID Endpoint
@app.post("/link_id")
async def link_id(link_data: LinkID):
    db_user = users_collection.find_one({"_id": link_data.user_id})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    linked_id = {"user_id": db_user["_id"], "id_link": link_data.external_id}
    ids_collection.insert_one(linked_id)
    return {"message": "ID linked successfully"}

# Joins Example
@app.get("/user/{user_id}/linked_ids")
async def get_user_with_linked_ids(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    linked_ids = ids_collection.find({"user_id": ObjectId(user_id)})
    return {"user": user, "linked_ids": list(linked_ids)}

# Chain Delete
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    ids_collection.delete_many({"user_id": ObjectId(user_id)})
    return {"message": "User and associated data deleted successfully"}

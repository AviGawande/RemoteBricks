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
        "linked_ids": []  # Placeholder for linked IDs
    }
    result = users_collection.insert_one(new_user)

    # Create an entry in the linked_ids collection for this user
    linked_id_entry = {
        "user_id": result.inserted_id,  # Using the generated ObjectId for the user
        "id_link": "initial_id"  # Replace "initial_id" with the actual ID you want to link
    }
    ids_collection.insert_one(linked_id_entry)

    return {"message": "User registered and linked ID created successfully"}

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
    db_user = users_collection.find_one({"_id": ObjectId(link_data.user_id)})
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Push the ID to the user's linked_ids array (embedding approach)
    users_collection.update_one(
        {"_id": ObjectId(link_data.user_id)},
        {"$push": {"linked_ids": link_data.id_link}}
    )

    # Alternatively, add to a separate collection (original approach)
    linked_id = {"user_id": db_user["_id"], "id_link": link_data.id_link}
    ids_collection.insert_one(linked_id)

    return {"message": "ID linked successfully"}

# Get User with Linked IDs
@app.get("/user/{user_id}/linked_ids")
async def get_user_with_linked_ids(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    linked_ids = ids_collection.find({"user_id": ObjectId(user_id)})

    # Combine linked IDs from both the embedded and separate collection approaches
    combined_linked_ids = user.get("linked_ids", []) + [linked["id_link"] for linked in linked_ids]

    # Convert ObjectId to str for proper JSON serialization
    user['_id'] = str(user['_id'])
    return {"user": user, "linked_ids": combined_linked_ids}

# Chain Delete
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    ids_collection.delete_many({"user_id": ObjectId(user_id)})

    return {"message": "User and associated data deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    except Exception as e:
        logging.error(f"Error starting the server: {e}")

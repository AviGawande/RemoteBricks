# API Documentation

## Overview
This document provides an overview of the available API endpoints. You can find the all the endpoints of  this apis on 
this: https://www.postman.com/abhigawande123/workspace/remote-bricks-apis/collection/36164059-b3c8d355-bfc1-4369-b9d8-7ca14eff4892?action=share&creator=36164059
Each endpoint is designed to perform specific actions related to user management and data handling. Below are descriptions for each endpoint, along with placeholders for related images.

## Endpoints

### 1. Registration API
**Endpoint:** `/register`

**Description:**
This endpoint allows the registration of a new user. It requires the user's details and creates a new account in the system.

**Method:** POST

**Result:**
![Screenshot 2024-08-25 134631](https://github.com/user-attachments/assets/017ac15a-eeb3-4fc2-bfbb-59961ac72bdd)



### 2. Login API
**Endpoint:** `/login`

**Description:**
This endpoint allows users to log in by verifying their credentials (email and password).

**Method:** POST

**Result:**
![Screenshot 2024-08-25 134613](https://github.com/user-attachments/assets/0f4f4bd0-6cf9-4fe9-a409-4dc173342aa8)



### 3. Linking ID API
**Endpoint:** `/link_id`

**Description:**
This endpoint that allows users to link an ID to their account.

**Method:** POST

**Result:**
![Screenshot 2024-08-25 134545](https://github.com/user-attachments/assets/05b98037-a59b-42e9-9018-675a2d8c4511)


### 4. Joins API
**Endpoint:** `/user/{user_id}/linked_ids`

**Description:**
This endpoint allows join data from multiple collections, enabling complex queries that involve multiple data sources.

**Method:** GET

**Result:**
![Screenshot 2024-08-25 134513](https://github.com/user-attachments/assets/cf035636-61ea-4f7c-94cc-6e0450e33248)


### 5. Chain Delete API
**Endpoint:** `/user/{user_id}`

**Description:**
This endpoint allows to delete a user and all associated data across collections, ensuring that all related records are properly removed.

**Method:** DELETE

**Result:**
![Screenshot 2024-08-25 134400](https://github.com/user-attachments/assets/d8a83c56-d39c-49c5-9f27-b28c321b86b0)



# API Documentation

## Overview
This document provides an overview of the available API endpoints. Each endpoint is designed to perform specific actions related to user management and data handling. Below are descriptions for each endpoint, along with placeholders for related images.

## Endpoints

### 1. Registration API
**Endpoint:** `/api/register`

**Description:**
This endpoint allows the registration of a new user. It requires the user's details and creates a new account in the system.

**Method:** POST


### 1. Registration API
**Endpoint:** `/register`

**Description:**
This endpoint allows the registration of a new user. It requires the user's details and creates a new account in the system.

**Method:** POST


### 2. Login API
**Endpoint:** `/login`

**Description:**
This endpoint allows users to log in by verifying their credentials (email and password).

**Method:** POST


### 3. Linking ID API
**Endpoint:** `/link_id`

**Description:**
This endpoint that allows users to link an ID to their account.

**Method:** POST

### 4. Joins API
**Endpoint:** `/user/{user_id}/linked_ids`

**Description:**
This endpoint allows join data from multiple collections, enabling complex queries that involve multiple data sources.

**Method:** GET


### 5. Chain Delete API
**Endpoint:** `/user/{user_id}`

**Description:**
This endpoint allows to delete a user and all associated data across collections, ensuring that all related records are properly removed.

**Method:** DELETE


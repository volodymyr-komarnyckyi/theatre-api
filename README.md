# Theatre Service API Service

Theatre API Service is a Django-based RESTful API for managing plays, performances, actors and more. It provides endpoints for creating, updating, and retrieving thatre-related data, as well as user registration and order management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Endpoints](#endpoints)
- [Presentation](#presentation)

## Introduction

Theatre API Service is designed to streamline the management of theatre-related data and user interactions. Whether you're developing an app for theatre, building a play reservation system, or just exploring Django REST APIs, this project provides a solid foundation.

### Features:
- CRUD operations for performances, plays, actors, genres, theatre halls and orders.
- Add images for plays
- Ticket validation based on cargo and seat availability.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/volodymyr-komarnyckyi/theatre-api
   ```
2. Create .env file and define environmental variables following .env.example:
   ```
   POSTGRES_HOST= your db host
   POSTGRES_DB= name of your db
   POSTGRES_USER= username of your db user
   POSTGRES_PASSWORD= your db password
   SECRET_key=" your django secret key "
   ```
3. Run command:
   ```
   docker-compose up --build
   ```
4. App will be available at: ```127.0.0.1:8000```
5. Login using next credentials:
   ```
   admin@admin.com
   Volodymyr8204
   ```
## Endpoints
   ```
   "theatre" : 
                "http://127.0.0.1:8000/api/theatre/genres/"
                "http://127.0.0.1:8000/api/theatre/actors/"
                "http://127.0.0.1:8000/api/theatre/plays/"
                "http://127.0.0.1:8000/api/theatre/theatre_halls/"
                "http://127.0.0.1:8000/api/theatre/performances/"
                "http://127.0.0.1:8000/api/theatre/reservations/"
   "user" : 
                   "http://127.0.0.1:8000/api/user/register/"
                   "http://127.0.0.1:8000/api/user/me/"
                   "http://127.0.0.1:8000/api/user/token/"
                   "http://127.0.0.1:8000/api/user/token/refresh/"
   "documentation": 
                   "http://127.0.0.1:8000/api/doc/"
                   "http://127.0.0.1:8000/api/swagger/"
                   "http://127.0.0.1:8000/api/redoc/"
   ```

## Schema
![db_schema.png](rest_db.png)

## Presentation
![swagger.png](swagger.png)
![trip_list.png](play_list.png)
![api_root.png](api_root.png)
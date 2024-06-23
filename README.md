# Interview Test task: Python Developer

Develop a web application in Python using FastAPI, which provides an API for working with a collection of memes. The application should consist of two services: a service with a public API with business logic and a service for working with media files using S3-compatible storage (eg, MinIO).

## Running

`docker compose -f "docker-compose.yml" up -d --build`

## About

A Python Fast API memes service.

## Technologies

1. Programing Language: Python
2. Web Framework: FastAPI
3. Database ORM: Turtoise
4. Database: Postgres
5. Storage: AWS S3
6. Standards and libraries: Docker, git, github, Swagger

## Improvements

1. Added proper security. Create auth data models, data classes, rest endpoints. Use JWT.
2. Use AWS instead of an interface

## Instructions

Functionality:

● GET /memes: Get a list of all memes (with pagination).

● GET /memes/{id}: Retrieve a specific meme by its ID.

● POST /memes: Add a new meme (with picture and text).

● PUT /memes/{id}: Update an existing meme.

● DELETE /memes/{id}: Delete a meme.

Requirements:

● Use a relational DBMS to store data.

● Provide error handling and input validation.

● Use Swagger/OpenAPI to document APIs.

● Write at least a few unit tests to test core functionality.

● Write a Readme that explains the functionality of the project and instructions for running it locally for development.

● The project must consist of at least: 1 service with a public API, 1 service with a private API for images, 1 DBMS service, 1 S3-storage service.

● Write docker-compose.yml to run the project.

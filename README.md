# Evreka Case Study Solution
This project is a solution to the Python case study provided by Evreka as part of my application for the Backend Developer position. 

## Project description
This project is designed to handle high-volume device data ingestion, including device location and speed information, via REST API. The data is processed asynchronously and stored in a database for retrieval within specific date ranges or as the latest record for each device.

## Features
- Asynchronous data processing with Celery and RabbitMQ.
- REST API endpoints for data ingestion, range-based retrieval, and fetching the latest record.
- Dockerized for easy deployment and environment setup.
- Unit and integration tests for data validation and API functionality.

## Technologies Used
**Programming Language:** Python

**Backend Framework:** Django + Django REST Framework

**Asynchronous Processing:** Celery with RabbitMQ

**Database:** PostgreSQL

**Containerization:** Docker & Docker Compose

**Testing:** Django’s Test Framework and Django REST Framework’s test client

# Installation

**Clone the Repository**
```
git clone git@github.com:vlyalcin/evreka_case.git
cd evreka_case
```

**Set Up Environment Variables**

Ensure that your environment variables match those used in Docker Compose:
```
POSTGRES_USER=evreka
POSTGRES_PASSWORD=mypass
POSTGRES_DB=evreka_case
RABBITMQ_DEFAULT_USER=evreka
RABBITMQ_DEFAULT_PASS=mypass
```

**Build and Run Docker Containers**

Run the following command to start all services:

```docker-compose up --build```

**Run Migrations:** 

To set up the database schema, run the migrations:

```docker-compose exec web python manage.py migrate```

# API Documentation

**Endpoint 1: Data Ingestion**

- **URL:** `/data/`

- **Method:** `POST`

- **Description:** Adds device data to the queue for asynchronous processing.

- **Payload:**

```
{
  "device_id": "string",
  "timestamp": "ISO 8601 datetime",
  "location": { "lat": float, "lon": float },
  "speed": float
}
```

**Response:**
- `202 ACCEPTED: { "status": "Data has been queued" }`
- `400 BAD REQUEST: { "error": "Validation errors" }`

**Endpoint 2: Data Retrieval by Date Range**

- **URL:** /data/range/
  
- **Method**: GET
  
- **Description**: Retrieves data for a specific device within a specified date range.
  
- **Query Parameters:**
  - `device_id`: The device identifier.
  - `start_date`: Start of the date range in ISO 8601 format.
  - `end_date`: End of the date range in ISO 8601 format.
    
- **Response**:
  - `200 OK`: JSON array of data objects.
  - `400 BAD REQUEST: { "error": "Validation errors" }`


**Endpoint 3: Get Latest Data for a Device**

- **URL**: /data/latest/<device_id>/
  
- **Method**: GET
  
- **Description**: Retrieves the latest data entry for the specified device.
  
- **Response**:
  - `200 OK`: JSON object of the latest data entry.
  - `404 NOT FOUND: { "error": "No data found for the specified device_id" }`
 
# Testing
To run tests, use:

```
docker-compose exec web python manage.py test
```
- **Test Coverage:**
  - Checking if data is processed and stored in the database.
  - API endpoint responses.


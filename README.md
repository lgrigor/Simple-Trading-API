# Trading Platform API

Trading platform with WebSocket support.

## Table of Contents

- [Overview](#overview)
- [Endpoints](#endpoints)
- [WebSocket](#websocket)
- [Usage](#usage)

## Overview

The server is asynchronous, and WebSocket functionality has been implemented. After receiving orders from the client, the server responds with the orderId, orderStatus, stocks, and quantity. The order can have three statuses: PENDING, EXECUTED, and CANCELLED. Initially, the status is set to PENDING, and after a delay of 1-5 seconds, it is changed to EXECUTED. If the client sends a DELETE request, the status is changed to CANCELLED. The application uses a non-relational in-memory database with three initial orders for testing purposes.

## Endpoints

#### Home Page

- **Endpoint**: `GET /`
- **Description**: Returns the home page HTML file.
- **Response**: The HTML content of the home page.

#### Get Orders

- **Endpoint**: `GET /orders`
- **Description**: Retrieves all orders.
- **Response**: A list of orders.

#### Get Order by ID

- **Endpoint**: `GET /orders/{order_id}`
- **Description**: Retrieves a specific order by its ID.
- **Parameters**:
  - `order_id` (integer): The ID of the order.
- **Response**:
  - If the order is found: The details of the order.
  - If the order is not found: JSON response with a 404 status code and an error message.

#### Place a New Order

- **Endpoint**: `POST /orders`
- **Description**: Places a new order.
- **Request Body**: JSON object containing order information, including:
  - `stocks` (string): The stocks of the order.
  - `quantity` (integer): The quantity of the order.
- **Response**:
  - If the order is successfully placed: JSON response with a 201 status code and the details of the created order.
  - If the request is invalid (missing stocks or quantity, redundant properties): JSON response with a 400 status code and an error message.

#### Cancel Order by ID

- **Endpoint**: `DELETE /orders/{order_id}`
- **Description**: Cancels a specific order by its ID.
- **Parameters**:
  - `order_id` (integer): The ID of the order to cancel.
- **Response**:
  - If the order is found and successfully canceled: Response with a 204 status code.
  - If the order is not found: JSON response with a 404 status code and an error message.


## WebSocket

Once an order is requested, a message will be sent via WebSocket with the ID and status "PENDING." After a delay of 1-5 seconds, the status will change to "EXECUTED." Once the status changes, a new message will be sent via WebSocket with the ID and status.

## Usage

Steps required to install and set up the project locally. Include any dependencies and prerequisites that need to be installed.

run locally:
  - Download the latest python
  - `pip install -r requirements.txt`
  - `uvicorn main:app --reload`

run from docker:
  - `docker build -t my-fastapi-server .`
  - `docker run -p 8000:8000 -e HOST=0.0.0.0 my-fastapi-server`

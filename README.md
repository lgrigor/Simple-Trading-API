# Trading Platform API

Trading platform with WebSocket support.

## Table of Contents

- [Overview](#overview)
- [Endpoints](#endpoints)
- [WebSocket](#websocket)
- [Usage](#usage)

## Overview

Brief overview of the project, its purpose, and key features.

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

WebSocket functionality in the project. How it is used, the supported events/messages, and any other relevant details.

## Usage

Steps required to install and set up the project locally. Include any dependencies and prerequisites that need to be installed.

run locally:
  - `pip install -r requirements.txt`
  - `uvicorn main:app --reload`

run from docker:
  - `docker build -t my-fastapi-server .`
  - `docker run -p 8000:8000 -e HOST=0.0.0.0 my-fastapi-server`

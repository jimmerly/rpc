# RPC-Based Customer Payment Checkout System

## Overview

This document details the design and implementation of a Remote Procedure Call (RPC)-based customer payment checkout system. It comprises a server component that simulates backend payment processing services and a client component that simulates user interactions during checkout.

## System Components

### Server Side (`server.py`)

The server acts as the backend, processing payment requests. It listens on a specified host and port for RPC calls from clients, registering methods that can be remotely invoked.

#### Key Features

- **Method Registration**: Enables registering functions for remote invocation.
- **Request Handling**: Manages incoming requests, executing requested methods, and sending responses.
- **Concurrency Support**: Uses threading to handle multiple requests simultaneously for scalability.

#### Implementation Details

- Initializes on `0.0.0.0:8080`.
- Uses `registerMethod` for updating an internal dictionary with method names and functions.
- The `__handle__` method decodes data, executes functions, and sends back results.

### Client Side (`client.py`)

The client simulates the checkout process, making RPC calls to the server to process payments.

#### Key Features

- **Server Connection**: Establishes a connection to the server.
- **Remote Method Invocation**: Calls server-registered methods as if they were local.
- **Graceful Disconnection**: Properly closes socket connections after operations or on errors.

#### Implementation Details

- Connects to `localhost:8080`.
- Dynamic method calls are handled by the `__getattr__` method, sending serialized method names and arguments to the server and deserializing the response.

## Usage

### Running the Server

1. Open `server.py`.
2. Execute the file to start the server. It should display a message indicating it's listening for requests.

### Running the Client

1. Ensure the server is running.
2. Open and run `client.py` to simulate a payment process.

## Testing

1. Start the server by running `server.py`.
2. Run `client.py` in a separate terminal to simulate the checkout and payment process.
3. Verify the client's successful response and the server's log of the request processing.

## Conclusion

This project demonstrates a basic approach to an RPC-based client-server model for payment processing, providing foundational knowledge of RPC mechanisms, server-client interactions, and payment processing in a distributed environment.

## Notes

- This project is for educational purposes. Use robust frameworks like gRPC for production.
- Ensure Python is installed and configured to run the provided samples.

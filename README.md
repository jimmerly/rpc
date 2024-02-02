# RPC-Based Customer Payment Checkout System

## Overview

This document outlines the design and implementation of a Remote Procedure Call (RPC)-based customer payment checkout system, including a server component for backend payment processing services and a client component for user interactions during checkout.

## System Components

### Server Side (`credit_evaluation_service.py`)

The server simulates backend services for credit evaluation during payment processing. It listens on a specified host and port for RPC calls from clients, offering methods for remote invocation related to credit checks.

#### Key Features

- **Credit Report Fetching**: Simulates fetching of credit reports for given user IDs.
- **Method Registration**: Allows for the registration of functions that can be remotely invoked.
- **Request Handling**: Manages incoming requests, executing the requested methods, and sending back responses.
- **Concurrency Support**: Utilizes threading to handle multiple requests simultaneously, enhancing scalability.

#### Implementation Details

- Listens on `0.0.0.0:8081` by default.
- Registers a method `fetch_credit_report` to simulate retrieving user credit reports.
- Handles client requests in the `__handle__` method, decoding data, executing the registered function, and sending results back to the client.

### Client Side (`checkout_service.py`)

The client mimics the checkout process, making RPC calls to the server to retrieve credit reports as part of the payment process.

#### Key Features

- **Server Connection**: Connects to the server to initiate the checkout process.
- **Remote Credit Report Retrieval**: Dynamically invokes server-side methods for credit checks.
- **Graceful Disconnection**: Ensures proper closure of socket connections after operations are completed or in case of errors.

#### Implementation Details

- Connects to `localhost:8081`.
- Implements dynamic method invocation through `__getattr__`, allowing it to request credit report fetching by calling `fetch_credit_report` method as if it were local.

## Usage

### Running the Server

1. Navigate to the `credit_evaluation_service.py` file.
2. Execute the file to start the server, which will then wait for client requests.

### Running the Client

1. Ensure the server is running and listening for requests.
2. Open and execute `checkout_service.py` to simulate the checkout process, including credit report retrieval.

## Testing

1. Start the server by running `credit_evaluation_service.py`.
2. In a separate terminal, run `checkout_service.py` to simulate the checkout process and request a credit report.
3. Observe the successful response on the client side and the processing log on the server side.

## Conclusion

This project showcases a simple yet effective RPC-based approach for simulating a payment checkout system that includes credit evaluation, providing a solid foundation for understanding RPC communication, server-client interaction, and the intricacies of payment processing in distributed systems.

## Notes

- This system is designed for educational and demonstration purposes. For production environments, consider using more robust and secure frameworks like gRPC.
- Ensure you have Python installed on your system to run the provided code samples.

# Cegeka Assignment - CV API Service

This project provides an API service for querying CV data. 

## Table of Contents

1. [Getting Started](#getting-started)
2. [API Endpoints](#api-endpoints)
3. [Command-Line Interface](#command-line-interface)
4. [Running Tests](#running-tests)

## Getting Started

### Prerequisites

- Python 3.11+
- Flask

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/mr-grj/cegeka_assignment.git
    cd cegeka_assignment
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the service:

    ```bash
    make run
    ```

## API Endpoints

### Personal Data

```
GET /api/personal/
```

### Experience

```
GET /api/experience/
```

### Education

```
GET /api/education/
```

## Swagger Documentation

The CV API service also provides interactive documentation using Swagger. Once 
the service is running, you can access the Swagger UI by navigating to `/api/` 
in your web browser. This interface allows you to explore the APIs' 
capabilities, see endpoint descriptions, and even try out API calls directly 
from the browser.


## Command-Line Interface

You can retrieve CV data via command-line as well:

```bash
make cv section=<section_name>
```

Replace `<section_name>` with `personal`, `experience`, `education`, etc.

## Running Tests

To run tests:

```bash
make test
```

## Possible Improvements

There are several areas where enhancements could be made to further improve this project:

- **.env file**: For a production-ready app, sensitive data should be stored in a `.env` 
file.

- **Authentication**: To ensure that only authorized users can access the CV data, 
integrating an authentication mechanism like JWT or OAuth would be beneficial.

- **Logging**: Implementing a logging system would help in monitoring the app, 
troubleshooting issues, and ensuring transparency of operations.

- **Rate Limiting**: To protect the API from potential abuse, implementing rate limiting can 
be a good idea. This will prevent any single user or bot from making too many requests in a 
short period.

- **Data Validation**: Introducing more robust data validation mechanisms can ensure that the 
data in the CV remains consistent and error-free. (e.g. Adding pydantic / marshmellow)

- **Caching**: Implementing caching mechanisms could also reduce load times, especially if the CV 
data grows.

- **Continuous Integration/Continuous Deployment (CI/CD)**: Implementing a CI/CD pipeline would 
ensure that any changes to the codebase are automatically tested and deployed, ensuring the 
robustness and uptime of the service.

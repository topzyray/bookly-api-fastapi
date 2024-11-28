# Bookly API

## Overview

Bookly API is a FastAPI-based application that provides authentication and authorization features. It enables users to perform CRUD operations on books.

## Technologies

- **Programming Language:** Python
- **Framework:** FastAPI
- **Database:** Neon (Serverless PostgreSQL)

## Features

- User authentication and authorization
- Perform CRUD operations on books (Create, Read, Update, Delete)

## Installation

Follow these steps to set up and run the project locally:

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.7+
- Git
- FastAPI (will be installed in the next steps)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/topzyray/bookly-api-fastapi.git
   ```

2. **Navigage to the project directory:**

   ```bash
   cd bookly-api-fastapi
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment:**

- Windows (PowerShell):

  ```bash
  .venv\Scripts\Activate.ps1
  ```

- Windows (Bash):

  ```bash
  source .venv/Scripts/Activate
  ```

- Linux/MacOS (Bash):
  ```bash
  source .venv/bin/Activate
  ```

5. **Verify Virtual Environment Activation:**

- Windows PowerShell:

  ```bash
  Get-Command python
  ```

- Linux/MacOS/Windows Bash:
  ```bash
    which python
  ```

6. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

7. **Start the Application:**

   - Development Mode:

   ```bash
   fastapi dev src
   ```

   - Production Mode:

   ```bash
   fastapi run src
   ```

8. **Test the API:**

   You can test the API through the following interfaces:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Postman, Thunder Client, or any API testing tool.

9. **Deactivate the Virtual Environment:**

   Once you're done testing, deactivate the virtual environment with:

   ```
   deactivate
   ```

### Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

### License

Pending

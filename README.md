# Trellis Backend

## Setup
1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Documentation

The API documentation is available at `/swagger/` endpoint. You can access it by navigating to:
```
http://127.0.0.1:8000/swagger/
```

## Endpoints

### Convert Number to English

- **GET /api/num_to_english/**

    Query Parameters:
    - `number` (integer): The number to be converted to English words.

    Responses:
    - `200 OK`: Number converted successfully.
    - `400 Bad Request`: Invalid number format or number is too large to process.

- **POST /api/num_to_english/**

    Request Body:
    ```json
    {
        "number": <integer>
    }
    ```

    Responses:
    - `200 OK`: Number converted successfully.
    - `400 Bad Request`: Invalid number format or number is too large to process.
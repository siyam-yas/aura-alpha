# Aura - Meme API

## Description

**Aura** is a Flask-based API that allows users to upload and retrieve random memes. Users can upload memes with a title and image (via URL or file upload). The API includes token-based authentication for secure access, ensuring that only authorized users can upload and retrieve memes.

## Features

- **Upload Memes**: Upload memes using a title and image URL or file.
- **Random Meme**: Retrieve a random meme from the collection.
- **Token-Based Authentication**: Secure API access using tokens.
- **Token Generation**: Easily generate tokens to access the API.

## Endpoints

### 1. Generate Token

**Endpoint**: `/generate_token`  
**Method**: `GET`  
**Description**: Generates a new token for accessing the API.

**Response**:
```json
{
    "token": "your-generated-token"
}
```

### 2. Upload Meme

**Endpoint**: `/api/upload?token=YOUR_TOKEN`  
**Method**: `POST`  
**Description**: Upload a meme by providing a title and an image (via URL or file).

**Form Data**:
- `title`: The title of the meme.
- `img`: The meme image URL or file.

**Example**:
```bash
curl -X POST -F 'title=Funny Meme' -F 'img=https://example.com/meme.png' "http://localhost:5000/api/upload?token=YOUR_TOKEN"
```

### 3. Get Random Meme

**Endpoint**: `/api/meme?token=YOUR_TOKEN`  
**Method**: `GET`  
**Description**: Retrieves a random meme in JSON format.

**Response**:
```json
{
    "title": "Funny Meme",
    "img": "https://example.com/meme.png"
}
```

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/siyam-yas/aura.git
    ```

2. Navigate to the project directory:
    ```bash
    cd aura-meme-api
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate # For Linux/Mac
    venv\Scripts\activate # For Windows
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask app:
    ```bash
    python api.py
    ```

6. Access the app at `http://localhost:5000`.

## Technologies Used

- Flask
- Python
- JSON for data storage

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
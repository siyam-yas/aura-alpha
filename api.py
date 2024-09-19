import os
import json
import random
import uuid
from flask import Flask, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

MEME_DB = 'memes.json'
TOKEN_DB = 'tokens.json'


# Initialize meme storage
def load_memes():
    if os.path.exists(MEME_DB):
        with open(MEME_DB, 'r') as f:
            return json.load(f)
    return []


def save_memes(memes):
    with open(MEME_DB, 'w') as f:
        json.dump(memes, f, indent=4)


# Initialize token storage
def load_tokens():
    if os.path.exists(TOKEN_DB):
        with open(TOKEN_DB, 'r') as f:
            return json.load(f)
    return []


def save_tokens(tokens):
    with open(TOKEN_DB, 'w') as f:
        json.dump(tokens, f, indent=4)


# Token verification
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        tokens = load_tokens()
        if token not in tokens:
            return jsonify({'error': 'Invalid or missing token'}), 403
        return f(*args, **kwargs)
    return decorated_function


# Endpoint to generate a new token
@app.route('/generate_token', methods=['GET'], endpoint="generate_token")
def generate_token():
    new_token = str(uuid.uuid4())
    tokens = load_tokens()
    tokens.append(new_token)
    save_tokens(tokens)
    return jsonify({'token': new_token})


# Meme upload endpoint (supports image link or file upload)
@app.route('/api/upload', methods=['POST'], endpoint="upload_meme")
@token_required
def upload_meme():
    title = request.form.get('title')
    img = request.form.get('img')

    if 'file' in request.files:
        img_file = request.files['file']
        img_file.save(os.path.join('uploads', img_file.filename))
        img = f'uploads/{img_file.filename}'

    if not title or not img:
        return jsonify({'error': 'Both title and image are required'}), 400

    meme = {'title': title, 'image': img}
    memes = load_memes()
    memes.append(meme)
    save_memes(memes)

    return jsonify({'message': 'Meme uploaded successfully!', 'meme': meme})


# Fetch a random meme
@app.route('/api/meme', methods=['GET'], endpoint="get_random_meme")
@token_required
def get_random_meme():
    memes = load_memes()
    if not memes:
        return jsonify({'error': 'No memes available'}), 404

    random_meme = random.choice(memes)
    return jsonify(random_meme)


# Initialize empty JSON files if they don't exist
if not os.path.exists(MEME_DB):
    save_memes([])

if not os.path.exists(TOKEN_DB):
    save_tokens([])

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
# Version : 0.0.1 (Alpha)
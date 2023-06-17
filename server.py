from flask import Flask, request, jsonify
import random
import string
import boto3

app = Flask(__name__)

# Configure AWS SDK with your AWS credentials
s3 = boto3.client(
    's3',
    aws_access_key_id='xxxxxxxxxxx',
    aws_secret_access_key='xxxxxxxxxxx',
    region_name='us-east-1'  # Replace with your desired AWS region
)

# GET /api/health endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

# POST /api/upload-random endpoint
@app.route('/api/upload-random', methods=['POST'])
def upload_random():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    random_filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    s3.upload_fileobj(file, 'opercredit-bucket', random_filename)  # Replace with your S3 bucket name

    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(port=4545)

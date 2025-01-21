from config import app, ALLOWED_EXTENSIONS
from flask import jsonify, request

import os
from PIL import Image
from rembg import remove

UPLOAD_FOLDER = os.path.join(os.getcwd(), "../backend", "uploads")
PROCESSED_FOLDER = os.path.join(os.getcwd(), "../backend", "processed")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_images():
    # req_files = ['front', 'left', 'right', 'back']
    req_files = ['front']
    uploaded_files = {}
    processed_files = {}

    for file_key in req_files:
        file = request.files.get(file_key)
        if not file or not allowed_file(file.filename):
            return jsonify({'error': f'Invalid or missing files: {file_key}'}), 400
        
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        uploaded_files[file_key] = file_path

    # preprocess uploaded images here
    for file_key, file_path in uploaded_files.items():
        try:
            processed_path = preprocess_image(file_path)
            processed_files[file_key] = processed_path
        except Exception as e:
            return jsonify({'error':f'Failed to process {file_key}: {str(e)}'}), 500
        
    return jsonify({
        'message':'Files uploaded and processed successfully.',
        'processed_files': processed_files
    }), 200

def resize_img(input_path, output_path, target_width=512):
    with Image.open(input_path) as img:
        aspect_ratio = img.height / img.width
        target_height = int(target_width * aspect_ratio)

        # resize image here
        img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        img_resized.save(output_path)
        return output_path

def preprocess_image(file_path):
    # resize and remove bg from image
    processed_path = file_path.replace('uploads', 'processed')

    with Image.open(file_path) as img:
        resize_img(file_path, processed_path, target_width=512)

        with open(processed_path, 'rb') as f:
            img_data = f.read()
        res = remove(img_data)
        with open(processed_path, 'wb') as f:
            f.write(res)
    
    return processed_path

@app.route('/server-test', methods=['POST'])
def server_test():
    return jsonify({'message':'Serveр OK'})

if __name__ == "__main__":
    app.run(debug=True)
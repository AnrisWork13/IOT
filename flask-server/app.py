# Flask server to receive images (Optional)
from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    filename = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(path)
    return "Image saved", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)


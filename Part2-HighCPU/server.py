from unittest import expectedFailure
from flask import Flask, request, send_from_directory
from PIL import Image
import os, uuid, json, time

app = Flask(__name__)
UPLOAD_DIR = '/home/tshoot/images/'

def encode_image(path, fname):
    while True:
        try:
            image = Image.open(os.path.join(path, fname))
            break
        except Exception as e:
            raise e
    if os.path.exists("./test.jpg"):
        os.remove(os.path.join(path, "./test.jpg"))
    image.resize((200,200))
    image.save(os.path.join(path, "./test.jpg"), dpi=(200,200))
    image.close()

@app.route('/UploadImage', methods = ['POST'])
def upload_image():
    
    if len(os.listdir(UPLOAD_DIR)) >= 10:
        for fname in os.listdir(UPLOAD_DIR):
            os.remove(UPLOAD_DIR + fname)

    file = request.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid.uuid4()) + extension
    file.save(os.path.join(UPLOAD_DIR, f_name))
    file.close()
    return json.dumps({'filename':f_name})


@app.route('/UploadAndEncode', methods = ['POST'])
def upload_and_encode():
    file = request.files['file']
    extension = os.path.splitext(file.filename)[1]
    f_name = str(uuid.uuid4()) + extension
    f_path = os.path.join(UPLOAD_DIR, f_name)
    file.save(f_path)
    file.close()
    encode_image(UPLOAD_DIR, f_name)
    os.remove(os.path.join(UPLOAD_DIR, f_name))
    os.remove(os.path.join(UPLOAD_DIR, "test.jpg"))
    return "Encoding Done"



app.run()

        
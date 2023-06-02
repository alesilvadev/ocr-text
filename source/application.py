from flask import Flask, request, jsonify
import easyocr
import io
from PIL import Image
import numpy as np
application = app = Flask(__name__)

reader = easyocr.Reader(['en']) # especifica el lenguaje aquí

@app.route('/', methods=['GET'])
def home():
    return {"status": "OK"}
    


@app.route('/ocr', methods=['POST'])
def ocr():
    print(request.files)
    if 'image' not in request.files:
        return 'No se proporcionó imagen', 400
    
    img_bytes = request.files['image'].read()
    img = Image.open(io.BytesIO(img_bytes))
    results = reader.readtext(np.array(img))
    results = [[str(item[0]), item[1], item[2]] for item in results]
    return {"data": results}
    

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
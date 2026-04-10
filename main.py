from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import io
from PIL import Image
import base64
import matplotlib.pyplot as plt
from Helpers import *

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    images = []
    sharpness_values = []
    for file in request.files.getlist("file[]"):
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filestr = file.read()
            npimg = np.frombuffer(filestr, np.uint8)
            image = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
            image = Helpers.resize(image, height=500)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            result = "Not Blurry" if fm >= 100 else "Blurry"
            sharpness_value = "{:.0f}".format(fm)
            message = [result, sharpness_value]
            sharpness_values.append(fm)

            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            file_object = io.BytesIO()
            img = Image.fromarray(Helpers.resize(img, width=500))
            img.save(file_object, 'PNG')
            base64img = "data:image/png;base64," + base64.b64encode(file_object.getvalue()).decode('ascii')
            images.append([message, base64img])

    # Generate the sharpness values graph
    plt.figure()
    plt.plot(sharpness_values, marker='o')
    plt.title('Sharpness Values of Uploaded Images')
    plt.xlabel('Image Index')
    plt.ylabel('Sharpness Value')
    plt.grid(True)
    graph_object = io.BytesIO()
    plt.savefig(graph_object, format='PNG')
    graph_object.seek(0)
    graph_base64 = "data:image/png;base64," + base64.b64encode(graph_object.getvalue()).decode('ascii')

    return render_template('upload.html', images=images, graph_base64=graph_base64)

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, port=8000) 

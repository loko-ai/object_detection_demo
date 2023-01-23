from flask import Flask, request, jsonify
from flask_cors import CORS
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions
import cv2
import numpy as np

app = Flask("", static_url_path="/web", static_folder="/frontend/dist")
comp = Component("faces")
save_extensions([comp])

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


@app.route("/", methods=["POST"])
@extract_value_args(_request=request, file=True)
def detect(file, args):
    image = np.asarray(bytearray(file.read()), dtype="uint8")

    # use imdecode function
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if faces != ():
        faces = faces.tolist()
    else:
        faces = []
    return jsonify(faces)


CORS(app)
if __name__ == "__main__":
    app.run("0.0.0.0", 8080)

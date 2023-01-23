from io import BytesIO

from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, Input, Arg, save_extensions
from sanic import Sanic, json as sjson
import PIL
import torch
from sanic_cors import CORS
import yolov7
import numpy as np
import pdb
# torch.multiprocessing.set_start_method('spawn')

app = Sanic("yolo")
app.static("/web", "/frontend/dist")
CORS(app)

model = yolov7.load('../resources/yolov7.pt', trace =  False)
# model.share_memory()
# or load custom model
# model = yolov5.load('train/best.pt')
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # maximum number of detections per image
comp = Component("Object Detector", inputs=[Input(id="image")], args=[Arg(name="keep", value='all',
description="Objects to be detected. Existing labels are: 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'. Comma separated")], icon="RiDoorOpenLine")

save_extensions([comp])


@app.post("/")
@extract_value_args(file=True)
def extract(file, args):
    file = file[0]
    image = PIL.Image.open(BytesIO(file.body))
    labels = args.get('keep', 'all')
    labels = [l.strip().lower() for l in labels.split(',')] if labels else []
    results = model(image)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    ret = []
    for category, score, box in zip(categories, scores, boxes):
        temp = dict(label=results.names[int(category)], score=float(score), bbox=box.tolist())
        print(temp)
        if labels==['all'] or temp['label'] in labels:
            ret.append(temp)
    return sjson(ret)


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, single_process=True)
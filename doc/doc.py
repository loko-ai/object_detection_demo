object_detection_doc = '''### Description
The Object Detection component relies on Yolo-v7 to detect objects from images.

### Configuration

**keep** parameter sets which objects you want to detect. The available categories are:
```
'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'.
``` 
If you leave this argument to "all", which is its default value, all the available categories will be detected.

### Input

The component accepts a single image in input.

### Output

Object Detection returns as output all the detected objects:

```
{"label":"person","score":0.8791136741638184,"bbox":[4.884635925292969,377.1213073730469,47.26206970214844,424.5968933105469]}
```

'''
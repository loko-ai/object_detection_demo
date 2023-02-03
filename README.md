<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Object Detection Demo</h1><br></html>

The object detection demo relies on Yolo-v7 to detect objects from images. 
A custom extension named "Object Detector" accepts a single image in input and returns as output all 
the detected objects:
```
{"label":"person","score":0.8791136741638184,"bbox":[4.884635925292969,377.1213073730469,47.26206970214844,424.5968933105469]}
```
Within the component, you can set which objects you want to detect, using the `keep` argument. Here you can find the 
list of all the model's categories. If you leave this argument to `all`, which is its default value, all the available
categories will be detected.

You can directly use the component in your flow, using a FileReader:
<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/216632040-d9c186d3-dddb-4c98-a731-c5446fea16df.png" width="80%" />
</p>


Otherwise, you can visualize the bounding boxes using the custom GUI, clicking on "Open Object detection":

<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/216580421-ead52db4-4aa1-4ef6-82ad-8d19c0467331.png" width="80%" />
</p>



Here you can drag and drop your images and visualize the results. This GUI is connected to the second flow of the 
project:
<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/216632886-b0279772-9458-4284-81b6-d4f82dd09763.png" width="80%" />
</p>

In this case you can configure the "Object Detector" component and expose a service named "detect". You can find the
complete url into the Route component (click on the copy button in the path parameter). This url is used by the GUI to 
show the results. 


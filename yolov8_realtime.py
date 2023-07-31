from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import SegmentationPredictor
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
# import cv2
model = YOLO("model/yolov8n-seg.pt")
# # model.predict("",show=True,conf=0.5)
model.predict(0,show=True,conf=0.4)


#from ultralytics import YOLO
#import cv2

#model = YOLO("box_seg.pt")

#model.predict("download.jpeg",show=True,save=True)

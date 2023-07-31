from ultralytics import YOLO


model = YOLO("model/yolov8n-seg.pt")

# realtime camera
model.predict(0,show=True,conf=0.4)
# picture
model.predict("download.jpeg",show=True,save=True)

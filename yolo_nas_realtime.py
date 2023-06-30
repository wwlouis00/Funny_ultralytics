from ultralytics import NAS
model = NAS('yolo_nas_s.pt')
model.predict(0,show=True)

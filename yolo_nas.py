from ultralytics import NAS
model = NAS('yolo_nas_s.pt')
model.predict("/home/wwlouis/project/SAM_demo/smart/05_10_19_01_16.mp4",show=True)



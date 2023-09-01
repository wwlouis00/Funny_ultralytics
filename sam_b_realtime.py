from ultralytics import SAM
model = SAM("sam_b.pt")
model.predict("images/jean.jpeg",show=True)

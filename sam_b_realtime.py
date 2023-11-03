from ultralytics import SAM
model = SAM("sam_b.pt")

# camera
model.predict("0",show=True)

# picture
model.predict("your image",show=True)

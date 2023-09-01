from ultralytics.vit import SAM
model = SAM("sam_b.pt")
model.predict(0,show=True)

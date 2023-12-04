from ultralytics.vit import SAM
model = SAM("sam_b.pt")
model.predict("img/test.jpg",show=True)

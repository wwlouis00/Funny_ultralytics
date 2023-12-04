from ultralytics import SAM
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = SAM("sam_b.pt")
# camera
model.predict("0",show=True)

# picture
#model.predict("your image",show=True)

# 使用 Python 與 Ultralytics

[Ultralytics](https://www.ultralytics.com/) 是一個開源的深度學習研究框架，旨在提供易於使用的工具，協助開發者進行目標檢測、圖像分類和語意分割等任務。這裡提供了一個簡單的介紹和使用 Ultralytics 的方法：

## 安裝 Ultralytics

首先，你需要使用 pip 安裝 Ultralytics 模組。打開終端機並執行以下命令：

```
pip install -U ultralytics
```

## 使用目標檢測模型

Ultralytics 提供了一個名為 [YOLOv5](https://github.com/ultralytics/yolov5) 的目標檢測模型。以下是一個簡單的範例，展示了如何使用 YOLOv5 模型進行目標檢測：

```python
import torch
from PIL import Image
from pathlib import Path
from matplotlib import pyplot as plt
from IPython.display import display

# 匯入目標檢測模型
from yolov5 import YOLOv5

# 初始化模型
model = YOLOv5()

# 載入圖像
image_path = Path("path/to/your/image.jpg")
image = Image.open(image_path)

# 執行目標檢測
results = model(image)

# 取得預測結果
predictions = results.pandas().xyxy[0]

# 顯示圖像和預測框
plt.imshow(image)
plt.axis('off')

# 繪製預測框
for _, prediction in predictions.iterrows():
    xmin, ymin, xmax, ymax = prediction[["xmin", "ymin", "xmax", "ymax"]]
    plt.rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, color="red")
    plt.text(xmin, ymin, prediction["name"], color="red")

# 顯示圖像和預測結果
plt.show()
```

這個範例示範了使用 YOLOv5 模型進行目標檢測的基本步驟，包括初始化模型、載入圖像、執行目標檢測，並將預測結果顯示在圖像上。

透過 Ultralytics 的工具，開發者可以更方便地進行目標檢測任務，並根據需要進行模型調整和結果視覺化。

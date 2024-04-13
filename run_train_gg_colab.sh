#!/bin/bash

# Download model
wget -P /content/yolov9/weights https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt

# Di chuyển vào thư mục data/data_tiktok_capcha
pip install -r requirements.txt

# Di chuyển vào thư mục data/data_tiktok_capcha
cd /content/yolov9/data/data_tiktok_capcha

# Giải nén file capcha.zip
unzip tiktok.v7i.yolov9.zip

# Di chuyển trở lại thư mục chính
cd /content/yolov9

# Chạy lệnh Python
python train_dual.py --workers 8 --device 0 --batch 4 --data /content/yolov9/data/data_tiktok_capcha/data.yaml --img 640 --cfg /content/yolov9/models/detect/yolov9-e-custom.yaml --weights /content/drive/MyDrive/yolov9/yolov9-e.pt --name yolov9-c --hyp /content/yolov9/data/hyps/hyp.scratch-high.yaml --min-items 0 --epochs 50 --close-mosaic 15

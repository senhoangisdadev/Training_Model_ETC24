import os
import shutil
from xmlrpc.client import ResponseError

from google.colab import drive
from minio import Minio

# Sử dụng hàm
# minio_host = 'localhost:9001'
minio_host = '4f8d-2405-4802-b2b7-d380-102-22ce-2fea-9dc8.ngrok-free.app'
minio_access_key = 'root'
minio_secret_key = 'password'
# model_path = 'models/model-e.pt'
# /content/yolov9/runs/train/{yolov9-c3}/weights/best.pt

# Tạo headers tùy chỉnh với host header

# Khởi tạo client Minio
minio_client = Minio(minio_host,
                         access_key=minio_access_key,
                         secret_key=minio_secret_key,
                         secure=True
                         )  # Trong môi trường thực tế, bạn có thể sử dụng secure=True cho kết nối an toàn


def put_model_to_minio(model_path ,bucket_name='yolov9', object_name='models/model-e.pt'):
    # Khởi tạo client Minio
    # minio_client = Minio(minio_host,
    #                      access_key=minio_access_key,
    #                      secret_key=minio_secret_key,
    #                      secure=False
    #                      )  # Trong môi trường thực tế, bạn có thể sử dụng secure=True cho kết nối an toàn
    

    try:
        # Kiểm tra xem bucket có tồn tại không, nếu không, tạo mới
        found = minio_client.bucket_exists(bucket_name)
        if not found:
            minio_client.make_bucket(bucket_name)

        # Đưa file model lên Minio
        minio_client.fput_object(bucket_name, object_name, model_path)

        print(f"Model đã được đưa lên Minio thành công vào đối tượng {object_name}")

    except ResponseError as err:
        print(err)


# file = os.path.abspath('test.pt')
# put_model_to_minio(file)


def save_to_drive(file_path, drive_path):
    """
    Lưu file từ Colab vào Google Drive.

    Parameters:
        file_path (str): Đường dẫn đến file cần lưu.
        drive_path (str): Đường dẫn trên Google Drive để lưu file.

    Returns:
        None
    """
    # Mount Google Drive
    # drive.mount('/content/drive')

    # Tạo thư mục nếu chưa tồn tại trên Google Drive
    drive_folder = os.path.join('/content/drive/MyDrive', drive_path)
    if not os.path.exists(drive_folder):
        os.makedirs(drive_folder)

    # Lưu file vào Google Drive
    shutil.copy(file_path, drive_folder)

    # Báo thành công
    print(f"File đã được lưu vào {drive_folder}/{os.path.basename(file_path)}")
    
# from utils.minio_helper import put_model_to_minio, save_to_drive

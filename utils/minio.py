from xmlrpc.client import ResponseError

from minio import Minio

# Sử dụng hàm
minio_host = 'localhost:9001'
minio_access_key = 'root'
minio_secret_key = 'password'
model_path = 'models/model-e.pt'

# Khởi tạo client Minio
minio_client = Minio(minio_host,
                         access_key=minio_access_key,
                         secret_key=minio_secret_key,
                         secure=False
                         )  # Trong môi trường thực tế, bạn có thể sử dụng secure=True cho kết nối an toàn


def put_model_to_minio(bucket_name='yolov9', object_name='models/model-e.pt'):
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



put_model_to_minio()
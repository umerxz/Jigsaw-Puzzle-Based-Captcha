import os,base64,io
import numpy as np
from PIL import Image
from io import BytesIO

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CAPTCHA.settings')
django.setup()

from app.models import Images,Partition

def length(a):
    return len(a)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def base64_to_image(encoded_string):
    return io.BytesIO(base64.b64decode(encoded_string))

def partition_to_base64(image_piece):
    img_bytes=BytesIO()
    image_piece.save(img_bytes,format="PNG")
    return base64.b64encode(img_bytes.getvalue()).decode("utf-8")

def store_partitions(sliced_img,position,img_obj):
    part=Partition.objects.create()
    part.partition_id=img_obj
    part.position=position
    part.sliced_img=partition_to_base64(sliced_img) 
    part.save()


if __name__ == "__main__":

    image_path="./Gravity Falls/correct"
    image_list=os.listdir(image_path)
    image_list.sort()
    image_list.sort(key=length)

    for image in image_list:
        temp=image_path+'/'+image
        img_obj=Images.objects.create()
        encoded_string=image_to_base64(temp)
        img_obj.img=encoded_string
        img_obj.save()
        img = Image.open(base64_to_image(str(img_obj.img)))
        # img.show()

        arr=np.array(img)   #converting image to array
        (x,y,*values)=arr.shape    #unpacking returned tuple 

        step_x=x//3
        step_y=y//3
        position=1

        for i in range(0,3):
            for j in range(3):
                x1=j*step_x
                x2=step_x+x1
                y1=i*step_y
                y2=step_y+y1
                img_piece=Image.fromarray(arr[y1:y2,x1:x2]) #cropped image from given dimensions
                store_partitions(img_piece,position,img_obj)
                position=position+1

# os.environ['KAGGLE_USERNAME'] = "umerxz"
# os.environ['KAGGLE_KEY'] = "2e56830d90bb463d437452ebcbf4820c"

# from kaggle.api.kaggle_api_extended import KaggleApi

# def download_dataset():
#     api = KaggleApi()
#     api.authenticate()
#     api.dataset_download_files('serhiibiruk/jigsaw-puzzle', unzip=True)
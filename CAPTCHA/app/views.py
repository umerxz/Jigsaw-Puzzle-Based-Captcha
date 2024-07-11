from django.shortcuts import render
from django.http import HttpResponse
from app.models import Images,Partition
import random,io,base64
# Create your views here.

def puzzle(request):
    random_number=random.randrange(1,110)
    pieces=list(Partition.objects.filter(partition_id=random_number))
    org_img=Images.objects.get(pk=pieces[0].partition_id.id)
    random.shuffle(pieces)

    my_dict={'org_img':org_img,'pieces':pieces}

    return render(request,'captcha.html',context=my_dict)


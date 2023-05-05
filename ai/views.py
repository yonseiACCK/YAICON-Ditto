from django.shortcuts import render, HttpResponseRedirect
from .apps import AiConfig
from PIL import Image
from .utils import *
import uuid
# Create your views here.
import sys
import os


def home(request):
    print(sys.path)
    if request.method == "POST":
        
        # generate code per inference
        col = uuid.uuid4()
        
        # inference
        img = request.FILES["image"]
        img = convert_uploaded_file_to_numpy(img)
        prompt = request.POST["prompt"]
        
        result_image = AiConfig.model.inference(img, prompt)
        
        
        # save images(num_samples=1 indexing)
        sketch_input = Image.fromarray(result_image[0])
        result_image = Image.fromarray(result_image[1])
        
        sketch_input.save(f"data/{col}_sketch.jpg")
        result_image.save(f"data/{col}.jpg")
        return HttpResponseRedirect(f"/{col}")
    return render(request, "ai/home.html")



def show_result(request, image_uuid):
    context = {"uuid": image_uuid}
    return render(request, "ai/result.html", context)
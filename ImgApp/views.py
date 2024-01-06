from django.shortcuts import render, redirect
from . models import MultipleImgModel

def home(request):
    img_data = []
    if request.method == 'POST':
        files = request.FILES.getlist('documents')
        img_data = [MultipleImgModel(file = file) for file in files]
        MultipleImgModel.objects.bulk_create(img_data)
    return render(request, 'home.html', {'images': img_data})

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    if request.method == "POST":
        upload = request.FILES['my_uploaded_file']
        print(upload.type)
        print(upload)

    return render(request, "index.html",{})
    # return HttpResponse("Please upload a file!")

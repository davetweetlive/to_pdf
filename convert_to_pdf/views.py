from django.shortcuts import render
# from django.http import HttpResponse
import pdfkit
import filetype
# Create your views here.

def index(request):
    if request.method == "POST":
        upload = request.FILES['my_uploaded_file']
        kind = filetype.guess(upload)

        # Getting the name of output file
        output_file = str(upload).split(".")[0] + ".pdf"
        pdfkit.from_file(upload,output_file)
        print(upload)
        print(kind)
        print(output_file)

    return render(request, "index.html",{})
    # return HttpResponse("Please upload a file!")

from django.shortcuts import render
from PIL import Image
# from django.http import HttpResponse
import pdfkit
import filetype
import img2pdf
# Create your views here.

def index(request):
    show_download_link = False

    if request.method == "POST":
        upload = request.FILES['my_uploaded_file']
        kind = filetype.guess(upload)

        # getting the filetype
        type_of_the_input_file = kind.mime.split("/")[0]
        # Getting the name of output file
        output_file = str(upload).split(".")[0] + ".pdf"


        if type_of_the_input_file == "image":
            file_conv = from_image_to_pdf(upload,output_file)
            file = open("file.pdf", "wb")

        if type_of_the_input_file in ["doc", "docx"]:
            pass

    return render(request, "index.html",{})
    # return HttpResponse("Please upload a file!")


def from_image_to_pdf(img_path, pdf_file_name):
    image = Image.open(img_path)
    print(image)
    pdf_bytes = img2pdf.convert(image.filename)
    print(pdf_bytes)
    


























    # file = open(pdf_file_name, "wb")
    # with open(pdf_file_name, "wb") as file:
    #     # file.write(pdf_bytes)
    #     pass
        
    # writing pdf files with chunks
        
    # image.close()

    # # closing pdf file
    # file.close()
    return True
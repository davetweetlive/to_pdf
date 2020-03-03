#pip install img2pdf
import img2pdf
from PIL import Image
import os
import shutil 
# storing image path
img_path = "/home/dave/Pictures/'Screenshot from 2020-01-27 20-38-07.png"

# storing pdf path
pdf_path = "C:/Users/Admin/Desktop/file.pdf"

# opening image
image = Image.open("/home/dave/Pictures/srcss.png")

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(r"/home/dave/Pictures/pngfile.pdf", "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# shutil.copy("file.pdf", "C:/Users/p.kumar/Pictures/")
# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")














# /c/Users/p.kumar/Pictures/Aadhar.JPG

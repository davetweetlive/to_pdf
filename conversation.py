#pip install img2pdf
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "C:/Users/p.kumar/Pictures/Aadhar.JPG"

# storing pdf path
pdf_path = "C:/Users/Admin/Desktop/file.pdf"

# opening image
image = Image.open(r"C:\Users\p.kumar\Pictures\completion.JPG")

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(r"C:\Users\p.kumar\to_pdf\to_pdf\file.pdf", "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")














# /c/Users/p.kumar/Pictures/Aadhar.JPG

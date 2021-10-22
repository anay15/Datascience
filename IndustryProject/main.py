from pdf2image import convert_from_path,convert_from_bytes
import re
from typing import Pattern
import cv2
import pytesseract

def pdf_to_image(pdf_path):
  images = convert_from_path(pdf_path,350,poppler_path='C:/Program Files/poppler-0.68.0/bin' )
  for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    
pdf_to_image('pdf\invoice_4.pdf')

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
float_list=[]
image=cv2.imread("page0.jpg")
text=pytesseract.image_to_string(image)
cv2.imshow("image",image)
cv2.waitKey(0)
text_to_search=text
pattern=re.compile(r'[+-]?[0-9]+\.[0-9]+')
matches=pattern.finditer(text_to_search)
for match in matches:
    float_list.append(float(text[match.span()[0]:match.span()[1]]))
# print(text[match.span()[0]:match.span()[1]]) #for getting the grand total
print(max(float_list))

# import EAN13 from barcode module 
from barcode import EAN13, Code39, Code128, ISBN13
# import ImageWriter to generate an image file 
from barcode.writer import ImageWriter 
  
# Make sure to pass the number as string 
number = '9780439908870'
  
# Now, let's create an object of EAN13 
# class and pass the number 
# my_code = EAN13(number, writer=ImageWriter())
my_code = Code128(number, writer=ImageWriter())
# my_code = ISBN13(number, writer=ImageWriter())

options = {
    "font_size": 7
}
# Our barcode is ready. Let's save it. 
my_code.save("my_code", options)
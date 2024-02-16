from barcode import EAN13, Code39, Code128, ISBN13

from barcode.writer import ImageWriter 
  
number = '9780439908870'
  

# my_code = EAN13(number, writer=ImageWriter())
my_code = Code128(number, writer=ImageWriter())
# my_code = ISBN13(number, writer=ImageWriter())

options = {
    "font_size": 10
}
# Our barcode is ready. Let's save it. 
my_code.save("my_code", options)
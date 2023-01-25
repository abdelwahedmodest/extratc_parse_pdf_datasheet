#!  /usr/bin/python

#this script  is  supposed  to be  interpreted  by python3.5.2

#print("hello world")

# Import the PyPDF2 library
import PyPDF2

# Open the PDF file
with open('abc.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)
    # Get the number of pages in the PDF
    #num_pages = pdf.getNumPages()
    num_pages=len(pdf.pages) 
                            
# Iterate over each page
for page_num in range(num_pages):
    # Get the page object
    page = pdf.pages[page_num]
    # Extract the text from the page
    text = page.extract_text()
    # Print the text
    print("{}:{}".format(page_num+1,text))


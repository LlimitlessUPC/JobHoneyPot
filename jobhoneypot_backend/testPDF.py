# importing all the required modules
import PyPDF2

# creating an object 
file = open('/Users/macos/Desktop/Amel_AZZI_CV.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)
number_of_pages = fileReader.getNumPages()

# Print the content of pages
for x in range(number_of_pages):
    page = fileReader.getPage(x)
    page_content = page.extractText()
    print page_content.decode('utf-8')
    print '\n'
    print x
    print '\n'


# print the number of pages in pdf file
print(fileReader.numPages)

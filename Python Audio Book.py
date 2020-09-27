import pyttsx3
import PyPDF2
# In place of pdf name enter the name of your pdf with extension don't forget to keep it in same folder
book = open('pdf name', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
# In place of start page number enter 1- number of page from which you want to read because python reads from 0
for num in range(start page number, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
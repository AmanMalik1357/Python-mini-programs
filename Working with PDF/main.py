from PyPDF2 import PdfReader

reader = PdfReader("D:\\Work\\VS Code program\\Python\\Mini Projects\\Working with PDF\\Notification_02_2022_English.pdf")
#object


print(reader.documentInfo)
print(reader.getNumPages())
str = ""
for i in range(1, 10):
    page = reader.pages[i]
    str += page.extract_text()
with open("Python\Mini Projects\Working with PDF\\text.txt", "w", encoding= 'utf-8') as file:
    file.write(str)

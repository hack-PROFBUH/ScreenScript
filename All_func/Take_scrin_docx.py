import os
from docx import Document

doc = Document('.docx')

screenshots_folder = "screenshots"

files = os.listdir(screenshots_folder)

files.sort()

for file in files:
    if file.endswith((".png", ".jpg", ".jpeg")):
        doc.add_picture(os.path.join(screenshots_folder, file))

doc.save(".docx")

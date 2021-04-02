from github import Github
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
contents = repo.get_contents(os.getenv('GITHUB_REPOSITORY_FILE'))
print(contents.html_url)
remote_file = open("downloaded_data/demo.py", "wb")
remote_file.write(contents.decoded_content)
remote_file.close()

decoded_elements = contents.decoded_content.decode("utf-8")

c = canvas.Canvas("generated_pdf/main.pdf")
textobject = c.beginText(2*cm, 29.7 * cm - 2 * cm)
for line in decoded_elements.splitlines(False):
    textobject.textLine(line.rstrip())
c.drawText(textobject)
c.save()

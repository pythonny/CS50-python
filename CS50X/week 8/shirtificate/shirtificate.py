# Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

# In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.
# All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

# Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

# No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!
# https://pypi.org/project/fpdf2/
#https://py-pdf.github.io/fpdf2/Tutorial.html
#https://py-pdf.github.io/fpdf2/fpdf/fpdf.html

from fpdf import FPDF

name = input("Name: ")

# orientation = Portrait, measurements = milimeters and format "A4"
shirt = FPDF(orientation="P", unit="mm", format="A4")

# Create the first page
shirt.add_page()

# insert the shirtificate.png
# Format = A4, dimensions of A4 are: 210MM Width * 297 MM high
# x = distance from the left side, w = total width of the shirt.
# This means the shirt will be centered > Total width A4 = 210, width image = 190, 210 - 190 = 20mm.
# distance from left = 10mm , so distance from right is also 10mm
# Y = top of image is "x" amount from the top. In this case, top of image = 297 - 75mm
shirt.image("shirtificate.png", x=10, y=75, w=190)


shirt.set_font("helvetica", style="B",  size=45)

# Chooses how far from the top (Y) the curser will be
shirt.set_y(25)

# Cell is a text square. "0" means use entire width, "10" is the height of the box , "Text", "Align = centered"
shirt.cell(0, 10, "CS50 shirtificate", align='c')

# When writing a new text we have to move the cursor  again to the right position
shirt.set_y(140)
shirt.set_font("helvetica", "", size=30)

# Set colorto white
shirt.set_text_color(255,255,255)

shirt.cell(0, 10, f"{name} took CS50", align='c')

shirt.output("shirtificate.pdf")

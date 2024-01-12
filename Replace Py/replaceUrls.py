# This is a script that replaces the address or any other text from PDF with another string
# in this use case, two lines need to be find and modify separetly, so two conditionals are made
# the more lines, the script needs to be adapted to have more conditionals. 


import fitz  # PyMuPDF
import os  # we need this to read all files in a directory

# These are the available styles that the flitz library can take
# ---------------------------------------------------------------
# Times-Roman, Times-Italic, Times-Bold, Times-BoldItalic
# Helvetica, Helvetica-Oblique, Helvetica-Bold, Helvetica-BoldOblique
# Courier, Courier-Oblique, Courier-Bold, Courier-BoldOblique
# Symbol, ZapfDingbats
# ---------------------------------------------------------------

# get the list of all pdf files in the replace directory
files = [f for f in os.listdir("./replace") if f.endswith(".pdf")]

for file_name in files:
    file_path = "./replace/" + file_name
    doc = fitz.open(file_path)

    for page_num in range(len(doc)):
        page = doc[page_num]

        # These are the parameters of the new text
            # --------------------------------------------------------------------
        fontsize = 8  # Change as needed to match  the 

        font = "Helvetica-Bold"  # Style, change as needed

        color = (0, 0, 0)  # black, change as needed

        padding = 7 # This is the amount of padding that both lines will have, change as needed

        text = "https://vip.enjoymydeals.com/ " # URL to find

            # --------------------------------------------------------------------

        areas_line1 = page.search_for("https://clubsavellc.com/") # This the first line that the script will look for
        areas_line2 = page.search_for("https://kbshoppingdeals.com/") # This the second line that the script will look for
        areas_line3 = page.search_for("https://smartdiscountusa.com") # This the third line that the script will look for
        areas = areas_line1 + areas_line2  # combine areas from both lines

        for area in areas:
            # Add rectangle with the same color as the background to hide old text, Ik its cheap, but it is what it is
            rect = fitz.Rect(area)
            shape = page.new_shape()
            shape.draw_rect(rect)
            shape.finish(fill=(1, 1, 1), color=(1, 1, 1), stroke_opacity=0)
            shape.commit()

        # Add new text, check for areas_line1
        if areas_line1:  # if there is a first, second or third line to replace
            x1, y1, x2, y2 = areas_line1[0]  # coordinates for the texts
            
            # Insert the line of text
            page.insert_text((x1, y1 + padding), text, fontsize=fontsize, color=color, fontname=font)

        # Add new text, check for areas_line2
        elif areas_line2:
            x1, y1, x2, y2 = areas_line2[0]  # coordinates for the texts
            # Insert the line of text
            page.insert_text((x1, y1 + padding), text, fontsize=fontsize, color=color, fontname=font)

        # Add new text, check for areas_line3
        elif areas_line3:
            x1, y1, x2, y2 = areas_line3[0]  # coordinates for the texts
            # Insert the line of text
            page.insert_text((x1, y1 + padding), text, fontsize=fontsize, color=color, fontname=font)   
# ----------------------------------------------------------------------------

    # save the modified pdf to newfiles directory with the same file name
    doc.save("./newfiles/" + file_name)

# This script has no validation for repeated file names, so make sure to handle files correctly

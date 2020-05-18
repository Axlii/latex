from pylatex import Document, Section, Subsection, Command, Math, Quantity
from pylatex.utils import italic, NoEscape       

def generatepdf(text):
    doc = Document('basic')
    textsplit = text.split('\n')

    with doc.create(Section(textsplit[0])):
        for i, line in enumerate(textsplit[1:]):
            print("LINE (" + str(i) + "): " + line)
            if len(line) == 0:
                continue
            
            if "=" in line:
                math = Math(data=[line])
                doc.append(math)
            else:
                doc.append(line + "\n")
    
    doc.generate_pdf('output/document', clean_tex=False)
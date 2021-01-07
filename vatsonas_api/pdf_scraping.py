import PyPDF2 as pypdf
import os

import tabula

# def iterate_dict(dict):
#     for key in dict.keys():
#         try:
#             value = dict[key]
#         except:
#             continue
        
#         if isinstance(value, dict):            
#             iterate_dict(dict)            
#         else:
#             print(value)

pdfobject = open(os.path.join(os.getcwd(),
                              "form scraping",
                              "FR0600.pdf"), "rb")
    
pdf = pypdf.PdfFileReader(pdfobject)

pageObj = pdf.getPage(0)

print(pdf.resolvedObjects)

# print(pdf.resolvedObjects)

# xfa = iterate_dict(pdf.resolvedObjects)

# xml = xfa[7].getObject().getData()
# pdf.getFormTextFields()

# fp = os.path.join(os.getcwd(),
#                   "form scraping",
#                   "FR0600.pdf")

# df = tabula.read_pdf(fp,
#                      multiple_tables=True)

# for i in df:
#     print(i)
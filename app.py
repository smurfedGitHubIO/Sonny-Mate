import docx
doc = docx.Document()
doc.add_paragraph('Hello World!')
paraObj1 = doc.add_paragraph('Second paragraph')
paraObj2 = doc.add_paragraph('Third paragraph')
paraObj1.add_run('This text is being added to the second paragraph')
doc.save('./test/multiparagraph.docx')
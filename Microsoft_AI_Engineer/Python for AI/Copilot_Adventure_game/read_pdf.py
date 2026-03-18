import PyPDF2
path=r'C:\Developer\Python\Projects\Simplilearn\Copilot_Adventure_game\1748437489_course_end_project_02_problem_statement_pr.pdf'
reader=PyPDF2.PdfReader(path)
text='\n'.join(page.extract_text() or '' for page in reader.pages)
print(text)

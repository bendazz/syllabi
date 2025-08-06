from weasyprint import HTML, CSS
import os

# Get the current directory
current_dir = os.getcwd()

# Path to the HTML file
html_file = os.path.join(current_dir, 'machine-learning-syllabus.html')

# Custom CSS for better PDF formatting
pdf_css = CSS(string='''
@page {
    size: letter;
    margin: 0.75in;
}

body {
    font-family: 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.4;
}

.course-title {
    font-size: 20pt;
    page-break-after: avoid;
}

.course-info {
    page-break-inside: avoid;
    margin-bottom: 20pt;
}

.course-info h2 {
    font-size: 14pt;
    page-break-after: avoid;
    margin-top: 16pt;
    margin-bottom: 8pt;
}

table {
    page-break-inside: auto;
}

tr {
    page-break-inside: avoid;
    page-break-after: auto;
}

.header-image {
    max-height: 2in;
    width: auto;
}

/* Ensure good page breaks */
h2 {
    page-break-after: avoid;
}

ul, ol {
    page-break-inside: avoid;
}

li {
    page-break-inside: avoid;
}
''')

try:
    # Convert HTML to PDF
    html_doc = HTML(filename=html_file)
    pdf_output = os.path.join(current_dir, 'machine-learning-syllabus.pdf')
    
    html_doc.write_pdf(pdf_output, stylesheets=[pdf_css])
    
    print(f"PDF successfully created: {pdf_output}")
    
except Exception as e:
    print(f"Error creating PDF: {e}")
    # Try without custom CSS if there's an error
    try:
        html_doc = HTML(filename=html_file)
        pdf_output = os.path.join(current_dir, 'machine-learning-syllabus.pdf')
        html_doc.write_pdf(pdf_output)
        print(f"PDF created with basic formatting: {pdf_output}")
    except Exception as e2:
        print(f"Error creating basic PDF: {e2}")

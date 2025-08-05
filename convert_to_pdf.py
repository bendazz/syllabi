#!/usr/bin/env python3

import weasyprint
import os

def html_to_pdf(html_file, pdf_file):
    """Convert HTML file to PDF"""
    try:
        # Read the HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Create PDF from HTML
        html_doc = weasyprint.HTML(string=html_content, base_url=os.path.dirname(os.path.abspath(html_file)))
        html_doc.write_pdf(pdf_file)
        
        print(f"Successfully converted {html_file} to {pdf_file}")
        return True
        
    except Exception as e:
        print(f"Error converting HTML to PDF: {e}")
        return False

if __name__ == "__main__":
    html_file = "/workspaces/syllabi/football-analytics-syllabus.html"
    pdf_file = "/workspaces/syllabi/football-analytics-syllabus.pdf"
    
    html_to_pdf(html_file, pdf_file)

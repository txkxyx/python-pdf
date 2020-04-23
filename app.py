import markdown
import pdfkit
from pygments import highlight
from pygments.formatters import HtmlFormatter

def mark_to_html():
    f = open('file/source/source.md', mode='r', encoding='UTF-8')
    with f:
        text = f.read()
        style = HtmlFormatter(style='solarized-dark').get_style_defs('.codehilite')
        md = markdown.Markdown(extensions=['admonition', 'extra', 'codehilite'])
        body = md.convert(text)
        html = '<html lang="ja"><meta charset="utf-8"><body>'
        html += '<style>{}</style>'.format(style)
        html += '''<style> table,th,td { 
            border-collapse: collapse;
            border:1px solid #333; 
            } </style>'''
        html += body + '</body></html>' 
        return html

def html_to_pdf(html: str):
    outputfile = 'file/pdf/output.pdf'
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(html, outputfile, configuration=config)

if __name__=='__main__':
    html = mark_to_html()
    html_to_pdf(html)
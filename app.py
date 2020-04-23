import markdown
import pdfkit
from pygments import highlight
from pygments.formatters import HtmlFormatter

def mark_to_html():
    # マークダウンファイルの読み込み
    f = open('file/source/source.md', mode='r', encoding='UTF-8')
    with f:
        text = f.read()
        # Pygmentsでハイライト用のスタイルシートを作成
        style = HtmlFormatter(style='solarized-dark').get_style_defs('.codehilite')
        # # マークダウン→HTMLの変換を行う
        md = markdown.Markdown(extensions=['extra', 'codehilite'])
        body = md.convert(text)
        # HTML書式に合わせる
        html = '<html lang="ja"><meta charset="utf-8"><body>'
        # Pygmentsで作成したスタイルシートを取り込む
        html += '<style>{}</style>'.format(style)
        # Tableタグに枠線を付けるためにスタイルを追加
        html += '''<style> table,th,td { 
            border-collapse: collapse;
            border:1px solid #333; 
            } </style>'''
        html += body + '</body></html>' 
        return html

def html_to_pdf(html: str):
    # 出力ファイルの指定
    outputfile = 'file/pdf/output.pdf'
    # wkhtmltopdfの実行ファイルのパスの指定
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # HTML→PDF変換の実行
    pdfkit.from_string(html, outputfile, configuration=config)

if __name__=='__main__':
    html = mark_to_html()
    html_to_pdf(html)
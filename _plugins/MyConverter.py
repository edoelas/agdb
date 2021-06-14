import sys
import markdown
import os 

from md_extensions.table_caption import TableCaptionExtension

markdown_extensions = [
    'md_extensions.table_caption:TableCaptionExtension',
    'markdown_captions',
    'def_list',
    'nl2br',
    'codehilite',
    'fenced_code',
    'md_in_html',
    'attr_list',
    'plantuml_markdown',
    'smarty'
]

extension_configs = {
    'codehilite': {
        'linenums': False,
    }
}

md_file = open("./_plugins/temp/temp.md", "r")
md_string = md_file.read()
md_file.close()

html_string = markdown.markdown(md_string, extensions=markdown_extensions, extension_configs =extension_configs)

html_file = open("./_plugins/temp/temp.html", "w")
html_file.write(html_string)
html_file.close()
import sys
import markdown

markdown_extensions = ["tables","admonition","codehilite", "fenced_code", "attr_list", "plantuml_markdown"]

extension_configs = {
    'codehilite': {
        'linenums': False,
    }
}

md_file = open("./_plugins/temp.md", "r")
md_string = md_file.read()
md_file.close()

html_string = markdown.markdown(md_string, extensions=markdown_extensions, extension_configs =extension_configs)

html_file = open("./_plugins/temp.html", "w")
html_file.write(html_string)
html_file.close()
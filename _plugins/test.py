import sys
import markdown

md_file = open("./_plugins/temp.md", "r")
md_string = md_file.read()
md_file.close()

md_string = "TEST" + md_string

html_string = markdown.markdown(md_string, extensions=["tables"])

html_file = open("./_plugins/temp.html", "w")
html_file.write(html_string)
html_file.close()
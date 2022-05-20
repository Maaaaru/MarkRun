import markdown2

def convert_md_to_html(markdown, md2 = markdown2.Markdown()):
  return md2.convert(markdown)

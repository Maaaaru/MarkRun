import sys
import argparse
from src.utils.convert_md_to_html import convert_md_to_html
from src.utils.extract_code_from_html import extract_code_from_html
from src.utils.validate_is_markdown import validate_is_markdown
from src.executor import executor


def main(file_path):
  try:
    with open(file_path) as f:
      md = f.read()
  except:
    print("[ERROR]: An error occurred while loading the file")

  html = convert_md_to_html(md)
  code_list = extract_code_from_html(html)
  executor(code_list)

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Flow")
  parser.add_argument("--path", "-P")

  args = parser.parse_args()

  file_path = args.path

  if not file_path:
    print("[ERROR]: --path argument not found")
    sys.exit()
  
  if not validate_is_markdown(file_path):
    print("[ERROR]: This file is not a markdown")
    sys.exit()

  main(file_path)


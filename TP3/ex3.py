import sys
import re

def hearders(input):
    md_headers = [r'^#\s+(.*)$', r'^##\s+(.*)$', r'^###\s+(.*)$']
    html_headers = [r'<h1>\1<h1>', r'<h2>\1<h2>', r'<h3>\1<h3>']
    for i in range(3):
        input = re.sub(md_headers[i], html_headers[i], input, flags=re.MULTILINE)
    return input

def bold(input):
    md_bold = r'\*\*(.*?)\*\*'
    html_bold = r'<b>\1</b>'
    input = re.sub(md_bold, html_bold, input)
    return input

def italic(input):
    md_italic = r'\*(.*?)\*'
    html_italic = r'<i>\1</i>'
    input = re.sub(md_italic, html_italic, input)
    return input

def links(input):
    md_links = r'\[([^!].*?)\]\((.*?)\)'
    html_links = r'<a href="\2">\1</a>'
    input = re.sub(md_links, html_links, input)
    return input

def images(input):
    md_images = r'!\[(.*?)\]\((.*?)\)'
    html_images = r'<img src="\2" alt="\1">'
    input = re.sub(md_images, html_images, input, flags=re.MULTILINE)
    return input

def lists(input):
    md_lists = r'^\d\.\s+(.*)$'
    html_lists = r'<ul><li>\1</li></ul>'
    for i in range(2):
        input = re.sub(md_lists, html_lists, input, flags=re.MULTILINE)
    return input

def main():
    input = sys.stdin.read()
    input = hearders(input)
    input = bold(input)
    input = italic(input)
    input = images(input)
    input = links(input)
    input = lists(input)
    print(input)

if __name__ == '__main__':
    main()
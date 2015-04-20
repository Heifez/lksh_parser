import urllib.request
from html.parser import HTMLParser
class page(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == 'div') and (attrs == smth):
            checker = True
            stack.append(1)
        if (tag == 'img') and (checke 
    def handle_endtag(self, tag):
        if tag == 'div':
            del stack[len(stack) - 1]
            if len(stack) == 0:
                body_content_checker = false
body_content_checker = false
stack = []


import urllib.request
from html.parser import HTMLParser
class page(HTMLParser):
    def mal(self):
        self.counter = 0
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if ((tag == 'div') and ('thumbinner' in get_attrs(attrs))):
            self.counter += 1
            hyper_text = []
        elif (tag == 'table' and 'toccolours' in get_attrs(attrs) and self.counter == 0):
            self.counter += 1
        elif (tag == 'a' and '\'/wiki' in get_attrs(attrs)):
            if ('http://ga.wikipedia.org' + attrs[0][1]) not in self.hrefs:
                self.hrefs.append('http://ga.wikipedia.org' + attrs[0][1])
def get_attrs(attrs):
    answ = str(attrs)
    return answ
def get_num_of_imgs(url, urls, max_images):
    data = str(urllib.request.urlopen(url).read())
    parsing_item = page()
    parsing_item.mal()
    parsing_item.feed(data)
    f = parsing_item.counter
    if f > max_images:
        max_images = f
    if f not in urls:
        urls[f] = [url]
    else:
        urls[f] += [url]
    for i in parsing_item.hrefs:
        urls, max_images = get_num_of_imgs(i, urls, max_images)
    return urls, max_images

def work():
    final, maxi = get_num_of_imgs('http://ga.wikipedia.org/wiki/Ailtireacht_na_Seap%C3%A1ine', {}, 0)
    file = open('output.html', 'w')
    file.write('<html><head></head><body><h1>Max images :' , final, '</h1><p>')
    for i in maxi[final]:
        file.write('<a href=\"', str(i), '\">Le page with those imgs</a></br>')
    file.write('</p></body></html>')
work()

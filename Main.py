from urllib.request import urlopen
url = "https://www.decadirect.org/"
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
#title_index = html.find("<title>")
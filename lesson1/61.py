page = 'somewebsite'

start_link = page.find('<a href=')

url_start_pos = page.find('"', start_link)
url_end_pos   = page.find('"', url_start_pos+1)

url = page[url_start_pos+1:url_end_pos]

from bs4 import BeautifulSoup
import urllib2
import re

software = ['tumblr', 'reddit is fun', 'quora', 'wikihow','wikipedia', 'stack+exchange', 'google', 'facebook', 'twitter', 'youtube', 'amazon', 'google+play', 'goodreads', 'buzzfeed','imgur', 'economist', 'calm', 'lumosity']
for sf in software:
    url = 'http://apkleecher.com/?id=%s' % sf
    open = urllib2.urlopen(url)
    read = open.read()
    open.close()
    date = re.compile(r'\d+-\d+-\d+')
    bs = BeautifulSoup(read)
    version = bs.find('p', 'text-success').find('font').text
    update_date =  bs.find('div','col-md-10').find(text = date).strip()
    print "%s:    ||||| %s" % (version,update_date)
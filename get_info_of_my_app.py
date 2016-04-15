from bs4 import BeautifulSoup
import urllib2
import re

# software is a variable collecting the names of apps I want to check for update new. You can create new strings.
software = ['tumblr', 'reddit is fun', 'quora', 'wikihow','wikipedia', 'stack+exchange', 'google', 'facebook', 'twitter', 'youtube', 'amazon', 'google+play', 'goodreads', 'buzzfeed','imgur', 'economist', 'calm', 'lumosity']


for sf in software:
    url = 'http://apkleecher.com/?id=%s' % sf
    open = urllib2.urlopen(url)
    read = open.read()
    open.close()
    # use regex to match the updated date.
    date = re.compile(r'\d+-\d+-\d+')
    bs = BeautifulSoup(read)
    # get the version information of apps
    version = bs.find('p', 'text-success').find('font').text
    # get the updated date.
    update_date =  bs.find('div','col-md-10').find(text = date).strip()
    print "%s:    ||||| %s" % (version,update_date)
    
## By the way, what I want to do next is to collect my current apps version information, then the script can automately compare the version information, and notify me when the version is newer.

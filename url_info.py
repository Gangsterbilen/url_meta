import urllib2
import datetime



InURL = raw_input('URL:')

print datetime.datetime.now()
print "url requested:"
print InURL

#Loads,reads the page and converts the data to a UTF-8 string.	
load = urllib2.urlopen(InURL)
Page_info = load.info()
Page_code = load.getcode()

print "Meta-information of the page:"
print Page_info
print "HTTP status code:"
print Page_code





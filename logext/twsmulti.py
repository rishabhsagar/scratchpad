import urllib, urllib2, cookielib,re,sqlite3, time, threading
from datetime import datetime
from Queue import Queue

username = 'support'
password = 'support'
hostname = 'http://dsgpc01u1-sv.lloydstsb.co.uk:8080'
workStation = 'S016'
databaseURL = "C:\\Program Files\\sqlite\\sqlite-shell\\spotter.db"
twspage = '/DSViewer/LogBrowser?type=tws'
credentials = [username, password, hostname]

# Prep the connection to the database.
con = sqlite3.connect(databaseURL)

def logOn(username, password, hostname):
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  login_data = urllib.urlencode({'j_username' : username, 'j_password' : password})

  # Strangely, untill client tries to login to main page, the portal refuses login! :)
  opener.open(hostname + '/DSViewer/Main')

  # This will login to the portal and will accept a cookie, as the cookie jar is baked into opener.
  opener.open(hostname + '/DSViewer/j_security_check', login_data)

  #print "Logged into the portal..."
  return opener

def htmlSpider(credentials, link, prelink=""):
  # visits the link (without hostname) and returns a list of lines in the resulting html page.
  # does not check for returned html code, just return the parsed html page.
  # Sometimes, a pre-link is supplied; this is becase such links work only when two links are visited in order.
  
  opener = logOn(credentials[0], credentials[1], credentials[2])
  
  if prelink <> "":
    resp = opener.open( hostname + prelink)
    data = resp.read()
    data = []

  resp = opener.open( hostname + link)
  
  data = resp.read().splitlines()
  
  opener.close()
  
  return data

def htmlExtractor(htmlPage, openTag, closeTag, filterLst=[""]):

  # Extracts data between the tags specified.
  # Assumes that the tag is properly closed, and the lines in the order as they appear on the page.

  flgStartCapture = 0
  outputLines  = []

  for htmlLine in htmlPage:
    if openTag in htmlLine:
      flgStartCapture = 1
      continue
    
    if closeTag in htmlLine:
      flgStartCapture = 0

    if flgStartCapture == 1:
      for filterStr in filterLst:
        if filterStr in htmlLine:
          outputLines.append(htmlLine)
          break

  return outputLines
  
def htmlPageLinkExtractor(hrefLines):
  # Given a list of html lines, this function returns a href targets.

  htmlLinks = []

  for htmlLine in hrefLines:
    if "href" in htmlLine:
      pattern = re.search(r".*href=\"([^\"]*)\".*", htmlLine)
      if ( pattern is not None):
        #print pattern.group(1)
        htmlLinks.append(pattern.group(1))

  return htmlLinks

def parseTWSLog(logData):
    try:
      # All parsing happens on position of strings in TWS logs, this is bad :(
      jobName = logData[1][-8:]
      end = logData[-2][6:23]
      start = logData[5][6:23]
      startTime = datetime.strptime(start, "%m/%d/%y %H:%M:%S")
      endTime = datetime.strptime(end, "%m/%d/%y %H:%M:%S")
      duration = (endTime - startTime).total_seconds()
      exitStatus = logData[-5].split(':')[1].strip()
    except ValueError as err:
      print "Encountered error while trying to parse this log"
      print logData
      print "Error was : " + err
    else:
      # Compile and return row
      #print jobName + "," + exitStatus + "," + start + "," + end + "," + str(duration)
      row = (jobName, exitStatus, start, end, duration)
    
    return row

def getTWSLogs(events, credentials):
	rows = []
	def producer(q, events, credentials):
		for event in events:
			thread = LogPuller(event, credentials)
			thread.start()
			q.put(thread, True)
	
	def consumer(q, total_events, printat=100):
		while len(rows) < total_events:
			thread = q.get(True)
			thread.join()
			rows.append(thread.get_log())
			if ( len(rows) > printat ):
				printat += 100
				print "Harvest size crossed : " + str(len(rows)) + ", next status at " + str(printat)
				print "Queue size is " + str(q.qsize())
	
	# Create a queue to fill with executing threads
	q = Queue(5)
	
	# Create the producer and consumer threads
	prod_thread = threading.Thread(target=producer, args=(q, events, credentials))
	cons_thread = threading.Thread(target=consumer, args=(q, len(events)))
	
	# Start the threads
	prod_thread.start()
	cons_thread.start()
	
	# Wait for the threads to complete
	prod_thread.join()
	cons_thread.join()
	
class LogPuller(threading.Thread):
    def __init__(self, event, credentials):
        self.event = event
        self.credentials = credentials
        self.result = None
        threading.Thread.__init__(self)
    
    def get_log(self):
        return self.result
        
    def run(self):
      lnk  = self.event[0]
      prelnk = self.event[1]
      self.result = parseTWSLog(htmlExtractor(htmlSpider(credentials, lnk, prelnk), "<pre>", "</pre>"))
    
# All code should read like a poem.

# Get a list of all the dates for which the tws logs are available.
listOfTWSDirLinks = htmlPageLinkExtractor(htmlExtractor(htmlSpider(credentials, twspage), "<pre>", "</pre>", ["DSViewer", "LogBrowser"]))

# For each day, create a list of all the logs
ev_tuples = []                                          # Stores the tuples (eventlink, daylink)

for day in listOfTWSDirLinks:
    events = htmlPageLinkExtractor(htmlExtractor(htmlSpider(credentials, day), "<pre>", "</pre>", ["DSViewer", "FileBrowser"]))
    for event in events: ev_tuples.append((event, day))

print "Completed collecting the events, total events : " + str(len(ev_tuples))
getTWSLogs(ev_tuples, credentials)

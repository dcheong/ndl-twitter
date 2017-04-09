import sys
import tweepy
import datetime
import MySQLdb as mysql

 
 
 
# Insert information from your Twitter App.
CONSUMER_KEY = 'yPyurOc0Nqy8DYGIU0ofZYzso'
CONSUMER_SECRET = 'C5J5SxUxqXFqxf0KSd9APUzL53P2a0mcPMto5fNLfaumVVINlb'
ACCESS_KEY = '1896011364-M9Cr8NrQN9MAte9sGcLLIPWCpbYqRDIZXC2kV5U'
ACCESS_SECRET = 'lCReGwuWCF8C3yzGyGm8dGDaUg9Xr15OTVzUNps3XfBvK'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#msql information
host='127.0.0.1'
user='root'
password='password'
port = 3306
db = 'ndltest'

#atlanta bounding box.
# [Southwest longitude, southwest latitude, northeast longitude, northeast latitude]
box = [-84.55,33.64,-84.29,33.88]


conn = mysql.connection(
    host=host,
    user=user,
    passwd=password,
    port=port,
    db=db
)

conn.query("""CREATE TABLE IF NOT EXISTS new_table (
    id INT(11) NOT NULL AUTO_INCREMENT,
    message VARCHAR(250) DEFAULT NULL,
    PRIMARY KEY (id)) DEFAULT CHARSET=utf8""")
conn.commit()

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            if status.geo!=None:
                # now = datetime.datetime.now()
                # filename = open( "Z:/statuses_%s%s%s_%s_copy.p" % (str(now.year),str(now.month),str(now.day),str(now.hour)),"a+b")             #Set your own directory; a new file will be created each hour.  
                # pickle.dump(status, filename)
                # filename.close()
                print status
                # escapedText = conn.escape_string(status.text.encode('utf-8'))
                # query = "INSERT INTO new_table(message) VALUES ('%s')" % escapedText
                # print query
                # conn.query(query)
                # conn.commit()
               
 
                #print "%s\t" % status.id
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            print datetime.datetime.now()
            pass
 
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        print datetime.datetime.now()
        return True # Don't kill the stream
 
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        print datetime.datetime.now()
        return True # Don't kill the stream
 
# Create a streaming API and set a timeout value of 30 seconds
 
while True:
    try:
        streaming_api1 = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=30)     
        print >> sys.stderr, 'Filtering the public timeline for '
        streaming_api1.filter(locations=box)
    except Exception, e:
                print >> sys.stderr, 'Encountered Exception:', e
                print datetime.datetime.now()
                pass
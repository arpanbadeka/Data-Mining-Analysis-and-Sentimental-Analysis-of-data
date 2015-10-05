# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allinone.ui'
#
# Created: Wed May 13 09:28:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from streaming import StreamListener
import time
import threading
import tweepy
import csv
start_time=time.time()
ckey = 'fR5FnN3RmBZbAUNrdrGSjC40S'
csecret = 'neFWC5k1jhxWAUJ8jOaVbgjR2EAsskaCVJWBtwZzwxQboKI9GS'
atoken = '3088495247-4WfVTQSZBfT5DbT6tOYzDMAuhINfgUaBhG0ZQS4'
asecret = '0P2mg7tw8aUYqaeJ7jtaJLXqvnGDQBUEfkwy6vgoEIWRI'
auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
api = tweepy.API(auth)
lock=threading.Lock()
def key():
    print("enter the keyword")
    keyword=input()
    print("enter the language")
    language=input()
    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener(start_time,time_limit=300))
        twitterStream.filter( track=[keyword], languages=[language])
    except Exception as e:
        time.sleep(5)

def loc():
        locat=[]
        print("enter the location")
        locat1=input()
        loca1=float(locat1)
        locat2=input()
        loca2=float(locat1)
        locat3=input()
        loca3=float(locat1)
        locat4=input()
        loca4=float(locat1)
        locat.append(locat1)
        locat.append(locat2)
        locat.append(locat3)
        locat.append(locat4)
        print("enter the language")
        language=input()
        locat=list(map(float,locat))
        print(locat)
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener1(start_time,time_limit=300))
        twitterStream.filter(  languages=[language], locations=locat)

def lockey():
    print("enter the file name")
    filename=input()
    csvFile = open(filename, 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
    start_time=time.time()
    print("enter the keyword")
    keyword=input()
    print("enter the language")
    language=input()
    print("enter max tweets")
    maxtw=input()
    max_tweets=int(maxtw)
    print("enter the from date")
    sinc=input()
    print("enter the to date")
    too=input()
    print("enter the location")
    location=input()
    count=1
    c=1
    '''t=0
    a=2014
    while t < 10:
        
        auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
        api = tweepy.API(auth)
        results = api.search(q=keyword,lang=language,geo='48.85681, 2.34760,15km',since_id=a)
        a=resu.getMaxId()
        t=t+1
    '''
    #max_tweets=1000
    auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
    api = tweepy.API(auth)
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=keyword,language=language,since_id=sinc,until=too,location=location).items(max_tweets)]
    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=keyword, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            time.sleep(30)
            continue
    for tweets in searched_tweets:
        print (c,tweets.created_at.date,tweets.text.encode('utf-8'))
        c=c+1
        csvWriter.writerow([tweets.created_at, tweets.text.encode('utf-8')])
        #print tweet.created_at, tweet.text
    csvFile.close()
def lockey1():
        counter=0
        print("enter the file name")
        filename=input()
        csvFile = open(filename, 'a')
        #Use csv Writer
        csvWriter = csv.writer(csvFile)
        start_time=time.time()
        print("enter the keyword")
        keyword=input()
        print("enter the language")
        language=input()
        print("enter the from date")
        sinc=input()
        print("enter the to date")
        too=input()
        print("enter the location")
        location=input()
        auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
        api = tweepy.API(auth)
        count=1
        for tweet in tweepy.Cursor(api.search,q=keyword,language=language,location=location,since_id=sinc).items():
                try:
                           #Write a row to the csv file/ I use encode utf-8
                            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
                            print(tweet.created_at, tweet.text.encode('utf-8'))
                            counter = counter + 1
                            print(counter)
                            if counter == 2000:
                                time.sleep(60*20) # wait for 20 min everytime 2,000 tweets are extracted 
                                counter = 0
                                continue
                except tweepy.error.TweepyError as e:
                        time.sleep(60*20)
                        continue
       
        csvFile.close()
def multi():
    t=d1()
    t1=d1()
    lock.acquire()
    try:
        t.start()
    finally:
        lock.release()
    lock.acquire()
    try:
        t1.start()
    finally:
        lock.release()
    t.sleep2()
    t1.sleep()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class listener(StreamListener):

    def __init__(self,start_time,time_limit=300):
        self.time=start_time
        self.limit=time_limit
    '''def __init__data(keyword,location):
        keyword=self.keyword.text()
        location=self.location.text()'''

    def on_data(self, data):
        while(time.time()-self.time)<self.limit:
            try:
                #print (data)
                tweet = data.split(',"text":"')[1] .split('","source')[0]
                print (tweet)
                saveThis = str(time.time())+'::'+tweet   
                saveFile = open('file1.csv','a')
                saveFile.write(tweet)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException (e):
                print ('failed ondata,',str(e))
                time.sleep(5)
        exit()
        

    def on_error(self, status):
        print (status)

class listener1(StreamListener):

    def __init__(self,start_time,time_limit=300):
        self.time=start_time
        self.limit=time_limit
    '''def __init__data(keyword,location):
        keyword=self.keyword.text()
        location=self.location.text()'''

    def on_data(self, data):
        while(time.time()-self.time)<self.limit:
            try:
                #print (data)
                tweet = data.split(',"text":"')[1] .split('","source')[0]
                print (tweet)
                saveThis = str(time.time())+'::'+tweet   
                saveFile = open('file.csv','a')
                saveFile.write(tweet)
                saveFile.write('\n')
                saveFile.close()
                return True
            except BaseException (e):
                print ('failed ondata,',str(e))
                time.sleep(5)
        exit()
        

    def on_error(self, status):
        print (status)

class d1(threading.Thread):
    def __init__(self):
        super(d1,self).__init__()
        #time.sleep(10)
    def sleep(self):
        time.sleep(2)
    def sleep2(self):
        time.sleep(2)
    def run(self):
            counter=0
            print("enter the filename")
            filename=input()
            csvFile = open(filename, 'a')
            #Use csv Writer
            csvWriter = csv.writer(csvFile)
            start_time=time.time()
            print("enter the keyword")
            keyword=input()
            print("enter the language")
            language=input()
            print("enter the from date")
            sinc=input()
            print("enter the to date")
            too=input()
            print("enter the location")
            location=input()
            auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
            api = tweepy.API(auth)
            count=1
            for tweet in tweepy.Cursor(api.search,q=keyword,language=language,location=location,since_id=sinc).items():
                    try:
                                auth = tweepy.OAuthHandler(consumer_key=ckey, consumer_secret=csecret)
                                api = tweepy.API(auth)
                               #Write a row to the csv file/ I use encode utf-8
                                csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
                                print(tweet.created_at, tweet.text.encode('utf-8'))
                                counter = counter + 1
                                #print(counter)
                                if counter == 2000:
                                    time.sleep(60*20) # wait for 20 min everytime 2,000 tweets are extracted 
                                    counter = 0
                                    continue
                    except tweepy.error.TweepyError as e:
                            time.sleep(60*20)
                            continue
                    except BaseException as e:
                            time.sleep(60*2.5)
                            continue
                    except Exception as e:
                            time.sleep(60*2.5)
                            continue
            
            csvFile.close()
class Ui_Form(QtGui.QWidget):
    def __init__(self):#,start_time,time_limit=300):
        #self.time=start_time
        #self.limit=time_limit
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(441, 330)
        self.keyword = QtGui.QPushButton(Form)
        self.keyword.setGeometry(QtCore.QRect(140, 50, 141, 23))
        self.keyword.setObjectName(_fromUtf8("keyword"))
        self.location = QtGui.QPushButton(Form)
        self.location.setGeometry(QtCore.QRect(140, 100, 141, 23))
        self.location.setObjectName(_fromUtf8("location"))
        self.keyloc = QtGui.QPushButton(Form)
        self.keyloc.setGeometry(QtCore.QRect(140, 150, 141, 23))
        self.keyloc.setObjectName(_fromUtf8("keyloc"))
        self.keyloc1 = QtGui.QPushButton(Form)
        self.keyloc1.setGeometry(QtCore.QRect(140, 200, 141, 23))
        self.keyloc1.setObjectName(_fromUtf8("keyloc1"))
        self.multithread = QtGui.QPushButton(Form)
        self.multithread.setGeometry(QtCore.QRect(140, 250, 141, 23))
        self.multithread.setObjectName(_fromUtf8("multithread"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.keyword.setText(_translate("Form", "Keyword", None))
        self.location.setText(_translate("Form", "location", None))
        self.keyloc.setText(_translate("Form", "Keyword Location", None))
        self.keyloc1.setText(_translate("Form", "Keyword Location(infinite)", None))
        self.multithread.setText(_translate("Form", "Multithreading", None))
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    ex = Ui_Form()#start_time,time_limit=300)
    ex.show()
    #keyword=keyword.get()
    ex.keyword.clicked.connect(key)
    ex.location.clicked.connect(loc)
    ex.keyloc.clicked.connect(lockey)
    ex.keyloc1.clicked.connect(lockey1)
    ex.multithread.clicked.connect(multi)
    sys.exit(app.exec_())



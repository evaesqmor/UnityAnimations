import speech_recognition as sr
import webbrowser as wb
import speak
import requests
from bs4 import BeautifulSoup
import time

chrome_path = '"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s'

keyworda1="explain" #wikipedia     #1/ wikipedia function
keyworda2="search for" #google     #2/ google search function
keyworda3="open" #url              #3/ open function  
keyworda4="date" #time             #4/ today function
keyworda5="weather" #weather       #5/ weather function
keyworda6="where" #place           #6/ where function

keywordt1="yesterday"
keywordt2="today"
keywordt3="tomorrow"
keywordtn2="tonight"
keywordtn0="night"
keywordtn1="yesterday night"
keywordtn3="tomorrow night"

#location search (restaurant, hospital, station, school, office, university, college, toilet, site etc.) ---Advanced 'search for' function

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    print("done!")
try:
    text = r.recognize_google(audio)
    text = text.lower()
    print("This is your original text:{}".format(text)) #Test usage

    if text.find(keyworda1)+1:  # <explain> function
        content = text[text.find(keyworda1)+8:len(text)]         
        url = "https://en.wikipedia.org/wiki/" + content
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")
        print(content)
        wb.get(chrome_path).open(url)      #search on chrome in wikipedia
        for item in soup.select(".r a"):
            print (item.text)
            speak.tts(item.text,'en') 
            break
    elif text.find(keyworda2)+1:  # <search for> function
        content = text[text.find(keyworda2)+11:len(text)]         
        url = "https://www.google.co.uk/search?ei=hj_IW8-iG42IaY3VsKAL&q=" + content
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")
        print(content)
        wb.get(chrome_path).open(url)      #search on chrome in google
        for item in soup.select(".r a"):
            print (item.text)
            speak.tts(item.text,'en') 
            break
    elif text.find(keyworda3)+1:  # <open> function
        content = text[text.find(keyworda3)+5:len(text)]         
        url = "https://" + content
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")
        print(content)
        wb.get(chrome_path).open(url)      #open the site on chrome
        for item in soup.select(".r a"):
            print (item.text)
            speak.tts(item.text,'en') 
            break
    elif text.find(keyworda4)+1:  # <date> function
        keywordta="Mon"
        keywordTa="monday"
        keywordtb="Tue"
        keywordTb="tuesday"
        keywordtc="Wed"
        keywordTc="wednesday"
        keywordtd="Thu"
        keywordTd="thursday"
        keywordte="Fri"
        keywordTe="friday"
        keywordtf="Sat"
        keywordTf="saturday"
        keywordtg="Sun"
        keywordTg="sunday"

        keywordtmath1="last"    # (3/ date subtraction)
        keywordtmath2="this"    # (3/ date math)
        keywordtmath3="next"    # (3/ date addition)

        localtime = time.asctime( time.localtime(time.time()) )    # (3/ date function)
        localweekday = time.strftime("%a", time.localtime(time.time()))     # (3/ the day in a week)

        thisweekday=0
        if localweekday.find(keywordta)+1:
            thisweekday=1
        elif localweekday.find(keywordtb)+1:
            thisweekday=2
        elif localweekday.find(keywordtc)+1:
            thisweekday=3
        elif localweekday.find(keywordtd)+1:
            thisweekday=4
        elif localweekday.find(keywordte)+1:
            thisweekday=5
        elif localweekday.find(keywordtf)+1:
            thisweekday=6
        elif localweekday.find(keywordtg)+1:
            thisweekday=7

        localdate1 = time.strftime("%a %b %d %Y", time.localtime(time.time()-86400))    # (3/ date_yesterday)
        localdate2 = time.strftime("%a %b %d %Y", time.localtime(time.time()))          # (3/ date_today)
        localdate3 = time.strftime("%a %b %d %Y", time.localtime(time.time()+86400))    # (3/ date_tommorow)

        if text.find(keywordt1)+1:
            print ("Yesterday was "+localdate1)
            speak.tts("Yesterday was ",'en')
            speak.tts(localdate1,'en')      #display yesterday's date
        elif text.find(keywordt3)+1:
            print ("Tommorw will be "+localdate3)
            speak.tts("Tommorow will be ",'en')
            speak.tts(localdate3,'en')      #display tommorow's date
        elif text.find(keywordt2)+1:
            print ("Today is "+localdate2)
            speak.tts("Today is ",'en')
            speak.tts(localdate2,'en')      #display today's date
        elif text.find(keywordtmath1)+1:
            if text.find(keywordTa)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+1)))        
                print (keywordtmath1+" "+keywordTa+" was "+localdate)
                speak.tts(keywordtmath1+keywordTa+" was "+localdate, 'en')
            elif text.find(keywordTb)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+2)))        
                print (keywordtmath1+" "+keywordTb+" was "+localdate)
                speak.tts(keywordtmath1+keywordTb+" was "+localdate, 'en')
            elif text.find(keywordTc)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+3)))        
                print (keywordtmath1+" "+keywordTc+" was "+localdate)
                speak.tts(keywordtmath1+keywordTc+" was "+localdate, 'en')
            elif text.find(keywordTd)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+4)))        
                print (keywordtmath1+" "+keywordTd+" was "+localdate)
                speak.tts(keywordtmath1+keywordTd+" was "+localdate, 'en')
            elif text.find(keywordTe)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+5)))        
                print (keywordtmath1+" "+keywordTe+" was "+localdate)
                speak.tts(keywordtmath1+keywordTe+" was "+localdate, 'en')
            elif text.find(keywordTf)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+6)))        
                print (keywordtmath1+" "+keywordTf+" was "+localdate)
                speak.tts(keywordtmath1+keywordTf+" was "+localdate, 'en')
            elif text.find(keywordTg)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-7-thisweekday+7)))        
                print (keywordtmath1+" "+keywordTg+" was "+localdate)
                speak.tts(keywordtmath1+keywordTg+" was "+localdate, 'en')
            else:
                print (keywordtmath1+" day was "+localdate1)
                speak.tts(keywordtmath1+" day was ",'en')
                speak.tts(localdate1,'en')      #display past time
        elif text.find(keywordtmath2)+1:
            if text.find(keywordTa)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+1)))        
                print (keywordtmath2+" "+keywordTa+" is "+localdate)
                speak.tts(keywordtmath2+keywordTa+" is "+localdate, 'en')
            elif text.find(keywordTb)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+2)))        
                print (keywordtmath2+" "+keywordTb+" is "+localdate)
                speak.tts(keywordtmath2+keywordTb+" is "+localdate, 'en')
            elif text.find(keywordTc)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+3)))        
                print (keywordtmath2+" "+keywordTc+" is "+localdate)
                speak.tts(keywordtmath2+keywordTc+" is "+localdate, 'en')
            elif text.find(keywordTd)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+4)))        
                print (keywordtmath2+" "+keywordTd+" is "+localdate)
                speak.tts(keywordtmath2+keywordTd+" is "+localdate, 'en')
            elif text.find(keywordTe)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+5)))        
                print (keywordtmath2+" "+keywordTe+" is "+localdate)
                speak.tts(keywordtmath2+keywordTe+" is "+localdate, 'en')
            elif text.find(keywordTf)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+6)))        
                print (keywordtmath2+" "+keywordTf+" is "+localdate)
                speak.tts(keywordtmath2+keywordTf+" is "+localdate, 'en')
            elif text.find(keywordTg)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(-thisweekday+7)))        
                print (keywordtmath2+" "+keywordTg+" is "+localdate)
                speak.tts(keywordtmath2+keywordTg+" is "+localdate, 'en')
            else:
                print (keywordtmath2+" day is "+localdate2)
                speak.tts(keywordtmath2+" day is ",'en')
                speak.tts(localdate2,'en')      #display current time
        elif text.find(keywordtmath3)+1:
            if text.find(keywordTa)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+1)))        
                print (keywordtmath3+" "+keywordTa+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTa+" will be "+localdate, 'en')
            elif text.find(keywordTb)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+2)))        
                print (keywordtmath3+" "+keywordTb+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTb+" will be "+localdate, 'en')
            elif text.find(keywordTc)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+3)))        
                print (keywordtmath3+" "+keywordTc+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTc+" will be "+localdate, 'en')
            elif text.find(keywordTd)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+4)))        
                print (keywordtmath3+" "+keywordTd+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTd+" will be "+localdate, 'en')
            elif text.find(keywordTe)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+5)))        
                print (keywordtmath3+" "+keywordTe+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTe+" will be "+localdate, 'en')
            elif text.find(keywordTf)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+6)))        
                print (keywordtmath3+" "+keywordTf+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTf+" will be "+localdate, 'en')
            elif text.find(keywordTg)+1:
                localdate = time.strftime("%b %d %Y", time.localtime(time.time()+86400*(7-thisweekday+7)))        
                print (keywordtmath3+" "+keywordTg+" will be "+localdate)
                speak.tts(keywordtmath3+keywordTg+" will be "+localdate, 'en')
            else:
                print (keywordtmath3+" day will be "+localdate3)
                speak.tts(keywordtmath3+" day will be ",'en')
                speak.tts(localdate3,'en')      #display future time
        else:
            print ("Now is "+localtime)
            speak.tts("Now is ",'en')
            speak.tts(localtime,'en')      #display current time
    elif text.find(keyworda5)+1:        # <weather> function
        if text.find(keywordtn1)+1:
            print("sorry, i can't provide the past weather forecast.")
            speak.tts("sorry, i can't provide the past weather forecast.", 'en')
        elif text.find(keywordt1)+1:
            print("sorry, i can't provide the past weather forecast.")
            speak.tts("sorry, i can't provide the past weather forecast.", 'en')
        elif text.find(keywordtn2)+1:
            url = "https://weather.com/weather/tenday/l/FRXX0059:1:FR"
            response = requests.get(url)
            soup = BeautifulSoup(response.text,"lxml")
            print(text)
            wb.get(chrome_path).open(url)      #open the webpage
            for item in soup.select("tr[classname]"):
                print (item.text)
                speak.tts(item.text,'en') 
                break       
        #elif text.find(keywordt2):
        #elif text.find(keywordtn3):    
        #elif text.find(keywordt3):

    elif text.find(keyworda6)+1:        # <where> function
        res = requests.get('https://ipinfo.io/')
        location = res.json()
        locate = location['loc'].split(',')
        latitude = locate[0]
        longitude = locate[1]
        city = location['city']
        
        latitudehome = "48.8185"
        longitudehome = "2.343"
        cityhome = "Paris"
        
        latitudeisep = "48.8246" 
        longitudeisep = "2.280"
        cityisep = "Paris"

        keywordp0="isep"
        keywordp1="am i"
        keywordp2="home"
        keywordp3="is"
        
        if text.find(keywordp1)+1:
            print("You are at : ")
            print("Latitude : " + latitude + ", Longitude : " + longitude + ", City : " + city)
            speak.tts("You are at ", 'en')
            speak.tts("Latitude : " + latitude + ", Longitude : " + longitude + ", City : " + city, 'en')
        elif text.find(keywordp2)+1:
            print(keywordp2 + " is at : ")
            print("Latitude : " + latitudehome + ", Longitude : " + longitudehome + ", City : Paris")
            speak.tts(keywordp2 + " is at : ", 'en')
            speak.tts("Latitude : " + latitudehome + ", Longitude : " + longitudehome + ", City : Paris", 'en')
        elif text.find(keywordp0)+1:
            print(keywordp0 + " is at : ")
            print("Latitude : " + latitudeisep + ", Longitude : " + longitudeisep + ", City : Paris")
            speak.tts(keywordp0 + " is at : ", 'en')
            speak.tts("Latitude : " + latitudeisep + ", Longitude : " + longitudeisep + ", City : Paris", 'en')
        else:
            print("Sorry, can you describe the place more specifically?")
            speak.tts("Sorry, can you please describe the place more specifically?", 'en')
    else:       #basic search function
        print("Lishuo's showtime")
                 
except Exception as e:
    print(e)
    print("Sorry could not recognize what you said")
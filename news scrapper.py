import time
from urllib import request
from bs4 import BeautifulSoup

genre = input("Write what type of news you want(sports,normal and science) ")


norm=("normal")
spor=("sports")
scinew=("science")
fullnam = ("Daily News.txt")
with open(fullnam, "w", encoding="utf-8") as f:

    if genre == norm:
        normalnews1=("https://www.aljazeera.com/")
        news1 = request.urlopen(normalnews1)
        soup = BeautifulSoup(news1, "html.parser")
        nor1=("Normal news 1")
        f.write(nor1)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1) 

        normalnews2=("https://www.bbc.com/")
        news2 = request.urlopen(normalnews2)
        soup = BeautifulSoup(news2, "html.parser")
        nor2=("Normal news 2")
        f.write(nor2)
        f.write("\n")
        for headlines2 in soup.find_all('h3'):
            strhead2 = (headlines2.get_text())
            strhead2 += "\n"
            f.write(strhead2)
            time.sleep(1) 

        normalnews3=("https://www.washingtonpost.com/")
        news3 = request.urlopen(normalnews3)
        soup = BeautifulSoup(news3, "html.parser")
        nor3=("Normal news 3")
        f.write(nor3)
        f.write("\n")
        for headlines3 in soup.find_all('h2'):
            strhead3 = (headlines3.get_text())
            strhead3 += "\n"
            f.write(strhead3)
            time.sleep(1) 


    elif genre == spor:
        sportnews1=("https://www.skysports.com/")
        sport1 = request.urlopen(sportnews1)
        soup = BeautifulSoup(sport1, "html.parser")
        spo1=("sports news 1")
        f.write(spo1)
        f.write("\n")
            for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1) 

    
        sportnews2=("https://www.dailymail.co.uk/sport/index.html")
        sport2 = request.urlopen(sportnews2)
        soup = BeautifulSoup(sport1, "html.parser")
        spo2=("sports news 2")
        f.write(spo2)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1) 

    
        sportnews3=("https://www.theguardian.com/uk/sport")
        sport3 = request.urlopen(sportnews3)
        soup = BeautifulSoup(sport3, "html.parser")
        spo3=("sports news 3")
        f.write(spo3)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1)     
    

    elif genre == scinew:

        scinews1=("https://www.bbc.co.uk/news/science_and_environment")
        sci1 = request.urlopen(scinews1)
        soup = BeautifulSoup(sci1, "html.parser")
        ssci1=("science news 1")
        f.write(ssci1)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1)     

        scinews2=("https://www.snexplores.org/")
        sci2 = request.urlopen(scinews2)
        soup = BeautifulSoup(sci2, "html.parser")
        ssci2=("science news 2")
        f.write(ssci2)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1)       

        scinews3=("https://www.sciencenews.org/")
        sci3 = request.urlopen(scinews3)
        soup = BeautifulSoup(sci3, "html.parser")
        ssci3=("science news 3")
        f.write(ssci3)
        f.write("\n")
        for headlines in soup.find_all('h3'):
            strhead = (headlines.get_text())
            strhead += "\n"
            f.write(strhead)
            time.sleep(1)                 
     

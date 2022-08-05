import time
from urllib import request
from bs4 import BeautifulSoup

genre = input("Write what type of news you want(sports,normal and science) ")


norm=("normal")
spor=("sports")
scinew=("science")
fullnam = ("Daily News.txt")
with open(fullnam, "w", encoding="utf-8") as f:

  if genre = norm:
    normalnews1=("https://www.aljazeera.com/")
    news1 = request.urlopen(normalnews1)
    soup = BeautifulSoup(news1, "html.parser")
    headlines = soup.select_one("#novel_honbun").text
    honbun += "\n" 

    f.write(honbun)

    print("part {:d} downloaded".format(part)) 

    time.sleep(1) 
    

    normalnews2=("https://www.cnn.com/")
    news2 = request.urlopen(normalnews2)
    soup = BeautifulSoup(news2, "html.parser")

    normalnews3=("https://www.washingtonpost.com/")
    news3 = request.urlopen(normalnews3)
    soup = BeautifulSoup(news3, "html.parser")

    allnormalnews=(normalnews1+normalnews2+normalnews3)
    

sportnews1=("")
sportnews2=("")
sportnews3=("")

scinews1=("")
scinews2=("")
scinews3=("")
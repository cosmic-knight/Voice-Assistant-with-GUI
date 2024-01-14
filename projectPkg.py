import os,pyttsx3,requests,time,random,webbrowser,httpx,AppOpener,postman,threading,killer
from bs4 import BeautifulSoup
from plyer import notification
from tkinter import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print("start")
# engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)
engine.runAndWait()
def wishMe(code):
    engine.setProperty('voice', voices[code].id)
    timeNow=int(time.strftime("%H"))
    if timeNow>=0 and timeNow<12:
        threading.Thread(target=speakThis, args=["Good Morning Sir"]).start()
    elif timeNow>=12 and timeNow<18:
        threading.Thread(target=speakThis, args=["Good Afternoon Sir"]).start()
    else:
        threading.Thread(target=speakThis, args=["Good Evening Sir"]).start()

def find_files(filename,a=True):
   result = []
   for root, dir, files in os.walk("C:\\Users"):
        if a==True:
            if filename in files:
                result.append(os.path.join(root, filename))
                break
        elif a==False:
            if filename in files:
                result.append(os.path.join(root))
   return result

def news():
    main_url = " https://newsapi.org/v2/top-headlines?country=in&apiKey=(Your API key)"
    res = requests.get(main_url)
    news = res.json()
    article = news["articles"]
    results = []
    threading.Thread(target=speakThis, args=["here are top headlines"]).start()
    s=""
    for ar in article:
        results.append(ar["title"])
    for i in range(10):
        s+=str(i+1)+") "+results[i]+"\n"
    print(s)
    return str(s)

def youtube(inputQuery):
    b=inputQuery.split()
    if (b[0]=="search" and b[1]=="youtube") or (b[0]=="youtube" and b[1]=="search"):
        a=b[3:]
        z=""
        for i in a:
            z=z+i
        opner="https://www.youtube.com/results?search_query="+z
        webbrowser.open(opner)
        print("Searching...")
        threading.Thread(target=speakThis, args=[f"Searching for {z}"]).start()
        ret="Searching "+str(z)+" in youtube"
        return ret
    elif b[0]=="youtube":
        a=b[2:]
        z=""
        for i in a:
            z=z+i
        opner="https://www.youtube.com/results?search_query="+z
        webbrowser.open(opner)
        print("Searching...")
        threading.Thread(target=speakThis, args=[f"Searching for {z}"]).start()
        ret="Searching "+str(z)+" in youtube"
        return ret
    elif b[0]=="search":
        a=b[1:-2]
        z=""
        for i in a:
            z=z+i
        opner="https://www.youtube.com/results?search_query="+z
        webbrowser.open(opner)
        print("Searching...")
        threading.Thread(target=speakThis, args=[f"Searching for {z}"]).start()
        ret="Searching "+str(z)+" in youtube"
        return ret
    elif b[1]=="in":
        a=b[3:]
        z=""
        for i in a:
            z=z+i
        opner="https://www.youtube.com/results?search_query="+z
        webbrowser.open(opner)
        print("Searching...")
        threading.Thread(target=speakThis, args=[f"Searching for {z}"]).start()
        ret="Searching "+str(z)+" in youtube"
        return ret

def closeCmd(t=1):
    time.sleep(t)
    os.system('cmd /c taskkill /F /IM cmd.exe')

def reminder(msg,tim):
    time.sleep(int(tim))
    notification.notify(title = 'REMINDER',message = msg)

def genImg(q):
    links=[]
    response = httpx.post("https://lexica.art/api/infinite-prompts", json={"text": q})
    prompts = [f"https://image.lexica.art/full_jpg/{ids['id']}" for ids in response.json()["images"]]
    for i in prompts:
        links.append(i)
    choosen=links[int(time.strftime("%S"))%len(links)-1]
    return choosen

def speakThis(smtg):
    engine.say(smtg)
    engine.runAndWait()

def takeCommand(inText,code=1):
    engine.setProperty('voice', voices[code].id)
    
    if "news" in inText or "headlines" in inText:
        a=news()
        return a

    elif ".com" in inText or ".org" in inText or ".in" in inText or ".gov" in inText or ".edu" in inText:
        a=inText.replace("open ","")
        print("Opening ",a)
        threading.Thread(target=speakThis, args=[f"Opening {a}"]).start()
        webbrowser.open(a)
        ans="Opening "+str(a)
        return (ans)

    elif "open" in inText and "." in inText:
        a=inText.replace("open ","")
        print("Opening ",a)
        b=find_files(a)
        threading.Thread(target=speakThis, args=[f"Opening {a}"]).start()
        threading.Thread(target=closeCmd, args=[]).start()
        os.system(f'cmd /c "{b[0]}"')
        re="opening"+" "+str(a)
        return re

    elif "search" in inText and "." in inText:
        a=inText.replace("search ","")
        print("Searching ",a)
        print("paths: ",find_files(a))
        paths=find_files(a)
        strPath=""
        for i in paths:
            strPath+=str(i)+","
        threading.Thread(target=speakThis, args=[f"Found {a}"]).start()
        return strPath

    elif "open" in inText:
        a=inText.replace("open ","")
        print("Opening ",a)
        threading.Thread(target=speakThis, args=[f"Opening {a}"]).start()
        AppOpener.open(a, match_closest=True)
        ans=a+" opened successfully"
        return (ans)

    elif "search" in inText and "youtube" in inText:
        a=youtube(inText)
        return a

    elif "google search" in inText:
        a=inText.replace("google search ","")
        b="https://www.google.com/search?q="+a
        print("Searching ",a)
        threading.Thread(target=speakThis, args=[f"Searching on google for {a}"]).start()
        webbrowser.open(b)
        ret="Searching"+str(a)
        return ret
    
    elif "generate" in inText:
        a=inText.split()
        a=a[4:]
        b=""
        for i in a:
            b+=i+" "
        webbrowser.open(genImg(b))
        print(f"Generating an image of {b}")
        threading.Thread(target=speakThis, args=[f"Generating an image of {b}"]).start()
        ret="Generating an image of "+str(b)
        return ret
    
    elif "search" in inText and "image" in inText:
        query=inText[5:]
        link=f"https://www.bing.com/images/search?q={query}&form=HDRSC3&first=1"
        r=requests.get(link)
        soup=BeautifulSoup(r.content,"html.parser")
        links=[]
        img=soup.find_all("img")
        for i in img:
            links.append(i)
        this=links[random.randint(9,20)]
        this=str(this)
        a=this.find("src")
        this=this[a+6:-14]
        webbrowser.open(str(this))
        return "Image found"
            
    elif "close all" in inText:
        killer.start()
        return "All applications closed successfully"

    elif "close " in inText:
        a=inText.replace("close ","")
        threading.Thread(target=speakThis, args=[f"Closing{a}"]).start()
        AppOpener.close(a)
        ret="Closing "+str(a)
        return ret

    elif "send" in inText:
        file=inText.replace("send ","")
        paths=find_files(file,False)
        path=paths[0]
        a=postman.start(path)
        threading.Thread(target=speakThis, args=[f"QR code generated successfully for {file}"]).start()
        return "QR created successfully..."
    
    elif "+" in inText or "-" in inText or "*" in inText or "/" in inText or "%" in inText:
            que=""
            for j,i in enumerate(inText):
                if (i=="+" or i=="-" or i=="*" or i=="/" or i=="%")and inText[j+2]!="o":
                    que+=i
                elif i=="%" and inText[j+2]=="o":
                    que+="/100*"
                elif i.isdigit():
                    que+=i
            ans=str(eval(que))
            threading.Thread(target=speakThis, args=[ans]).start()
            return ans
    
    elif "remind" in inText or "reminder" in inText:
        if "remind" in inText:
            a=inText.replace("remind me to ","")
        elif "reminder" in inText:
            a=inText.replace("add a reminder to ","")
        c=a.split()
        if c[-1]=="minutes":
            b=int(c[-2])*60
        elif c[-1]=="seconds":
            b=c[-2]
        else:
            threading.Thread(target=speakThis, args=[f"Please specify timing"]).start()
            return "Please specify timing"
        a=c[0:-3]
        txt=""
        for i in a:
            txt=txt+" "+i
        tim1=threading.Thread(target=reminder, args=[txt,b])
        tim1.start()
        threading.Thread(target=speakThis, args=[f"Reminder created successfully"]).start()
        return "Reminder created"

    elif "quit" in inText or "exit" in inText or "close" in inText:
        os.system('cmd /c taskkill /F /IM gui.exe')
        os.system('cmd /c taskkill /F /IM python3.11.exe')
        quit()

    elif "shutdown" in inText:
        speakThis("Shutting down")
        os.system("shutdown /s /t 1")
    
    elif "restart" in inText:
        speakThis("Restarting")
        os.system("shutdown /r /t 1")

    elif "logout" in inText:
        speakThis("Logging out")
        os.system("shutdown -l")
        
    else:
        url = "https://google.com/search?q=" + inText
        request_result = requests.get( url )
        soup = BeautifulSoup( request_result.text, "html.parser" )
        result = soup.find( "div" , class_='BNeawe').text
        if "₹" in result:
            result=result.replace("₹","rupees")
        threading.Thread(target=speakThis, args=[result]).start()
        return result

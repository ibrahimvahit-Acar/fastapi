from fastapi import Body, FastAPI,Response,status,HTTPException
import psycopg2
from  psycopg2.extras import RealDictCursor
import time
import requests
from bs4 import BeautifulSoup
from WebScraping import makale_cek
from Alghoritms import luhn,lex_rank,lsa_summary,giso
from pydantic import BaseModel

while True:
        try:
            conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Darkside.345',cursor_factory=RealDictCursor)
            conn.set_session(autocommit=True)
            cursor=conn.cursor()
            
            print("Succes")
            break
        except Exception as error:
            print("Failed",error)
            time.sleep(2)




def scrapingSonDakika():
    r = requests.get("https://www.sozcu.com.tr/son-dakika/")
    soup = BeautifulSoup(r.content,"lxml")
    news = soup.find_all("div",attrs={"class":"timeline-card"})

    for new in news:
        link = new.a.get("href")
        head = new.find("img", attrs={"loading": "lazy"})
        image = head.get("src").replace("?w=220&h=165&mode=crop", "?w=800&h=300&mode=crop")
        contenttext = makale_cek(link)
        imgtitle = new.find("img", attrs={"loading": "lazy"})
        title = imgtitle.get("alt")

        
        req = requests.get(link)
        soup2 = BeautifulSoup(req.content,"lxml")
        datetime = soup2.find("time")
        datetime=datetime.text
        WebSite="Sözcü"
        NewsType="Son Dakika"
        luhnSum=luhn(contenttext)
        lexSum=lex_rank(contenttext)
        lsaSum=lsa_summary(contenttext)
        gisoSum=giso(contenttext)

        try:
            cursor.execute("""INSERT INTO news(link,title,image,contenttext,datetime,webSite,newstype,luhnsum,lexsum,lsasum,gisosum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *""",(link,title,image,contenttext,datetime,WebSite,NewsType,luhnSum,lexSum,lsaSum,gisoSum))
            cursor.fetchone()
            conn.commit()        
        except Exception as Es:
             a=1





def scrapingEkonomi():
    r = requests.get("https://www.sozcu.com.tr/kategori/ekonomi/")
    soup = BeautifulSoup(r.content, "lxml")
    news = soup.find_all("div", attrs={"class": "news-item"})

    for new in news:
        link = new.a.get("href")
        head = new.find("img", attrs={"loading": "lazy"})
        image = head.get("src").replace("?w=220&h=165&mode=crop", "?w=800&h=300&mode=crop").replace(
            "?w=243&h=136&mode=crop", "?w=800&h=300&mode=crop")
        contenttext = makale_cek(link)
        imgtitle = new.find("img", attrs={"loading": "lazy"})
        title = imgtitle.get("alt")
        req = requests.get(link)
        soup2 = BeautifulSoup(req.content, "lxml")
        datetime = soup2.find("time")
        datetime=datetime.text
        WebSite="Sözcü"
        NewsType="Ekonomi"
        luhnSum=luhn(contenttext)
        lexSum=lex_rank(contenttext)
        lsaSum=lsa_summary(contenttext)
        gisoSum=giso(contenttext)

        try:
            cursor.execute("""INSERT INTO news(link,title,image,contenttext,datetime,webSite,newstype,luhnsum,lexsum,lsasum,gisosum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *""",(link,title,image,contenttext,datetime,WebSite,NewsType,luhnSum,lexSum,lsaSum,gisoSum))
            cursor.fetchone()
            conn.commit()        
        except Exception as Es:
             a=1




def scrapingDunya():
    r = requests.get("https://www.sozcu.com.tr/kategori/dunya/")
    soup = BeautifulSoup(r.content, "lxml")
    news = soup.find_all("div", attrs={"class": "news-item"})

    for new in news:
        link = new.a.get("href")
        head = new.find("img", attrs={"loading": "lazy"})
        image = head.get("src").replace("?w=220&h=165&mode=crop", "?w=800&h=300&mode=crop").replace(
            "?w=243&h=136&mode=crop", "?w=800&h=300&mode=crop")
        contenttext = makale_cek(link)
        imgtitle = new.find("img", attrs={"loading": "lazy"})
        title = imgtitle.get("alt")
        req = requests.get(link)
        soup2 = BeautifulSoup(req.content, "lxml")
        datetime = soup2.find("time")
        datetime=datetime.text
        WebSite="Sözcü"
        NewsType="Dünya"
        luhnSum=luhn(contenttext)
        lexSum=lex_rank(contenttext)
        lsaSum=lsa_summary(contenttext)
        gisoSum=giso(contenttext)

        try:
            cursor.execute("""INSERT INTO news(link,title,image,contenttext,datetime,webSite,newstype,luhnsum,lexsum,lsasum,gisosum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *""",(link,title,image,contenttext,datetime,WebSite,NewsType,luhnSum,lexSum,lsaSum,gisoSum))
            cursor.fetchone()
            conn.commit()        
        except Exception as Es:
             a=1

def scrapingOtomotiv():
    r = requests.get("https://www.sozcu.com.tr/kategori/otomotiv/")
    soup = BeautifulSoup(r.content, "lxml")
    news = soup.find_all("div", attrs={"class": "news-item"})

    for new in news:
        link = new.a.get("href")
        head = new.find("img", attrs={"loading": "lazy"})
        image = head.get("src").replace("?w=220&h=165&mode=crop", "?w=800&h=300&mode=crop").replace(
            "?w=243&h=136&mode=crop", "?w=800&h=300&mode=crop")
        contenttext = makale_cek(link)
        imgtitle = new.find("img", attrs={"loading": "lazy"})
        title = imgtitle.get("alt")
        req = requests.get(link)
        soup2 = BeautifulSoup(req.content, "lxml")
        datetime = soup2.find("time")
        datetime=datetime.text
        WebSite="Sözcü"
        NewsType="Otomotiv"
        luhnSum=luhn(contenttext)
        lexSum=lex_rank(contenttext)
        lsaSum=lsa_summary(contenttext)
        gisoSum=giso(contenttext)

        try:
            cursor.execute("""INSERT INTO news(link,title,image,contenttext,datetime,webSite,newstype,luhnsum,lexsum,lsasum,gisosum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *""",(link,title,image,contenttext,datetime,WebSite,NewsType,luhnSum,lexSum,lsaSum,gisoSum))
            cursor.fetchone()
            conn.commit()        
        except Exception as Es:
             a=1
    print("Ekleme Bitti")


















app=FastAPI()

def login_user(login):
    cursor.execute("""SELECT * FROM users WHERE (username= %s OR email=%s OR phone=%s) AND password=%s """,(login.user,login.user,login.user,login.password))
    result=cursor.fetchall()
    resLen=len(result)
    if resLen >0:
        res=True
    else: 
        res=False
    return res


def searchUser(user):
    cursor.execute("""SELECT * FROM users WHERE username= %s OR email=%s OR phone=%s """,(user.username,user.email,user.phone))
    result=cursor.fetchall()
    result=len(result)
    if result==0:
        result=True
    else:
        result=False
    return result
#Schema ları belirleme gelen verilerin türlerini ve isimlerini tanımlama
class User(BaseModel):
    username:str
    password:str
    email:str
    phone:str

class Login(BaseModel):
    user:str
    password:str

@app.get("/")
def root():
    return {"message": "Ana Sayfa"}


@app.post("/usercreate",status_code=status.HTTP_201_CREATED)
def create_user(user:User):

    result=searchUser(user)
    if result==True:
        cursor.execute("""INSERT INTO users(username,email,phone,password) VALUES (%s, %s, %s, %s) RETURNING *""",(user.username,user.email,user.phone,user.password))
        new_user=cursor.fetchone()
        conn.commit()
        return {'data':new_user}
    else:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,detail="Bu bilgilerde zaten kullanıcı var")

@app.post("/login")
def get_user(login:Login):
    print(login.user)
    result=login_user(login)
    return{"data":result}

@app.get("/sozcu/sondakika")
def sozcuSondakika():
    scrapingSonDakika()
    cursor.execute("""SELECT * FROM news WHERE newstype='Son Dakika' AND website='Sözcü' """)
    posts=cursor.fetchall()
    return {"data":posts}


@app.get("/sozcu/ekonomi")
def sozcuEkonomi():
    scrapingEkonomi()
    cursor.execute("""SELECT * FROM news WHERE newstype='Ekonomi' AND website='Sözcü' """)
    posts=cursor.fetchall()
    return {"data":posts}

@app.get("/sozcu/dünya")
def sozcuDünya():
    scrapingDunya()
    cursor.execute("""SELECT * FROM news WHERE newstype='Dünya' AND website='Sözcü' """)
    posts=cursor.fetchall()
    return {"data":posts}
@app.get("/sozcu/otomotiv")
def sozcuOtomotiv():
    scrapingOtomotiv()
    cursor.execute("""SELECT * FROM news WHERE newstype='Otomotiv' AND website='Sözcü' """)
    posts=cursor.fetchall()
    return {"data":posts}





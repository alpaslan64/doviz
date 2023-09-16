import requests
from bs4 import BeautifulSoup
import time
from os import system
#Yukarıdaki satırlarda "request" kütüphanesini, "BeautifulSoup" kütüphanesini, "time" kütüphanesini ve "os" kütüphanesini kodumuza import ettik. 


def doviz_kuru():
    url = "https://www.doviz.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #doviz_kuru fonksiyonu oluşturduk ve bağlantı kuracağımız disteye gösterdik. Siteye get istekleri gönderiyoruz. HTML parse işlemini yapıyoruz.

    gram_altin = soup.find("span", {"class": "value", "data-socket-key": "gram-altin", "data-socket-attr": "s"}).text.strip()
    dolar_tl = soup.find("span", {"class": "value", "data-socket-key": "USD", "data-socket-attr": "s"}).text.strip()
    euro_tl = soup.find("span", {"class": "value", "data-socket-key": "EUR", "data-socket-attr": "s"}).text.strip()
    sterlin_tl = soup.find("span", {"class": "value", "data-socket-key": "GBP", "data-socket-attr": "s"}).text.strip()
    brent = soup.find("span", {"class": "value", "data-socket-key": "BRENT", "data-socket-attr": "s"}).text.strip()
    bitcoin = soup.find("span", {"class": "value", "data-socket-key": "bitcoin", "data-socket-attr": "s"}).text.strip()
    borsa = soup.find("span", {"class": "value", "data-socket-key": "XU100", "data-socket-attr": "s"}).text.strip()
    #Burada çekmek istediğimiz verileri çekiyoruz. Uygun değerli olup olmadğığnı test ettikten sonra çekme işlemini yapıp değişkenlere değerler atanıyor.
    
    print("--------------------------")    
    print("Gram Altın: " + gram_altin)
    print("Dolar: " + dolar_tl)
    print("Euro : " + euro_tl)
    print("Sterlin: " + sterlin_tl)
    print("Brent Petrol: " + brent)
    print("Borsa (100): " + borsa)
    print("Bitcoin: " + bitcoin)
    print("--------------------------")
    #Ekrana yazdırma bloğunu burda görüyoruz.

while True:
    doviz_kuru()
    time.sleep(2)
    system("cls")
    #Burada da sonsuz döngüde fonksiyon çalışıyor, 2 saniye bekliyor sonra terminali temizliyor. Bu şekilde döngü devam ediyor.
    
# Yapımcılar = https://github.com/alpaslantiryaki || 

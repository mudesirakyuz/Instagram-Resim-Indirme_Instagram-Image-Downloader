import urllib
from bs4 import BeautifulSoup
import datetime

def indir(url):
    print("İndirme Başlatılıyor...")
    f = urllib.request.urlopen(url)
    s = BeautifulSoup(f.read(),'html.parser')
    mTag = s.find_all('meta', {'property':'og:image'})
    imgUrl = mTag[0]['content']
    fileName = datetime.now().strftime("%Yç%m.%d_%H.%M.%S")+".jpg"
    urllib.request.urlretrieve(imgUrl,fileName)
    print(fileName+" dosyası başarıyla indirildi...")

print("URL: ")
URL = input()
indir(URL)
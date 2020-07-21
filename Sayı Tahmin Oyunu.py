from time import time,sleep
from random import randint,choice,sample
from os import chdir,makedirs,remove,system,listdir
giris=True
class Bonus:
    def __init__(self,isim,sayisal_deger):
        self.isim=isim
        self.sayisal_deger=sayisal_deger


#def eklenecekOgeler(x):
#    pass
#def stokDurumu(x):
#    pass
#def jokerDurumu(x):
#    pass
#def lvlKontrolu(x):
class Test:
    #init yok çünkü tek bir örnek olcak
    isim="Test"
    odul=10
    ceza=5
    ucret=0
    acildiğiLvl=0
    hak=5
    can=5
    soruSayisi=randint(10,30)
    ucret=2
    ilk=randint(1,100)
    soruAraligi=randint(ilk,randint(ilk,8225))
    
  

class TekSoru:
    #init yok çünkü tek bir örnek o
    isim="Tek Soru"
    odul=10
    ceza=5
    hak=3
    can=0
    ucret=0
    acildiğiLvl=1
    soruSayisi=1
    sans=20
    ucret=0
    ilk=randint(1,9576843)
    soruAraligi=randint(ilk,randint(ilk,87653421225))

class ZorMod:
    #init yok çünkü tek bir örnek o
    #bir hatada gider 10 soru
    isim="Zor Mod"
    odul=10
    ceza=5
    ucret=0
    acildiğiLvl=10
    soruSayisi=10
    sans=0
    ucret=10
    ilk=randint(1,9576843)
    soruAraligi=randint(ilk,randint(ilk,87653421225))
    hak=0
    can=0
    

class HızlıMaraton:
    #init yok çünkü tek bir örnek o
    #20 saniye içinde cevapladın cevapladın
    isim="Hızlı Maraton"
    odul=10
    ceza=5
    ucret=0
    acildiğiLvl=15
    sans=10
    ucret=5
    ilk=randint(1,2)
    soruAraligi=randint(ilk,randint(ilk,10))
    hak=1000000000000000000000000000000
    soruSayisi=1234567890
    can=134532364578980
    # soruSayisi=yok sonsuz
    #20 saniye bitmedikçe infiinite loop dönsün



class KolayMod:
    #init yok çünkü tek bir örnek o
    #sınırsız hata hakkı
    isim="Kolay Mod"
    odul=10
    ceza=5
    ucret=0
    acildiğiLvl=5
    sans=0
    ucret=0
    soruSayisi=10
    ilk=randint(1,10)
    soruAraligi=randint(ilk,randint(ilk,50))
    can=11#yani sporu sayisi 10 olduğuna göre sonsuz
    hak=55#en fazla 1 ile 50 arasında olacağından np (soru başı hak sayısıs)
    #süre yok
    


    



class OyunModu:
    def __init__(self,isim,odul,ceza,ucret,sure,soruSayisi,soruAraligi,can,hak,sans):
        #para:oynaömak için verilmesi gereken par(0 da olabilir)
        #odul kazanınca ceza kaybedince gelir
        
        self.isim=isim               
        self.odul=odul
        self.ceza=ceza
        self.ucret=ucret
        self.sure=sure
        self.soruSayisi=soruSayisi
        self.soruAraligi=soruAraligi
        self.can=can
        self.hak=hak
        self.sans=sans
    
    acildiğiLvl=0

    def copy(self):
        return OyunModu(self.isim,self.odul,self.ceza,self.ucret,self.sure,self.soruSayisi,self.soruSayisi,self.can,self.hak,self.sans)


    
class Kullanici:
    def __init__(self,level,isim,kullanici_adi,sifre,bakiye):
        self.level=level
        self.isim=isim
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre
        self.bakiye=bakiye
    


class Level:
    def __init__(self,bonuslar:list,OyunModlari:list):
        self.bonuslar=bonuslar#list in icinde LvlBonus classı
        self.OyunModlari=OyunModlari#listin içine oyunöodu class ı
        




     

class Dukkan:
    def __init__(self,isim,esyalar:list):
        self.isim=isim
        self.esyalar=esyalar



    

 
#kullanıcının marketteki şeylerle ve lvl ile kazanabilceği imkanlar


class Esya:
    def __init__(self,stok,fiyat,isim,bonuslar:list,sure):
        self.stok=stok
        self.fiyat=fiyat
        self.isim=isim
        self.bonuslar=bonuslar

alinanEsyalar=[]
girenKullanici=Kullanici(None,None,None,None,None)
dukkanlar=[]
#esyalar=[]
oyunmodlari=[]

kullanicilar=[]
girisBonusuVerildi=False
girisBonusu=0
sistemLevelleri=[Test(),TekSoru(),ZorMod(),HızlıMaraton(),KolayMod()]#__init__ ayarlanınca doldur burayı
jokerler=["hak","can","sure","odul","ceza","sans"]
kelimeler=["Extra","Az","Moralci","Extrem","Yalan","Sanal","Savaşçı","Tecrübeli","Amatör","Acemi","Kalfa","Dovakhiin","Master","Usta","Legend"]
secenekler=[" "]
secenekler+=[x for x in range(3600,98765)]
sistemDukkanlari=["Sistem Dükkanı","Fakirhane","Bilge","Ekmek Teknesi","Ustanın Yeri"]
joker=choice(jokerler)
#randomEsyalar=[Esya(randint(1,787867),randint(100,30000),f"{choice(kelimeler)} {joker}",[Bonus(f"{joker}" for i in range(randint(1,15),f"{randint(0,16)}" for i in range(randint(1,15)) for i in range(randint(10,578))))]
randomEsyalar=[Esya(randint(10,20),randint(100,1000),(choice(kelimeler)+joker),[Bonus(joker,randint(0,100))  for i in range(randint(0,20))],randint(10000,1000000))]
#    pass





    ##dosya işlemlerini de yap
    

#class Test(OyunModu):
#    pass

#class TekSoru(OyunModu):
#    pass

#class ZorMod(OyunModu):
#    #bir hatada gider 10 soru

#class HızlıMaraton(OyunModu):
#    #20 saniye içinde cevapladın cevapladın


#class KolayMod(OyunModu):
#    #sınırsız hata hakkı






try:
    for klasor in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar"):
        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(klasor),"r") as dosya:
            veri=dosya.read().split("\n")
                
            kullanicilar.append(Kullanici(int(veri[0]),klasor,veri[1],veri[2],int(veri[3])))

           
except FileNotFoundError:
    try:    
        makedirs(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar")

    except FileExistsError:
        pass





        





            
            
            

            

        









def baslangic(isim):
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    #tüm dosya işlemleri falan burda

    for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar".format(girenKullanici.isim)):
        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}".format(klasor,i),"w") as dosya:
            veri=dosya.read().split("\n")
            content=[]
            for index,ii in enumerate(veri):
                if (index-1) %5==0:
                    
                    content.append(Esya(int(veri[index]),int(veri[index+1]),veri[index+2],[Bonus(i.split()[0],i.split()[1]) for i in veri[index+3].split(",")],veri[index+3]))
                           
                    

    dukkanlar.append(Dukkan(veri[0],content))

    for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{isim}\Alınan Eşyalar"):
        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{isim}\Alınan Eşyalar\{}".format(i),"r") as dosya:

            veri=dosya.read().split("\n")
           
            alinanEsyalar.append(Esya(int(veri[0]),int(veri[1]),veri[3],[Bonus(i.split(" ")[0],i.split(" ")[1]) for i in veri[index+3].split(",")],veri[5]))



    for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Oyun Modları".format(isim)):
        #acildiği lvl  isim odul ceza ucret
        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Oyun Modları\{}".format(isim,i)) as dosya:
            veri=dosya.read().split("\n")
            aralik=veri[6].split(" ")
            aralik[0]=int(aralik[0])
            aralik[1]=int(aralik[1])
            
            oyunmodlari.append(OyunModu(veri[0],int(veri[1]),int(veri[2]),int(veri[3]),int(veri[4]),int(veri[5]),aralik,int(veri[7]),int(veri[8]),int(veri[9])))
            

    return 1


 





def hesapOlustur():

    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri

    def isim1():
        global isim
        system("cls")
        isim=input("İsminiz: ")
        if isim.isalpha():
            return 1
        else:isim()

    def parola1():
        global parola
        system("cls")
        parola=input("Parolanız: ")
        if len(parola)>=6:return
        else:print("Parola 6 veya daha fazla karakter içermeli!!"),sleep(3),parola()



    def kullanici_adi1():
        global kullanici_adi
        system("cls")
        kullanici_adi=input("Kullanıcı Adı: ")
        if kullanici_adi:return
        
        else:print("Geçersiz Değer!!"),sleep(3), kullanici_adi()

    def veriTabani():
        try:
            global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
            chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar")
            makedirs(isim)
            chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}".format(isim))
            makedirs("Dükkanlar")
            makedirs("Alınan Eşyalar")
            makedirs("Oyun Modları")
            
            with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(isim),"w") as dosya:
                dosya.write(f"0\n{kullanici_adi}\n{parola}\n{1000}")

            print("Hoşgeldin Hediyesi olarak size 1000kredi veriyoruz!!!")
            kullanicilar.append(Kullanici(0,isim,kullanici_adi,parola,0))

            joker=choice(jokerler)
            #randomEsyalar=[Esya(randint(1,787867),randint(100,30000),f"{choice(kelimeler)} {joker}",[Bonus(f"{joker} {randint(0,16)}") for i in range(randint(1,15))],choice(secenekler)) for i in range(randint(10,578))]
            randomEsyalar=[Esya(randint(10,20),randint(100,1000),(choice(kelimeler)+joker),[Bonus(joker,randint(0,100))  for i in range(randint(0,20))],randint(10000,1000000))]
            for i in sistemDukkanlari:
                with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}.txt".format(isim,i),"w") as dosya:
                    dosya.write(i)
                    for i in randomEsyalar:
                        bonuslar1=",".join([f"{x.isim} {x.sayisal_deger}" for x in i.bonuslar])
                        dosya.write(f"\n{i.stok}\n{i.fiyat}\n{i.isim}\n{bonuslar1}")


                    joker=choice(jokerler)
                    #randomEsyalar=[Esya(randint(1,787867),randint(100,30000),f"{choice(kelimeler)} {joker}",[Bonus(f"{joker} {randint(0,16)}") for i in range(randint(1,15))],choice(secenekler)) for i in range(randint(10,578))]
                    randomEsyalar=[Esya(randint(10,20),randint(100,1000),(choice(kelimeler)+joker),[Bonus(joker,randint(0,100))  for i in range(randint(0,20))],randint(10000,1000000))]
        except FileExistsError:
            pass

        return 1


        #lari=["Sistem Dükkanı","Fakirhane","Bilge","Ekmek Teknesi","Ustanın Yeri"]



    isim1()
    parola1()
    kullanici_adi1()
    veriTabani()

    print("Hesap Başarılı Bir Şekilde Oluşturuldu!!!")
    sleep(3)
    retrun 1
    #her kullanıcının dosyasının adı (klasörünün) adı isim değişkeni olsun
    #kullanıcı bilgileri için dosya adı Bilgiler.txt birinci satır=level,ikinci satır=kullanıcı adı,üçüncü satır= şifre,dördüncü satır=bakiye
    #kullanıcının kişisel klasörleri: Dükkanlar,Alınan Eşyalar,OyunModlari 
    #varsayılan oyun modları ve dükkan yeni kullanıcı oluişturulduğuında onların dükkan ve oyun modu klasörlerine eklensin böylece veriler çekilirken onlar da gelir
        ########3dükkana yeni eklencek eşyalar için kullanıcın dükkanlar klasöründe her dükkana bir txt oluştur 
    #sonra ilk satıra dülkkan ismi yaz sonra alt alta tüm eşyaları şu şekilde sırala:
    ##stok=1.satır 2.satır=fiyat 3.satır=isim 
    #4.satır=tüm bonusları yaz aralara virgül koy(son bonussa koyma) her bonusun da adı sayısal_deger(arada sadece ad ile sayısal değer arasında bpoşluk olabilir) 
    #5.satır=kalan süre
    
    ##############kullanıcılar klasööründe adamın kendi isminde klasörün iöçinbe oluşturulcak dosyalar: Bilgiler.txt Alınan Eşyalar, Oyun Modları ,Dükkanlar
    ########oyun modlarına sistem modlarını ekleme onlar başka sekilde depolanıypo
    ####level değişkeninin ilk oluştururken 00000000000 olarakaa ayarla
    ###########sistem  oyun modlarını dosyaya yazma 




def girisYap():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    def kullaniciAdi():
        system("cls")
        kullanici_adi=input("Kullanıcı Adınız: ")
        basari=False
        for i in kullanicilar:
            if i.kullanici_adi==kullanici_adi:
                print(f"Hoşgeldiniz {i.isim}")
                parola=input("Parolanızı Rica Ediyim: ")
                if i.sifre==parola:
                    girenKullanici=i
                    print("Başarıyla giriş yapıldı!!")
                    sleep(2.7)
                    basari=True
                    break

                else:
                    print("Geçersiz Değer!!!")
                    kullanici_adi()

        if not basari:kullaniciAdi()
        
        baslangic(girenKullanici.isim)
        kontrol()

    kullaniciAdi()


    #girenKullanici.append() ya giren kişiyi yap
    #baslangic fonksiyonunu giriş yapılanh hesabın "İSİM" değişkenini paramtere olarak verip çağır giriş yapıldıktan sonra
    
    


def oyunModuOlustur():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    while True:
        system("cls")
        isim=input("Oyun modunun ismi: ")
        if isim.isalpha():break 
        else:print("Geçersiz Değer"),sleep(2)

    while True:
        system("cls")
        odul=input("Oyun modunun ödülü(ödül olsun istemiyorsanız 0 seçin)")
        if odul.isdigit() : break 
        else:print("Geçersiz Değer"),sleep(3)

    while True:
        system("cls")
        ceza=input("Oyun modunun cezası(ceza olsun istemiyorsanız 0 seçin)")
        if ceza.isdigit(): break 
        else:print("Geçersiz Değer"),sleep(3)

    while True:
        
        system("cls")
        ucret=input("Oyun modunun ücreti(ücreti olsun istemiyorsanız 0 seçin)")
        if ucret.isdigit(): break 
        else:print("Geçersiz Değer"),sleep(3)

    while True:
        system("cls")
        sure=input("modun Süresi(saniye cinsinden)(sure olsun istemiyorsanız 0 seçin)")
        if sure.isdigit():break 
        elif sure=="0":
            sure=""
            break
        else :print("Geçersiz Değer"),sleep(3)



    while True:
        system("cls")
        soruSayisi=input("modun Soru Sayısı")
        if soruSayisi.isdigit():break 
        else :print("Geçersiz Değer"),sleep(3)

    while True:
        system("cls")
        try:
            aralik=input("Sorulardaki sayıların aralığı (a b şeklinde girin)(boşluk olacak şekilde)").split(" ")
            if  aralik[0].isdigit() and aralik[1].isdigit()and len(aralik)==2 and aralik[0]<aralik:break 
        except:
            print("Geçersiz Değer!!")
            sleep(2.5)


    while True:
        system("cls")
        can=input("Modun tanıdğı  can sayıssı(cAN SAYISI olsun istemiyorsanız 0 seçin)")
        if can.isdigit():break 
        elif can=="0":
            can=""
            break 
        else:print("Geçersiz Değer"), sleep(3)

    while True:
        system("cls")
        sans=input("Modun Tandığı Şans: (şans olsun istemiyorsanız 0 seçin)")
        if sans.isdigit(): break 
        else:print("Gçersiz Değer"), sleep(3)

    
    while True:
        system("cls")
        hak=input("modun Soru başına hak sayısı(hak olsun istemiyorsanız 0 seçin)")
        if hak.isdigit():break
        elif hak=="0":
            hak=""
            break 
        else :print("Geçersiz Değer"),sleep(3)

    with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{girenKullanici.isim}\Oyun Modları\{}".format(isim),"w") as dosya:
        dosya.write(f"{isim}\n{odul}\n{ceza}\n{ucret}\n{sure}\n{soruSayisi}\n{aralik}\n{can}\n{hak}\n{sans}")

    oyunmodlari.append(OyunModu(isim,odul,ceza,ucret,sure,soruSayisi,aralik,can,hak,sans))
    return 1

        
        ##isim=birinci satır               
        ##odul=ikinci satır
        ##ceza=üçüncü satır
        ##ucret=dördüncü satır
        #sure=beşinci satır
        #soru sayısı=altıncı satır
        #soruların aralığı randint() için=yedinci satır
        #can(soruyu sana verilen hak kadar bilemezsen bir eksilir)=sekizinci satır
        #9.satır=sans
        #hak=bir soru için verilcek hak
        #bu soruları sormadan önce ilk başta bu özellikten ister misiniz diye sor (isim dışında) ve istemiyorsa süresiz olsun diyposa mesela dosyada onun yerine \n yaz 
        #yani arda boş satır olsun 
        #kullanıcıya bu olsun istemiyosanız 0 a basın de ve if secim==0 : \n yazılcak dosyaya 

        #######################sans eğer 0sa kullancıı sadece doğru cevap verdiğinde doğru kabul edilsin yükselidkce mesela 1 se
        # kullancının cevabı answera 2 yakınsa doğru sans 3 se kullanıcın
        # cevabı 4 yakınsa normal cevaba doğru kabuıl edilsin misal
        #sans ın sadece 0 100 arasında seçilmesine izin ver
    

def dukkanaEsyaEkle():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    while True:
        system("cls")
        karsilik={}
        for i in enumerate(dukkanlar):
            print(f"[{i[0]}] {i[1].isim}") 
            karsilik.setdefault(i[0],i[1])
    
        secim=input("Seçiiniz: ")
        for i in list(karsilik.keys()):
            if str(i)==secim :
                dukkan=karsilik[secim]
                break
            elif i==len(dukkanlar)-1:
                continue

        break

    joker=choice(jokerler)
    #randomEsyalar=[Esya(randint(1,787867),randint(100,30000),f"{choice(kelimeler)} {joker}",[Bonus(f"{joker} {randint(0,16)}") for i in range(randint(1,15))],choice(secenekler)) for i in range(randint(10,578))]
    randomEsyalar=[Esya(randint(10,20),randint(100,1000),(choice(kelimeler)+joker),[Bonus(joker,randint(0,100))  for i in range(randint(0,20))],randint(10000,1000000))]
    
    while True:
        system("cls")
        stok=input("Kaç Tane Getirtelim Ondan?? ")
        if stok.isdigit():break 
        else:
            print("Ge.çersiz Değer!!!")
            sleep(2.5)

    while True:
        system("cls")
        fiyat=input("Kaça Getirtelim Ondan?? ")
        if fiyat.isdigit():break 
        else:
            print("Ge.çersiz Değer!!!")
            sleep(2.5)

    while True:
        system("cls")
        isim=input("Kaç Tane Getirtelim Ondan?? ")
        if stok.isalpha():break 
        
        else:
            print("Ge.çersiz Değer!!!")
            sleep(2.5)

    while True:
        system("cls")
        eklenecekler=[]
        tane=input("Kaç Tane Bonus Gireceksiniz??")


       
        print("seçilebilir Bonuslar")
        for i in jokerler:
            print(i)
        for i in range(1,int(tane)+1):
            while True:
                global bonus
                bonus=input(f"{i}. bonus:")
                for ii in jokerler:
                    if ii.lower()==bonus.lower():
                        bonus=ii
                        break
                    elif jokerler.index(ii)==len(jokerler)-1:
                        break
                        

            while True:
                global sayi
                sayi=input("Ne kadar Bonus Versin Bu:")
                if not sayi.isdigit() : 
                    print("Geçersiz Değer")
                    sleep(2.8)
                    continue
                break


            eklenecekler.append(f"{bonus} {sayi}")


        else:
            print("Geçersiz Değer!!")
            sleep(2.5)

    while True:
        system("cls")
        sure=input("Ne kadar zaman snra getireliM?(saniye cinsinden)")
        if sure.isdigit(): 
            para=int(sure/3600)*10+len(eklenecekler)*5+stok*8+dukkanlar.index(dukkan)*7
            break 
        else:
            print("Ge.ersiz Değer")
            sleep(2.5)
    
    print(f"Gereken Ücret : {para}")
    if girenKullanici.bakiye>=para:
        girenKullanici.bakiye-=para
        sure+=3600
        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}.txt".format(girenKullanici.isim,isim),"a+") as dosya:
            bonuslar1=",".join([f"{x.split()[0]} {x.split()[1]}" for x in i.bonuslar])
            dosya.write(f"\n{i.stok}\n{i.fiyat}\n{i.isim}\n{bonuslar1}")

        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\{}".format(girenKullanici.isim,isim),"w") as dosya:
            dosya.write(sure+"\n"+time())


        
            


    else:
        print("Yeteri kadar <Paanız Yok, sizin için kostimüze ediliyor...")
        sure+=(girenKullanici.bakiye-para)*10000


    return 1 



    #her kullanıcının dosyasının adı (klasörünün) adı isim değişkeni olsun
    #kullanıcı bilgileri için dosya adı Bilgiler.txt birinci satır=level,ikinci satır=kullanıcı adı,üçüncü satır= şifre,dördüncü satır=bakiye
    #kullanıcının kişisel klasörleri: Dükkanlar,Alınan Eşyalar,OyunModlari 
    #varsayılan oyun modları ve dükkan yeni kullanıcı oluişturulduğuında onların dükkan ve oyun modu klasörlerine eklensin böylece veriler çekilirken onlar da gelir
        ########3dükkana yeni eklencek eşyalar için kullanıcın dükkanlar klasöründe her dükkana bir txt oluştur 
    #sonra ilk satıra dülkkan ismi yaz sonra alt alta tüm eşyaları şu şekilde sırala:
    ##stok=1.satır 2.satır=fiyat 3.satır=isim 
    #4.satır=tüm bonusları yaz aralara virgül koy(son bonussa koyma) her bonusun da adı sayısal_deger(arada sadece ad ile sayısal değer arasında bpoşluk olabilir) 
    #5.satır=kalan süre
    



def oyunModuSil():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    def sil():
        system("cls")
        if oyunmodlari:
            karsilik={}
            
            for i in enumerate(oyunmodlari):
                print(f"[{i[0]}] {i[1]}")
                karsilik.setdefault(i[0],i[1])

                secim=input("Hangisini silcen?")
                for i in list(karsilik.keys()):
                    if i==secim:
                        oyunmodlari.remove(karsilik[secim])
                        remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Oyun Modları\{}".format(girenKullanici.isim,karsilik[secim].isim))
            
                        return
                sil()       
        else:
            print("Silincek Oyun Modu Yok")
            sleep(3)
            

        return 1


def oyna():
    
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    
    system("cls")
    count=0
    karsilik={}
    for i in sistemLevelleri:
        if i.acildiğiLvl<=girenKullanici.level:
            count+=1

            print(i.isim)
            karsilik.setdefault(count,i)  

    for i in oyunmodlari:
        count+=1
        print(i.isim)
        karsilik.setdefault(count,i)

    secim=input("Seçiminiz: ")
    if secim in list(karsilik.keys()):
        secim=karsilik[secim].copy()
        


        if  not secim.ucret>=girenKullanici.bakiye: 
            print("Yeterli Balkiye Yok!!"),sleep(2.6)
            return 1
        girenKullanici.bakiye-=secim.ucret
        while True:
            sayi=input("Başlamadan Önce Biraz Joker??(sayisi)")
            if sayi.isdigit():
                for i in range(int(sayi)):
                    if alinanEsyalar:
                        karsilik1={}
                        coun1t=0
                        while True:
                            for i in alinanEsyalar:
                                count1+=1
                                print(f"[{count1}]---->>>"+i.isim+"------>>>"+ [x[0]+x[1]  for x in [a for a in i.bonuslar]])
                                karsilik1.setdefault(count1,i)

                                


                            seecim=input("Seçiminiz: ")
                            if seecim in list(karsilik1.keys()):
                                for i in list(karsilik1.keys()):
                                    if i == seecim:
                                        for ii in karsilik1[seecim].bonuslar:
                                            secim.ii.isim+=int(ii.saysisalDeger)                                                          
                                            for ii in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Kullanıcılar\{}\Alınan Eşyalar".format(girenKullanici.isim)):
                                                if ii.lower()==karsilik1[seecim].lower()+".txt":
                                                    esyamiz=alinanEsyalar[alinanEsyalar.index(karsilik1[seecim])]
                                                    if esyamiz.stok>=1:
                                                        with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{girenKullanici.isim}\Alınan Eşyalar\{}".format(ii),"w",encoding="utf-8") as dosya:
                                                            
                                                            esyamiz.stok-=1
                                                            bonuslar1=",".join([f"{x[0]} {x[1]}" for x in esyamiz.bonuslar])
                                                            dosya.write(f"{esyamiz.stok}\n{esyamiz.fiyat}\n{esyamiz.isim}\n{bonuslar1}\n{esyamiz.sure}")
                                                        break
                                                    
                                                    else:
                                                        remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Alınan Eşyalar\{}".format(girenKullanici.isim,ii))
                                                        break
                                                        

                                break

                            else:
                                print("Geçersiz Değer")
                                sleep(2.6)

                    else:
                        print("Eşya Kalmadı!!")
                        sleep(2.5)
                        break

                
                print(f"{secim.isim} moduna hoş geldiniz!!!!")
                kontrol()
                baslangic(girenKullanici.isim)
                for i in secim.soruSayisi:
                    baslangic1=time()
                    aralik=secim.soruAraligi
                    if not hak:hak=aralik[0]+2
                    if not can:can=aralik[0]+2
                    deneme=hak
                    
                    for hak in secim.hak:
                        
                        if not secim.sure and time()-baslangic1>=20:
                            print("Oyun Bitii!!!")
                        
                            sleep(2.6)
                            return 1
                        deneme-=1
                        cvp=randint(aralik[0],aralik[1])
                        soru=input(f"{aralik[0]} {aralik[1]} arasında bir sayı tutuldu?? Tahminleri alıyım bakıyım!!!")
                        try:
                            if int(soru)==cvp or secim.sans*5+int(soru)==cvp or secim.sans*5-int(soru)==cvp:
                                print("Doğru!!")
                                girenKullanici.bakiye+=deneme*secim.odul
                                girenKullanici.level+=0.00001*secim.odul*secim.sans
                                break
                            elif deneme<=1:
                                print("Bu soruyu Bilemediniz!!")
                                girenKullanici.bakiye-=secim.ceza
                                secim.can-=1 
                                if secim.can==0:
                                    print("Oyunu Kaybettiniz!!")
                                    sleep(2.5)
                                    girenKullanici.level+=0.001
                                    return 1
                                else:break

                        except:print("Hatalı değer!!,Bir hakkınızı kaybettiniz"),sleep(2.9999999)


                with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(girenKullanici.isim),"w") as dosya:
                    dosya.write(f"{girenKullanici.level}\n{girenKullanici.kullanici_adi}\n{girenKullanici.sifre}\n{girenKullanici.bakiye}")

                
                

                break
            else:
                print("GEçersiz Değer")
                sleep(2.5)


    else:
        print("Geçersiz Değer")
        sleep(2.6)
        oyna()

    return 1

    
    #####hak sayısı soru başına
    #if mod.isim=="isim" gibisinden bişeyler yap 
    #ve oyunu sunarken msela süre konulcağında if sure: yap çünkü kullanıcı istememişse boş buırakmıştır
            #######################sans eğer 0sa kullancıı sadece doğru cevap verdiğinde doğru kabul edilsin yükselidkce mesela 1 se
        # kullancının cevabı answera 2 yakınsa doğru sans 3 se kullanıcın
        # cevabı 4 yakınsa normal cevaba doğru kabuıl edilsin misal
        #secim den kullanıcıya tüm oyunların bilgilerini göster sans falan dahil
    

def randomlar():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    #bu fonksiyon en başta her seferinde bi kere çağrılsın ve kullanıcıoya günlük bir miktar random.randint(100,200) para versin ve rastgele bir dükkana bir eşya eklesin
    #giriş bonusu verildiğinde girisbonusuverildi true girisbonusu da verilen mşiktar olsunb
    #bu random seçeneklerden sürekli dükkanı güncelle (eğer time.time()-time.time()>=10000) yap) birinci time.time() en son ne zaman eklenirse o zmn alınsın o time.time() 
    #ve ayrı bilgiler.txt in yanında başka bir txt olarak kaytdedilsin
    #dosyayı da güncellemeyi unutma(bunu sadece sistem dükanları için yap)(yani if dsoyanın adı in sistem dükkanları şeklinde yap)
    #her kullancıı için yarı ayurı gerçekleştir bu işlemleri

    #####dosya işlemlerinde \n i eşyayı yazmadan önce bırak sonra deil(aaşağıda sistem ona gçöre oluşturudu)
    girisBonusu=randint(100,200)
    for i in dukkanlar:
        i.esyalar.append(sample([x for x in randomEsyalar],6))
        randomEsyalar=[Esya(randint(10,20),randint(100,1000),(choice(kelimeler)+joker),[Bonus(joker,randint(0,100))  for i in range(randint(0,20))],randint(10000,1000000))]
        #randomEsyalar=[Esya(randint(1,787867),randint(100,30000),f"{choice(kelimeler)} {joker}",[Bonus(f"{joker} {randint(0,16)}") for i in range(randint(1,15))],choice(secenekler)) for i in range(randint(10,578))]
    print("\nGiriş Bonusu {} olarak verildi!!!\n".format(girisBonusu))
    girenKullanici.bakiye=float(girenKullanici.bakiye)
    girenKullanici.bakiye+=girisBonusu
    with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(girenKullanici.isim),"w") as dosya:
        dosya.write(f"{girenKullanici.level}\n{girenKullanici.kullanici_adi}\n{girenKullanici.sifre}\n{girenKullanici.bakiye}")

    return 1
    #lvl için exp sistemi yap
giris=True
def dukkanaGit():
    global dukkan,giris,level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    kontrol()
    def dukkan():
        global giris
        system("cls")
        karsilik={}
        c=0
        for i in dukkanlar:
            print(f"{c}  {i.isim}")
            karsilik.setdefault(c,i)


        print("[Q] Çıkış")
        karsilik.setdefault("q","Çıkış")
        secim=input("Seçiminiz: ")
        try:
            secim=karsilik[secim]
            if secim.lower()=="q":
                giris=False
                return 1
                



            karsilik={}
            count=0
            for i in secim.esyalar:
                count+=1
                print(count+" "+i.isim)
                karsilik.setdefault(count,i)

            print("[Q] Çıkış")
            karsilik.setdefault("q","Çıkış")
            secim1=input("İşleminiz: ")
            if secim1.lower()=="q":
                giris=False
                return 1
            secim1=karsilik[secim1]


            tane=input("Kaç Tane Alacaksınız??")
            try:
                int(tane)
                if not  int(tane)<=secim1.stok :
                    print("Geçersiz Değer!!(1 olarak ayarllandı)")
                    sleep(2)
                    tane=1
            except:
                print("Geçersiz Değer(1 olarak ayarllandı)")
                sleep(2)
                tane=1
            

            if not girenKullanici.bakiye>=secim1.fiyat*tane:
                print("BAkiye Yetersizz!!")
                sleep(2.4)
                dukkan()
                


            girenKullanici.bakiye-=secim1.fiyat*tane
            with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program files\Kullanıcılar\{}\Alınan Eşyalar\{}".format(girenKullanici.isim,secim1.isim),"w",encoding="utf-8") as dosya:
                dosya.write(rf"{tane}\n{secim1.sure}\n{secim1.fiyat}")
                for i in secim1.bonuslar:
                    dosya.write(f"\n{i[0]} {i[1]}")


            

        except:
            print("Geçersiz Değer!!!!")
            sleep(2)
            dukkan()


    
    #kullanıcıya eşyaları listelerken en alta q seçeneği koy


        
    dukkan()
    kontrol()
    baslangic(girenKullanici.isim)
    return 1
    #görüntüledikten sonrea satın alma seçeneği ver
    ##alınan eşyalar klasörünün içine her alınan eşyanın özelliğini kjaydet  
    #dükkandaki ürünler gösterilmeden önce kontrol() fonksiypounu çağüır
    #bişey satın alınırsa alınan eşyalar klasörüne git eşyanın adını taşıyan txt oluştur
    # ilk sırya kullanıcının ne kadar aldığını(stok) yaz ikinci süreye kalan süreyi yaz üçüncü sıraya ne adara aldığını(adet fiyatı olarak) yaz 
    #  sonra alt alta sağladığı bonusları bas (her satır şöyle gözüksün: bonusun adı = sayısal olarak sağladığı değer) aralara boşluk koyma 
    #  stokDurumu()
    #  #eklenecekOgeler() 
    #esyalarda jokerse süre =yok  (kullanınca biter) özellikse süresi neyse o
    #eşyalar alınınca stok değeri oyuncunun aldığı olsun ve kullandıkça bir eksilsin bitince kaybolsunh
    ##########################alınan eşyadan ne kadar alıncağını kulancıya sor ve ona göre alınan eşyanın stoğu o olsun


def dukkanOlustur():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    
    while True:
        
        system("cls")
        isim=input("Dükkannın İsmi:")
        if isim:
            break  
        else:
            print("Geçersiz Değer")
            sleep(1.99999)

    def tane():
        global sayi
        system("cls")
        sayi=input("Kaç tane eşya ekliyceksiniz?")
        if not sayi.isdigit():
        
            print("Geçersiz Değer")
            sleep(1.99999)
            tane()

    tane()
    dukkanlar.append(Dukkan(isim,list(choice([x for x in randomEsyalar]))))
    with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}.txt".format(girenKullanici.isim,isim),"w") as dosya:
        dosya.write(isim)


    print("Şimdi Eklenecek Eşyalar İçin EŞya Ekleme Menüsüs Geliyo oradan yeni oluşturduğunuz dükkanı seçin!!")
    sleep(2)
    for i in range(int(sayi)):
        dukkanaEsyaEkle()

    return 1


    ########3dükkana yeni eklencek eşyalar için kullanıcın dükkanlar klasöründe her dükkana bir txt oluştur 
    #sonra ilk satıra dülkkan ismi yaz sonra alt alta tüm eşyaları şu şekilde sırala:
    #stok=1.satır 2.satır=fiyat 3.satır=isim 
    #4.satır=tüm bonusları yaz aralara virgül koy(son bonussa koyma) her bonusun da adı sayısal_deger(arada sadece ad ile sayısal değer arasında bpoşluk olabilir) 
    #5.satır=kalan süre
    #esyalarda jokerse süre =yok  (kullanınca biter) özellikse süresi neyse o


def dukkanSil():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    while True:
        count=0
        karsilik={}
        for i in dukkanlar:

            count+=1
            karsilik.setdefault(count,i)
            print(f"[{count}] {i.isim}")

        secim=input("Hangisi")

        try:
            dukkanlar.remove(karsilik[secim])
            for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar".format(girenKullanici.isim)):
                if karsilik[secim].lower()+".txt" ==i.lower():
                
                    remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}".format(girenKullanici.isim,i))
                    break
            break
        except:
            print("Gçeresiz Değer")
            sleep(2.66)

    return 1
    #stokDurumu() ve eklenecekOgeler() sil





def esyaSat():
    
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    while True:
        count=0
        karsilik={}
        for i in oyunmodlari:

            count+=1
            karsilik.setdefault(count,i)
            print(f"[{count}] {i.isim}")

        secim=input("Hangisi")
        tane =input("kaç Tane")
        
        try:
            if not tane.isdigit() and not karsilik[secim].stok>=int(tane):continue
            alinanEsyalar[alinanEsyalar.index(karsilik[secim])].stok-=tane
            with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(girenKullanici.isim),"w") as dosya:
                dosya.write(f"{girenKullanici.level}\n{girenKullanici.kullanici_adi}\n{girenKullanici.sifre}\n{girenKullanici.bakiye}")

    

        except:
            print("Geçersiz Değer")
            sleep(3)


        kontrol()
        return 1



def kontrol():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    #burda dükkana eklenecek öğelerin gelme süresi dolmuş mu diye konbtorl et dolmuşsa ekle(dosyaya da yaz)
    ####################x parametre girmiş kullanıcının "isim" değişkenmi################ ki ona göre işlem yapş
    #aynı zamanda stok durumunu da kontrol et stok bitmişse dosyadan listeden dükkanmdan sil
    #########şu kontrrolu ekle: eğğer for i in leveller kullanıcı.lvl >=  i.acildigi lvl dosya=open(oyun modu adı,"w") dosya.write(hbilgileri) oyunmodları.append(i)
    #joker sürelerininb bitip bitmediğini de kontrol et
    #kontrol ederkenaynı zaömanda dosyayı güncelle
    

    def eklenecekOgeler(x):
        global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
        
        for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}".format(x)):
            with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\{}".format(x,i)) as dosya:
                if len(dosya.readlines())==2:
                    if int(dosya.read().split("\n")[1])-int(dosya.read().split("\n")[0])>=0:
                        for ii in dukkanlar:
                            for iii in ii:
                                if iii.isim.lower()+".txt"==i.lower():
                                    ii.esyalar.remove(iii)
                                    break

                            

    def cikarilcakOgeler(x):
        #buraya tüm alinan eşyalrın suresini kontrol et eğer time.time()-sure<=0 iseonun dosyasını sil yap
        pass

            #vazgeçtim bunun kontrolu için po kadar satır kodu değiştirememe


        baslangic(girenKullanici.isim)

    def sure(x):
        # alınan eşyaların sürelerini kontroö et
        pass

    def stokDurumu(x):
        global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
        # buradaa dükkanlardaki eşyalara bak stok 0 veya altıysa sil aynısını alınan eşyalar için de yap
        for i in dukkanlar:
            for ii in i:
                if ii.stok<=0:
                    i.remove(ii)
            for ig in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar".format(girenKullanici.isim)):
                if ig.lower()==i.lower()+".txt":
                    with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}".format(girenKullanici.isim,ig),"w") as dosya:
                        dosya.write("\n"+i)
                        for im in i.esyalar:
                            bonuslar1=",".join([f"{x.split()[0]} {x.split()[1]}" for x in i.bonuslar])
                            dosya.write(f"\n{i.stok}\n{i.fiyat}\n{i.isim}\n{bonuslar1}")




    def jokerDurumu(x):
        global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri

        for i in alinanEsyalar:
            for ii in i:
                if ii.stok<=0:
                    i.remove(ii)
            for ig in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Alınan Eşyalar".format(girenKullanici.isim)):
                if ig.lower()==i.lower()+".txt":
                    with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Alınan Eşyalar\{}".format(girenKullanici.isim,ig),"w") as dosya:
                        dosya.write("\n"+i)
                        for im in i.esyalar:
                            bonuslar1=",".join([f"{x.split()[0]} {x.split()[1]}" for x in i.bonuslar])
                            dosya.write(f"\n{i.stok}\n{i.fiyat}\n{i.isim}\n{bonuslar1}")

    def levelKontrol():
        global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
        if int(girenKullanici.level)-girenKullanici.level==0:
            with open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Bilgiler.txt".format(girenKullanici.isim),"w") as dosya:
                dosya.write(f"{girenKullanici.level}\n{girenKullanici.kullanici_adi}\n{girenKullanici.sifre}\n{girenKullanici.bakiye}")




    stokDurumu(girenKullanici.isim)
    jokerDurumu(girenKullanici.isim)
    levelKontrol()
    eklenecekOgeler(girenKullanici.isim)
    baslangic(girenKullanici.isim)
    return 1

    #bunları kullanıcılar klasöründe direk bu kullanıcının klasörünün içine her joker eklenecek öğe stok durumu için txt oluşturarak yap
def kullaniciİslemleri():

    
    global giris, level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    if giris:
        girisYap()
        randomlar()
    if girisBonusuVerildi:
        print("Tebrikler, giriş yaptığınız için {} kredi kazandınız ".format(girisBonusu))
    giris=False

    kontrol()
    sleep(3)
    kontrol()
    system("cls")
    print("""
          [1]  Hesap Bilgilerini Görüntüle
          [2]  Dükkanları Görüntüle
          [3]  Dükkana Eşya Ekle/Talep Et
          [4]  Oyna
          [5]  Dükkana Git/Satın Al
          [6]  Yeni Dükkan
          [7]  Yeni Oyun Modu
          [8]  Eşya Sat
          [9]  Dükkan Sil
          [10] Oyun Modu Sil
          [A]  Hesabı Sıfırla
          [D]  Hesabı Sil
          [Q]  Hesaptan Çıkış
          """)
    #çıkış için clear falan kullan ve return ve girenKullanici=[] yap
    secim=input("\nSeçiminiz: ")
    if secim=="1":
        #görünütleme işlemleri
        print(f"""
        Kullanıcı Adı:            {girenKullanici.kullanici_adi}
        İsim:                     {girenKullanici.isim}
        Şifre:                    {girenKullanici.sifre}
        Level:                    {int(girenKullanici.level)}
        Bir Sonraki Levele Kalan: {1-(girenKullanici.level-int(girenKullanici.level))}
        Bakiye:                   {girenKullanici.bakiye}
        """)
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="2":
        print("Yapmadım burayaı sana ne")
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="3":
        dukkanaEsyaEkle()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="4":
        oyna()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="5":
        dukkanaGit()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()
        
    elif secim=="6":
        dukkanOlustur()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="7":
        oyunModuOlustur()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="8":
        esyaSat()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    
    elif secim=="9":
        dukkanSil()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    elif secim=="10":
        oyunModuSil()
        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()


    elif secim.lower()=="d":
        kullanicilar.remove(girenKullanici)
        remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}".format(girenKullanici.isim))
        return 1

    elif secim.lower()=="q":
        dukkanlar.clear()
        del girenKullanici
        return 1

    elif secim.lower()=="a":
        for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar".format(girenKullanici.isim)):
            if not i.lower in  [x.lower+".txt" for x in sistemDukkanlari]:
                remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Dükkanlar\{}".format(girenKullanici.isim,i))

        for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Alınan Eşyalar".format(girenKullanici.isim)):
            remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Alınan Eşyalar\{}".format(girenKullanici.isim,i))


        for i in listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Oyun Modları".format(girenKullanici.isim)):
            remove(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Python Giriş Seviye ve OOP\Program Files\Kullanıcılar\{}\Oyun Modları\{}".format(girenKullanici.isim,i))


        input("\nAna menüye dönmek için enter a basın!!!")
        kullaniciİslemleri()

    else:
        kullaniciİslemleri()



    #recrusive kullan





def main():
    global level,kullanicilar,bonuslar,alinanEsyalar,dukkanlar,esyalar,oyunmodlari,randomEsyalar,secenkler,kelimeler,jokerler,girenKullanici,girisBonusuVerildi,girisBonusu,sistemLevelleri,sistemDukkanlari,sistemLevelleri
    

    



    sleep(2)    
    system("cls")
    print("""
    [0] Bilgi
    [1] Kullanıcı Girişi
    [2] Yeni Kayıt
    [Q] Çıkış
    """)
    secim=input("İşleminiz: ")
    


    if secim=="1":
        if kullanicilar:
            kullaniciİslemleri()
            input("\nAna menüye dönmek için enter a basın!!!")

            
            main()

        else:
            print("Kullanıcı yok!!")
            sleep(2.5)
            main()
        

    elif secim=="2":
        hesapOlustur()
        input("\nAna menüye dönmek için enter a basın!!!")
        main()

    elif secim.lower()=="q":
        return 1

    elif secim.lower()=="h":
        
        print("""
        Eğlenir misin bilmiyom ama boş beleş bişey!!
        13.07.20
        """)
        sleep(3)
        input("\nAna menüye dönmek için enter a basın!!!")
        main()

    elif secim=="0":
        print("Sayı Tahminimsi V=0.1")
        sleep(2)
        input("\nAna menüye dönmek için enter a basın!!!")
        main()

    else:
        main()






if __name__=="__main__":
    giris=True
    main()























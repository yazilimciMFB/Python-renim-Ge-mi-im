z=0
if z==0:
    masalar=[]
    girenMusteri=[]
    yemekler=[]
    icecekler=[]
    menuler=[]
    LokantaSahip=[]
    Müşteriler=[]
    rezervasyonlar=[]
    LokantaSahip=[]
    Müşteriler=[]


from time import sleep as ts
from time import time as tt
import random as ra
import os
sahipGirildi=False
musteriGirdi=False

#bu geçmiş oluşturma sistemi içöinb time.time() ile tarih oluşturma işlkemini yap

class Kullanici():
    def __init__(self,kullanici_adi,parola,isim):
        self.kullanici_adi=kullanici_adi
        self.parola=parola
        self.isim=isim

class Musteri(Kullanici):
    pass


class LokantaSahibi(Kullanici):
    pass

class Lux():
    def __init__(self,ad,ek_hizmetler,ek_malzemeler,fiyat:int):
        ad=ad#str
        ek_hizmetler=ek_hizmetler#list
        ek_malzemeler=ek_malzemeler#list
        fiyat=fiyat
#bu ek malzeme ve hizmetleri kaydederken kullanıcıya adlarını sor ve {çiçek:10tl} gibisinden elemanlar ekle listeye, 

class Tarif():
    #malzemeler için şu kadar miktarda yapmak için bu kadar malzeme yaz
    def __init__(self,malzemeler:list,surec:dict):
        malzemeler=malzemeler#list
        surec=surec#dict




class Masa():
    def __init__(self,ad:str,no:int,gecmis:list,luxluk_seviyesi:Lux):
        ad=ad#str
        no=no#int
        gecmis=gecmis #list içinde her eski hesap için DİCT
        luxluk_seviyesi=luxluk_seviyesi#Lux()




class Rezervasyon():
    def __init__(self,masaAdi,fiyat,tarih,yiyeceklerİcecekler):
        self.masaAdi=masaAdi
        self.fiyat=fiyat
        self.tarih=tarih
        self.yiyeceklerİcecekler=yiyeceklerİcecekler

#geçmişe dosyadan veri çek her eski hesabı ayrı eleman larak listeye at
#her masaya ayrı liste
#lükslük seviyesine göre fiyatlar artsın

class Yemek():
    def __init__(self,ad:str,fiyat:int,tarif:Tarif,miktar:int,miktarOlcegi:str):
        ad=ad#str
        fiyat=fiyat#int
        tarif=tarif#Tarif()
        miktar=miktar#1 2 3
        miktarOlcegi=miktarOlcegi#bardak tabak vb



class Icecek():
    def __init__(self,ad:str,fiyat:int,tarif:Tarif,miktar:int,miktarOlcegi:str):
        ad=ad#str
        fiyat=fiyat#int
        tarif=tarif#Tarif()
        miktar=miktar#1 2 3
        miktarOlcegi=miktarOlcegi#bardak tabak vb



class Menu():
    def __init__(self,icerik:list,kar:int,ad:str,fiyat:int):
        icerik=icerik#list
        
        kar=kar#int
        ad=ad#str
        fiyat=fiyat#int
#yemekler ve içecekler listine ayrı icecek ve yemek class ında veri ata

#sipariş geçmişi sistemi oluşrur belli bir kayıt dosyasıyla birlikte
#bu geçmiş oluşturma sistemi içöinb time.time() ile tarih oluşturma işlkemini yap



#yeni bir tarif süreci oluşturmadan önce kullanıcıya kaç adımlı olduğunu sor ona hgöre dict içine 1:ajks, 2:lasdkj gibi şeyler ekle!!!


#ilk başta os modulu ile python projelerim klasoru içine lokanta veri tabanı diye klasör oluştur onun
#  içine kullancılar adında dosyalar oluştur
# (bilgisyara os ile oluşturt) ve daha sonra kullanıcılar klasörünün içine her kullanıcının kendi klasörümnü oluştur
# ve hepsinin içine ayrı türde 
# (giriş masa menu rezervasyon geçmiş) vb bilgilerinin kaydedildiğii txt dosyalarını ayrı ayrı oluştur 
# bu dosyaları oluştururken ilk çalıştırmada kullanıcılar diye klasör oluştur sonra her kullancı oluşturulunca 
#kullanıcılar klasörünün içine o kullanıcının kullancıı adıyla eya kullanıcı1 kullanıcı2 şeklinde doyslkar oluştur
#kullanıcı girişi sonsuz olacağından .format kullan veya bir listeden seç kaçıncı kullanıcıysa ona göre klasör adları tasarla
#her kullanıcının klasörünün içine masalar.txt menuler.txt yemekeler.txt iceccdekler.txt kullanıcıbilgileri.txtt vb doyslr oluitur



def lokantaSahibiKayit():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar
    # LokantaSahibi=[]
    
    while True:
        os.system("cls")
        print("""Kullanıcı adı en az 6 harften oluşmalı 
        ve 
        içinde en az bir harf ve bir rakam bulunmalıdır.""".lower())
        kullanici_adi=input("\nHesabınız için kullanıcı adı: \n")

        if not kullanici_adi.isdigit() and not kullanici_adi.isalpha() and len(kullanici_adi)>=6:
            break
        else:
            print("Geçersiz Kullanıcı Adı!!!")
            ts(3)

    while True:
        os.system("cls")
        print("""Parola en az 6 harften oluşmalı 
        ve 
        içinde en az bir harf ve bir rakam bulunmalıdır.""")
        parola=input("\nHesabınız için parola: \n".lower())

        if not parola.isdigit() and not parola.isalpha() and len(parola)>=6:
            break

        else:
            print("Geçersiz Parola!!!")
            ts(3)

    while True:
        os.system("cls")
        
        isim=input("\nSon olarak isminiz: \n")

        if isim:
            break

        else:
            print("Geçersiz İsim!!!")
            ts(3)
        


    print(f"""\nTebrikler!
    Kullanıcı Adı: {kullanici_adi}
    Parola: {parola[:3]+(len(parola)-3)*"*"}

    olan {isim}  hesabı oluşturuldu!!!

    """)

    LokantaSahip.append(LokantaSahibi(kullanici_adi,parola,isim))
    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi")
    os.makedirs("Masalar")
    os.makedirs("Yemekler")
    os.makedirs("İçecekler")
    os.makedirs("Menüler")
    os.makedirs("Luxlukler")
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Bilgiler.txt","w")
    dosya.write(f"{kullanici_adi}")
    dosya.write("\n")
    dosya.write(f"{parola}")
    dosya.write("\n")
    dosya.write(F"{isim}")

    dosya.close()

    LokantaSahip.append(LokantaSahibi(kullanici_adi,parola,isim))

    
    
        
    
        






def sahipGirisi():
    
    global musteriGirdi,sahipGirildi,LokantaSahip
    sahipGirildi=False
    while True:
        os.system("cls")
        
        #o=1
        if not sahipGirildi:
            kullanici_adi=input("Kullanınıcı Adınız: ")
            count=0
            for i in LokantaSahip:
                if i.kullanici_adi==kullanici_adi:
                    parola=input(f"Hoşgeldiniz {i.isim}, Parola rica ediyim: ".lower())
                    if i.parola==parola:
                        print("Giriş Yapıldı!!")
                        sahipGirildi=True
                        return 1
                       

            
                        
          
                        

                    else:
                        print("Geçersiz Parola!!")
                        o=1
                        break
            
            



                else:
                    count+=1

            


            if count==len(LokantaSahip):
                print("Geçersiz Kullancı Adı!!")
                continue


    

       





                    

                

    
                    

        

            
def masaEkle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True :
        os.system("cls")
        ad=input("Masanın adı: ")
        if ad.isalpha():
            break

        else:
            print("İsim sadece harflerden oluşabilir!!")
            ts(3)


    while True:
        os.system("cls")
        isim=input("Lükslük Seviyesinin İsmi: ")
        if isim.isalpha():
            break

        else:
            print("İsim sadece harflerden oluşabilir!!")
            ts(3)

    while True:
        os.system("cls")
        sayi=input("Kaç tane ek malzeme olacak? ")
        if sayi.isdigit():
            break

        else:
            print("Miktar sadece sayılardan oluşabilir!!")
            ts(3)


    while True:
        os.system("cls")
        sayi1=input("Kaç tane ek hizmet olacak? ")
        if sayi1.isdigit():
            break

        else:
            print("Miktar sadece sayılardan oluşabilir!!")
            ts(3)



    os.system("cls")
    hizmetler=[]
    malzemeler=[]
    totalFiyat=0
    count=1
    for i in range(int(sayi//1)):
        
        while True:
            os.system("cls")
            ad1=input(f"{count}. Malzemenin adı: ")
            fiyat1=input(f"\n{count}. Malzemenin Fiyatı: ")
            if fiyat1.isdigit():
                break
            else:
                print("Miktar sadece sayılardan oluşabilir!!")
                ts(3)

        malzemeler.append(ad1)
        totalFiyat+=int(fiyat1)
        count+=1

    count=0
    for i in range(int(sayi//1)):
        
        while True:
            os.system("cls")
            ad1=input(f"{count}. Hizmetin adı: ")
            fiyat1=input(f"\n{count}. Hizmetin Fiyatı: ")
            if fiyat1.isdigit():
                break
            else:
                print("Miktar sadece sayılardan oluşabilir!!")
                ts(3)

        hizmetler.append(ad1)
        totalFiyat+=int(fiyat1)
        count+=1

    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar")
    os.makedirs(f"Masa---> {isim}")
    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\Masa---> {}".format(isim))
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\Masa---> {}\Geçmiş.txt".format(isim),"w")
    dosya.close()
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\Masa---> {}\Lüx.txt".format(isim),"w")
    dosya.write(f"{ad}\n")
    for i in malzemeler:
        dosya.write(f"{i}\n")

    dosya.write("Hizmetler\n")
    for i in hizmetler:
        dosya.write(f"{i}\n")

    dosya.write(totalFiyat)
    dosya.close()
    cout=0
    for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar"):
        cout+=1
    masalar.append(Masa(ad,cout,list(),Lux(isim,hizmetler,malzemeler,totalFiyat)))
    print("\nMasa Oluşturuldu!!")
    #Lux()
        

    



    #masalrı dosyaya kaydederken masaya kullanıcnın verdiği isim ile masalar 
    # klasöünde yeni klasör yap sonra içine ilk olarak şuanki sonra geçmiş hesapları en son da 
    
    #her yeni işlem yapılığında şeçili masada çıkrma ekleme dahil dosyada sadece sşoyle kayıt yap:
    #su tarih\n şu kadar tl 
    #masa file adlar masanın adı Güncel.txt ,masanınadı Geçmiş.txt ve masanın adı Lüx.txt şeklinde olsun

# masaları kaydederken luxluk seviyesine gelince ilk adını sor onu txt in ilk satırına kaydet sonra kaç ek malzeme ve 
# kaç ek hizmet istediğini sor ona göre döngüyle sor bunları 1. mazeme 2.hizmet formatında en son toplma fiyatı 
# sor onu dosyanın en altına yaz ismi yazdıktan dosyaya hemen sonra malzemeleri sırala alt alta ondan 
# sonra Hizmetler yaz sonra lat alta hizmetleri sırala dosyaay en sona da fiyat yaz 
# kullanıcıya malzemeler için tek tek fiyat sorma en son toplam fiyat sor
    
def yemekEkle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        ad  =input("Yemeğin Adı: ")
        if not ad.isdigit():
            break

        else:
            print("\nGeçersiz İsim\n")
            ts(3)



    while True:
        os.system("cls")
        fiyat=input("Yemeğin Fiyatı: ")
        if fiyat.isdigit():
            
            break


        else:
            print("\nGeçersiz Fiyat\n")
            ts(3)


    print("\nŞimdi de tarif bilgileri istenecek!!\n")
    while True:
        #(malzemeler: list, surec: dict)
        os.system("cls")
        sayi=input("Kaç tane malzeme seçeceksiniz? ")
        if sayi.isdigit():
            malzemeler=[]
            surec=dict()
            for i in range(int(sayi)):
                malzeme=input(f"{i+1}. Malzeme: ")

                malzemeler.append(malzeme)
            break


        else:
            print("\nGeçersiz Sayı\n")
            ts(3)

    while True:
        os.system("cls")
        
        sayi=input("Kaç tane adım gireceksiniz? ")
        if sayi.isdigit():
            
            surec=dict()
            for i in range(int(sayi)):
                adim=input(f"{i+1}. Adım: ")

                surec.setdefault(i+1,adim)
                
            break    

        else:
            print("\nGeçersiz Sayı\n")
            ts(3)


    while True:
        os.system("cls")
        miktar1=input("Yemeğin/İçeceğin Miktarı(1,2,3 vb): ")
        if  miktar1.isdigit():
            miktar1=int(miktar1)
            break
        else:
            print("\nGeçersiz Değer")
            ts(3)


    while True:
        os.system("cls")
        miktarOlcegi=input("Yemeğin/İçeceğin Miktar Ölçeği(bardak,tabak,kaşık vb): ")
        if miktarOlcegi.isalpha():
            
            break
        else:
            print("\nGeçersiz Değer")
            ts(3)



    yemekler.append(Yemek(ad,fiyat,Tarif(malzemeler,surec),miktar1,miktarOlcegi))
    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler")
    os.makedirs(ad)
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Tarif.txt".format(ad),"w")
    for i in malzemeler:
        dosya.write(f"\n{i}")

    dosya.write("Tarif")


    for i in surec:
        dosya.write(f"\n{i}")


    dosya.close()

    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Miktar1.txt".format(ad),"w")
    dosya.write(str(miktar1))
    dosya.close()


    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Miktar Ölçeği.txt".format(ad),"w")
    dosya.write(miktarOlcegi)
    dosya.close()


    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Fiyat.txt".format(ad),"w")
    dosya.write(str(fiyat))
    dosya.close()

    print("\nYemek Oluşturuldu!!")








    
        #miktar ölçegğ ve miktar sor



    #yemek file adları yemek adı Tarif.txt, yemek adı Fiyat.txt, yuemek adı Miktar1.txt, ymek adı Miktar Ölçeği.txt şeklinde olsun
    #kullanıcın yemeğe verdiği isim yemekler klasörünün içinde oluşturulck o yemeğin veri tabanına işaret eden klasörün ismi olcak
    #yityecek içeçek tarif ekleme için kullanıcıya malzeme sayısını sor o kadar kere malzeme al sonra satır satır dosyaya yaz sonra tarif 
    # diye başlık at dosyaya sonra kullanıcıya ne kadar adım yazcağını sor for ile o kadar kere adım sor kullanıcıya sonra
    #  dosyaya tarif yazdığın yerin altından başlkayarak yaz süreci
    #  kullanıcıya malzemeler için tek tek fiyat sorma en son toplam fiyat sor(ozellikle tarif sürcinde)
    #malzemeleri list ile süreci de {1:yap,:et} sekşlinde sakla

def icecekEkle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar


    while True:
        os.system("cls")
        ad  =input("İçeceğin Adı: ")
        if not ad.isdigit():
            break

        else:
            print("\nGeçersiz İsim\n")
            ts(3)



    while True:
        os.system("cls")
        fiyat=input("İçeceğin Fiyatı: ")
        if fiyat.isdigit():
            fiyat=int(fiyat)
            break


        else:
            print("\nGeçersiz Fiyat\n")
            ts(3)


    print("\nŞimdi de tarif bilgileri istenecek!!\n")
    while True:
        #(malzemeler: list, surec: dict)
        os.system("cls")
        sayi=input("Kaç tane malzeme seçeceksiniz? ")
        if sayi.isdigit():
            malzemeler=[]
            surec=dict()
            for i in range(int(sayi)):
                malzeme=input(f"{i+1}. Malzeme: ")

                malzemeler.append(malzeme)
            break


        else:
            print("\nGeçersiz Sayı\n")
            ts(3)

    while True:
        os.system("cls")
        
        sayi=input("Kaç tane adım gireceksiniz? ")
        if sayi.isdigit():
            
            surec=dict()
            for i in range(int(sayi)):
                adim=input(f"{i+1}. Adım: ")

                surec.setdefault(i+1,adim)
                
            break    

        else:
            print("\nGeçersiz Sayı\n")
            ts(3)


    while True:
        os.system("cls")
        miktar1=input("Yemeğin/İçeceğin Miktarı(1,2,3 vb): ")
        if miktar1.isdigit():
            miktar1=int(miktar1)
            break
        else:
            print("\nGeçersiz Değer")
            ts(3)


    while True:
        os.system("cls")
        miktarOlcegi=input("Yemeğin/İçeceğin Miktar Ölçeği(bardak,tabak,kaşık vb): ")
        if miktarOlcegi.isalpha():
            
            break
        else:
            print("\nGeçersiz Değer")
            ts(3)



    icecekler.append(Icecek(ad,fiyat,Tarif(malzemeler,surec),miktar1,miktarOlcegi))
    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler")
    os.makedirs(ad)
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Tarif.txt".format(ad),"w")
    for i in malzemeler:
        dosya.write(f"\n{i}")

    dosya.write("Tarif")


    for i in surec:
        dosya.write(f"\n{i}")


    dosya.close()

    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Miktar1.txt".format(ad),"w")
    dosya.write(str(miktar1))
    dosya.close()


    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Miktar Ölçeği.txt".format(ad),"w")
    dosya.write(miktarOlcegi)
    dosya.close()


    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Fiyat.txt".format(ad),"w")
    dosya.write(fiyat)
    dosya.close()

    print("\nİçecek Oluşturuldu!!")
    #içecek file adları yemek adı Tarif.txt, yemek adı Fiyat.txt, yuemek adı 
    # ^^^^^33###########Miktar1.txt################
    # , ymek adı Miktar Ölçeği.txt şeklinde olsun
    #kullanıcın yemeğe verdiği isim yemekler klasörünün içinde oluşturulck o yemeğin veri tabanına işaret eden klasörün ismi olcak
    #yityecek içeçek tarif ekleme için kullanıcıya malzeme sayısını sor o kadar kere malzeme al sonra satır satır dosyaya yaz sonra tarif 
    # diye başlık at dosyaya sonra kullanıcıya ne kadar adım yazcağını sor for ile o kadar kere adım sor kullanıcıya sonra
    #  dosyaya tarif yazdığın yerin altından başlkayarak yaz süreci
    #  kullanıcıya malzemeler için tek tek fiyat sorma en son toplam fiyat sor(ozellikle tarif sürcinde)
    #malzemeleri list ile süreci de {1:yap,:et} sekşlinde sakla

def icecekCikar():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        
        
        os.system("cls")
        if icecekler:
            karsilik=dict()
            for index,i in enumerate(icecekler):
                print(f"[{index+1}]------> {i}")
                karsilik.setdefault(index+1,i)

            secim=input("Seçiminiz: ")
            if secim in list(karsilik.keys()):
                for i in icecekler:
                    if i.ad.lower()==karsilik[secim].lower():

                        icecekler.remove(i)
    
                os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler")
                for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):
                    if i.lower()==karsilik[secim].lower():
                        os.removedirs(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}".format(i))
                        break

            else:
                print("\nSeçim Bulunamadı!!!!!!!!\n")
                ts(3)

        else:
            print("İçecek Yok!!!")
            ts(3)
            break




def yemekCikar():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        
        
        os.system("cls")
        if yemekler:
            karsilik=dict()
            for index,i in enumerate(yemekler):
                print(f"[{index+1}]------> {i}")
                karsilik.setdefault(index+1,i)

            secim=input("Seçiminiz: ")
            if secim in list(karsilik.keys()):
                for i in yemekler:
                    if i.ad.lower()==karsilik[secim].lower():

                        yemekler.remove(i)
                os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler")
                for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                    if i.lower()==karsilik[secim].lower():
                        os.removedirs(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}".format(i))
                        break

            else:
                print("\nSeçim Bulunamadı!!!!!!!!\n")
                ts(3)

        else:
            print("Yemek Yok!!!")
            ts(3)
            break
def icecekDuzenle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        karsilik=dict()
        for i in icecekler:
            print(f"[{icecekler.index(i)}]--{i.ad}")
            karsilik.setdefault(icecekler.index(i),i)


        secim=input("\nSeçiminiz: ")
        if secim.isdigit():
            if int(secim) in list(karsilik.keys()):
                secim=int(secim)
                break
                
                

        else:
            print("\nGeçersiz Değer\n")
            ts(3)

    while True:
        os.system("cls")
        print("""
        [1] Ad
        [2] Fiyat
        [3] Tarif
        [4] Miktar
        [5] Miktar Ölçeği
        """)
        secim1=input("Seçiminiz: ")


        if secim1=="1":
            print("Geçerli İsim:: ")
            print(f"\n{karsilik[secim].ad}")
            yeniAd=input("\nYeni İsim: ")
            for i in icecekler:
                if  i.ad == karsilik[secim].ad:
                    i.ad=yeniAd
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}".format(karsilik[secim].ad))
                    os.rename(karsilik[secim].ad,yeniAd)
                    break

        


        elif secim1=="2":
            print("Geçerli Fiyat:: ")
            print(f"\n{karsilik[secim].fiyat}")
            yeniFiyat=input("\nYeni Fiyat: ")
            for i in icecekler:
                if  i.fiyat == karsilik[secim].fiyat:
                    i.fiyat=yeniFiyat
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}".format(karsilik[secim].ad))
                    for ii in os.listdir():
                        if "Fiyat" in ii:
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\{}".format(i,ii),"w")
                            dosya.write(yeniFiyat)
                            
                            break

        elif secim1=="3":
            while True:
                os.system("cls")
                print("""
                [1] Malzemeler
                [2] Süreç
                
                """)

                secim=input("İşleminiz: ")

                if secim=="1":
                    for i in icecekler:
                        if i.ad.lower() ==karsilik[secim].ad.lower():
                            for ii in i.tarif:
                                if i.tarif.index(ii)==0:
                                    for iii in ii:
                                        print(iii)

                                    yeniSayi=input("Kaç Malzeme İstiyorsunuz: ")
                                    
                                    if yeniSayi.isdigit():
                                        malzemeler=list()
                                        for iii in range(int(yeniSayi)):
                                            yeniMalzeme=input(f"{iii+1}. yeni malzeme: ")
                                            malzemeler.append(yeniMalzeme)
                                        i.tarif[0]=malzemeler

                                        for r in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):

                                            if r.lower()==karsilik[secim].lower():


                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Tarif.txt".format(r),"a+")
                                                x=dosya.read()
                                                x.split("Tarif")
                                                x[0]=malzemeler
                                                dosya.close()
                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Tarif.txt".format(r),"w")
                                                for i in x[0]:
                                                    dosya.write(f"{i}\n")
                                                dosya.write("Tarif\n")
                                                for i in x[1]:
                                                    dosya.write(f"{i}\n")
                                                break

                                                dosya.close()
                                        


                                    else:
                                        print("Geçersiz Değer!!")
                                        ts(3)


                        
                        

                elif secim=="2":
                    for i in icecekler:
                        if i.ad.lower() ==karsilik[secim].ad.lower():
                            for ii in i.tarif:
                                if i.tarif.index(ii)==0:
                                    for iii in ii:
                                        print(iii)

                                    yeniSayi=input("Kaç Adım İstiyorsunuz: ")
                                    
                                    if yeniSayi.isdigit():
                                        surec=list()
                                        for iii in range(int(yeniSayi)):
                                            yeniAdim=input(f"{iii+1}. yeni adım: ")
                                            surec.append(yeniAdim)

                                            
                                        i.tarif[1].clear()
                                        for o in enumerate(surec):
                                            i.tarif[1][o[0]+1]=o[2]



                                        for r in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):

                                            if r.lower()==karsilik[secim].lower():


                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Tarif.txt".format(r),"a+")
                                                x=dosya.read()
                                                x.split("Tarif")
                                                x[1]=surec
                                                dosya.close()
                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Tarif.txt".format(r),"w")
                                                for i in x[0]:
                                                    dosya.write(f"{i}\n")
                                                dosya.write("Tarif\n")
                                                for i in x[1]:
                                                    dosya.write(f"{i}\n")

                                                break
                                                dosya.close()

                else:
                    print("\nGeçersiz Değer")
                    ts(3)


        elif secim1=="4":
            while True:
                os.system("cls")
                print(icecekler[icecekler.index(karsilik[secim])].miktar)
                yeniMiktar=input("Yeni Miktar: ")
                if yeniMiktar.isdigit():
                    icecekler[icecekler.index(karsilik[secim])].miktar=yeniMiktar
                    for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):
                        if i.lower()==karsilik[secim].lower():
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Miktar1.txt".format(i),"w")
                            dosya.write(yeniMiktar)
                            break

                            dosya.close()

                    break
                    


                else:
                    print("\nGeçersiz Değer\n")
                    ts(3)
            #miktar düzenleme

        elif secim1=="5":
            while True:
                os.system("cls")
                print(icecekler[icecekler.index(karsilik[secim])].miktarOlcegi)
                yeniMiktarOlcegi=input("Yeni Miktar Ölçeği: ")
                if yeniMiktarOlcegi.isalpha():
                    icecekler[icecekler.index(karsilik[secim])].miktarOlcegi=yeniMiktarOlcegi
                    for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):
                        if i.lower()==karsilik[secim].lower():
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\Miktar Ölçeği.txt".format(i),"w")
                            dosya.write(yeniMiktarOlcegi)
                            break

                            dosya.close()

                    break
                    


                else:
                    print("\nGeçersiz Değer\n")
                    ts(3)
            #miktar ölçeği düzenleme

        else:
            print("\nGeçersiz Değer!!\n")
            ts(3)
    

    
def yemekDuzenle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        karsilik=dict()
        for i in yemekler:
            print(f"[{yemekler.index(i)}]--{i.ad}")
            karsilik.setdefault(yemekler.index(i),i)


        secim=input("\nSeçiminiz: ")
        if secim.isdigit():
            if int(secim) in list(karsilik.keys()):
                secim=int(secim)
                break
                
                

        else:
            print("\nGeçersiz Değer\n")
            ts(3)

    while True:
        os.system("cls")
        print("""
        [1] Ad
        [2] Fiyat
        [3] Tarif
        [4] Miktar
        [5] Miktar Ölçeği
        """)
        secim1=input("Seçiminiz: ")


        if secim1=="1":
            print("Geçerli İsim:: ")
            print(f"\n{karsilik[secim].ad}")
            yeniAd=input("\nYeni İsim: ")
            for i in yemekler:
                if  i.ad == karsilik[secim].ad:
                    i.ad=yeniAd
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}".format(karsilik[secim].ad))
                    os.rename(karsilik[secim].ad,yeniAd)
                    break

        


        elif secim1=="2":
            print("Geçerli Fiyat:: ")
            print(f"\n{karsilik[secim].fiyat}")
            yeniFiyat=input("\nYeni Fiyat: ")
            for i in yemekler:
                if  i.fiyat == karsilik[secim].fiyat:
                    i.fiyat=yeniFiyat
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}".format(karsilik[secim].ad))
                    for ii in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                        if "Fiyat" in ii:
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\{}".format(i,ii),"w")
                            dosya.write(yeniFiyat)
                            
                            break

        elif secim1=="3":
            while True:
                os.system("cls")
                print("""
                [1] Malzemeler
                [2] Süreç
                
                """)

                secim=input("İşleminiz: ")

                if secim=="1":
                    for i in yemekler:
                        if i.ad.lower() ==karsilik[secim].ad.lower():
                            for ii in i.tarif:
                                if i.tarif.index(ii)==0:
                                    for iii in ii:
                                        print(iii)

                                    yeniSayi=input("Kaç Malzeme İstiyorsunuz: ")
                                    
                                    if yeniSayi.isdigit():
                                        malzemeler=list()
                                        for iii in range(int(yeniSayi)):
                                            yeniMalzeme=input(f"{iii+1}. yeni malzeme: ")
                                            malzemeler.append(yeniMalzeme)
                                        i.tarif[0]=malzemeler

                                        for r in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):

                                            if r.lower()==karsilik[secim].lower():


                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Tarif.txt".format(r),"a+")
                                                x=dosya.read()
                                                x.split("Tarif")
                                                x[0]=malzemeler
                                                dosya.close()
                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Tarif.txt".format(r),"w")
                                                for i in x[0]:
                                                    dosya.write(f"{i}\n")
                                                dosya.write("Tarif\n")
                                                for i in x[1]:
                                                    dosya.write(f"{i}\n")
                                                break

                                                dosya.close()
                                        


                                    else:
                                        print("Geçersiz Değer!!")
                                        ts(3)


                        
                        

                elif secim=="2":
                    for i in yemekler:
                        if i.ad.lower() ==karsilik[secim].ad.lower():
                            for ii in i.tarif:
                                if i.tarif.index(ii)==0:
                                    for iii in ii:
                                        print(iii)

                                    yeniSayi=input("Kaç Adım İstiyorsunuz: ")
                                    
                                    if yeniSayi.isdigit():
                                        surec=list()
                                        for iii in range(int(yeniSayi)):
                                            yeniAdim=input(f"{iii+1}. yeni adım: ")
                                            surec.append(yeniAdim)

                                            
                                        i.tarif[1].clear()
                                        for o in enumerate(surec):
                                            i.tarif[1][o[0]+1]=o[2]



                                        for r in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):

                                            if r.lower()==karsilik[secim].lower():


                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Tarif.txt".format(r),"a+")
                                                x=dosya.read()
                                                x.split("Tarif")
                                                x[1]=surec
                                                dosya.close()
                                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Tarif.txt".format(r),"w")
                                                for i in x[0]:
                                                    dosya.write(f"{i}\n")
                                                dosya.write("Tarif\n")
                                                for i in x[1]:
                                                    dosya.write(f"{i}\n")

                                                break
                                                dosya.close()

                else:
                    print("\nGeçersiz Değer")
                    ts(3)


        elif secim1=="4":
            while True:
                os.system("cls")
                print(yemekler[yemekler.index(karsilik[secim])].miktar)
                yeniMiktar=input("Yeni Miktar: ")
                if yeniMiktar.isdigit():
                    yemekler[yemekler.index(karsilik[secim])].miktar=yeniMiktar
                    for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                        if i.lower()==karsilik[secim].lower():
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Miktar1.txt".format(i),"w")
                            dosya.write(yeniMiktar)
                            break

                            dosya.close()

                    break
                    


                else:
                    print("\nGeçersiz Değer\n")
                    ts(3)
            #miktar düzenleme

        elif secim1=="5":
            while True:
                os.system("cls")
                print(yemekler[yemekler.index(karsilik[secim])].miktarOlcegi)
                yeniMiktarOlcegi=input("Yeni Miktar Ölçeği: ")
                if yeniMiktarOlcegi.isalpha():
                    yemekler[yemekler.index(karsilik[secim])].miktarOlcegi=yeniMiktarOlcegi
                    for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                        if i.lower()==karsilik[secim].lower():
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\Miktar Ölçeği.txt".format(i),"w")
                            dosya.write(yeniMiktarOlcegi)
                            break

                            dosya.close()

                    break
                    


                else:
                    print("\nGeçersiz Değer\n")
                    ts(3)
            #miktar ölçeği düzenleme

        else:
            print("\nGeçersiz Değer!!\n")
            ts(3)



def musteriGirisi():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    global musteriGirdi,sahipGirildi,girenMusteri
    while True:
        os.system("cls")
        
        o=1
        if o==1:
            kullanici_adi=input("Kullanınıcı Adınız: ".lower())
            count=0
            for i in Müşteriler:
                if i.kullanici_adi==kullanici_adi:
                    parola=input(f"Hoşgeldiniz {i.isim}, Parola rica ediyim: ".lower())
                    if i.parola==parola:
                        print("Giriş Yapıldı!!")
                        musteriGirdi=True
                        girenMusteri.clear()
                            
                        girenMusteri.append(Musteri(kullanici_adi,parola,i.isim))
                        

                    else:
                        print("Geçersiz Parola!!")
                        o=1
                        break




                else:
                    count+=1

            if count==len(Müşteriler):
                print("Geçersiz Kullancı Adı!!")
                continue
    #musteriGirdi yi true ve false diye ayarlamayı unutma!!
    

def rezervasyonYap():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    if not os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi"):

        
        while True:
            flag=False
            os.system("cls")
            if masalar:
                for i in  masalar:
                    print(i.ad)

                secim=input("Masanız: ")

                if secim.lower() in [x.ad.lower() for x in masalar]:
                    for i in masalar:
                        if i.ad.lower()==secim.lower():
                            masa=i
                            flag=True
                            break

                    break

                else:
                    print("Hatalı Giriş!!!")
                

            else:
                print("Lokantada masa yok!!!!!\n")
                break

        
        if flag:
            tarih=tt()

            while True:
                os.system("cls")
                print("""
                [1] İçecekler
                [2] Yemekler
                [3] Menüler
                [4] Tamamlandı
                """)
                alinanlar=[]
                secim=input("Hangi Kategoriden Alacaksınız? ")
                
                if secim=="1":
                    
                    while True:
                        if icecekler:
                            os.system("cls")
                            for i in icecekler:
                                print(f"{i.ad}---->{i.fiyat}")

                            secim=input("Hangisi: ")
                            if secim.lower() in [x.ad.lower() for x in icecekler]:
                                for i in icecekler:
                                    if i.ad.lower()==secim.lower():
                                        alinanlar.append(i)



                                break


                            else:
                                print("Geçersiz İnput!!!")
                                ts(3)

                        else:
                            print("İçecek Yok!!!")
                            ts(3)
                            break
                    
                            

                elif secim=="2":

                    while True:
                        if yemekler:
                            os.system("cls")
                            for i in yemekler:
                                print(f"{i.ad}---->{i.fiyat}")

                            secim=input("Hangisi: ")
                            if secim.lower() in [x.ad.lower() for x in yemekler]:
                                for i in yemekler:
                                    if i.ad.lower()==secim.lower():
                                        alinanlar.append(i)


                                break


                            else:
                                print("Geçersiz İnput!!!")
                                ts(3)

                        else:
                            print("Yemek Yok!!!")
                            ts(3)
                            break


                elif secim=="3":
                    while True:
                        if menuler:
                            os.system("cls")
                            count=0
                            karsilik=dict()
                            for i in menuler:
                                count+=1
                                print(f"[{count}] {[x for x in i.icerik]}---->{i.fiyat}")
                                karsilik.setdefault(count,i)

                            secim=input("Seçiminiz: ")
                            if secim.isdigit() and secim.lower() in list(karsilik.keys()):
                                for  i in list(karsilik.keys()):
                                    if i==secim:
                                        alinanlar.append(karsilik[i])

                                break



                            else:
                                print("\nHatalı Giriş\n")
                                ts(3)


                        else:
                            print("İçecek Yok!!!")
                            ts(3)
                            break 


                elif secim=="4":
                    if alinanlar:
                    
                        break

                    else:
                        print("Bişey Alın Da Öyle Gidin")
                        ts(3)


                else:
                    print("Geçersiz Değer!!")
                    ts(3)



            fiyat=0
            for i in alinanlar:
                fiyat+=int(i.fiyat)
            fiyat+=masa.fiyat
            total= []
            for i in alinanlar:
                if type(i)==Menu:
                    for x in i.yiyeceklerİcecekler:
                        total.append(x)

                else:
                    total.append(i)
            rezervasyonlar.append(Rezervasyon(masa,fiyat,tarih,total))

            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Rezervasyonlar\{}.txt".format(f"Rezervasyon{len(rezervasyonlar)+1}"))
            dosya.write(f"{masa}\n{fiyat}\n{tarih}")

            for i in total:
                dosya.write("\n"+i)

            dosya.close()
            
        
    else:
        print("\nDaha Lokanta Yok.....!!!!!!!?******\n")
        ts(3)


    # class Rezervasyon():
    # def __init__(self,masaAdi,fiyat,tarih,yiyeceklerİcecekler):
    #     self.masaAdi=masaAdi
    #     self.fiyat=fiyat
    #     self.tarih=tarih
    #     self.yiyeceklerİcecekler=yiyeceklerİcecekler


#her yeni müşteri için Bilgiler.txt ve Rezervasyonlar klasörü oluştur
        #her rezervasyonda ilk satıra kullanıcının seçtiği masa adı ikinci satıra fiyat üçüncü satıra tarih kalanlara menü seçmiş olsa 
    # bile menünün içeriğindeki yemek ve içecekleri menü almamışsa normal yemek ve içecekleri bas 
    #her rezervasyon için ayrı txt oluştur Rezervasyon1,Rezervasyon2,rezervasyon3.txt şeklinde
    #dosya oluşturuken Revervasyon{}.txt.format(len(rezervasyonlar)+1) şeklinde yap
    ##############################({i:Rezervasyon(j[0],j[1],j[2],j[3:])}) rezervasyon listesinde fpormat bu şekilde i:kullanıcının ismi
    #her rezervasyonda seçili masanın hesabına ücreti eklemeyi unutma masa geçmişine de kaydet ayrıca 
    #######################eğer masanın hesabı 0 deilse kullanıcıya bu masa dolu de ve başka masa seçmeini iste




def menuEkle():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    if icecekler and yemekler:
        while True:
            os.system("cls")
            karsilik={}
            count=0
            eklenecekler=[]
            for  i in yemekler:
                count+=1
                print(f"[{count}] {i.ad}")
                karsilik.setdefault(count,i)
            
            count+=1
            print(f"[{count}]-->İçecek Seçmeyle Devam!")


            secim=input("\nSeçiminiz: \n")

            if secim in list(karsilik.keys()):
                for i in icecekler:
                    if i.ad==karsilik[secim]:
                        eklenecekler.append(i)

            elif secim==count:
                break


            else:
                print("\nGeçersiz Değer!!!")
                ts(3)

        while True:
            os.system("cls")
            karsilik={}
            count=0
            #eklenecekler=[]
            for  i in icecekler:
                count+=1
                print(f"[{count}] {i.ad}")
                karsilik.setdefault(count,i)
            
            count+=1
            print(f"[{count}]-->Tamamlandı!")


            secim=input("\nSeçiminiz: \n")

            if secim in list(karsilik.keys()):
                for i in icecekler:
                    if i.ad==karsilik[secim]:
                        eklenecekler.append(i)

            elif secim==count:
                break


            else:
                print("\nGeçersiz Değer!!!")
                ts(3)

        while True:
            os.system("cls")
            ad=input("Menünün Adı: ")
            if ad:
                break

            else:
                print("Geçersiz Değer")
                ts(3)

        while True:
            os.system("cls")
            fiyat=input("Menünün Fiyatı: ")
            if fiyat.isdigit():
                fiyat=int(fiyat)
                break

            else:
                print("Geçersiz Değer")
                ts(3)

        totalFiyat=0
        for i in eklenecekler:
            totalFiyat+=i.fiyat


        kar=fiyat-totalFiyat
        menuler.append(Menu([x.ad for  x in eklenecekler],kar,ad,fiyat))
        dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Menüler\{}.txt".format(ad),"w")
        dosya.write(ad)
        dosya.write("\n")
        for i in eklenecekler:
            dosya.write(f"{i.ad}\n")

        dosya.write(f"{kar}\n{fiyat}")
        dosya.close()
            



        

    else:
        print("İçecek ve Yemek Yok!!!")
        ts(3)



    ###$$#$#$£#>½#[$bu fonksiyona if icecekler ve if yemekler ifadfelerini ekle sonra sırayla iki listeyi de ekrana bas 
    # (sadece objelerin adlarını listele ekrana) sonra kullanıcıdan menüye kelemek istediklerini [1] [2] 
    # numaralndırma sistemi kullanarak girmesini iste sonra pc hesaplasın girilen yiyecek içeceklerin normal 
    # fiyatını sonra kar miktarını hesaplasın vwe listeye öyle eklesin fiyatı ve adı al txt dosyasının tepesine ad ve txt dosyasının ad=menü adı
    # en alta fiyat yaz fiyatın bi üstü kar olsun dosyada onun üstü d içecek yemek falan(dosyada)
    #masa yemekde olduğu gibi ekstra klasör olmadan direk her menün ün bir txt dosyası olsun
    

                            
def masaSil():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        karsilik={}
        count=0
        for i in masalar:
            count+=1
            print(f"[{count}] {i.ad}")
            
            karsilik.setdefault(count,i.ad)

        secim=input("\nSeçiminiz: \n")
        
        if secim in list(karsilik.keys()):
            for i in masalar:
                if i.ad==karsilik[secim]:
                    masalar.remove(i)
                    for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar"):
                        if dosya.lower()==i.ad.lower():
                            os.removedirs(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\{}".format(dosya))
            
            break

        else:
            print("Geçersiz Değer!!")
            ts(3) 

def yeniMusteriKayit():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        isim=input("İsminiz: ")
        if isim.isalpha():
            break
        else:
            print("\nLütfen sadece harf giriniz::::")
            ts(3)

    while True:
        os.system("cls")
        kullanici_adi=input("Kullanıcı Adınız: ")
        if len(kullanici_adi)>6:
            break

        else:
            print("\nKullanıcı adının karakter sayısı 6dan fazl aolmalı")
            ts(3)

    while True:
        os.system("cls")
        parola=input("Parolanız: ")
        if len(parola)>6:
            break

        else:
            print("\nParolanın karakter sayısı 6dan fazl aolmalı")
            ts(3)

    Müşteriler.append(Musteri(kullanici_adi,parola,isim))
    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler\{}".format(isim),"w")
    dosya.write(f"{kullanici_adi}\n{parola}\n{isim}")

    dosya.close()        
    #her yeni müşteri için Kullanıcı Bilgileri.txt klasörü oluştur
    #her kullanıcı için ayrı dosya(normal klasör) klasörlerinin adları seçtikleri isim olsun
    #  oluştur ve klasörlerin içine 
    # kullanıcı girişl bilgileri için ayrı ve her rezervasyon bilgileri için(bir müşteride birden fazla olabilir) ayrı txt ler oluştur
    #Kullanıcı giriş bilgileri için dosya adı = Giriş Bilgileri.txt   rezervasyon için ad= aşağıda yazıyo
    #Bilgiler dosyasının ilk satırında kullanıcı adı ikinci satırında parola üçüncü satırında da isim yazsın
    #her rezervasyonda ilk satıra kullanıcının seçtiği masa adı ikinci satıra fiyat üçüncü satıra tarih menü seçmiş olsa 
    # bile menünün içeriğindeki yemek ve içecekleri menü almamışsa normal yemek ve içecekleri bas 
    #her rezervasyon için ayrı txt oluştur Rezervasyon1,Rezervasyon2,rezervasyon3.txt şeklinde
    #dosya oluşturuken Revervasyon{}.txt.format(len(rezervasyonlar)+1) şeklinde yap



def menuCikar():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    while True:
        os.system("cls")
        karsilik={}
        count=0
        for i in menuler:
            count+=1
            print(f"[{count}] {i.ad}")
            
            karsilik.setdefault(count,i.ad)

        secim=input("\nSeçiminiz: \n")
        
        if secim in list(karsilik.keys()):
            for i in menuler:
                if i.ad==karsilik[secim]:
                    menuler.remove(i)
                    for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menuler"):
                        l=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menüler\{}".format(dosya))
                        l1=l.readlines()
                        l1=l1[0]
                        if dosya.lower()==l1.lower():
                            os.removedirs(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menuler\{}".format(dosya))
            
            break

        else:
            print("Geçersiz Değer!!")
            ts(3) 







def musteriİslemleri():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    global musteriGirdi,sahipGirildi
    musteriGirisi()
    #Bitmediiiiiiiiiiiiii
    while True:
        musteriGirdi=True
        os.system("cls")
        print("""
        [1] Rezervasyon yap
        [2] Bilgileri Görüntüle
        [Q] Çıkış
        """)
        secim=input("Seçiminiz: ")
        
        if secim=="1":
            rezervasyonYap()
            input("\nana Menüye Dönmek İçin Entera Basın!!!")


        elif secim=="2":
            for i in girenMusteri:
                print(f"İsim: {i.isim}")
                print(f"Kullanıcı Adı: {i.kullanici_adi}")
                print(f"Parola: {i.parola}")

            input("\nana Menüye Dönmek İçin Entera Basın!!!")
            


        elif secim.lower()=="q":
            break
            musteriGirdi=False

        else:
            print("Geçersiz Değer!!!!!!!!!")
            ts(3)

#sahip işlemleri tamamlanmadı!!!!!!!!!!!
def sahipİslemleri():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar
    global musteriGirdi,sahipGirildi
    sahipGirisi()
    z=0
    if z==0:
        if z==0:
            if z==0:
                
                # çıkış işlemini tüm listleri clear ile temizleyip burda çıkcak seçenek menüsünün döngüsünü kırp üste geçerek yap
                while True:
                    os.system("cls")
                    print("""
                    [0] Hesaptan Çıkış
                    [1] Görüntüle
                    [2] Ekle/Çıkar/Düzenle
                    [3] Hesap İşlemleri

                    """)
                    secim=input("İşleminiz: ")

                    if secim=="0":
                        input("Çıkmak için 'enter'a basın!!!")
                        break
                        # çıkış işlemini tüm listleri clear ile temizleyip burda çıkcak seçenek menüsünün döngüsünü kırp üste geçerek yap

                    elif secim=="1":
                        while True:
                            os.system("cls")
                            print("""
                            [0] Üst Menü
                            [1] Hesap Bilgileri Görüntüle
                            [2] Masaları {0} Görüntüle (Lüxlük Seviyesi ve Bilgileri Dahil)
                            [3] Menüleri {1} Görüntüle
                            [4] İçecekleri {1} Görüntüle
                            [5] Yemekleri {1} Görüntüle
                            [6] Tüm Rezervasyonları Görüntüle
                            [7] Masaların Geçmişini Görüntüle
                            [8] Müşterileri Görüntüle

                            """.format("(Geçmiş Harç Tüm Bilgiler)","(Tüm Bilgiler)"))
                            secim=input("\nİşleminiz: ")

                            if secim=="0":
                                os.system("cls")
                                
                                input("Onaylıyorsanız 'enter'a basın!!!")
                                sahipGirildi=False
                                break

                            elif secim=="1":
                                os.system("cls")
                                for i in enumerate( LokantaSahip):
                                    if i[0]=="0":
                                        print(f"\nKullanıcı Adı: {i.kullanici_adi}")

                                    elif i[0]=="1":
                                        print(f"\nŞifreniz: {i.parola}")


                                    else:
                                        print(f"\nAdınız: {i.isim}")

                                input("\nAna Menüye Dönmek İçin 'enter'a bas!!")

                            elif secim=="2":
                                os.system("cls")
                                for i in masalar:
                                    print("Masa".center(20,"\n"))
                                    ts(0.4)
                                    print(f"\nMasa Adı       : {i.ad}\n")
                                    ts(0.5)
                                    print(f"Masa Numarası  : {i.no}\n")
                                    ts(0.6)
                                    print("Lüxlük".center(20,"\n"))
                                    ts(0.7)
                                    print(f"Masa {i.ad},{f'({i.no})'} için Lüxlük Adı:    {i.luxluk_seviyesi.ad} ")
                                    ts(0.8)
                                    print(f"Masa {i.ad},{f'({i.no})'} için Lüxlük Ücreti: {i.luxluk_seviyesi.fiyat} ")
                                    ts(2)
                                    for ii in i.luxluk_seviyesi:
                                        if i.luxluk_seviyesi.index(ii)=="1":
                                            print(f"Masa {i.ad},{f'({i.no})'} için  Ek Hizmetler: ")
                                            for iii in ii:
                                                print(f"{ii}\n")

                                        elif i.luxluk_seviyesi.index(ii)=="2":
                                            print(f"Masa {i.ad},{f'({i.no})'} için  Ek Malzemeler: ")
                                            for iii in ii:
                                                print(f"{ii}\n")

                                    input("\nDiğerini Görüntülemek İçin 'enter'a bas!!")


                                input("Ana menüye dönmek için 'enter'a bas!!")

                            elif secim=="3":
                                os.system("cls")
                                for i in menuler:#icerik: list, kar: int, ad: str, fiyat: in
                                    print("Menü".center(20,"\n"))
                                    ts(0.4)
                                    print(f"\nMenü Adı       : {i.ad}\n")
                                    ts(0.5)
                                    print(f"Menü Fiyatı  : {i.fiyat}\n")
                                    ts(0.6)
                                    print(f"Menü Kar  : {i.kar}\n")
                                    ts(0.6)
                                    print("İçerik".center(20,"\n"))
                                    ts(0.7)
                                    
                                    for ii in i.icerik:
                                        print(ii)
                                        ts(3)

                                    input("\nDiğerini Görüntülemek İçin 'enter'a bas!!")
                                   
                                input("Ana menüye dönmek için 'enter'a bas!!")


                            elif secim=="4":
                                os.system("cls")
                                for i in icecekler:#ad: str, fiyat: int, tarif: Tarif, miktar: int, miktarOlcegi: str)
                                    print("İçecek".center(20,"\n"))
                                    ts(0.4)
                                    print(f"\nİçecek Adı       : {i.ad}\n")
                                    ts(0.5)
                                    print(f"İçecek Fiyatı  : {i.fiyat}\n")
                                    ts(0.6)
                                    print(f"İçecek Miktarı  : {i.miktar}\n")
                                    ts(0.6)
                                    print(f"İçecek Miktar Ölçeği  : {i.miktarOlcegi}\n")
                                    ts(0.6)
                                    for ii in i.tarif:#malzemeler: list, surec: dict
                                        if i.tarif.index(ii)==0:
                                            print("Tarif Malzemeleri".center(20,"\n"))
                                            ts(0.7)
                                            for iii in ii:
                                                print(iii)
                                                ts(0.4)

                                        elif i.tarif.index(ii)==1:
                                            print("Tarif Süreci".center(20,"\n"))
                                            ts(0.7)
                                            sozluk={}
                                            for a in i.tarif[1] :
                                                sozluk.setdefault(a[0]+1,a[1])
                                            for iii in ii:
                                                print(f"{iii}----> {sozluk[iii]}")


                                    input("\nDiğerini Görüntülemek İçin 'enter'a bas!!")


                                input("Ana menüye dönmek için 'enter'a bas!!")



                            elif secim=="5":
                                os.system("cls")
                                for i in yemekler:#ad: str, fiyat: int, tarif: Tarif, miktar: int, miktarOlcegi: str)
                                    print("Yemek".center(20,"\n"))
                                    ts(0.4)
                                    print(f"\nYemek Adı       : {i.ad}\n")
                                    ts(0.5)
                                    print(f"Yemek Fiyatı  : {i.fiyat}\n")
                                    ts(0.6)
                                    print(f"Yemek Miktarı  : {i.miktar}\n")
                                    ts(0.6)
                                    print(f"Yemek Miktar Ölçeği  : {i.miktarOlcegi}\n")
                                    ts(0.6)
                                    for ii in i.tarif:#malzemeler: list, surec: dict
                                        if i.tarif.index(ii)==0:
                                            print("Tarif Malzemeleri".center(20,"\n"))
                                            ts(0.7)
                                            for iii in ii:
                                                print(iii)
                                                ts(0.4)

                                        elif i.tarif.index(ii)==1:
                                            print("Tarif Süreci".center(20,"\n"))
                                            ts(0.7)
                                            sozluk={}
                                            for a in i.tarif[1] :
                                                sozluk.setdefault(a[0]+1,a[1])
                                            for iii in ii:
                                                print(f"{iii}----> {sozluk[iii]}")


                                    input("\nDiğerini Görüntülemek İçin 'enter'a bas!!")


                                input("Ana menüye dönmek için 'enter'a bas!!")



                            elif secim=="6":
                                os.system("cls")
                                for i in rezervasyonlar:
                                    print(f"{i.tarih}----->Masa Adı:{i.masaAdi} Fiyat:{i.fiyat}")
                                    for ii in i.yiyeceklerİcecekler:
                                        print(ii)
                               


                                                




                                    
                                    
                                    
                            
                            elif secim=="7":
                                os.system("cls")
                                for i in masalar:
                                    for a,b in i.gecmis.items():
                                        print("{:<30}---->{:>30}".format(a,b))



                                input("Ana menüye dönmek için 'enter'a bas!!")


                            elif secim=="8":
                                for i in Müşteriler:
                                    print(f"{i.isim}-------->Kullanıcı Adı: {i.kullanici_adi} Parola: {i.parola}")

                                input("Ana menüye dönmek için 'enter'a bas!!")

                            else:
                                print("Geçersiz Değer!!")
                                ts(3)


                                
                    


                    elif secim=="2":
                        while True:
                            os.system("cls")
                            print("""
                            [1] Çıkar
                            [2] Ekle
                            [3] Düzenle
                            [Q] Çıkış
                            """)

                            secim=input("İşleminiz: ")



                            if secim=="1":
                                while True:
                                    os.system("cls")
                                    print("""
                                    [1] Yemekler
                                    [2] İçecekler
                                    [3] Masalar
                                    [4] Menüler
                                    [Q] Çıkış
                                    
                                    """)

                                    secim=input("\nHangi kategoriden eleman Çıkaracaksınız?\n")

                                    if secim=="1":
                                        yemekCikar()
                                        input("Ana menüye dönmek için 'enter'a bas!!")

                                    elif secim=="2":
                                        icecekCikar()
                                        input("Ana menüye dönmek için 'enter'a bas!!")



                                    elif  secim=="3":
                                        masaSil()
                                        input("Ana menüye dönmek için 'enter'a bas!!")
                                        

                                    elif secim=="4":
                                        menuCikar()
                                        input("Ana menüye dönmek için 'enter'a bas!!")

                                    elif secim.lower()=="q":
                                        break
                                        
                                    else:
                                        print("\nGeçersiz Seçim\n")
                                        ts(3)
                                    
                            #burada masa yemek iiçecek vb arasınan [1] sistemi ile seçim yapmasını iste kullanıcıdan sonra kalan herşey 
                            # fonksiyonda tanımlı





                            elif secim=="2":
                                while True:
                                    os.system("cls")
                                    print("""
                                    [1] Yemekler
                                    [2] İçecekler
                                    [3] Masalar
                                    [4] Menüler
                                    [Q] Çıkış
                                    
                                    """)

                                    secim=input("\nHangi kategoriye eleman ekleyeceksiniz??\n")

                                    if secim=="1":
                                        yemekEkle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")

                                    elif secim=="2":
                                        icecekEkle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")



                                    elif  secim=="3":
                                        masaEkle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")
                                        

                                    elif secim=="4":
                                        menuEkle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")

                                    elif secim.lower()=="q":
                                        break
                                        
                                    else:
                                        print("\nGeçersiz Seçim\n")
                                        ts(3)
                                    
                            #burada masa yemek iiçecek vb arasınan [1] sistemi ile seçim yapmasını iste kullanıcıdan sonra kalan herşey 
                            # fonksiyonda tanımlı




                            elif secim.lower()=="q":
                                break


                            elif secim=="3":
                                while True:
                                    os.system("cls")
                                    print("""
                                    [1] Yemekler
                                    [2] İçecekler
                                    [Q] Çıkış
                                    
                                    """)

                                    secim=input("\nHangi kategoriden eleman düzenleyeceksiniz?\n")

                                    if secim=="1":
                                        yemekDuzenle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")

                                    elif secim=="2":
                                        icecekDuzenle()
                                        input("Ana menüye dönmek için 'enter'a bas!!")



                                   

                                    elif secim.lower()=="q":
                                        break
                                        
                                    else:
                                        print("\nGeçersiz Seçim\n")
                                        ts(3)
                                    
                            #burada masa yemek iiçecek vb arasınan [1] sistemi ile seçim yapmasını iste kullanıcıdan sonra kalan herşey 
                            # fonksiyonda tanımlı


                            else:
                                print("Geçersiz Seçim!!")
                                break


                    elif secim=="3":

                        while True:
                            os.system("cls")
                            print("""
                            [1] İsim
                            [2] Kullanıcı Adı
                            [3] Parola
                            """)

                            secim=input("\nHangisini Düzenlemek İstersiniz?\n")
                            
                            if secim=="1":
                                print(f"\nGeçerli İsminiz----->{LokantaSahip[0].ad}")
                                yeniAd=input("\nYeni Adınız: ")
                                LokantaSahip[0].ad=yeniAd
                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Bilgiler.txt","w")
                                dosya.write(LokantaSahip[0].kullanici_adi)
                                dosya.write("\n")
                                dosya.write(LokantaSahip[0].parola)
                                dosya.write("\n")
                                dosya.write(yeniAd)
                                dosya.close()
                                
                                

                            elif secim=="2":
                                print(f"\nGeçerli Kullanıcı Adınız----->{LokantaSahip[0].kullanici_adi}")
                                yeniKullanici_adi=input("\nYeni Kullanıcı Adınız: ")
                                LokantaSahip[0].kullanici_adi=yeniKullanici_adi
                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Bilgiler.txt","w")
                                dosya.write(yeniKullanici_adi)
                                dosya.write("\n")
                                dosya.write(LokantaSahip[0].parola)
                                dosya.write("\n")
                                dosya.write(LokantaSahip[0].ad)
                                dosya.close()

                            elif secim=="3":
                                print(f"\nGeçerli Parolanız----->{LokantaSahip[0].parola}")
                                yeniParola=input("\nYeni Parolanız: ")
                                LokantaSahip[0].parola=yeniParola
                                dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Bilgiler.txt","w")
                                dosya.write(LokantaSahip[0].kullanici_adi)
                                dosya.write("\n")
                                dosya.write(yeniParola)
                                dosya.write("\n")
                                dosya.write(LokantaSahip[0].ad)
                                dosya.close()



                            else:
                                print("\nGeçersiz Seçim\n")
                                ts(3)

                        #burada hesap bilgilerinin göster ve düzenleme fırsatı ver, düzenlemek 
                        #için replace metodu kullan(sonu.çta listlerin içinde str var) dosyaya da yaz

                            

                                

                    #her rezervasyon müşterisinin geçmişte yaptığı 
                    # rezervasyonlar seçtiği masa yediği yemek içecek menü verdiği bahşiş 
                    # ücret her şeyi gösterecek bir şey olsun [6] seçimi (yani kullanıcı profili)


def main():
    global yemekler,icecekler,menuler,Müşteriler,LokantaSahibi,rezervasyonlar,masalar,sahipGirildi,musteriGirdi
    


    flag1=False
    if  os.path.exists(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı"):
        flag1=True

    if flag1:
        
        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar")
        if "Bilgiler.txt" in  os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi") :
            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Bilgiler.txt","r")
            v=dosya.read().split("\n")
            a=v[-1]
            
            LokantaSahip.append(LokantaSahibi(v[0],v[1],v[2]))
            
            dosya.close()



        
            
        if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Rezervasyonlar"):
            for dosya in  os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Rezervasyonlar"):
                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Rezervasyonlar\{}".format(dosya))
                dd=dosya1.readlines()
                d=dd[0]
                d1=dd[1]
                d2=dd[2]
                d3=dd[3:]
                
                rezervasyonlar.append(Rezervasyon(d,d1,d2,d3))




        


                        




        try:
            os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar")
            if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar"):
                lll=0
                for index,dosya in enumerate(os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar")):
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar")
                    if lll==0:
                        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\{}".format(dosya))
                        for txt in os.listdir():
                            z=0
                            if z==0 :
                                lll+=0
                                a=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\{}\{}".format(dosya,txt),"r")
                                b=a.read()
                                b=b.split("\n")
                                b.pop()
                                if not b:
                                    b=a.read()

                                a.close()
                                cout=0
                                for txt1 in os.listdir():
                                    if "Geçmiş" in txt1:
                                        cout+=1
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\{}\{}".format(dosya,txt1),"r")
                                        c=d.read()
                                        c=c.split("\n")
                                        c.pop()
                                        if len(c)%2==1:
                                            c=d.read()
                                            c=c.split("\n")
                                        

                                        d.close()
                                        plpl=[]
                                        for eleman in c:
                                            if c.index(eleman)%2==0:
                                                plpl.append({eleman:c.index(c.index(eleman)+1)})

                                            else:
                                                pass

                                        break
                                                    

                                                    
                                                    
                                    else:
                                        cout+=1

                                cout=0
                                for txt1 in os.listdir():
                                    if "Lüx" in txt1:
                                        cout+=1
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Masalar\{}\{}".format(dosya,txt1),"r")
                                        c=d.read()
                                        c=c.split("\n")
                                        c.pop()
                                        if not c:
                                            c=d.read()

                                        d.close()
                                        w=c[0]
                                        w1=c[-1]
                                        del c[-1]
                                        del c[0]
                                        c=c.split("Hizmetler")
                                        cout=0
                                        for eleman in c:
                                            if cout==0:
                                                cout+=1
                                                u=eleman.split("\n")

                                            elif cout==1:
                                                h=eleman.split("\n")
                                                
                                                
                                    else:
                                        cout+=1
                                        
                                                
                                
                                masalar.append(Masa(dosya,index,plpl,Lux(w,h,u,w1)))
                                lll+=1
                                            
                                break
                                            



                                
                                
                                
                            else:
                                pass
                            
                            
                        #break        

                    else:
                        continue        

            os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler")
            if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                sss=0
                for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler"):
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler")

                    if sss==0:
                        
                        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}".format(dosya))
                        for txt in os.listdir():
                            if "Tarif" in txt:
                                
                                a=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\{}".format(dosya,txt),"r")
                                b=a.read()
                                b=b.split("Tarif")
                                for index,eleman in enumerate(b):
                                    if index==0:
                                        s=eleman.split("\n")

                                    if index ==1:
                                        p=eleman.split("\n")
                                

                                a.close()
                                cout=0
                                for txt1 in os.listdir():
                                    if "Fiyat" in txt1:
                                        cout+=1
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\{}".format(dosya,txt1),"r")
                                        c=d.readlines()
                                        
                                        if len(c)%2==0:
                                            c.pop()
                                            #c=c.split("\n")
                                        

                                        d.close()
                                        cout=0
                                        for eleman in c:
                                            if cout==0:
                                                cout+=1
                                                c=int(eleman)

                                    elif "Miktar1" in txt1:
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\{}".format(dosya,txt1),"r")
                                        y=d.readlines()
                                        if len(y)%2==0:
                                            y.pop()

                                        d.close()
                                        cout=0
                                        for eleman in y:
                                            if cout==0:
                                                cout+=1
                                                y=int(eleman)

                                    elif "Miktar Ölçeği" in txt1:
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Yemekler\{}\{}".format(dosya,txt1),"r")
                                        z=d.readlines()
                                        if len(z)%2==0:
                                            z.pop()

                                        d.close()
                                        cout=0
                                        for eleman in z:
                                            if cout==0:
                                                cout+=1
                                                z=str(eleman)

                                yemekler.append(Yemek(dosya,c,Tarif(s,p),y,z))


                                        
                                        
                                break




            
            os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler")
            if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):
                sss=0
                for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler"):
                    os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler")

                    if sss==0:
                        
                        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}".format(dosya))
                        for txt in os.listdir():
                            if "Tarif" in txt:
                                
                                a=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\{}".format(dosya,txt),"r")
                                b=a.read()
                                b=b.split("Tarif")
                                for index,eleman in enumerate(b):
                                    if index==0:
                                        s=eleman.split("\n")

                                    if index ==1:
                                        p=eleman.split("\n")
                                

                                a.close()
                                cout=0
                                for txt1 in os.listdir():
                                    if "Fiyat" in txt1:
                                        cout+=1
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\{}".format(dosya,txt1),"r")
                                        c=d.readlines()
                                        
                                        if len(c)%2==0:
                                            c.pop()
                                            #c=c.split("\n")
                                        

                                        d.close()
                                        cout=0
                                        for eleman in c:
                                            if cout==0:
                                                cout+=1
                                                c=int(eleman)

                                    elif "Miktar1" in txt1:
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\{}".format(dosya,txt1),"r")
                                        y=d.readlines()
                                        if len(y)%2==0:
                                            y.pop()

                                        d.close()
                                        cout=0
                                        for eleman in y:
                                            if cout==0:
                                                cout+=1
                                                y=int(eleman)

                                    elif "Miktar Ölçeği" in txt1:
                                        d=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\İçecekler\{}\{}".format(dosya,txt1),"r")
                                        z=d.readlines()
                                        if len(z)%2==0:
                                            z.pop()

                                        d.close()
                                        cout=0
                                        for eleman in z:
                                            if cout==0:
                                                cout+=1
                                                z=str(eleman)

                                icecekler.append(Icecek(dosya,c,Tarif(s,p),y,z))


                                        
                                        
                                break


                            

                                        

            os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menüler")
            if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menüler"):
                sss=0#menu versiyonu yap
                for dosya in os.listdir():
                    l=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi\Menüler\{}".format(dosya))
                    g=l.read()
                    g=g.split("\n")
                    w=g[-1]
                    w1=g[0]
                    w2=g[-2]
                    del g[-1]
                    del g[-2]
                    del g[0]
                   


                    menuler.append(Menu(g,w2,w1,w))



            if os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler"):
                for i in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler"):

                    if "Bilgileri" in i:
                        dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler\{}".format(i))
                        dosya1=dosya.readlines()
                        j=dosya1[0]
                        j1=dosya1[1] #parola
                        j2=dosya1[2]
                        dosya.close()
                        Müşteriler.append(Musteri(j,j1,j2))

        except:
            pass




    else:

        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim")
        os.makedirs("Lokanta Veri Tabanı")
        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı")
        os.makedirs("Kullanıcılar")
        os.chdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar")
        os.makedirs("Lokanta Sahibi")
        os.makedirs("Müşteriler")
        os.makedirs("Rezervasyonlar")


        for i in range(10):
            os.system("cls")
            print("\nİlk kez çalıştırıldığı için kayıt dosyaları oluşturuluyor{}".format(((i%3)+1)*"."))
            ts(0.4)
        ts(3)

        



 
    
    while True:
        os.system("cls")

        print("""
        [0] Bilgi
        [1] Rezervasyon İçin Kullanıcı Girişi/Kayıtı
        [2] Lokanta Yönetimi Kullanıcı Girişi/Kayıtı
        [H] Yardım
        [Q] Çıkış


        """)

        #2 seçildiğinde ayrı 1 seçildiğinde ayrı alt menüler çıksınb ve çıkış ile üst menü seçenkleri olsun

        #kullanıcı girişleri içinm hiç kullanıcı yoksa kayıt ol varsa kayıt ol artı giriş eçeneği çıksın ve 
        # veriabnındaki veriler ile eşleşiyosa kullanıcı sistreme giriş yapığp 
        # kendi eski verileriyle işleme devam etin rezervasyon da random la bazen çek ve kampanyalar sun kullanıcıya
        secim=input("İşleminiz: ")


        if secim=="0":
            print("Üst Düzey Şıkıllımı Değil Lokanta Uygulaması V0.000000000001")
            ts(4)


        elif secim=="1":
           
                    #her rezervasyon müşterisinin geçmişte yaptığı 
                    # rezervasyonlar seçtiği masa yediği yemek içecek menü verdiği bahşiş 
                    #eğer hiç masa yemek içecek menü yoksa bu lokantaada hiçbişey yok daha sonra tekrar deneyin yaz
                    # ücret her şeyi gösterecek bir şey olsun [6] seçimi (yani kullanıcı profili)


            if not sahipGirildi and not os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler"):
                print("\nHesap şimdi oluşturuluyor...\n")
                yeniMusteriKayit()
                
                n=input("\nAna menüye dönmek için 'enter'a hesabınıza giriş yapmak istiyorsanız a + enter a basın!!".strip())
                if not n:
                    continue

                elif n.lower()=="a":
                    musteriİslemleri()
                    #######buraya da lokanta sahibi özel menüsünü yapıştır(aşağıda oluşturup)#################


            elif musteriGirdi or sahipGirildi: 
                print("Şu anda başka bir hesap kullanımda eğer başka bir hesap kaydetmek veya girmek istiyorsanız çıkış yapın!!")
                ts(4)


            elif not sahipGirildi and  os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Müşteriler"):
                while True:
                    os.system("cls")
                    print("""
                    [1] Yeni Kayıt
                    [2] Giriş
                    """)

                    secim=input("Seçiminiz: ")
                    
                    if secim=="1":
                        print("\nHesap şimdi oluşturuluyor...\n")
                        yeniMusteriKayit()
                
                        n=input("\nAna menüye dönmek için 'enter'a hesabınıza giriş yapmak istiyorsanız a + enter a basın!!".strip())
                        if not n:
                            continue

                        elif n.lower()=="a":
                            musteriİslemleri()
                            #######buraya da lokanta sahibi özel menüsünü yapıştır(aşağıda oluşturup)#################

                    elif secim=="2":

                        musteriİslemleri()

                    else:
                        print("Geçersiz Giriş!!")
                        ts(3)


            else:
                print("\nLokanta Sahibi Hesap Oluşturmamış , oluşturmasını bekleyin!!!!!!\n")
                input("\nAna Menüye Dönmek İçin 'enter'a bas!!")



        elif secim=="2":
            if not musteriGirdi and not os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi"):
                print("\nLokanta hesabı şimdi oluşturuluyor...\n")
                lokantaSahibiKayit()
                
                n=input("\nAna menüye dönmek için 'enter'a hesabınıza giriş yapmak istiyorsanız a + enter a basın!!".strip())
                if not n:
                    continue

                elif n.lower()=="a":
                    sahipİslemleri()
                    #######buraya da lokanta sahibi özel menüsünü yapıştır(aşağıda oluşturup)#################


            elif musteriGirdi: 
                print("\nŞu anda başka bir hesap kullanımda eğer başka bir hesap kaydetmek veya girmek istiyorsanız çıkış yapın!!")
                ts(4)


            elif os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Lokanta Veri Tabanı\Kullanıcılar\Lokanta Sahibi") and not musteriGirdi:
                sahipİslemleri()




        elif secim.lower()=="h":
            print("Kullan Geç İşte!!!")
            ts(3)


        elif secim.lower()=="q":
            break

        else:
            print("Geçersiz Seçim!!!")
            ts(2.7)


if  __name__ == "__main__":
    main()
    qqqqq=1








# Volkan taşçının videosunu tekrar incele telefon rehberine bak oralardaki tüm özellikleri bursaya geçir
import sqlite3
from time import sleep as ts
import os
import time

def baslangic():
    
    
    global kisiler,gruplar,imlec,db
    kisiler=[]
    gruplar=[]
    z=0
    if z==0:
        db=sqlite3.connect(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\rehber.sqlite")
        imlec=db.cursor()
        try:
            imlec.execute("CREATE TABLE  'Rehber' (isim,soyisim,telNo,isi)")

        except:
            imlec.execute("SELECT * FROM 'Rehber' ")
            a=imlec.fetchall()
            for i in a:
                for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                    if dosya[-3:]==".txt" and i[0].lower()+".txt"==dosya.lower():
                        dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"r")
                        veri=dosya1.read()
                        veri=veri.split("\n")
                        veri.pop()
                        veri=list(set(veri))
                        dosya1.close()
                kisiler.append(Kisi(i[0],i[1],i[2],i[3],veri))
            grupu=[]
            for i in kisiler:
                grupu.append(i.grup())
            for i in grupu:
                aynilar=0
                for ii in grupu:
                    if i==ii:
                        aynilar+=1 
                        
                gruplar.append(Grup(i,aynilar))

        # finally:
        #     db.close()
            
            
            



baslangic()


class Kisi():
    def __init__(self,isim,soyisim,telNo,isi,grup:list):
        self.isim=isim
        self.grup=grup
        self.soyisim=soyisim
        self.telNo=telNo
        self.isi=isi


    

class Grup():
    def __init__(self,isim,kisiSayisi):
        self.isim=isim
        self.kisiSayisi=0


def grubaKisiEkle(x):
    global kisiler,gruplar,grupTaslak
    if kisiler:
        count=0
        while True:
            os.system("cls")
            print("""
            [1] Yeni Kişi Daha Ekle
            [2] Tamamlandı
            Not:Bir kişi aynı anda en fazla sadece bir grupta bulunabilir!!!!!!
            
            """)
            secim1=input("Seçiminiz: ")
            if secim1=="1":
                if count==0:
                    karsilik={}
                    grupTaslak=[]
                for i in enumerate(kisiler):
                    print(i[1])
                    if count==0:
                        karsilik.setdefault(i[0],i[1])

                count=9827489371111
                
                secim=input("\nSeçiminiz: ")
                
                if secim1 in list(karsilik.keys()):
                    for i in list(karsilik.keys()):
                        if i==secim1:
                            grupTaslak.append(karsilik[i])
                            
                            print("Kişi Eklendi!!")
                            ts(3)
                            
                            break

                else:
                    print("Geçersiz Seçim!!!")
                    ts(3)

            elif secim=="2":
                break

            else:
                print("Geçersiz Seçim")
                ts(3)

            for  dosya1  in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                if i[-3:]=="txt":
                    for i in grupTaslak:
                        if i.ad.lower()+".txt"==dosya1.lower():
                            dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya1),"a+")
                            dosya.write("\n")
                            dosya.write(x)
                            dosya.close()
            break


    else:
        print("Hiç Kişi Yok, kişi ekledikten sonra ana menüden kişi eklemeye gelebilirsiniz!!")
        grupTaslak=[]
        ts(3)

def grupOlustur():
    global kisiler,gruplar
    while True:
        os.system("cls")
        isim=input("Grubun İsmi: ")
        if isim.isalpha():
            flag=True
            for i in gruplar:
                if i.isim==isim:
                    flag=False
                    break
            
            if flag:
                break

            else:
                print("Bu isim kullanımda!!!")
                ts(3)


        else:
            print("\nGeçersiz Değer")
            ts(3)

    grubaKisiEkle(isim)
    z=0
    if z==0:
        pass





    gruplar.append(Grup(isim,len(grupTaslak)))

    



def grupSil():
    global kisiler,gruplar
    
    if gruplar:
        while True:
            os.system("cls")
            count=0
            karsilik={}
            for i in gruplar:
                count+=1
                print(f"[{count}] Grup Adı: {i.ad}, Kişi Sayısı: {i.kisiSayisi}")
                karsilik.setdefault(count,i.ad)

            secim=input("Seçiminiz: ")

            if secim in list(karsilik.keys()):
                for i in gruplar:
                    if karsilik[secim]==i.ad:
                        gruplar.remove(i)
                        break


                for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                    if "txt" in dosya[-3:]:
                        dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"r")
                        veri=dosya1.read()
                        veri=veri.split("\n")
                        veri.pop()
                        for i in veri:
                            if i.lower()==karsilik[secim].lower():
                                veri.remove(i)
                                break

                        dosya1.close()
                        dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"w")
                        for i in veri:
                            dosya1.write(i+"\n")

                        dosya1.close()

                break



            else:
                print("Geçersiz değer!!! ")
                ts(3)
    else:
        print("Grub yok ki silesin!!")
        ts(3)
    #grup silinince kullanıcının dosya veri tabanından da sil grubu

def  kisiEkle():#Kisi(isim, soyisim, telNo, isi, gruplari: list)
    #kişi gurba eklenirse grubtaki kişi sayısını arttır
    global kisiler,gruplar
    while True:
        os.system("cls")
        isim=input("Kişinin İsmi: ")
        if isim:
            break

        else:
            print("Geçersiz Değer!!!")
            ts(3)


    while True:
        os.system("cls")
        soyisim=input("Kişinin Soyismi: ")
        if soyisim:
            break

        else:
            print("Geçersiz Değer!!!")
            ts(3)


    while True:
        os.system("cls")
        telNo=input("Telefon Numarası: ")
        
        if telNo.isdigit():
            break

        else:
            print("\nGeçersiz Değer\n")
            ts(3)


    while True:
        os.system("cls")
        isi=input("Kişinin İsmi: ")
        if isi:
            break

        else:
            print("Geçersiz Değer!!!")
            ts(3)

    kisiTaslak=[]
    while True:
        if gruplar:
            os.system("cls")
            print("""
            [1] Bir tane Daha Ekle
            [2] Tamamlandı
            
            """)
            secim=input("Seçiminiz: ")
            if secim=="1":
                karsilik={}
                count=0
                for i in gruplar:
                    count+=1
                    print(f"[{count}]  {i.isim}")
                    karsilik.setdefault(count,i.isim)


                secim=input("Seçiminiz: ")
                
                if secim in list(karsilik.keys()):
                    for i in gruplar:
                        if i.isim==karsilik[secim]:
                            kisiTaslak.append(i.isim)
                            i.kisiSayisi+=1
                            break 


            elif secim=="2":
                break

            else:
                print("Geçersiz Değer!!!")

                ts(3)        
        
        else:
            kisiTaslak=[]
            print("Grup Yok! !!!")
            break
            ts(3)

    dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(isim),"w")
    for i in kisiTaslak:
       dosya.write(i+"\n")

    dosya.close()

    db=sqlite3.connect(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\rehber.sqlite")
    imlec=db.cursor()
    imlec.execute("INSERT INTO 'Rehber' VALUES (?,?,?,?,?)",isim,soyisim,telNo,isi,kisiTaslak)
    db.commit()
    db.close()
    
    
    

def kisiCikar():
    global kisiler,gruplar
    #veri tabanından çıkarma işlemi için neytten arştır nsıl çıkarılıypomuş veri sqlite dan diye"
    while True:
        os.system("cls")
        karsilik={}
        for i in enumerate(kisiler):
            print(f"[{i[0]}]  {i[1].isim}")
            karsilik.setdefault(i[0],i[1])


        secim=input("\nSeçiminiz: ")
        
        if secim in list(karsilik.keys()):
            for i in kisiler:
                if i.isim==karsilik[secim]:
                    kisiler.remove(i)
                    for ii in gruplar:
                        if ii.isim in karsilik[secim].gruplar:
                            ii.kisiSayisi-=1

                    
                    
                    for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                        if i.isim.lower()+".txt"==dosya.lower():
                            os.remove(dosya)
                            break


                    imlec.execute(f"DELETE FROM 'Rehber' WHERE isim={i.isim}")
                    break

            break


        else:
            print("Geçersiz Değer!!!")
            ts(3)





def grupDuzenle():
    global kisiler,gruplar
    count=0
    while True:
        if count==0:
            karsilik={}
        os.system("cls")
        
        for i in enumerate(gruplar):
            
            print(f"[{i[0]}] {i[1].isim}")
            if count==0:
                karsilik.setdefault(i[0],i[1].isim)
        count=1

        secim=input("Hangisi: ")
        
        if secim in list(karsilik.keys()):
            for i in gruplar:
                if i.isim.lower()==karsilik[secim].lower():
                    
                    while True:
                        os.system("cls")
                        print("""
                            [1] Grup İsmini Değiştir
                            [2] Kişi Ekle
                            [3] Kişi Çıkar
                            [Q] Tamamlandı
                        """)
                        secim=input("İşleminiz: ")
                        
                        
                        gecerli=i.isim
                        if secim=="1":
                            gecerli=i.isim
                            while True:
                                os.system("cls")
                                yeniAd=input("Yeni Grup Adı:  ")
                                
                                if yeniAd:
                                    for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                                        if dosya[-4:]==".txt":
                                            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya))
                                            a=dosya1.readlines()
                                            for i in a:
                                                del i[-2:]
                                                if i.lower()==gecerli.lower():
                                                    a[a.index(i)]=yeniAd

                                            dosya1.close()
                                            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"w")
                                            for i in a:
                                                dosya1.write(i+"\n")
                                            
                                    break               
                                    

                                else:
                                    print("Geçeriz Değer")
                                    ts(3)


                        elif secim=="2":
                            grubaKisiEkle(gecerli)
                           


                        
                        elif secim=="3":
                            #kişi çıkarma işlemi
                            while True:
                                os.system("cls")
                                for i in kisiler:
                                    count=0
                                    if i.grup==karsilik[secim]:
                                        count+=1
                                        print(i.isim)
                                        karsilik.setdefault(count,i.isim)
                                
                                secim1=input("Hangisini Sileceksiniz? ")
                                
                                if secim1 in list(karsilik.keys()):
                                    for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                                        if "txt" in dosya:
                                            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya))
                                            a=dosya1.read()
                                            a=a.split("\n")
                                            a.pop()
                                            for i in a:
                                                if i.lower()==karsilik[secim].lower():
                                                    del a[a.index(i)]
                                                    break

                                            dosya1.close()
                                            break
                                
                                    break
                                
                                else:
                                    print("Yanlış Seçim!!")
                                    ts(3) 


                        elif secim.lower()=="q":
                            break

                        else:
                            print("Geçersiz Değer!!!")
                            ts(3)


        else:
            print("\nGeçersiz Değer!!")
            ts(3)

    



def kisiDuzenle():
    global kisiler,gruplar
    while True:
        os.system("cls")
        count=0
        karsilik1={}
        for i in kisiler:
            count+=1
            print(i.isim)
            karsilik1.setdefault(count,i)
        
        secim1=input("Hangisi: ")
        
        if secim1 in list(karsilik1.keys()):
            kisi=karsilik1[secim1]
            for i in kisiler:
                if i.isim==kisi.isim:
                    while True:
                        os.system("cls")
                        print("""
                        [1] İsim
                        [2] Soyisim
                        [3] Telefon Numarası
                        [4] Meslek
                        [5] Gruplar
                        [Q] Tamamlandı
                        """)
                        secim=input("Hangisi: ")
                        
                        if secim1=="1":
                            while True:
                                os.system("cls")
                                print(f"Geçerli İsim: {kisi.isim}")
                                yeniAd=input("Yeni İsim: ")
                                eski=kisi.soyisim
                                if yeniAd:
                                    imlec.execute("UPDATE rehber SET isim=? WHERE soyisim=?",yeniAd,eski)
                                    break

                                else:
                                    print("Geçersiz Değer!!")
                                    ts(3)



                        elif secim1=="2":
                            while True:
                                os.system("cls")
                                print(f"Geçerli Soysim: {kisi.soyisim}")
                                yeniAd=input("Yeni Soyisim: ")
                                eski=kisi.isim
                                if yeniAd:
                                    imlec.execute("UPDATE rehber SET soyisim=? WHERE isim=?",yeniAd,eski)
                                    break

                                else:
                                    print("Geçersiz Değer!!")
                                    ts(3)

                        elif secim1=="3":
                            while True:
                                os.system("cls")
                                print(f"Geçerli Numara: {kisi.telNo}")
                                yeniAd=input("Yeni Numara: ")
                                eski=kisi.soyisim
                                if yeniAd.isdigit():
                                    imlec.execute("UPDATE rehber SET telNo=? WHERE soyisim=?",yeniAd,eski)
                                    break

                                else:
                                    print("Geçersiz Değer!!")
                                    ts(3)

                        elif secim1=="4":
                            while True:
                                os.system("cls")
                                print(f"Geçerli Mesleği: {kisi.isi}")
                                yeniAd=input("Yeni Mesleği: ")
                                eski=kisi.soyisim
                                if yeniAd:
                                    imlec.execute("UPDATE rehber SET isi=? WHERE soyisim=?",yeniAd,eski)
                                    break

                                else:
                                    print("Geçersiz Değer!!")
                                    ts(3)


                        elif secim1=="5":
                           
                            #grup düzenleme işlemi
                            while True:
                                os.system("cls")
                                print("""
                                [1] Gruba Ekle
                                [2] Gruptan Çıkar
                                [Q] Tamamlandı
                                """)
                                secim=input("\nSeçiminiz: \n")


                                if secim=="1":
                                    if gruplar:
                                        while True:
                                            os.system("cls")
                                            karsilik={}
                                            for i in enumerate(gruplar):
                                                if i not in karsilik1[secim1].grup:
                                                    print(f"[{i[0]}] {i[1].isim}")
                                                    karsilik.setdefault(i[0],i[1].isim)

                                            secim=input("Hangisinme ekleyecekesiniz?")
                                            
                                            if secim in list(karsilik.keys()):
                                                for i in kisiler:
                                                    if i.isim.lower()==karsilik1[secim1].isim.lower():
                                                        for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                                                            if dosya.lower()==i.isim.lower()+".txt":
                                                                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"a+")
                                                                dosya1.write(f"\n{i.isim}")
                                                                dosya1.close()
                                                                break

                                                        break

                                                break

                                            else:
                                                print("Geçersiz Değer!!")
                                                ts(3)
                                    else:
                                        print("eklenecek Grup Yok Dolayısıyla Hiç Bir iŞlem yapamazsınız!! ÇıkılıyoR!!!")
                                        ts(4)
                                        break

                                elif secim=="2":
                                    if gruplar:
                                        while True:
                                            os.system("cls")
                                            karsilik={}
                                            for i in enumerate(gruplar):
                                                if i not in karsilik[secim1].grup:
                                                    print(f"[{i[0]}] {i[1].isim}")
                                                    karsilik.setdefault(i[0],i[1].isim)

                                            secim=input("Hangisini Çıkaracaksınız?")
                                            
                                            if secim in list(karsilik.keys()):
                                                for i in kisiler:
                                                    if i.isim.lower()==karsilik1[secim1].isim.lower():
                                                        for dosya in os.listdir(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi"):
                                                            if dosya.lower()==i.isim.lower()+".txt":
                                                                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"a+")
                                                                a=dosya1.read()
                                                                a=a.split("\n")
                                                                a.pop()
                                                                for ii in a:
                                                                    if ii.lower()==karsilik[secim].lower():
                                                                        a.remove(ii)
                                                                        break


                                                                dosya1.close()
                                                                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Telefon Rehberi\{}".format(dosya),"w")
                                                                for ii in a:
                                                                    dosya.write(a+"\n")
                                                                dosya1.close()

                                                                break

                                                        break

                                                break

                                            else:
                                                print("Geçersiz Değer!!")
                                                ts(3)
                                    else:
                                        print("eklenecek Grup Yok Dolayısıyla Hiç Bir iŞlem yapamazsınız!! ÇıkılıyoR!!!")
                                        ts(4)
                                        break

                                else:
                                    break

                        elif secim.lower()=="q":
                            break


        else:
            print("Geçersiz!!!!!")
            ts(3)
        
    

def kisiGoruntule():
    global kisiler,gruplar
    while True:
        os.system("cls")
        karsilik={}
        count=0
        for i in kisiler:
            count+=1
            print(f"{count} {i.isim}")
            karsilik.setdefault(count,i)
        secim=input("\nSeçiminiz: \n")
        
        if secim in list(karsilik.keys()):
            a=karsilik[secim]
            print(f"Kişinin İsmi: {a.isim}")
            print(f"Kişinin Soyismi: {a.soyisim}")
            print(f"Kişinin Numarası: {a.telNo}")
            print(f"Kişinin Mesleği: {a.isi}")
            for i in a.grup:
                print(i)

            input("Çıkmak için enter a baısn")
            break

        else:
            print("Geçersiz Değer!!!")
            ts(3)


def grupGoruntule():
    global kisiler,gruplar
    while True:
        os.system("cls")
        karsilik={}
        count=0
        for i in gruplar:
            count+=1
            print(f"{count} {i.isim}")
            karsilik.setdefault(count,i)
        secim=input("\nSeçiminiz: \n")
        
        if secim in list(karsilik.keys()):
            a=karsilik[secim]
            print(f"Grubun İsmi: {a.isim}")
            print(f"Gruptaki Kişi Sayısı: {a.kisiSayisi}")
            
            print("Gruptaki Kişiler: ")
            for i in kisiler:
                if a in i.grup:
                    print(i)

            input("Çıkmak için enter a baısn")
            break 

        else:
            print("Geçersiz Değer!!!")
            ts(3)
    

def main():
    global kisiler,gruplar
    baslangic()
    # kisiler=[]
    # gruplar=[]
    
    while True:
        baslangic()
        os.system("cls")
        print("""
        [0] Bilgi
        [1] Rehberi Görüntüle
        [2] Grupları Görüntüle
        [3] Grupları Düzenle
        [4] Kişi Ekle
        [5] Kişi Çıkar
        [6] Kişi Bilgileri Görüntüle
        [7] Grup Bilgileri Görüntüle
        [8] Kişi Düzenle
        [9] Grup Düzenle
        [H] Yardım
        [Q] Çıkış
        """)
        secim=input("\nSeçiminiz: \n")
        
        if secim=="0":
            
            print("Rehberiniz VÇöp:bu")
            input("ana menüye dönmek için enter a basın!!!")


        elif secim=="1":
            for a in kisiler:
                os.system("cls")
                print(f"Kişinin İsmi: {a.isim}")
                print(f"Kişinin Soyismi: {a.soyisim}")
                print(f"Kişinin Numarası: {a.telNo}")
                print(f"Kişinin Mesleği: {a.isi}")
                for i in a.grup:
                    print(i)

                input("sıradakını görmek için enter a basın!!")

            input("ana menüye dönmek için enter a basın!!!")
            
        elif secim=="2":
            for i in gruplar:
                os.system("cls")
                print(f"Grubun İsmi: {a.isim}")
                print(f"Gruptaki Kişi Sayısı: {a.kisiSayisi}")
                
                print("Gruptaki Kişiler: ")
                for i in kisiler:
                    if a in i.grup:
                        print(i)

                input("sıradakını görmek için enter a basın!!")

            input("ana menüye dönmek için enter a basın!!!")
            

        elif secim=="3":
            grupDuzenle()
            input("ana menüye dönmek için enter a basın!!!")

        elif secim=="4":
            kisiEkle()
            input("ana menüye dönmek için enter a basın!!!")
        elif secim=="5":
            kisiCikar()
            input("ana menüye dönmek için enter a basın!!!")
           

        elif secim=="6":
            kisiGoruntule()
            input("ana menüye dönmek için enter a basın!!!")
        elif secim=="7":
            grupGoruntule()
            input("ana menüye dönmek için enter a basın!!!")
        elif secim=="8":
            kisiDuzenle()
            input("ana menüye dönmek için enter a basın!!!")

        elif secim=="9":
            grupDuzenle()
            input("ana menüye dönmek için enter a basın!!!")
        elif secim.lower()=="h":
            print("""
            rehber işte arayüz marayüz yok ve evet 12.07.2020
            """)
            input("ana menüye dönmek için enter a basın!!!")
        elif secim.lower()=="q":
            break

        else:
            print("\nGeçersiz Değer\n")
            ts(3)







if __name__=="__main__":
        main()













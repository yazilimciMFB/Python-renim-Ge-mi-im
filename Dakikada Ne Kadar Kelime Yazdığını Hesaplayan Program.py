import sqlite3
import os

import time


db =sqlite3.connect("Kelime Yazma.db")
imlec=db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'Skorlar'  (isim,tarih,kelime,dakika)")

while True:
    os.system("cls")
    print("""
    [1] Eski Skorlari Goster
    [2] Yeni Test
    [Q] Cikis
    
    """)

    secim=input("Seciminiz: ")

    if secim=="1":
        imlec.execute("SELECT * FROM 'Skorlar' ")
        skorlar=imlec.fetchall()
        for i in skorlar:
            print(f"Isim: {i[0]}")
            print(f"Tarih: {i[1]}")
            print(f"Kelime Sayisi: {i[2]}")
            print(f"Dakika: {i[3]}\n")

        input("\nAna menuye donmek icin 'enter'a basin!!!")
            
        


    elif secim=="2":


        while True:
            os.system("cls")
            isim=input("Rekorun Adi: ")
            if isim:
                break

            
        yazilanlar=[]
        baslangic=time.time()

        print("Her kelime yazdığınızda 'enter'a basın!!!")
        print("Başlayın!!!")
        for i in range(1,4,-1):
            os.system("cls")
            print(i)
        while True:
            os.system("cls")
            
            if time.time()-baslangic>60:
                print(f" Kelime Sayisi: {len(yazilanlar)}")
                break
                

            else:
                a=input()
                yazilanlar.append(a)


        imlec.execute("INSERT INTO 'Skorlar' VALUES (?,?,?,?)",((isim),(time.time()),(len(yazilanlar)),(1)))
        db.commit()

        



    elif secim.lower()=="q":
        db.close()
        break

    else:
        print("Gecersiz Secim!!")
        time.sleep(3)


import math
print("Hesap Makinesi Pro'ya Hoşgeldiniz.")
print(20*"=")
print("""
[0]  Bilgi
[1]  Toplama
[2]  Çıkarma
[3]  Çarpma
[4]  Bölme
[5]  Kuvvet Alma
[6]  Karekök Alma
[7]  Kalan Bulma(Mod Alma)
[8]  Taban Bölme
[9]  Mutlak Değer
[10] Faktöriyel Alma
[11] Teklik, Çiftlik Belirleme
[12] İşaret Değiştirme (Toplama İşlemine Göre Tersini Alma)
[13] Çarpma İşlemine Göre Tersini Alma
[14] Büyük, Küçük, Eşitlik Durumları Bulma
[15] Pi
[16] Radyan'dan Dereceye Çevirme
[17] Dereceden Radyana Çevirme
[18] Çemberin Çevresi
[19] Dairenin Alanı
[20] Basit Trigonometrik Fonksiyonlar
[H]  Yardım
[Q]  Çıkış

    """)
print(20*"=")
print("")
print("")

print("")
islem=input("İşleminizi Seçiniz(Lütfen Sadece Yukarda Belirtilen İşlevlerden Birini Seçin): ")
print("")
if bool(islem):

    if islem=="0" :
        print("Hesap Makinesi Pro V0.1")
        quit()

    elif islem=="1":
        x=(input("İlk Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("İkinci Sayı(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"+")
        print("")
        print("İşleminizin Sonucu= ",x+y )
        print("")
        print(30*"+")
        print("")
        quit()

    elif islem=="2":
        x=(input("İlk Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("İkinci Sayı(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"-")
        print("")
        print("İşleminizin Sonucu= ",x-y )
        print("")
        print(30*"-")
        print("")
        quit()    

    elif islem=="3":
        x=(input("İlk Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("İkinci Sayı(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"*")
        print("")
        print("İşleminizin Sonucu= ",x*y )
        print("")
        print(30*"*")
        print("")
        quit()

    elif islem=="4":
        x=(input("Bölünen(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("Bölen(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"/")
        print("")
        print("İşleminizin Sonucu= ",x/y)
        print("")
        print(30*"/")
        print("")
        quit()

    elif islem=="5":
        x=(input("Taban(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("Üs(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"^")
        print("")
        print("İşleminizin Sonucu= ",x**y )
        print("")
        print(30*"^")
        print("")
        quit()


    elif islem=="6":
        x=(input("Karekökü Alınacak Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
      
        import math
        print("")
        print(30*"2")
        print("")
        print("İşleminizin Sonucu= ",math.sqrt(x) )
        print("")
        print(30*"2")
        print("")
        quit()


    elif islem=="7":
        x=(input("Bölünen(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("Bölen(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"%")
        print("")
        print("İşleminizin Sonucu= ",x%y )
        print("")
        print(30*"%")
        print("")
        quit()

    elif islem=="8":
        x=(input("Bölünen(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("Bölen(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        print("")
        print(30*"//")
        print("")
        print("İşleminizin Sonucu= ",x//y)
        print("")
        print("Kalan= ",x%y )
        print("")
        print(30*"//")
        print("")
        quit()

    elif islem=="9":
        x=(input("Mutlak Değeri Alınacak Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        

        print("")
        print(30*"|")
        print("")
        print("İşleminizin Sonucu= ",abs(x) )
        print("")
        print(30*"|")
        print("")
        quit()

    elif islem=="10":
        x=(input("Faktöriyeli Alınacak Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)

        import math
        print("")
        print(30*"!")
        print("")
        print("İşleminizin Sonucu= ",math.factorial(x) )
        print("")
        print(30*"!")
        print("")
        quit()

    elif islem=="11":
        print("Teklik Çiftlik İşlemlerinde 1 olumlu, 0 olumsuz cevaptır.")
        print("")
        x=(input("Teklik veya Çiftlik Durumu Bulunacak Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        if x%2==0:
            print("")
            print(30*"21")
            print("")
            print("Çiftlik Durumu= 1")
            print("Teklik Durumu= 0")
            print("")
            print(30*"12")
            print("")
            quit()
        else :
            print("")
            print(30*"21")
            print("")
            print("Çiftlik Durumu= 0")
            print("Teklik Durumu= 1")
            print("")
            print(30*"12")
            print("")
            quit()    

    elif islem=="12":
        x=(input("İşaretini Değiştireceğiniz Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
       
        print("")
        print(30*"+-")
        print("")
        print("İşleminizin Sonucu= ",-x )
        print("")
        print(30*"-+")
        print("")
        quit()

    elif islem=="13":
        x=(input("Çarpma İşlemine Göre Tersi Alınacak Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        
        print("")
        print(30*"!*")
        print("")
        print("İşleminizin Sonucu= ",1/x )
        print("")
        print(30*"*!")
        print("")
        quit()

    elif islem=="14":
        x=(input("İlk Sayı(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
        y=input("İkinci Sayı(Lütfen sadece rakamsal değer giriniz.): ")
        y=float(y)

        if x>y:
            print("")
            print(30*"<=>")
            print("")
            print("İşleminizin Sonucu= " ,x,">",y )
            print("")
            print(30*"<=>")
            print("")
            quit()
        
        elif x<y:
            print("")
            print(30*"<=>")
            print("")
            print("İşleminizin Sonucu= ",x,"<",y )
            print("")
            print(30*"<=>")
            print("")
            quit()    
        
        elif x==y:
            print("")
            print(30*"<=>")
            print("")
            print("İşleminizin Sonucu= ", x,"=",y )
            print("")
            print(30*"<=>")
            print("")
            quit()

    elif islem=="15":
        import math
        print("")
        print(30*"π")
        print("")
        print("π= ",math.pi )
        print("")
        print(30*"π")
        print("")
        quit()

    elif islem=="16":
        import math
        x=float(input("Derece Cinsine Çevrilecek Radyan Değeri:"))
        
        print("")
        print(30*"°")
        print("")
        print("İşleminizin Sonucu:",math.degrees(x))
        print("")
        print(30*"°")
        print("")
        quit()

    elif islem=="17":
        import math
        x=float(input("Radyan Cinsine Çevrilecek Derecesel Değer:"))
        
        print("")
        print(15*"180°/π.")
        print("")
        print("İşleminizin Sonucu:",math.radians(x))
        print("")
        print(15*"180°/π.")
        print("")
        quit()

    elif islem=="18":
        x=(input("Yarıçap(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
       
        import math
        print("")
        print(30*"o")
        print("")
        print("Çemberinizin Çevresi= ",2*x*math.pi )
        print("")
        print(30*"o")
        print("")
        quit()

    elif islem=="19":
        x=(input("Yarıçap(Lütfen sadece rakamsal değer giriniz.): "))
        x=float(x)
       
        import math
        print("")
        print(30*"AoA")
        print("")
        print("Dairenizin Alanı= ",math.pi*x**2 )
        print("")
        print(30*"AoA")
        print("")
        quit()

    elif islem=="20":
        print("")
        print(30*"T")
        print("""
        [1]  Sinüs(Sin)
        [2]  Kosinüs(Cos)
        [3]  Tanjant(Tan)
        [4]  Kotanjant(Cot)
        [5]  Sekant(Sec)
        [6]  Kosekant(Csc)
        [7]  Arcsinüs
        [8]  Arckosinüs
        [9]  Arctanjant
        [10] Arckotanjant
        [11] Arcsekant
        [12] Arckosekant
        [H]  Yardım
        [Q] Çıkış
                """)
        print(30*"T")



        
        print("")
        trig=input("Hangi Trigonometrik Fonksiyonu Kullanmak İstiyorsunuz(Lütfen Sadece Yukarda Belirtilen İşlevlerden Birini Seçin): ")
        print("")

        if bool(trig):
            if trig=="1":
                import math
                x=float(input("Sinüsünü Alacağınız Açı Değeri:"))
                x=math.radians(x)
            


                import math
                print("")
                print(30*"SİN")
                print("")
                print("Açının Sinüsü:" , math.sin(x))
                print("")
                print(30*"SİN")
                print("")
                quit()

            elif trig=="2":
                import math
                x=float(input("Kosinüsünü Alacağınız Açı Değeri:"))
                x=math.radians(x)
                


                import math
                print("")
                print(30*"COS")
                print("")
                print("Açının Kosinüsü:" , math.cos(x))
                print("")
                print(30*"COS")
                print("")
                quit()

            elif trig=="3":
                import math
                x=float(input("Tanjantını Alacağınız Açı Değeri:"))
                x=math.radians(x)
                


                import math
                print("")
                print(30*"TAN")
                print("")
                print("Açının Tanjantı:" ,math.tan(x))
                print("")
                print(30*"TAN")
                print("")
                quit()

            elif trig=="4":
                import math
                x=float(input("Kotanjantını Alacağınız Açı Değeri:"))
                x=math.radians(x)
                


                import math
                print("")
                print(30*"COT")
                print("")
                print("Açının Kotanjantı:" ,1/math.tan(x))
                print("")
                print(30*"COT")
                print("")
                quit()


            elif trig=="5":
                import math
                x=float(input("Sekantını Alacağınız Açı Değeri:"))
                x=math.radians(x)
                


                import math
                print("")
                print(30*"SEC")
                print("")
                print("Açının Sekantı:" ,1/math.cos(x))
                print("")
                print(30*"SEC")
                print("")
                quit()

            elif trig=="6":
                import math
                x=float(input("Kosekantını Alacağınız Açı Değeri:"))
                x=math.radians(x)
                


                import math
                print("")
                print(30*"KOS")
                print("")
                print("Açının Kosekantı:" ,1/math.sin(x))
                print("")
                print(30*"KOS")
                print("")
                quit()


            elif trig=="7":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Sinüsü :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ARS")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.asin(x))
                print("")
                print(30*"ARS")
                print("")
                quit()


            elif trig=="8":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Kosinüsü :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ARC")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.acos(x))
                print("")
                print(30*"ARC")
                print("")
                quit()


            elif trig=="9":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Tanjantı :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ART")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.atan(x))
                print("")
                print(30*"ART")
                print("")
                quit()


            elif trig=="10":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Kotanjantı :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ARCO")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.atan(1/x))
                print("")
                print(30*"ARCO")
                print("")
                quit()

            elif trig=="11":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Sekantı :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ARSC")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.acos(1/x))
                print("")
                print(30*"ARSC")
                print("")
                quit()

            elif trig=="12":
                import time
                time.sleep(1)
                print("""
                    !!!!!!!Değeriniz "-1 <= X >=1" aralığında olmalı, aksi takdirde hata alırsınız.!!!!!!!!!
                    """)
                x=float(input("Bulacağınız Açının Kosekantı :"))
                import time
                time.sleep(1)
                import math
                print("")
                print(30*"ARCSC")
                print("")
                print("Açınız(Radyan Cinsinden):" ,math.asin(1/x))
                print("")
                print(30*"ARCSC")
                print("")
                quit()

            elif trig=="H" or trig=="h":
                print("")
                print(30*"HhH")
                print("")
                print("""
                    Bu bölümde yukarıda çıkan
                    işlevlere göre herhangi bir
                    rakama sonra da enter tuşuna
                    basmalısınız. Enter'a bastığınızda 
                    hangi sayıyı seçmişseniz 
                    onun karşısında yazılan işleme göre 
                    değer veya değerler istenir  ve ona 
                    göre işlem yapılır. Geçersiz bir 
                    değer girmeniz halinde hata 
                    alırsınız ve çıkarsınız. Düzgün bir şekilde 
                    işlemlerden herhangi birisini yapsanız 
                    sonucunda yine çıkarsınız.(Tabi işlem 
                    sonucunu da görürsünüz...) Eğer yukarıdaki 
                    işlemlerin ne anlama geldiklerini
                    bilmiyorsunuz lütfen trigonometri
                    nedir araştırın... Şimdi Çıkılıyor....
                    """)
                print("")
                print(30*"HhH")
                print("")

                quit()

            elif trig=="q" or trig=="Q":
                print("")
                print(30*"QqQ")
                print("")
                print("Çıkılıyor, lütfen bekleyiniz...")
                print("")
                print(30*"qQq")
                print("")

                import time
                time.sleep(2)
                quit()
 


        else:
            print("Geçersiz Bir Değer Girdiniz!")
            quit()


    elif islem=="H" or islem=="h":
                print("")
                print(30*"HhH")
                print("")
                print("""
                    Bu bölümde yukarıda çıkan
                    işlevlere göre herhangi bir
                    rakama sonra da enter tuşuna
                    basmalısınız. Enter'a bastığınızda 
                    hangi sayıyı seçmişseniz 
                    onun karşısında yazılan işleme göre 
                    değer veya değerler istenir  ve ona 
                    göre işlem yapılır. Geçersiz bir 
                    değer girmeniz halinde hata 
                    alırsınız ve çıkarsınız. Düzgün bir şekilde 
                    işlemlerden herhangi birisini yapsanız 
                    sonucunda yine çıkarsınız.(Tabi işlem 
                    sonucunu da görürsünüz...) Eğer yukarıdaki 
                    işlemlerin ne anlama geldiklerini
                    bilmiyorsunuz lütfen matematik
                    nedir araştırın... Şimdi Çıkılıyor....
                    """)
                print("")
                print(30*"HhH")
                print("")

                quit()



    elif islem=="q" or islem=="Q":

        print("")
        print(30*"QqQ")
        print("")
        print("Çıkılıyor, lütfen bekleyiniz...")
        print("")
        print(30*"qQq")
        print("")

        import time
        time.sleep(2)
        quit()


else:
    print("Geçersiz Bir Değer Girdiniz!")
    quit()

   


    
        
    

    

    
   

    

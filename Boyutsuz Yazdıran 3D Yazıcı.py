s=0
if s==0:
    while s==0:   
        import os 
        try:
        
            print("\n"*20)
            import time
            time.sleep(1)
            print()
            print("Boyutsuz Şekiler bastıran 3D yazıcısızlık sihirbazına hoşgeldiniz!!!\n")
            import time
            time.sleep(0.89)
            print()
            print("\\"*40)
            acilis="""
            [0]  Bilgi
            [1]  Çember {0}                                               {2}
            [2]  Kare {0}                                                 {2}
            [3]  Dik, Çeşitkenar, Eşkenar,İkizkenar Üçgenler {0}          {2}
            [4]  Dikdörtgen{0}                                            {2}
            [5]  Doğru{0}                                                 {2}
            [6] {1} Beşgen{0}                                             {2}
            [7] {1} Altıgen{0}                                            {2}
            [8] {1} Yamuk{0}                                              {2}
            [9]  Paralel Kenar{0}                                         {2}
            [10]{1} Yedigen{0}                                            {2}
            [11]{1} Sekizgen{0}                                           {2}
            [H]  Yardım
            [Q]  Çıkış
                """.format(" (Çizimler Yeni Pencerede Açılır)", " (Düzgün)", "(Eğer cisimlerin boyutunu çok büyük seçerseniz tam gözükmeyebilir ve yanlış çizimler ortaya çıkabilir...)")

            print(acilis)
            print("/"*40)
            import time
            time.sleep(0.9)
            print()
            import time
            time.sleep(0.989898)
            ahhhhh=0
            secim=input("\nSeçiminiz??(Lütfen Sadece Yukardaki Seçenklerden Birini Seçiniz)")
            if ahhhhh==0:
                if  secim=="1" or secim=="2" or secim=="3" or secim=="4" or secim=="5" or secim=="6" or secim=="7" or secim=="8" or secim=="9" or secim=="10" or secim=="11" :
                    s1=0
                    while s1==0:
                        import time
                        time.sleep(0.9)
                        print()
                        secim1=input("Yıldızlarla mı yoksa çizerek mi yazdırmak istersiniz(Lütfen sadece çizim ya da yıldız olarak cevap veriniz)?")    
                        import time
                        time.sleep(0.9)
                        if  secim1=="çizim":
                            os.system("cls")
                            import turtle
                            ok = turtle.Turtle()
                            ok.clear()
                            

                            if secim=="1":
                                c = 0
                                while c == 0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    print("Daire Seçtiniz.")
                                    print()
                                    import time
                                    time.sleep(1)
                                    print()
                                    
                                    yariCap=input("Görmek İstediğiniz Çemberin Yarıçapı(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    try:
                                        int(yariCap)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue


                                    yariCap=int(yariCap)
                                    import time
                                    time.sleep(0.88)
                                    print()
                                    def daire(deger):
                                        ok.goto(0,-500)
                                        ok.clear()
                                        turtle.circle(deger)
                                        ok.penup()
                                                

                                    daire(yariCap)
                                    break
                                break
                            elif secim=="2":
                                k = 0
                                while k == 0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    print("Kare Seçtiniz.")
                                    print()
                                    import time
                                    time.sleep(0.9)
                                    print()
                                    kenar = input("Görmek İstediğiniz Karenin Bir Kenar Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    
                                    try:
                                        int(kenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kenar=int(kenar)
                                    def rastgele(boy):
                                            if boy<=500:
                                                for i in range(4):
                                                    ok.backward(boy)
                                                    ok.right(90)
                                                ok.penup()
                                            else:
                                                ok.goto(500,500)
                                                ok.clear()
                                                for i in range(4):
                                                    ok.backward(boy)
                                                    ok.left(90)
                                                ok.penup()


                                    rastgele(kenar)
                                    break
                                break

                            elif secim=="3":
                                u=0
                                while u==0:
                                    import time 
                                    time.sleep(0.98)
                                    print()
                                    print("Girdiğiniz değerler üçgen eşitsizliğine uymalıdır, aksi takdirde hata alırsınız!!!! ")
                                    print()
                                    kenar1=int(input("Üçgenin Birinci Kenarı: "))
                                    import time 
                                    time.sleep(0.98)
                                    print()
                                    kenar2=int(input("Üçgenin İkinci Kenarı: "))
                                    import time 
                                    time.sleep(0.98)
                                    print()
                                    kenar3=int(input("Üçgenin Üçüncü Kenarı: "))
                                    lklk=0
                                    ğ2=0
                                    ğ1=0
                                    uı=0
                                    try  :
                                        int(kenar1)
                                        int(kenar2)
                                        int(kenar3)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kenarr1=int(kenar1)
                                    kenar2=int(kenar2)
                                    kenar3=int(kenar3)

                                    if lklk==0:
                                        if abs(kenar1-kenar2)<kenar3<(kenar1+kenar2) and abs(kenar3-kenar2)<kenar1<(kenar3+kenar2) and abs(kenar1-kenar3)<kenar2<(kenar1+kenar3) :
                                            if ğ2==0 :
                                                if ğ1==0 :
                                                    if uı==0:
                                                        if kenar1==kenar2 and kenar2==kenar1:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("Eşkenar BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)
                                                        

                                                            def eskenarUcgen(kenar):
                                                                if kenar<=500:
                                                                    ok.left(60)
                                                                    ok.forward(kenar)
                                                                    ok.right(120)
                                                                    ok.forward(kenar)
                                                                    ok.right(120)
                                                                    ok.forward(kenar)
                                                                    ok.penup()
                                                                else:
                                                                    ok.penup()
                                                                    ok.goto(-1000,-500)
                                                                    ok.pendown()
                                                                    ok.left(60)
                                                                    ok.forward(kenar)
                                                                    ok.right(120)
                                                                    ok.forward(kenar)
                                                                    ok.right(120)
                                                                    ok.forward(kenar)
                                                                    ok.penup()

                                                            eskenarUcgen(kenar1)


                                                            break
                                                                
                                                        elif kenar1^2 +kenar2^2==kenar3^2:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("Dik BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)

                                                            def dikUcgen(kenar1,kenar2,hipotenus):
                                                                if hipotenus>=500:
                                                                    ok.penup()
                                                                    ok.goto(-500,-500)
                                                                    ok.pendown()
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)
                                                                    
                                                            

                                                                else:
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)

                                                            dikUcgen(kenar1,kenar2,kenar3)
                                                            break

                                                        elif kenar2^2 +kenar3^2==kenar1^2:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("Dik BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)

                                                            def dikUcgen(kenar1,kenar2,hipotenus):
                                                                if hipotenus>=500:
                                                                    ok.penup()
                                                                    ok.goto(-500,-500)
                                                                    ok.pendown()
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)
                                                                    
                                                            

                                                                else:
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)

                                                            dikUcgen(kenar3,kenar2,kenar1)
                                                            break

                                                        elif kenar1^2 +kenar3^2==kenar2^2:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("Dik BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)

                                                            def dikUcgen(kenar1,kenar2,hipotenus):
                                                                if hipotenus>=500:
                                                                    ok.penup()
                                                                    ok.goto(-500,-500)
                                                                    ok.pendown()
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)
                                                                    
                                                            

                                                                else:
                                                                    ok.forward(kenar1)
                                                                    ok.penup()
                                                                    ok.backward(kenar1)
                                                                    ok.pendown()
                                                                    ok.left(90)
                                                                    ok.forward(kenar2)
                                                                    ok.right(127)
                                                                    ok.forward(hipotenus)

                                                            dikUcgen(kenar1,kenar3,kenar2)
                                                            break



                                                        elif kenar1==kenar2 and kenar2!=kenar3:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("İkizkenar BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)
                                                            
                                                            


                                                            def ikizkenarUcgen(kenar1,kenar3):
                                                                import random
                                                                if kenar1<=500 and kenar3<=500:
                                                                    if kenar1<kenar3:
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar3)
                                                                        ok.penup()

                                                                    elif kenar1>kenar3:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar3)
                                                                        ok.penup()


                                                                    


                                                                elif kenar1>=500 or kenar3>=500:
                                                                    import random
                                                                    ok.penup()
                                                                    ok.goto(-1000,-500)
                                                                    ok.pendown()
                                                                    if kenar1<kenar3:
                                                                        
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar3)
                                                                        ok.penup()

                                                                    elif kenar1>kenar3:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar3)
                                                                        ok.penup()

                                                            ikizkenarUcgen(kenar1,kenar3)
                                                            break

                                                        elif kenar1==kenar3 and kenar2!=kenar1:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("İkizkenar BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            import turtle
                                                            ok = turtle.Turtle()
                                                            ok.speed(1)
                                                            ok.color("pink")
                                                            import time
                                                            time.sleep(0.9)
                                                            ok.pensize(10)
                                                            


                                                            def ikizkenarUcgen(kenar1,kenar2):
                                                                import random
                                                                if kenar1<=500 and kenar2<=500:
                                                                    if kenar1<kenar2:
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar2)
                                                                        ok.penup()

                                                                    elif kenar1>kenar2:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar2)
                                                                        ok.penup()


                                                                    


                                                                elif kenar1>=500 or kenar2>=500:
                                                                    import random
                                                                    ok.penup()
                                                                    ok.goto(-1000,-500)
                                                                    ok.pendown()
                                                                    if kenar1<kenar2:
                                                                        
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar2)
                                                                        ok.penup()

                                                                    elif kenar1>kenar2:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar1)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar2)
                                                                        ok.penup()

                                                            ikizkenarUcgen(kenar1,kenar2)
                                                            break

                                                        elif kenar2==kenar3 and kenar2!=kenar1:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("İkizkenar BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()
                                                            
                                                            import time
                                                            time.sleep(0.9)
                                                            
                                                            


                                                            def ikizkenarUcgen(kenar2,kenar1):
                                                                import random
                                                                if kenar2<=500 and kenar1<=500:
                                                                    if kenar2<kenar1:
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar1)
                                                                        ok.penup()

                                                                    elif kenar2>kenar1:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar1)
                                                                        ok.penup()


                                                                    


                                                                elif kenar2>=500 or kenar1>=500:
                                                                    import random
                                                                    ok.penup()
                                                                    ok.goto(-1000,-500)
                                                                    ok.pendown()
                                                                    if kenar2<kenar1:
                                                                        
                                                                        x=random.uniform(1,60)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar1)
                                                                        ok.penup()

                                                                    elif kenar2>kenar1:
                                                                        x=random.uniform(60,90)
                                                                        y=180-2*x
                                                                        ok.left(x)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-y)
                                                                        ok.forward(kenar2)
                                                                        ok.right(180-x)
                                                                        ok.forward(kenar1)
                                                                        ok.penup()

                                                            ikizkenarUcgen(kenar2,kenar1)
                                                            break


                                                        elif kenar1!=kenar2 and kenar2!=kenar3 and kenar1!=kenar3:
                                                            import time
                                                            time.sleep(1)
                                                            print()
                                                            print("Çeşitkenar BİR ÜÇGEN SEÇTİNİZ.")
                                                            print()

                                                            

                                                            if kenar1>kenar2 and kenar2>kenar3:
                                                                enBuyuk=kenar1
                                                                enKucuk=kenar3
                                                                orta=kenar2
                                                            elif kenar2>kenar3 and kenar3>kenar1:
                                                                enBuyuk=kenar2
                                                                enKucuk=kenar1
                                                                orta=kenar3
                                                            elif kenar3>kenar2 and kenar2>kenar1:
                                                                enBuyuk=kenar3
                                                                enKucuk=kenar1
                                                                orta=kenar2
                                                            elif kenar1>kenar3 and kenar3>kenar2:
                                                                enBuyuk=kenar1
                                                                enKucuk=kenar2
                                                                orta=kenar3
                                                            elif kenar2>kenar1 and kenar1>kenar3:
                                                                enBuyuk=kenar2
                                                                enKucuk=kenar3
                                                                orta=kenar1
                                                            elif kenar3>kenar1 and kenar1>kenar2:
                                                                enBuyuk=kenar3
                                                                enKucuk=kenar2
                                                                orta=kenar1

                                                            def cesitkenarUcgen(orta,buyuk,kucuk):
                                                                
                                                                    if buyuk >= 500:
                                                                        ok.penup()
                                                                        ok.goto(-1000, -500)
                                                                        ok.pendown()
                                                                        ok.left(50)
                                                                        ok.forward(buyuk)
                                                                        ok.right(150)
                                                                        ok.forward(orta)
                                                                        ok.right(80)
                                                                        ok.forward(kucuk)
                                                                        ok.penup()


                                                                    elif buyuk < 500:
                                                                        ok.pendown()
                                                                        ok.left(50)
                                                                        ok.forward(buyuk)
                                                                        ok.right(150)
                                                                        ok.forward(orta)
                                                                        ok.right(80)
                                                                        ok.forward(kucuk)
                                                                        ok.penup()

                                                            cesitkenarUcgen(orta,enBuyuk,enKucuk)
                                                            break


                                        else:
                                            import time
                                            time.sleep(0.9)
                                            print()
                                            print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                            continue
                                            
                                            
                                                
                                                
                                break

                            elif secim=="4":
                                d = 0
                                while d == 0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    print("Dikdörtgen Seçtiniz.")
                                    print()
                                    import time
                                    time.sleep(0.9)
                                    print()
                                    import time
                                    time.sleep(1)
                                    print()
                                    uzunKenar=input("Dikdörtgenin Uzun Kenarı(Lütfen sadece sayısal değerler giriniz)? ")
                                    try:
                                        int(uzunKenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                        
                                    uzunKenar=int(uzunKenar)
                                    import time
                                    time.sleep(1)
                                    print()
                                    kisaKenar=input("Dikdörtgenin Kısa Kenarı(Lütfen sadece sayısal değerler giriniz)? ")
                                    try:
                                        int(kisaKenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kisaKenar=int(kisaKenar)
                                    
                                    if kisaKenar==uzunKenar or uzunKenar<kisaKenar:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    

                                    secim1_0=input("Dikdörtgeniniz düşey mi olsun yatay mı(Lütfen sadece düşey veya yatay olarak cevap verin)?")
                                        
                                    if secim1_0=="Düşey" or secim1_0=="düşey":

                                        def dikdortgen(uzunKenar,kisaKenar):
                                            if uzunKenar>=500 or kisaKenar>=500:
                                                ok.goto(-1000,-500)
                                                ok.clear()
                                                
                                                ok.left(90)
                                                ok.forward(uzunKenar)
                                                ok.right(90)
                                                ok.forward(kisaKenar)
                                                ok.right(90)
                                                ok.forward(uzunKenar)
                                                ok.right(90)
                                                ok.forward(kisaKenar)
                                                ok.penup()

                                            elif uzunKenar<500 and kisaKenar<500:
                                                ok.left(90)
                                                ok.forward(uzunKenar)
                                                ok.right(90)
                                                ok.forward(kisaKenar)
                                                ok.right(90)
                                                ok.forward(uzunKenar)
                                                ok.right(90)
                                                ok.forward(kisaKenar)
                                                ok.penup()

                                        dikdortgen(uzunKenar,kisaKenar)
                                        break

                                    elif secim1_0=="Yatay" or secim1_0=="yatay":

                                        def dikdortgen(uzunKenar,kisaKenar):
                                            if uzunKenar>=500 or kisaKenar>=500:
                                                ok.goto(-1000,-500)
                                                ok.clear()
                                                ok.forward(uzunKenar)
                                                ok.left(90)
                                                ok.forward(kisaKenar)
                                                ok.left(90)
                                                ok.forward(uzunKenar)
                                                ok.left(90)
                                                ok.forward(kisaKenar)
                                                    
                                                ok.penup()

                                            elif uzunKenar<500 and kisaKenar<500:
                                                ok.forward(uzunKenar)
                                                ok.left(90)
                                                ok.forward(kisaKenar)
                                                ok.left(90)
                                                ok.forward(uzunKenar)
                                                ok.left(90)
                                                ok.forward(kisaKenar)
                                                ok.penup()

                                        dikdortgen(uzunKenar,kisaKenar)
                                        break


                                    else:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                break

                            elif secim=="5":
                                import time
                                time.sleep(1)
                                print()
                                print("Doğru Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                d1=0
                                while d1==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    dogru=input("Doğrunun görünen uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    try:
                                        int(dogru)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    dogru=int(dogru)


                                    def dogru(deger):
                                        import turtle
                                        ok=turtle.Turtle()
                                        ok.penup()
                                        ok.goto(-999,0)
                                        ok.pendown()
                                        ok.left(60)
                                        ok.forward(20)
                                        ok.penup()
                                        ok.backward(20)
                                        ok.pendown()
                                        ok.right(120)
                                        ok.forward(20)
                                        ok.penup()
                                        ok.backward(20)
                                        ok.pendown()
                                        ok.left(60)
                                        ok.forward(deger)
                                        ok.left(60)
                                        ok.forward(20)
                                        ok.penup()
                                        ok.backward(130)
                                        ok.pendown()
                                        ok.right(120)
                                        ok.forward(20)
                                        ok.penup()
                                        ok.backward(20)



                                    dogru(dogru)
                                    break
                                break
                            
                            elif secim=="6":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Beşgen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                b=0
                                while b==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    besgen=input("Beşgenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    try:
                                        int(besgen)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    besgen=int(besgen)

                                    def besgen(kenar):
                                        if kenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                            for i in range(5):
                                                ok.forward(deger)
                                                ok.right(72)
                                            ok.penup()

                                        elif kenar<500:
                                            for i in range(5):
                                                ok.forward(deger)
                                                ok.right(72)
                                            ok.penup()

                                    besgen(besgen)
                                    break
                                break

                            elif secim=="7":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Altıgen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                b=0
                                while b==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    altigen=input("Altıgenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    try:
                                        int(altigen)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    altigen=int(altigen)

                                    def altigen(kenar):
                                        if kenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                            for i in range(6):
                                                ok.forward(100)
                                                ok.right(60)
                                            ok.penup()

                                        elif kenar<500:
                                            for i in range(6):
                                                ok.forward(100)
                                                ok.right(60)
                                            ok.penup()

                                    altigen(altigen)
                                    break
                                break

                            elif secim=="8":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Yamuk Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                y=0
                                while y==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    altTaban=input("Yamuğun alt tabanı uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    ustTaban=input("Yamuğun üst taban uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    solKenar=input("Yamuğun sol kenarı uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    sagKenar=input("Yamuğun sağ kenarı uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    try:
                                        int(altTaban)
                                        int(ustTaban)
                                        int(sagKenar)
                                        int(solKenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    altTaban=int(altTaban)
                                    ustTaban=int(ustTaban)
                                    sagKenar=int(sagKenar)
                                    solKenar=int(solKenar)

                                    def yamuk(altTaban,ustTaban,sagKenar,solKenar):
                                        if sagKenar>=500 or solKenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                            ok.forward(altTaban)
                                            ok.left(110)
                                            ok.forward(sagKenar)
                                            ok.left(70)
                                            ok.forward(ustTaban)
                                            ok.left(70)
                                            ok.forward(solKenar)

                                            
                                            ok.penup()

                                        else:
                                            ok.forward(altTaban)
                                            ok.left(110)
                                            ok.forward(sagKenar)
                                            ok.left(70)
                                            ok.forward(ustTaban)
                                            ok.left(70)
                                            ok.forward(solKenar)
                                        
                                            ok.penup()

                                    yamuk(altTaban,ustTaban,sagKenar,solKenar)
                                    break
                                break
                            
                            elif secim=="9":
                                import time
                                time.sleep(1)
                                print()
                                print("Paralelkenar Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    tabanTavan=input("Paralelkenarın taban,tavan uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    ke2nar=input("Paralelkenarın diğer 2 kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                
                                    try:
                                        int(ke2nar)
                                        int(tabanTavan)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    ke2nar=int(ke2nar)
                                    tabanTavan=int(tabanTavan)
                                    

                                    def paralelKenar(ke2nar,tabanTavan):
                                        if sagKenar>=500 or solKenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                            ok.forward(tabanTavan)
                                            ok.left(110)
                                            ok.forward(ke2nar)
                                            ok.left(70)
                                            ok.forward(tabanTavan)
                                            ok.left(70)
                                            ok.forward(ke2nar)

                                            
                                            ok.penup()

                                        else:
                                            ok.forward(tabanTavan)
                                            ok.left(110)
                                            ok.forward(ke2nar)
                                            ok.left(70)
                                            ok.forward(tabanTavan)
                                            ok.left(70)
                                            ok.forward(ke2nar)
                                        
                                        
                                            ok.penup()

                                    paralelKenar(ke2nar,tabanTavan)
                                    break
                                break

                            elif secim=="10":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Yedigen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    kenar=input("Düzgün yedigenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    
                                    try:
                                        int(kenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    kenar=int(kenar)
                                    

                                    def yedigen(kenar):
                                        if kenar>=500 or kenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                        
                                            for i in range(7):
                                                ok.forward(kenar)
                                                ok.left(52)

                                            
                                            ok.penup()

                                        else:
                                            for i in range(7):
                                                ok.forward(kenar)
                                                ok.left(52)
                                        
                                        
                                            ok.penup()

                                    yedigen(kenar)
                                    break
                                break

                            elif secim=="11":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Sekizgen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    kenar=input("Düzgün Sekizgenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    
                                    try:
                                        int(kenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    kenar=int(kenar)
                                    

                                    def sekizgen(kenar):
                                        if kenar>=500 or kenar>=500:
                                            ok.penup()
                                            ok.goto(-1000,-1000)
                                            ok.pendown()
                                        
                                            for i in range(7):
                                                ok.forward(kenar)
                                                ok.left(45)

                                            
                                            ok.penup()

                                        else:
                                            for i in range(7):
                                                ok.forward(kenar)
                                                ok.left(45)
                                        
                                        
                                            ok.penup()

                                    sekizgen(kenar)
                                    break
                                break

                
                                

                        elif  secim1=="yıldız": 
                            os.system("cls")

                            if secim=="1":
                                time.sleep(1)
                                print()
                                print("Cidden köşelerle daire m çizmek istiyorsunuz?!?!?!")
                                break

                            elif secim=="2":
                                k=0
                                while k==0:
                                    time.sleep(0.7)
                                    print()
                                    
                                    print()
                                    kenar = input("Görmek İstediğiniz Karenin Bir Kenar Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                        
                                    try:
                                        int(kenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kenar=int(kenar)
                                    

                                    if kenar%2==0:
                                        a=0
                                        for i in range(kenar):
                                            
                                            print(kenar*"*")
                                            time.sleep(a)
                                            a+=0.01

                                        break

                                    

                                    else:
                                        a=0
                                        for i in range(kenar):
                                            
                                            print(kenar*"*")
                                            time.sleep(a)
                                            a+=0.01

                                        break

                                        

                                break

                                
                                
                                
                            
                            elif secim=="3":
                                os.system("cls")
                                time.sleep(0.6)
                                print()
                                print("""
                                    Not: Yıldız ile bastırılan üçgenlerde sadece 
                                    eşkenar ve dik üçgenler bastırılabilir. 
                                    tam sürüm için çizim i seçin...
                                            
                                    """)
                                            
                                print()
                                acilis1="""

                                [1] Eşkenar Üçgen
                                [2] İkizkenar Dik Üçgen

                                !!!!!!!!!!!Seçiminizi yaptıktan sonra 
                                gireceğiniz değerler üçgen eşitsizliğine 
                                ve eğer dik üçgen seçmişseniz 
                                pisagor teoremine uymalıdır!!!!!!!!!!!!!

                                        """
                                print(acilis1)    
                                print()
                                time.sleep(0.4)
                                s2=0
                                while s2==0:
                                    os.system("cls")
                                    secim2=input("Lütfen yukardakilerden birini seçiniz!!!!")
                                    
                                    if secim2=="1":
                                        eu=0
                                        while eu==0:
                                            time.sleep(0.9)
                                            print()
                                            print("Bir kenar uzunluğu üçgenin çift olmalıdır...")
                                            print()
                                            kenar=input("Eşkenar üçgenin bir kenar uzunluğu:(Lütfen sadece sayısal değerler giriniz)")
                                            time.sleep(0.9)
                                            

                                            try:
                                                int(kenar)
                                                

                                            except TypeError:
                                                import time
                                                time.sleep(0.9)
                                                print()
                                                print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                                continue

                                            kenar=int(kenar)
                                            
                                            if kenar%2==0:
                                                
                                                
                                                def eskenarUcgen(kenar):
                                                    a=0
                                                    b=kenar-1
                                                    for i in range(0,kenar):
                                                        print(" "* int(b),end="")
                                                        print((int(i)+1)*"*"+((int((i)-1)*"*")))
                                                        time.sleep(a)
                                                        a+=0.01
                                                        b-=1

                                                eskenarUcgen(kenar)
                                                break
                                    



                                            else:
                                                import time
                                                time.sleep(0.9)
                                                print()
                                                print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                                continue
                                                
                                


                                        
                                        

                                    elif secim2=="2":
                                        du=0
                                        while du==0:
                                            time.sleep(0.9)
                                            print()
                                            hipotenus=input("Dik üçgenin hipotenüsünü giriniz(Lütfen sadece sayısal değerler giriniz)")
                                            time.sleep(0.9)
                                            print()
                                            kenar1=input("Dik üçgenin dik kenarını(yüksekliğini) giriniz(Lütfen sadece sayısal değerler giriniz)")
                                            

                                            try:
                                                int(hipotenus)
                                                int(kenar1)
                                                

                                            except TypeError:
                                                import time
                                                time.sleep(0.9)
                                                print()
                                                print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                                continue

                                            hipotenus=int(hipotenus)
                                            kenar1=int(kenar1)
                                            
                                            ğğğğğ=0
                                            
                                            if hipotenus<kenar1*2 and kenar1**2+kenar1**2==hipotenus**2 :
                                                if ğğğğğ==0:

                                                    def dikucgen(yukseklik):
                                                        a=0
                                                        for i in range(yukseklik):
                                                            print(i*("*"))
                                                            import time
                                                            time.sleep(a)
                                                            a+=0.01


                                                    dikucgen(kenar1)
                                                    break
                                        
                                            else:
                                                import time
                                                time.sleep(0.9)
                                                print()
                                                print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                                continue
                                                
                                                
                                        



                                    else:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                break

                            elif secim=="4":
                                d=0
                                while d==0:
                                    time.sleep(0.7)
                                    print()
                                    
                                    print()
                                    uzunKenar = input("Görmek İstediğiniz Dikdörtgenin Uzun Kenarının Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    kisaKenar = input("Görmek İstediğiniz Dikdörtgenin Kısa Kenarının Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                        
                                    try:
                                        int(kisaKenar)
                                        int(uzunKenar)

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kisaKenar=int(kisaKenar)
                                    uzunKenar=int(uzunKenar)
                                    

                                    def dikdortgen(uzunKenar,kisaKenar):
                                        ss=0
                                        while ss==0:
                                            import time
                                            print()
                                            time.sleep(0.9)
                                            secimm=input("Dikdörtgeniniz düşey mi olsun yatay mı(Lütfen sadece düşey veya yatay olarak cevap verin)?")
                                            a=1

                                            if secimm=="düşey" or secimm=="Düşey":
                                                print()
                                                time.sleep(0.9)

                                                for i in range(uzunKenar):
                                                    print(kisaKenar*"*")
                                                    a-=0.1
                                                break

                                            elif secimm=="Dikey" or secimm=="dikey":
                                                print()
                                                time.sleep(0.9)
                                                for i in range(kisaKenar):
                                                    print(uzunKenar*"*")
                                                    a-=0.1
                                                break
                                
                                            else:
                                                import time
                                                time.sleep(0.9)
                                                print()
                                                print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                                continue
                                    dikdortgen(uzunKenar,kisaKenar)  
                                    break 

                                break     
                            
                            elif secim=="5":
                                d=0
                                while d==0:
                                    time.sleep(0.7)
                                    print()
                                    
                                    print()
                                    gorunenUzunluk = input("Görmek İstediğiniz Doğrunun Görünen Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    
                                    try:
                                        int(gorunenUzunluk)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    gorunenUzunluk=int(gorunenUzunluk)

                                    def dogru(uzunluk):
                                        print(" "*2+"*"+" "*(uzunluk-4)+"*")
                                        print(" "*1+"*"+" "*(uzunluk-2)+"*")
                                        print(uzunluk*"*"+"*")
                                        print(" "*1+"*"+" "*(uzunluk-2)+"*")
                                        print(" "*2+"*"+" "*(uzunluk-4)+"*")

                                    dogru(gorunenUzunluk)
                                    break
                                break

                            elif secim=="6":
                                b=0
                                while b==0:
                                    time.sleep(0.7)
                                    print()
                                    
                                    print()
                                    kenar = input("Görmek İstediğiniz Düzgün Beşgenin Bir Kenar Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    
                                    try:
                                        int(kenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kenar=int(kenar)
                                    

                                    def besgen(kenar):
                                        import math
                                        a=0
                                        b=kenar-1
                                        kosegen=(kenar+ kenar*math.sqrt(5))//2
                                        
                                        print(" "*(b+1)+"*")
                                        for i in range(1,kenar):
                                            print(" "* int(b),end="")
                                            print((int(i)+1)*"*"+((int((i)-1)*"*")))
                                            time.sleep(a)
                                            a+=0.01
                                            b-=1
                                        c=kenar-1
                                        for i in range(0,kenar):
                                            print(" "+int(kosegen+3)*"*")
                                        
                                            

                                    besgen(kenar)
                                    break
                                break

                            elif secim=="7":
                                a=0
                                while a==0:
                                    time.sleep(0.7)
                                    print()
                                    
                                    print()
                                    kenar = input("Görmek İstediğiniz Düzgün Altıgenin Bir Kenar Uzunluğu(Lütfen sadece sayısal bir tam sayı değeri giriniz....): ")
                                    
                                    try:
                                        int(kenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue

                                    kenar=int(kenar)
                                    

                                    def altigen(kenar):
                                        import math
                                        a=0
                                        b=kenar
                                        
                                        
                                        for i in range(0,kenar):
                                            print(" "* int(b),end="")
                                            print((kenar+i*2)*"*")
                                            time.sleep(a)
                                            a+=0.01
                                            b-=1

                                        for i in range(0,int(kenar)):
                                            print(int(b)*" "+(kenar*2-i*2)*"*"+(kenar-1)*"*")
                                            time.sleep(a)
                                            a+=0.01
                                            b+=1
                                        
                                            

                                    altigen(kenar)
                                    break
                                break

                            elif secim=="8":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Yamuk Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                y=0
                                while y==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    
                                    print()
                                    time.sleep(1)
                                    ustTaban=input("Yamuğun üst taban uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    yanKenar=input("Yamuğun Yan kenar uzunlukları(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    altTaban=int(ustTaban)+int(yanKenar)
                                    print()
                                    time.sleep(1)
                                    print("Yamuğun alt taban uzunluğu düzgün bir çizim ortaya çıkması için {} olarak belirlendi...".format(altTaban))
                                    print()
                                    time.sleep(1)

                                    
                                    try:
                                        altTaban=int(altTaban)
                                        ustTaban=int(ustTaban)
                                        yanKenar=int(yanKenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    altTaban=int(altTaban)
                                    ustTaban=int(ustTaban)
                                    yanKenar=int(yanKenar)
                                    

                                    def yamuk(altTaban,ustTaban,yanKenar):
                                        a=0.1
                                        for i in range(0,yanKenar):
                                            print(" "*(ustTaban*2-i*1),end="")
                                            print((ustTaban+i*2)*"*")
                                            time.sleep(int(a))
                                            a+=0.05
                                            

                                    yamuk(altTaban,ustTaban,yanKenar)
                                    
                                    break
                                
                                break
                                
                            elif secim=="9":
                                import time
                                time.sleep(1)
                                print()
                                print("Paralelkenar Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    tabanTavan=input("Paralelkenarın taban,tavan uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    ke2nar=input("Paralelkenarın diğer 2 kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                
                                    try:
                                        int(ke2nar)
                                        int(tabanTavan)
                                        

                                    except :
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    ke2nar=int(ke2nar)
                                    tabanTavan=int(tabanTavan)
                                    

                                    def paralelKenar(ke2nar,tabanTavan):
                                        a=0.00876767
                                        if ke2nar>=tabanTavan:
                                            for i in range(0,ke2nar):
                                                print(" "*(ke2nar-i),end="")
                                                print("*"*tabanTavan)
                                                time.sleep(a)
                                                a+=0.02112112

                                        else:
                                            for i in range(0,ke2nar):
                                                print(" "*(tabanTavan-i),end="")
                                                print("*"*tabanTavan)
                                                time.sleep(a)
                                                a+=0.02112112


                                    paralelKenar(ke2nar,tabanTavan)
                                    break
                                break

                            elif secim=="10":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Yedigen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    kenar=input("Düzgün yedigenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    
                                    try:
                                        int(kenar)
                                        

                                    except :
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    kenar=int(kenar)
                                    
                                    

                                    def yedigen(kenar):
                                        a=0.07287237283
                                        for i in range(0,kenar):
                                            import time
                                            print(" "*int(kenar*2-i),end="")
                                            print("*"*int(i+1))
                                            time.sleep(a)
                                            a+=0.0001
                                        for i in range(0,kenar):
                                            print(int(kenar-i)*" ",end="")
                                            print("*"*int(kenar+1+i*2))
                                            time.sleep(a)
                                            a+=0.0002999
                                        for i in range(0,kenar):
                                            print(i*" ",end="")
                                            print("*"*int(kenar+1+i))
                                            time.sleep(a)
                                            a+=0.867647575


                                    yedigen(kenar)
                                    break
                                break

                            elif secim=="11":
                                import time
                                time.sleep(1)
                                print()
                                print("Düzgün Sekizgen Seçtiniz.")
                                print()
                                import time
                                time.sleep(0.9)
                                print()
                                p=0
                                while p==0:
                                    import time
                                    time.sleep(1)
                                    print()
                                    kenar=input("Düzgün Sekizgenin bir kenar uzunluğu(Lütfen sadece sayısal değerler giriniz)? ")
                                    print()
                                    time.sleep(1)
                                    
                                    try:
                                        int(kenar)
                                        

                                    except TypeError:
                                        import time
                                        time.sleep(0.9)
                                        print()
                                        print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                                        continue
                                    
                                    kenar=int(kenar)

                                    def sekizgen(kenar):
                                        os.system("cls")
                                        print("this is impossible!!!!!!!")

                                    sekizgen(kenar)
                                    break
                                break

                        else:
                            import time
                            time.sleep(0.9)
                            print()
                            print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                            continue

                elif secim=="0":
                    os.system("cls")
                    import time
                    time.sleep(0.89)
                    print()
                    print("Geometri Basic V0.00001")
                    continue


                elif secim=="H" or secim=="h":
                    os.system("cls")
                    import time
                    time.sleep(0.9)
                    print()
                    print("""Bu uygulama bir insanın python öğrenmesini kolaylaştırmak için yapılmıştır.
                    Yani profesyonel bir şey beklemeyin. Fakat seçeneklerden birisini seçerseniz zevkinize
                    göre istediğiniz bir şekil sizin için yıldızlarla ya da normal bir şekilde çizilecektir... 
                    """)
                    continue


                                

                elif secim=="q" or secim=="Q":
                    os.system("cls")
                    import time
                    time.sleep(0.9)
                    print()
                    print("Çıkılıyor...")
                    quit()


                else:
                    import time
                    time.sleep(0.9)
                    print()
                    print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
                    continue

        except TypeError:
            os.system("cls")
            import time
            time.sleep(0.9)
            print()
            print("Geçersiz değer!! Lütfen tekrar deneyinnnnnn")
            continue

        except:
            os.system("cls")
            print("Bir hata oluştu...")


        finally:
            print("\n"*10)
            print("\n"+ "Hata olsun olmasın yine bekleriz...")
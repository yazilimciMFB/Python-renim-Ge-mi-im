# #volkan taşçının lokanta hesap uygulaması vid lerini izle nasıl efektif kısa öz kod yazılcağını arştır öğren 
# # iki menünün main() fonksiyonu ile çağrılıp önceki gibi alt üst menü olayını yap lower()  gibi metotları da kullan such as:
# tür=input(tür: )  for i in range türler:  if tür.lower() in i.lower() :prnt("sonraki adım")

# kontrol="i"
import time
import os
z=0

kitaplik1=[]
kitaplik2=[]
kitaplik3=[]
kitaplik4=[]
kitaplik5=[]

ü=0
if ü==0:
        try:
            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","r")
            dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","r")
            dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","r")
            dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","r")
            dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","r")
            veriler1= dosya1.read()
            veriler2= dosya2.read()
            veriler3= dosya3.read()
            veriler4= dosya4.read()
            veriler5= dosya5.read()
            dosya1.seek(0)
            dosya3.seek(0)
            dosya2.seek(0)
            dosya4.seek(0)
            dosya5.seek(0)
            veriler1=veriler1.split("\n")
            veriler2=veriler2.split("\n")
            veriler3=veriler3.split("\n")
            veriler4=veriler4.split("\n")
            veriler5=veriler5.split("\n")
            if  not veriler1[0]:
                veriler1.pop()
                dosya1.seek(0)

            if not veriler2[0]:
                veriler2.pop()
                dosya2.seek(0)

            if  not veriler3[0]:
                veriler3.pop()
                dosya3.seek(0)

            if  not veriler4[0]:
                veriler4.pop()
                dosya4.seek(0)

            if not veriler5[0]:
                veriler5.pop()
                dosya5.seek(0)

            
            


            # o=0

            # for i in veriler1:
            #     if str(i.isdigit):
            #         if z==0:

            #             ii=i.split()
            #             del ii[-1]
            #             del ii[-1]
                
            #             yeni1+=str(ii)

            #     else:
            #         o+=1

            # if o==len(veriler1):
            #     for i in veriler1:
            #         del veriler1[veriler1.index(i)]

            # else:
            #     pass
                             

            
                   
               
               
            kontrol=0
            
            for i in veriler1:
                if veriler1.index(i)%6==0 or veriler1.index(i)==0:
                    a=veriler1.index(i)
                    x={veriler1[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler1[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler1[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler1[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler1[a+4].strip(),
                                            "Kitabın Konusu : ":veriler1[a+5].strip().title()}}

                    if x not in kitaplik1:
                        kitaplik1.append(x)

                else:
                    pass

            for i in veriler2:
                if veriler2.index(i)%6==0 or veriler2.index(i)==0:
                    a=veriler2.index(i)
                    x={veriler2[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler2[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler2[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler2[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler2[a+4].strip(),
                                            "Kitabın Konusu : ":veriler2[a+5].title().strip()}}

                    if x not in kitaplik2:
                        kitaplik2.append(x)

                else:
                    pass

            for i in veriler3:
                if veriler3.index(i)%6==0 or veriler3.index(i)==0:
                    a=veriler3.index(i)
                    x={veriler3[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler3[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler3[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler3[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler3[a+4].strip(),
                                            "Kitabın Konusu : ":veriler3[a+5].strip().title()}}

                    if x not in kitaplik3:
                        kitaplik3.append(x)

                else:
                    pass

            for i in veriler4:
                if veriler4.index(i)%6==0 or veriler4.index(i)==0:
                    a=veriler4.index(i)
                    x={veriler4[a].strip().title():{"Kitabın Sayfa Sayısı: ":veriler4[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler4[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler4[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler4[a+4].strip(),
                                            "Kitabın Konusu : ":veriler4[a+5].strip().title()}}
                    if x not in kitaplik4:
                        kitaplik4.append(x)

                else:
                    pass

            for i in veriler5:
                if veriler5.index(i)%6==0 or veriler5.index(i)==0:
                    a=veriler5.index(i)
                    x={veriler5[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler5[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler5[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler5[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler5[a+4].strip(),
                                            "Kitabın Konusu : ":veriler5[a+5].strip().title()}}

                    if x not in kitaplik5:
                        kitaplik5.append(x)

                else:
                    pass


            dosya1.close()
            dosya2.close()
            dosya3.close()
            dosya4.close()
            dosya5.close()


        

        except FileNotFoundError:
        
            print("\nKayıt dosyası oluşturuluyor...\n")
            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","w")
            dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","w")
            dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","w")
            dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","w")
            dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","w")
            time.sleep(1)
            kontrol=1

            dosya1.close()
            dosya2.close()
            dosya3.close()
            dosya4.close()
            dosya5.close()




kitaplikListesi=["Kitaplık-1","Kitaplık-2","Kitaplık-3","Kitaplık-4","Kitaplık-5"]



def kitaplikListele():
    print()
    for i in kitaplikListesi:
        print(i)
        time.sleep(0.7) 






def kitapListele(kitaplik):
    print()
    
    for i in kitaplik:
        if type(i)==dict:
        
            print(i.keys())

        else:
            pass
        


# # def dosya():
# #     try:
# #         dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","r")
# #         dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","r")
# #         dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","r")
# #         dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","r")
# #         dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","r")
# #         veriler1= dosya1.readlines()
# #         veriler2= dosya2.readlines()
# #         veriler3= dosya3.readlines()
# #         veriler4= dosya4.readlines()
# #         veriler5= dosya5.readlines()
# #         kontrol=0
        
# #         for i in veriler1:
# #             if veriler1.index(i)%6==0 or veriler1.index(i)==0:
# #                 a=veriler1.index(i)
# #                 x={veriler1[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler1[a+1].strip(),
# #                                         "Kitabın Yazarı: ":veriler1[a+2].strip().title(),
# #                                         "Kitabın Yayınevi: ":veriler1[a+3].strip().title(),
# #                                         "Kitabın Baskı Numarası : ":veriler1[a+4].strip(),
# #                                         "Kitabın Konusu : ":veriler1[a+5].strip().title()}}

# #                 if x not in kitaplik1:
# #                     kitaplik1.append(x)

# #             else:
# #                 pass

# #         for i in veriler2:
# #             if veriler2.index(i)%6==0 or veriler2.index(i)==0:
# #                 a=veriler2.indexi(i)
# #                 x={veriler2[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler2[a+1].strip(),
# #                                         "Kitabın Yazarı: ":veriler2[a+2].strip().title(),
# #                                         "Kitabın Yayınevi: ":veriler2[a+3].strip().title(),
# #                                         "Kitabın Baskı Numarası : ":veriler2[a+4].strip(),
# #                                         "Kitabın Konusu : ":veriler2[a+5].title().strip()}}

# #                 if x not in kitaplik2:
# #                     kitaplik2.append(x)

# #             else:
# #                 pass

# #         for i in veriler3:
# #             if veriler3.index(i)%6==0 or veriler3.index(i)==0:
# #                 a=veriler3.index(i)
# #                 x={veriler3[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler3[a+1].strip(),
# #                                         "Kitabın Yazarı: ":veriler3[a+2].strip().title(),
# #                                         "Kitabın Yayınevi: ":veriler3[a+3].strip().title(),
# #                                         "Kitabın Baskı Numarası : ":veriler3[a+4].strip(),
# #                                         "Kitabın Konusu : ":veriler3[a+5].strip().title()}}

# #                 if x not in kitaplik3:
# #                     kitaplik3.append(x)

# #             else:
# #                 pass

# #         for i in veriler4:
# #             if veriler4.index(i)%6==0 or veriler4.index(i)==0:
# #                 a=veriler4.index(i)
# #                 x={veriler4[a].strip().title():{"Kitabın Sayfa Sayısı: ":veriler4[a+1].strip(),
# #                                         "Kitabın Yazarı: ":veriler4[a+2].strip().title(),
# #                                         "Kitabın Yayınevi: ":veriler4[a+3].strip().title(),
# #                                         "Kitabın Baskı Numarası : ":veriler4[a+4].strip(),
# #                                         "Kitabın Konusu : ":veriler4[a+5].strip().title()}}
# #                 if x not in kitaplik4:
# #                     kitaplik4.append(x)

# #             else:
# #                 pass

# #         for i in veriler5:
# #             if veriler5.index(i)%6==0 or veriler5.index(i)==0:
# #                 a=veriler5.index(i)
# #                 x={veriler5[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler5[a+1].strip(),
# #                                         "Kitabın Yazarı: ":veriler5[a+2].strip().title(),
# #                                         "Kitabın Yayınevi: ":veriler5[a+3].strip().title(),
# #                                         "Kitabın Baskı Numarası : ":veriler5[a+4].strip(),
# #                                         "Kitabın Konusu : ":veriler5[a+5].strip().title()}}

# #                 if x not in kitaplik5:
# #                     kitaplik5.append(x)

# #             else:
# #                 pass


# #         dosya1.close()
# #         dosya2.close()
# #         dosya3.close()
# #         dosya4.close()
# #         dosya5.close()


        

# #     except FileNotFoundError:
        
# #         print("\nKayıt dosyası oluşturuluyor...\n")
# #         dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","w")
# #         dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","w")
# #         dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","w")
# #         dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","w")
# #         dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","w")
# #         time.sleep(1)
# #         kontrol=1

# #         dosya1.close()
# #         dosya2.close()
# #         dosya3.close()
# #         dosya4.close()
# #         dosya5.close()
        

def kitapEkle():
    l=0
    while l==0:
        os.system("cls")
        ad =input("Kitabın Adı: ")
        time.sleep(1)
        break
        
    l=1
    while l==1:
        os.system("cls")
        sayfa=input("Kitabın Sayfa Sayısı: ")
        try: 
            sayfa=int(sayfa)

        except TypeError:
            print("\nBir kitabın tam sayı tipinde bir sayfa miktarı olabilir!")
            time.sleep(1)    
            continue
        sayfa=str(sayfa)
        break

    l=2
    while l==2:
        os.system("cls")
        yazar=input("Kitabın Yazarı: ")
        try:
            float(yazar)
            print("İnsan isimleri yazı ile yazılır!!!")
            time.sleep(1.3)
            continue

        except TypeError:
            break

        except ValueError:
            break

    l=3
    while l==3:
        os.system("cls")
        yayinevi=input("Kitabın Yayınevi: ")
        try:
            float(yayinevi)
            print("\nEğer yayınevinin adında rakamlar varsa bile onları da harfler ile yazzmka zorundasınız!!!")
            time.sleep(2)
            continue

        except ValueError:
            break

        except TypeError:
            break


        yayinevi=yayinevi+" Yayınları"


    l=4
    while l==4:
        os.system("cls")
        baskiNo=input("Kitabın Baskı Numarası: ")
        try:
            baskiNo=int(baskiNo)

        except TypeError:
            print("\n{}. baskı öyle mi?!?!?!?!?!?".format(baskiNo))
            time.sleep(1.6)
            continue

        except ValueError:
            print("\n{}. baskı öyle mi?!?!?!?!?!?".format(baskiNo))
            time.sleep(1.6)
            continue

        baskiNo=str(baskiNo)
        break

    l=5
    while l==5:
        os.system("cls")
        konu=input("Kitabın Konusu: ")
        try :
            konu=int(konu)
            print("\n{} konusu öyle mi?!?!?!?!?!?".format(konu))
            time.sleep(1.6)
            continue


        except TypeError:
            konu=str(konu)
            break
            
        except ValueError:
            konu=str(konu)
            break


    l=6
    while l==6:
        os.system("cls")
        kitaplikListele()
        ktplk=input("\nHangi Kitaplık? ")

        if ktplk.title()=="Kitaplık-1":
            if kontrol==0:
                
            

                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","a+")
                dosya1.write("\n")
                dosya1.write(ad.strip().title())
                dosya1.write("\n")
                dosya1.write(sayfa.strip())
                dosya1.write("\n")
                dosya1.write(yazar.strip().title())
                dosya1.write("\n")
                dosya1.write(yayinevi.strip().title())
                dosya1.write("\n")
                dosya1.write(baskiNo.strip())
                dosya1.write("\n")
                dosya1.write(konu.strip().title())
                dosya1.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik1.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break

            else:
                dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","a+")
                dosya1.write(ad.strip().title())
                dosya1.write("\n")
                dosya1.write(sayfa.strip())
                dosya1.write("\n")
                dosya1.write(yazar.strip().title())
                dosya1.write("\n")
                dosya1.write(yayinevi.strip().title())
                dosya1.write("\n")
                dosya1.write(baskiNo.strip())
                dosya1.write("\n")
                dosya1.write(konu.strip().title())
                dosya1.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik1.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break


            
            
            


        elif ktplk.title()=="Kitaplık-2":


            if kontrol==0:

                dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","a+")
                dosya2.write("\n")
                dosya2.write(ad.title().strip())
                dosya2.write("\n")
                dosya2.write(sayfa.strip())
                dosya2.write("\n")
                dosya2.write(yazar.strip().title())
                dosya2.write("\n")
                dosya2.write(yayinevi.title().strip())
                dosya2.write("\n")
                dosya2.write(baskiNo.strip())
                dosya2.write("\n")
                dosya2.write(konu.strip().title())
                dosya2.close()
                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik2.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break


            else:

                    dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","a+")
                    dosya2.write(ad.title().strip())
                    dosya2.write("\n")
                    dosya2.write(sayfa.strip())
                    dosya2.write("\n")
                    dosya2.write(yazar.strip().title())
                    dosya2.write("\n")
                    dosya2.write(yayinevi.title().strip())
                    dosya2.write("\n")
                    dosya2.write(baskiNo.strip())
                    dosya2.write("\n")
                    dosya2.write(konu.strip().title())
                    dosya2.close()
                    x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                                "Kitabın Yazarı: ":yazar.title().strip(),
                                                "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                                "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                                "Kitabın Konusu : ":konu.title().strip()}}

                    kitaplik2.append(x)
                    print("\nEklendi!!!!")
                    print("\n{}".format(x))
                    break

                

        elif ktplk.title()=="Kitaplık-3":



            if kontrol==0:
                dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","a+")
                dosya3.write("\n")
                dosya3.write(ad.strip().title())
                dosya3.write("\n")
                dosya3.write(sayfa.strip().title())
                dosya3.write("\n")
                dosya3.write(yazar.title().strip())
                dosya3.write("\n")
                dosya3.write(yayinevi.strip().title())
                dosya3.write("\n")
                dosya3.write(baskiNo.strip())
                dosya3.write("\n")
                dosya3.write(konu.strip().title())
                dosya3.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik3.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break


            else:
                dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","a+")
                
                dosya3.write(ad.strip().title())
                dosya3.write("\n")
                dosya3.write(sayfa.strip().title())
                dosya3.write("\n")
                dosya3.write(yazar.title().strip())
                dosya3.write("\n")
                dosya3.write(yayinevi.strip().title())
                dosya3.write("\n")
                dosya3.write(baskiNo.strip())
                dosya3.write("\n")
                dosya3.write(konu.strip().title())
                dosya3.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik3.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break

            
        elif ktplk.title()=="Kitaplık-4":

            if kontrol==0:


                dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","a+")
                dosya4.write("\n")
                dosya4.write(ad.strip().title())
                dosya4.write("\n")
                dosya4.write(sayfa.strip())
                dosya4.write("\n")
                dosya4.write(yazar.strip().title())
                dosya4.write("\n")
                dosya4.write(yayinevi.strip().title())
                dosya4.write("\n")
                dosya4.write(baskiNo.strip())
                dosya4.write("\n")
                dosya4.write(konu.strip().title())
                dosya4.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik4.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break



            else:
                dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","a+")
                
                dosya4.write(ad.strip().title())
                dosya4.write("\n")
                dosya4.write(sayfa.strip())
                dosya4.write("\n")
                dosya4.write(yazar.strip().title())
                dosya4.write("\n")
                dosya4.write(yayinevi.strip().title())
                dosya4.write("\n")
                dosya4.write(baskiNo.strip())
                dosya4.write("\n")
                dosya4.write(konu.strip().title())
                dosya4.close()

                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik4.append(x)
                print("\nEklendi!!!!")
                print("\n{}".format(x))
                break
            
        elif ktplk.title()=="Kitaplık-5":

            if kontrol==0:
                dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","a+")
                dosya5.write("\n")
                dosya5.write(ad.strip().title())
                dosya5.write("\n")
                dosya5.write(sayfa.strip())
                dosya5.write("\n")
                dosya5.write(yazar.title().strip())
                dosya5.write("\n")
                dosya5.write(yayinevi.title().strip())
                dosya5.write("\n")
                dosya5.write(baskiNo.strip())
                dosya5.write("\n")
                dosya5.write(konu.strip().title())
                dosya5.close()
                
                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik5.append(x)
                print("\nEklendi!!!!")
                print(f"\n{x}")
                break


            else:
                dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","a+")
                
                dosya5.write(ad.strip().title())
                dosya5.write("\n")
                dosya5.write(sayfa.strip())
                dosya5.write("\n")
                dosya5.write(yazar.title().strip())
                dosya5.write("\n")
                dosya5.write(yayinevi.title().strip())
                dosya5.write("\n")
                dosya5.write(baskiNo.strip())
                dosya5.write("\n")
                dosya5.write(konu.strip().title())
                dosya5.close()
                
                x={ad.title().strip():{"Kitabın Sayfa Sayısı: ":sayfa.strip(),
                                            "Kitabın Yazarı: ":yazar.title().strip(),
                                            "Kitabın Yayınevi: ":yayinevi.title().strip(),
                                            "Kitabın Baskı Numarası : ":baskiNo.strip(),
                                            "Kitabın Konusu : ":konu.title().strip()}}

                kitaplik5.append(x)
                print("\nEklendi!!!!")
                print(f"\n{x}")
                break


        else:
            print("\nLütfen geçerli ve yukardaki kitaplıklardan birinin ismini yazın!!!")
            time.sleep(4)
            continue
        
            

        
        

    # dosyada 1 kitap adı
    # dosyada 2 sayfa sayısı
    #  dosyada 3  yazar
    # dosyada 4  yayınevi
    # dosyada 5 baskıno
    
    # dosyada 6 konu
    # dosyada belirtme kitaplıkno





def kitapCikar():
    # dosyaya yeniden yazmada karışklık çıkmasını önlemek için herşeyi silmeden önce readlines 
    # yap sonra readlines daki silinecekleri çıkar readlines listesinden sonra w kipi ile dosyay onları tekrar yaz!!!
    s=0
    while s==0:
        os.system("cls")
        kitaplikListele()
        kit=input("\nÇıkarmak İstediğiniz Kitabın Bulunduğu Kitaplik: ")
        kit=kit.title().strip()
        
        if kit.title() == "Kitaplık-1":
            o=0
            while o==0:
                os.system("cls")
                print("Kitaplık-1'teki Kitaplar: ")
                print()
                kitapListele(kitaplik1)
                cikarilcak=input("\nÇıkarmak İstediğiniz Kitabın İsmi: ")
                count=0
                for i in kitaplik1:
                    if type(i)==dict:
                        if cikarilcak.title().strip() in i.keys():
                            kitaplik1.remove(i)
                            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","w")
                            
                            for ii in  kitaplik1:
                                if type(ii)==dict:
                                    dosya1.write("\n")
                                    a=ii.keys()
                                    dosya1.write(a)
                                    dosya1.write("\n")
                                    dosya1.write(i[a]["Kitabın Sayfa Sayısı: "])
                                    dosya1.write("\n")
                                    dosya1.write(i[a]["Kitabın Yazarı: "])
                                    dosya1.write("\n")
                                    dosya1.write(i[a]["Kitabın Yayınevi: "])
                                    dosya1.write("\n")
                                    dosya1.write(i[a]["Kitabın Baskı Numarası : "])
                                    dosya1.write("\n")
                                    dosya1.write(i[a]["Kitabın Konusu : "])
                                        

                                else:
                                    pass


                            

                        else:
                            count+=1

                    else:
                        pass


                if count==len(kitaplik1):
                    print("\nAradaığınız kitap bulunamadı, lütfen tekrar deneyin!!!")
                    continue

                else:
                    time.sleep(1)
                    print("\nKitap Çıkarıldı!!")
                    dosya1.close()
                    break

            break


        elif kit.title() == "Kitaplık-2":
            o=0
            while o==0:
                os.system("cls")
                print("Kitaplık-2'teki Kitaplar: ")
                print()
                kitapListele(kitaplik2)
                cikarilcak=input("\nÇıkarmak İstediğiniz Kitabın İsmi: ")
                count=0
                for i in kitaplik2:
                    if type(i)==dict:
                        if cikarilcak.title().strip() in i.keys():
                            kitaplik2.remove(i)
                            dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","w")
                            
                            for ii in  kitaplik2:
                                if type(ii)==dict:
                                    dosya2.write("\n")
                                    a=ii.keys()
                                    dosya2.write(a)
                                    dosya2.write("\n")
                                    dosya2.write(i[a]["Kitabın Sayfa Sayısı: "])
                                    dosya2.write("\n")
                                    dosya2.write(i[a]["Kitabın Yazarı: "])
                                    dosya2.write("\n")
                                    dosya2.write(i[a]["Kitabın Yayınevi: "])
                                    dosya2.write("\n")
                                    dosya2.write(i[a]["Kitabın Baskı Numarası : "])
                                    dosya2.write("\n")
                                    dosya2.write(i[a]["Kitabın Konusu : "])

                                        

                                else:
                                    pass


                            

                        else:
                            count+=1

                    else:
                        pass


                if count==len(kitaplik2):
                    print("\nAradaığınız kitap bulunamadı, lütfen tekrar deneyin!!!")
                    continue

                else:
                    time.sleep(1)
                    print("\nKitap Çıkarıldı!!")
                    dosya2.close()
                    break

            break

        elif kit.title() == "Kitaplık-3":
            o=0
            while o==0:
                os.system("cls")
                print("Kitaplık-3'teki Kitaplar: ")
                print()
                kitapListele(kitaplik3)
                cikarilcak=input("\nÇıkarmak İstediğiniz Kitabın İsmi: ")
                count=0
                for i in kitaplik3:
                    if type(i)==dict:
                        if cikarilcak.title().strip() in i.keys():
                            kitaplik3.remove(i)
                            dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","w")
                            
                            for ii in  kitaplik3:
                                if type(ii)==dict:
                                    dosya3.write("\n")
                                    a=ii.keys()
                                    dosya3.write(a)
                                    dosya3.write("\n")
                                    dosya3.write(i[a]["Kitabın Sayfa Sayısı: "])
                                    dosya3.write("\n")
                                    dosya3.write(i[a]["Kitabın Yazarı: "])
                                    dosya3.write("\n")
                                    dosya3.write(i[a]["Kitabın Yayınevi: "])
                                    dosya3.write("\n")
                                    dosya3.write(i[a]["Kitabın Baskı Numarası : "])
                                    dosya3.write("\n")
                                    dosya3.write(i[a]["Kitabın Konusu : "])

                                        

                                else:
                                    pass


                            

                        else:
                            count+=1

                    else:
                        pass


                if count==len(kitaplik3):
                    print("\nAradaığınız kitap bulunamadı, lütfen tekrar deneyin!!!")
                    continue

                else:
                    time.sleep(1)
                    dosya3.close()
                    print("\nKitap Çıkarıldı!!")
                    break

            break

        elif kit.title() == "Kitaplık-4":
            o=0
            while o==0:
                os.system("cls")
                print("Kitaplık-4'teki Kitaplar: ")
                print()
                kitapListele(kitaplik4)
                cikarilcak=input("\nÇıkarmak İstediğiniz Kitabın İsmi: ")
                count=0
                for i in kitaplik4:
                    if type(i)==dict:
                        if cikarilcak.title().strip() in i.keys():
                            kitaplik4.remove(i)
                            dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","w")
                            for ii in  kitaplik4:
                                if type(ii)==dict:
                                    dosya4.write("\n")
                                    a=ii.keys()
                                    dosya4.write(a)
                                    dosya4.write("\n")
                                    dosya4.write(i[a]["Kitabın Sayfa Sayısı: "])
                                    dosya4.write("\n")
                                    dosya4.write(i[a]["Kitabın Yazarı: "])
                                    dosya4.write("\n")
                                    dosya4.write(i[a]["Kitabın Yayınevi: "])
                                    dosya4.write("\n")
                                    dosya4.write(i[a]["Kitabın Baskı Numarası : "])
                                    dosya4.write("\n")
                                    dosya4.write(i[a]["Kitabın Konusu : "])

                                        

                                else:
                                    pass


                            

                        else:
                            count+=1

                    else:
                        pass


                if count==len(kitaplik4):
                    print("\nAradaığınız kitap bulunamadı, lütfen tekrar deneyin!!!")
                    time.sleep(2)
                    continue

                else:
                    time.sleep(1)
                    print("\nKitap Çıkarıldı!!")
                    dosya4.close()
                    break
            break

        elif kit.title() == "Kitaplık-5":
            o=0
            while o==0:
                os.system("cls")
                print("Kitaplık-5'teki Kitaplar: ")
                print()
                kitapListele(kitaplik5)
                cikarilcak=input("\nÇıkarmak İstediğiniz Kitabın İsmi: ")
                count=0
                for i in kitaplik5:
                    if type(i)==dict:
                        if cikarilcak.title().strip() in i.keys():
                            kitaplik5.remove(i)
                            dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","w")
                            
                            for ii in  kitaplik5:
                                if type(ii)==dict:
                                    dosya5.write("\n")
                                    a=ii.keys()
                                    dosya5.write(a)
                                    dosya5.write("\n")
                                    dosya5.write(i[a]["Kitabın Sayfa Sayısı: "])
                                    dosya5.write("\n")
                                    dosya5.write(i[a]["Kitabın Yazarı: "])
                                    dosya5.write("\n")
                                    dosya5.write(i[a]["Kitabın Yayınevi: "])
                                    dosya5.write("\n")
                                    dosya5.write(i[a]["Kitabın Baskı Numarası : "])
                                    dosya5.write("\n")
                                    dosya5.write(i[a]["Kitabın Konusu : "])

                                        

                                else:
                                    pass


                            

                        else:
                            count+=1

                    else:
                        pass


                if count==len(kitaplik5):
                    print("\nAradaığınız kitap bulunamadı, lütfen tekrar deneyin!!!")
                    continue

                else:
                    time.sleep(1)
                    print("\nKitap Çıkarıldı!!")
                    dosya5.close()
                    break
            break

        
        else:
            print("\nKitaplık Bulunamadı!!!!")
            time.sleep(2)
            continue


def main():
    while True:
        try:
            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","r")
            dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","r")
            dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","r")
            dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","r")
            dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","r")
            veriler1= dosya1.read()
            veriler2= dosya2.read()
            veriler3= dosya3.read()
            veriler4= dosya4.read()
            veriler5= dosya5.read()
            dosya1.seek(0)
            dosya3.seek(0)
            dosya2.seek(0)
            dosya4.seek(0)
            dosya5.seek(0)
            veriler1=veriler1.split("\n")
            veriler2=veriler2.split("\n")
            veriler3=veriler3.split("\n")
            veriler4=veriler4.split("\n")
            veriler5=veriler5.split("\n")
            if  not veriler1[0]:
                veriler1.pop()
                dosya1.seek(0)

            if not veriler2[0]:
                veriler2.pop()
                dosya2.seek(0)

            if  not veriler3[0]:
                veriler3.pop()
                dosya3.seek(0)

            if  not veriler4[0]:
                veriler4.pop()
                dosya4.seek(0)

            if not veriler5[0]:
                veriler5.pop()
                dosya5.seek(0)

            
            


            # o=0

            # for i in veriler1:
            #     if str(i.isdigit):
            #         if z==0:

            #             ii=i.split()
            #             del ii[-1]
            #             del ii[-1]
                
            #             yeni1+=str(ii)

            #     else:
            #         o+=1

            # if o==len(veriler1):
            #     for i in veriler1:
            #         del veriler1[veriler1.index(i)]

            # else:
            #     pass
                             

            
                   
               
               
            kontrol=0
            
            for i in veriler1:
                if veriler1.index(i)%6==0 or veriler1.index(i)==0:
                    a=veriler1.index(i)
                    x={veriler1[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler1[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler1[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler1[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler1[a+4].strip(),
                                            "Kitabın Konusu : ":veriler1[a+5].strip().title()}}

                    if x not in kitaplik1:
                        kitaplik1.append(x)

                else:
                    pass

            for i in veriler2:
                if veriler2.index(i)%6==0 or veriler2.index(i)==0:
                    a=veriler2.index(i)
                    x={veriler2[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler2[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler2[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler2[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler2[a+4].strip(),
                                            "Kitabın Konusu : ":veriler2[a+5].title().strip()}}

                    if x not in kitaplik2:
                        kitaplik2.append(x)

                else:
                    pass

            for i in veriler3:
                if veriler3.index(i)%6==0 or veriler3.index(i)==0:
                    a=veriler3.index(i)
                    x={veriler3[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler3[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler3[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler3[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler3[a+4].strip(),
                                            "Kitabın Konusu : ":veriler3[a+5].strip().title()}}

                    if x not in kitaplik3:
                        kitaplik3.append(x)

                else:
                    pass

            for i in veriler4:
                if veriler4.index(i)%6==0 or veriler4.index(i)==0:
                    a=veriler4.index(i)
                    x={veriler4[a].strip().title():{"Kitabın Sayfa Sayısı: ":veriler4[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler4[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler4[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler4[a+4].strip(),
                                            "Kitabın Konusu : ":veriler4[a+5].strip().title()}}
                    if x not in kitaplik4:
                        kitaplik4.append(x)

                else:
                    pass

            for i in veriler5:
                if veriler5.index(i)%6==0 or veriler5.index(i)==0:
                    a=veriler5.index(i)
                    x={veriler5[a].title().strip():{"Kitabın Sayfa Sayısı: ":veriler5[a+1].strip(),
                                            "Kitabın Yazarı: ":veriler5[a+2].strip().title(),
                                            "Kitabın Yayınevi: ":veriler5[a+3].strip().title(),
                                            "Kitabın Baskı Numarası : ":veriler5[a+4].strip(),
                                            "Kitabın Konusu : ":veriler5[a+5].strip().title()}}

                    if x not in kitaplik5:
                        kitaplik5.append(x)

                else:
                    pass


            dosya1.close()
            dosya2.close()
            dosya3.close()
            dosya4.close()
            dosya5.close()
            kitaplik1.sort()
            kitaplik2.sort()
            kitaplik3.sort()
            kitaplik4.sort()
            kitaplik5.sort()


        

        except FileNotFoundError:
        
            print("\nKayıt dosyası oluşturuluyor...\n")
            dosya1=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-1.txt","w")
            dosya2=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-2.txt","w")
            dosya3=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-3.txt","w")
            dosya4=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-4.txt","w")
            dosya5=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\Kütüphane Veri Tabanı\Kitaplık-5.txt","w")
            time.sleep(1)
            kontrol=1

            dosya1.close()
            dosya2.close()
            dosya3.close()
            dosya4.close()
            dosya5.close()

        # kitaplik1.sort()
        # kitaplik2.sort()
        # kitaplik3.sort()
        # kitaplik4.sort()
        # kitaplik5.sort()
        time.sleep(1)
        os.system("cls")
        print("""
        [0] Bilgi
        [1] Katalog İşlemleri
        [2] Görüntüleme
        [H] Yardım
        [Q] Çıkış
        """)

        
        secim=input("\n\nİşleminiz: ")

        if secim=="0":
            os.system("cls")
            time.sleep(1)
            print("Kitaplığınız V0.1")
            print("\nAna menüye dönmek için 'enter'a bas!!!!")
            input()
            continue

        elif secim=="1":
            os.system("cls")
            time.sleep(1)
            print("""
            [0] Üst Menü
            [1] Kitap Ekle
            [2] Kitap Çıkar
            """)

            
            secim2=input("\n\nİşleminiz: ")



            if secim2=="0":
                os.system("cls")
                time.sleep(1)
                print("\nAna Menüye Dönme İşlemini Onaylıyorsanız 'enter'a basın!!!")
                input()
                print("\nDönülüyor!!..")
                time.sleep(1)
                continue


            elif secim2=="1":
                os.system("cls")
                time.sleep(1)
                kitapEkle()
                print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                input()
                time.sleep(1)
                continue


            elif secim2=="2":
                os.system("cls")
                time.sleep(1)
                kitapCikar()
                print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                input()
                time.sleep(1)
                continue


        elif secim=="2":
            os.system("cls")
            time.sleep(1)
            print("""
            [0] Üst Menü
            [1] Belli Kütüphanedeki Kitapları Görünütle
            [2] Kitaplıkları Görüntüle
            [3] Belli Kütüphanedeki Kitap Sayısı
            [4] Total Kitap Sayısısı
            [5] Belli Bir Kitabın Bilgileri
            [6] Kitap Kontrolü
            """)

            
            secim3=input("\n\nİşleminiz: ")



            if secim3=="0":
                os.system("cls")
                time.sleep(1)
                print("\nAna Menüye Dönme İşlemini Onaylıyorsanız 'enter'a basın!!!")

                input()
                print("\nDönülüyor!!..")
                time.sleep(1)
                continue


            elif secim3=="1":
                l=0
                while l==0:
                    os.system("cls")
                    time.sleep(1)
                    kitaplikListele()
                    p=input("\nGörüntülemek İstediğiniz Kitaplık: ")
                    if p.strip().title()=="Kitaplık-1":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik1:
                            if type(i)==dict:
                                print(i.keys())
                                time.sleep(1)

                            else:
                                pass

                        break


                    elif p.strip().title()=="Kitaplık-4":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik4:
                            if type(i)==dict:
                                print(i.keys())
                                time.sleep(1)


                            else:
                                pass

                        break



                    elif p.strip().title()=="Kitaplık-5":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik5:
                            if type(i)==dict:
                                print(i.keys())
                                time.sleep(1)


                            else:
                                pass


                        break

                    elif p.strip().title()=="Kitaplık-3":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik3:
                            if type(i)==dict:
                                print(i.keys())
                                time.sleep(1)


                            else:
                                pass
                        

                        break

                    elif p.strip().title()=="Kitaplık-2":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik2:
                            if type(i)==dict:
                                print(i.keys())
                                time.sleep(1)


                            else:
                                pass


                        break

                    else:
                        os.system("cls")
                        time.sleep(1)
                        print("\nBöyle Bir Kitaplık Yok!!!")
                        continue
                


                print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                input()
                time.sleep(1)
                continue



            elif secim3=="2":
                os.system("cls")
                time.sleep(1)
                kitaplikListele()
                print("\nAna menüye dönmek için 'enter'a basın!!!!")
                input()
                print("\nDönülüyor!!..")
                time.sleep(1)
                continue


            elif secim3=="3":
                l=0
                while l==0:
                    os.system("cls")
                    time.sleep(1)
                    kitaplikListele()
                    p=input("\nSaymak İstediğiniz Kitaplık: ")
                    if p.strip().title()=="Kitaplık-1":
                        os.system("cls")
                        time.sleep(1)
                        a=0
                        for i in kitaplik1:
                            if type(i)==dict:
                                a+=1
                                time.sleep(0.4)

                            else:
                                pass

                        print(f"\n{p.title().strip()} kitaplığında {a} tane kitap var!!!!")
                        time.sleep(5)

                        break


                    elif p.strip().title()=="Kitaplık-4":
                        os.system("cls")
                        time.sleep(1)
                        a=0
                        for i in kitaplik4:
                            if type(i)==dict:
                                a+=1
                                time.sleep(0.4)

                            else:
                                pass

                        print(f"\n{p.title().strip()} kitaplığında {a} tane kitap var!!!!")
                        time.sleep(5)


                        break



                    elif p.strip().title()=="Kitaplık-5":
                        os.system("cls")
                        time.sleep(1)
                        a=0
                        for i in kitaplik5:
                            if type(i)==dict:
                                a+=1
                                time.sleep(0.4)

                            else:
                                pass

                        print(f"\n{p.title().strip()} kitaplığında {a} tane kitap var!!!!")
                        time.sleep(5)



                        break

                    elif p.strip().title()=="Kitaplık-3":
                        os.system("cls")
                        time.sleep(1)
                        a=0
                        for i in kitaplik3:
                            if type(i)==dict:
                                a+=1
                                time.sleep(0.4)

                            else:
                                pass

                        print(f"\n{p.title().strip()} kitaplığında {a} tane kitap var!!!!")
                        time.sleep(5)


                        break

                    elif p.strip().title()=="Kitaplık-2":
                        os.system("cls")
                        time.sleep(1)
                        a=0
                        for i in kitaplik2:
                            if type(i)==dict:
                                a+=1
                                time.sleep(0.4)

                            else:
                                pass

                        print(f"\n{p.title().strip()} kitaplığında {a} tane kitap var!!!!")
                        time.sleep(5)



                        break

                    else:
                        os.system("cls")
                        time.sleep(1)
                        print("\nBöyle Bir Kitaplık Yok!!!")
                        continue

                print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                input()
                time.sleep(1)
                continue



            elif secim3=="4":
                os.system("cls")
                time.sleep(1)
                a=0
                for i in kitaplik1:
                    a+=1
                    time.sleep(0.3)

                for i in kitaplik2:
                    a+=1
                    time.sleep(0.3)


                for i in kitaplik3:
                    a+=1
                    time.sleep(0.3)



                for i in kitaplik4:
                    a+=1
                    time.sleep(0.3)


                for i in kitaplik5:
                    a+=1
                    time.sleep(0.3)


                print(f"\nToplamda {a} tane kitap var!!!!")
                print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                input()
                time.sleep(1)
                continue


                
                
                
            
            elif secim3=="5":
                l=0
                while l==0:
                    os.system("cls")
                    time.sleep(1)
                    kitaplikListele()
                    p=input("\nAradığınız Kitabın Bulunduğu Kitaplık: ")
                    if p.strip().title()=="Kitaplık-1":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik1:
                            if type(i)==dict:
                                a=i.keys()
                                print(a)
                                time.sleep(1)
                                

                            else:
                                pass


                        l=1
                        while l==1:
                            os.system("cls")
                            time.sleep(1)
                            kitapListele(kitaplik1)
                            p=input("\nHangi Kitabın Bilgilerini Görüntülemek İstiyorsunuz??? ")
                            count=0
                            
                            for i in veriler1:
                                if z==0:
                                    if p.title().strip() in i:
                                        a=veriler1.index(i)
                                        print("\nİşte Kitap:    \n")
                                        print(veriler1[a],veriler1[a+1],veriler1[a+2],veriler1[a+3],veriler1[a+4],veriler1[a+5],sep="\n")
                                        print("\nAna menüye dönmek için 'enter'a basın!!!")
                                        input()
                                        time.sleep(1)
                                        break

                                    else:
                                        count+=1

                                else:
                                    pass

                            if count==len(kitaplik1):
                                print("\nKitap Bulunamadı!!!")
                                time.sleep(2)
                                continue
                            else:
                                break

                


                    elif p.strip().title()=="Kitaplık-4":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik4:
                            if z==0:
                                a=i.keys()
                                print(a)
                                time.sleep(1)
                                

                            else:
                                pass


                        l=1
                        while l==1:
                            os.system("cls")
                            time.sleep(1)
                            kitapListele(kitaplik4)
                            p=input("\nHangi Kitabın Bilgilerini Görüntülemek İstiyorsunuz??? ")
                            count=0
                            for i in veriler4:
                                if z==0:
                                    if  p.strip().title() in i:
                                        a=veriler4.index(i)
                                        print("\nİşte Kitap:    \n")
                                        print(veriler4[a],veriler4[a+1],veriler4[a+2],veriler4[a+3],veriler4[a+4],veriler4[a+5],sep="\n")
                                        print("\nAna menüye dönmek için 'enter'a basın!!!")
                                        input()
                                        time.sleep(1)
                                        break

                                    else:
                                        count+=1

                                else:
                                    pass

                            if count==len(kitaplik4):
                                print("\nKitap Bulunamadı!!!")
                                time.sleep(2)
                                continue
                            else:
                                break



                    elif p.strip().title()=="Kitaplık-5":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik5:
                            if z==0:
                                a=i.keys()
                                print(a)
                                time.sleep(1)
                                

                            else:
                                pass


                        l=1
                        while l==1:
                            os.system("cls")
                            time.sleep(1)
                            kitapListele(kitaplik5)
                            p=input("\nHangi Kitabın Bilgilerini Görüntülemek İstiyorsunuz??? ")
                            count=0
                            for i in veriler5:
                                if type(i)==dict:
                                    if p.title().strip() in i:
                                        a=veriler5.index(i)
                                        print("\nİşte Kitap:    \n")
                                        print(veriler5[a],veriler5[a+1],veriler5[a+2],veriler5[a+3],veriler5[a+4],veriler5[a+5],sep="\n")
                                        print("\nAna menüye dönmek için 'enter'a basın!!!")
                                        input()
                                        time.sleep(1)
                                        break

                                    else:
                                        count+=1

                                else:
                                    pass

                            if count==len(kitaplik5):
                                print("\nKitap Bulunamadı!!!")
                                time.sleep(2)
                                continue
                            else:
                                break

                    elif p.strip().title()=="Kitaplık-3":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik3:
                            if z==0:
                                a=i.keys()
                                print(a)
                                time.sleep(1)
                                

                            else:
                                pass


                        l=1
                        while l==1:
                            os.system("cls")
                            time.sleep(1)
                            kitapListele(kitaplik3)
                            p=input("\nHangi Kitabın Bilgilerini Görüntülemek İstiyorsunuz??? ")
                            count=0
                            for i in veriler3:
                                if type(i)==dict:
                                    if p.title().strip() in i:
                                        a=veriler3.index(i)
                                        print("\nİşte Kitap:    \n")
                                        print(veriler3[a],veriler3[a+1],veriler3[a+2],veriler3[a+3],veriler3[a+4],veriler3[a+5],sep="\n")
                                        print("\nAna menüye dönmek için 'enter'a basın!!!")
                                        input()
                                        time.sleep(1)
                                        break

                                    else:
                                        count+=1

                                else:
                                    pass

                            if count==len(kitaplik3):
                                print("\nKitap Bulunamadı!!!")
                                time.sleep(2)
                                continue
                            else:
                                break

                    elif p.strip().title()=="Kitaplık-2":
                        os.system("cls")
                        time.sleep(1)
                        for i in kitaplik2:
                            if z==0:
                                a=i.keys()
                                print(a)
                                time.sleep(1)
                                

                            else:
                                pass


                        l=1
                        while l==1:
                            os.system("cls")
                            time.sleep(1)
                            kitapListele(kitaplik2)
                            p=input("\nHangi Kitabın Bilgilerini Görüntülemek İstiyorsunuz??? ")
                            count=0
                            for i in veriler2:
                                if type(i)==dict:
                                    if p.title().strip() in i:
                                        a=veriler2.index(i)
                                        print("\nİşte Kitap:    \n")
                                        print(veriler2[a],veriler2[a+1],veriler2[a+2],veriler2[a+3],veriler2[a+4],veriler2[a+5],sep="\n")
                                        print("\nAna menüye dönmek için 'enter'a basın!!!")
                                        input()
                                        time.sleep(1)
                                        break

                                    else:
                                        count+=1

                                else:
                                    pass

                            if count==len(kitaplik2):
                                print("\nKitap Bulunamadı!!!")
                                time.sleep(2)
                                continue
                            else:
                                break
                


                    else:
                        os.system("cls")
                        time.sleep(1)
                        print("\nBöyle Bir Kitaplık Yok!!!")
                        continue



                    break


                # print("\nİşleminiz tamamlandı, ana menüye dönmek için 'enter'a basın!!!")
                # input()
                # time.sleep(1)s
                # continue



            elif secim3=="6":
                os.system("cls")
                time.sleep(1)
                # print(veriler4)
                p=input("\nAradığınız Kitap: ")
                b=[]
                for i in kitaplik1:
                    b+=i
                    time.sleep(0.3)

                for i in kitaplik2:
                    b+=i
                    time.sleep(0.3)


                for i in kitaplik3:
                    
                    b+=i
                    time.sleep(0.3)

                for i in kitaplik4:
                    b+=i
                    time.sleep(0.3)


                for i in kitaplik5:
                    b+=i
                    time.sleep(0.3)



                count=0

                for ii in b:
                    if z==0:
                        
                        if p.strip().title()==ii:
                            for iii in kitaplik1:
                                if type(iii)==dict:
                                    if z==0:
                                        if p.strip().title() in iii.keys():
                                            c="Kitaplık-1"

                                        else:
                                            pass

                                else:
                                    pass


                            for iii in kitaplik2:
                                if type(iii)==dict:
                                    if z==0:
                                        if p.strip().title() in iii.keys():
                                            c="Kitaplık-2"

                                        else:
                                            pass

                                else:
                                    pass

                            for iii in kitaplik3:
                                if type(iii)==dict:
                                    if z==0:

                                        if p.strip().title() in iii.keys():
                                            c="Kitaplık-3"

                                        else:
                                            pass

                                else:
                                    pass


                            for ii in kitaplik4:
                                if type(ii)==dict:
                                    if z==0:
                                        if p.strip().title() in ii.keys():
                                            c="Kitaplık-4"

                                        else:
                                            pass

                                else:
                                    pass


                            for iii in kitaplik5:
                                if type(iii)==dict:
                                    if z==0:
                                        if p.strip().title() in iii.keys():
                                            c="Kitaplık-5"

                                        else:
                                            pass

                                else:
                                    pass

                            

                        else:
                            count+=1


                if count==len(b):
                    os.system("cls")
                    print(f"{p.strip().title()} Adında Bir Kitap Yok!!!!")
                    
                else:
                    os.system("cls")
                    print(f"Aradığınız Kitap , {p.strip().title()} {c} kitaplığında bulundu!!! ")

                print("\nAna menüye dönmek için 'enter'a basın!!!!")
                input()
                print("\nDönülüyor!!..")
                time.sleep(1)
                continue

        elif secim=="h" or secim=="h":
            os.system("cls")
            time.sleep(1)
            print("""\n
            Bu uygulama gelişmiş falan deil,
            ondan çok bi amacı falan da yok 
            sadece öğrenme sürecimi güçlendirmek için yapıldı!
            Fazıl eğer geleckten buraya bakıyorsan;
            18.06.2020 PERŞEMBE
            """)
            print("\nAna menüye dönmek için 'enter'a basın!!!!")
            input()
            time.sleep(1)
            continue

        elif secim=="q" or secim=="Q":
            os.system("cls")
            time.sleep(1)
            print("\nÇıkma İşlemini Onaylıyorsanız 'enter'a basın!!!")

            input()
            print("\nÇıkılıyor!!..")
            time.sleep(1)
            quit()



















# print(veriler1)
# print(type(veriler1))    []







































main()
bolenler=list()
flag=False

def pisagorMukemmel(a):
    global bolenler
    global flag
    bolenler.clear()
    for i in range(1,a):
        if a%i==0:
            bolenler.append(i)
        
    return sum(bolenler)-1==a
    
    
    
    
dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\'500 Yıllık Problem.txt","a+")
z=int(dosya.read())
dosya.close()
    
for e in range(z,64712348174564564897965674653542543567478656786875678456347648769869785675334254656789875433457890679786998696896886775657756756867978098098967858675634324320965498785764359318):
    
    if  pisagorMukemmel(e):
        print("\as")
        print(e)
        break

    else:
        dosya=open(r"C:\Users\abdullah\Muhammet Fazıl BALIKÇI\Yazılım\Python Projelerim\Veri Tabanları\'500 Yıllık Problem.txt","w")
        print(e)
        dosya.write(e)
        dosya.close()
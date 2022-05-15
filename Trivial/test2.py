import CaeserCipher as cc
import timeit

lines = []
f = open("Trivial/testText.txt", "r")
for line in f:
    lines.append(line.rstrip())
    
counterb=0
counterc=0
counterd=0
countere=0
countere2=0
time1=0
time2=0
time3=0
time4=0
ads = []
time42=0
for line in lines:
    for i in range(101):
        a = cc.encrypt(line, i)
        
        start3 = timeit.default_timer()
        d = cc.decrypt(a)
        stop3= timeit.default_timer()
    
        time3=time3+(stop3-start3)
        s = "current key: ",i,'\n3: ',d
        print("current key: ",i)
        print("linea: ",line)
        print(a)
        print('3: ',d)
       
        if(line==d):
            counterd=counterd+1
            print("func 3")
        else:
             ads.append(s)
        print(" ")
print("resultados de ",len(lines)*101," pruebas")
print("decifra 3: ",counterd)
print("tiempo: ",time3)

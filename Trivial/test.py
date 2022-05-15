import CaeserCipherUGLY as cc
import CaeserCipher as cc2
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
time42=0
for line in lines:
    a = cc.encrypt(line, 1)
    start1 = timeit.default_timer()

    b = cc.decrypt(a)

    stop1 = timeit.default_timer()
    start2= timeit.default_timer()

    c = cc.decrypt2(a)

    stop2 = timeit.default_timer()
    start3 = timeit.default_timer()
    d = cc.decrypt3(a)
    stop3= timeit.default_timer()
    
    start4 = timeit.default_timer()
    e = cc.Descifrado(a)
    stop4= timeit.default_timer()
    start42 = timeit.default_timer()
    e2 = cc2.decrypt(cc2.encrypt(line, 1))
    stop42= timeit.default_timer()
    time1=time1+(stop1-start1)
    time2=time2+(stop2-start2)
    time3=time3+(stop3-start3)
    time4=time4+(stop4-start4)
    time42=time42+(stop42-start42)
    print("linea: ",line)
    print('1: ',b)
    print('2: ',c)
    print('3: ',d)
    print('4: ',e)
    print('n: ',e2)
    
    if(line==b):
        counterb=counterb+1
        print("func 1")
    if(line==c):
        counterc=counterc+1
        print("func 2")
    if(line==d):
        counterd=counterd+1
        print("func 3")
    if(line==e):
        countere=countere+1
        print("func 4")
    if(line==e2):
        countere2=countere2+1
        print("func n")
    print(" ")
print("resultados de ",len(lines)," pruebas")
print("decifra 1: ",counterb)
print("tiempo: ",time1)
print("decifra 2: ",counterc)
print("tiempo: ",time2)
print("decifra 3: ",counterd)
print("tiempo: ",time3)
print("decifra 4: ",countere)
print("tiempo: ",time4)
print("decifra 42: ",countere2)
print("tiempo: ",time42)
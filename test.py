import CaeserCipher as cc
import timeit

lines = []
f = open("a.txt", "r")
for line in f:
    lines.append(line.rstrip())
    
counterb=0
counterc=0
counterd=0
time1=0
time2=0
time3=0
for line in lines:
    a = cc.encrypt(line, 15)
    start1 = timeit.default_timer()

    b = cc.decrypt(a)

    stop1 = timeit.default_timer()
    start2= timeit.default_timer()

    c = cc.decrypt2(a)

    stop2 = timeit.default_timer()
    start3 = timeit.default_timer()
    d = cc.decrypt3(a)
    stop3= timeit.default_timer()
    
    time1=time1+(stop1-start1)
    time2=time2+(stop2-start2)
    time3=time3+(stop3-start3)
    print("linea: ",line)
    print('1: ',b)
    print('2: ',c)
    print('3: ',d)
    
    if(line==b):
        counterb=counterb+1
        print("func 1")
    if(line==c):
        counterc=counterc+1
        print("func 2")
    if(line==d):
        counterd=counterd+1
        print("func 3")
    print(" ")
print("resultados de ",len(lines)," pruebas")
print("decifra 1: ",counterb)
print("tiempo: ",time1)
print("decifra 2: ",counterc)
print("tiempo: ",time2)
print("decifra 3: ",counterd)
print("tiempo: ",time3)
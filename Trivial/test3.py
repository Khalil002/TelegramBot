import CaeserCipher as cc


counter =0
e = cc.encrypt("Hola", 1)
print(e)
d= cc.decrypt(e)
print(d)
'''
ads=[]
for i in range(203):
    print("llave= ",i)
    e = cc.encrypt("Pene replete juguete", i)
    print(e)
    d= cc.decrypt3(e)
    
    
    print(d)
    if(d == "Pene replete juguete"):
        counter+=1
        print("correct")
    else:
        s=str(i),' bruh ',str(d)
        ads.append(s)
    print("")
print(counter)
for i in ads:
    print(i)
    '''
print(cc.characters)
print(cc.characters_by_frequency)
print(cc.special_characters)

import random
caracteres= '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
clave=''             
longitud=int(input('Ingresa la longitud de tu clave'))
for i in range(longitud):
    x=random.choice(caracteres)
    clave= clave + x    
print(clave)    

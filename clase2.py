import sys
sys.path.append(')# fill out with path

def decorator(func):
    def otra_funcion():
        print("se ejecutara una funcion")
        func()
        print ("se ejecuto la funcion")
    return otra_funcion

@decorator 
def function_add():
    print (10+11)
  
#function_add()

def new():
    loco = "arre loco"
    print (loco)
    
#import sys
#import time
#for i in range (100):
    #time.sleep(0.5)
    #sys.stdout.write("\r%d %%" %i)
    #sys.stdout.flush()
          
#if __name__=="__main__":
    #new()
import time
lineas=4
espacios=lineas
asteriscos=1
str=''

##for r in range (lineas):
##    for n in range (espacios):#agrega cuatro espacios
##        str += ' '
##    for n in range (asteriscos):#agrega un asterisco
##        str += '*'
##    print (str)
##    str=''

cadena =''
for i in range (lineas):
    for r in range (espacios):
        str += ' '
    espacios-=1
    for r in range (asteriscos):
        str += '* '
    asteriscos+=1
    print (str)
    if (asteriscos ==(lineas+1)):  # si el numero de asteriscos es igual al nimero de lineas entra el for para el decremento
        print('hello world')
        print (espacios)#0
        print (lineas)#4


        for a in range (lineas):#anidar otro ciclo for para seguir con el decremento
            cadena+=('*'*lineas)
            print (cadena)
            cadena+=' '
            lineas-=1

    str =''
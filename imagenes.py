'''
1- parseador de imagenes.
    1-a iterar entre las img con la clase ParsearImg y separar las 100 de las 200.. hasta las 800 en 8 clases diferentes
2- crear un dataset de imagenes para cada una de las clases
    2-a Se deberá usar la misma clase que la usada para el 1er parseo y ahí:
        2-a-1- llevarlas a un valor cuadrado, ya sea deformandolas o cortandolas 
        2-a-2  cortar n miniaturas de cada una de las imagenes almacenando las img en un directorio
    2-b Una vez separadas y lsa guardas las miniaturas se selecciona el batch de manera random.
'''
from preTratamiento import PreTratamientoImag as ptImg

pretratamiento=ptImg()
print(pretratamiento.numClases)





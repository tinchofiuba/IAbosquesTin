
import os
import cv2
import shutil

class PreTratamientoImag:
    def __init__(self):
        self.path= os.path.dirname(os.path.abspath(__file__)) # en caso de no asignar un path
        self.imgList=[]
        self.escalaClases=100 # por default
        self.class_dir=os.path.join(self.path, "clases") # en caso de no asignar un path
        self.numClases=41 #por default
        self.absClassDir=None

    ###########
    #setters
    ###########
    @property
    def pathImg(self)-> str:
        return self.path
    
    @pathImg.setter
    def pathImg(self, path: str):
        self.path=path
    @property
    def escala(self)->int:
        return self.escalaClases
    
    @escala.setter
    def escala(self, escala:int):
        if escala>0:
            self.escalaClases=escala
        else:
            print("la escala no puede ser menor a 0")
    @property        
    def pathClass(self)->str:
        return self.class_dir
    
    @pathClass.setter
    def pathClass(self, path: str):
        self.class_dir=path
        
    @property
    def cantidadClases(self)->int:
        return self.numClases
    
    @cantidadClases.setter
    def cantidadClases(self, num:int):
        if num>0:
            self.numClases=num
        else:
            print("el numero de clases no puede ser menor a 0")
    ##########
    #lo otro
    ##########
    
    def cortadoImg(self): #abre, corta y modifica la img
        print("cortando")
        
    def guardarImg(self, *args, **kwargs):
        print("guardando")
        
    def parseoImg(self):
        self.crearCarpeta()
        #iterno en el path carpeta a carpeta
        for dir in os.listdir(self.path):
            self.pathdir=os.path.join(self.path, dir) #direccion absoluta de la carpeta
            for file in os.listdir(self.pathdir):
                if file.endswith('.jpg') or file.endswith('.png'):
                    fileName=file.split(".")[0] 
                    if not fileName.isdigit(): #me fijo que solamente haya caracteres numericos en el archivo
                        print(f"El archivo {file} no es numerico!!")
                        continue
                    clase=int(fileName)//100 #numero de clase
                    if clase>self.numClases or clase<1: #me fijo que la clase no sea mayor a la cantidad de clases
                        print(f"El archivo {file} no pertenece a ninguna clase entre 1 y 42")
                        continue
                    self.absSaveDir = os.path.join(self.class_dir, f"clase_{clase}") #direccion absoluta de guardaro
                    shutil.copy(os.path.join(self.pathdir, file), self.absSaveDir) #copio el archivo a la carpeta correspondiente
    
    def crearCarpeta(self):
        for i in range(1, self.numClases): 
            self.absClassDir = os.path.join(self.class_dir, f"clase_{i}")
            if not os.path.exists(self.absClassDir):
                os.makedirs(self.absClassDir)
            else:
                print(f"La carpeta {self.absClassDir} ya existe.") 
    
    def cargarImagenes(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.png'):
                    self.imagenes.append(os.path.join(root, file))

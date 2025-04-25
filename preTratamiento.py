import os
import shutil
from concurrent.futures import ThreadPoolExecutor

class ClasificadorImg_cada100:
    '''
    Permite parsear imagenes tageadas como 102, 201, 307, 405 etc en clases de a 100 siempre y cuando el nombre sea COMPLETAMENTE NUMERICO-> 0123.jpg (OK) _0123A.jpg (mal)   
    Por defautl maneja 41 clases y los path son el mismo que el script
    Los formatos de img admitidos son .jpg y .png - aunque en se podŕia ampliar
    el nom
    '''
    
    def __init__(self):
        self.__path = os.path.dirname(os.path.abspath(__file__))  # Ruta predeterminada
        self.imgList = []
        self.escalaClases = 100  # Por default
        self.class_dir = os.path.join(self.__path, "clases")  # Carpeta de clases
        self.numClases = 41  # Número de clases
        self.absClassDir = None
        self.listaErrores = []

    ###########
    # Setters
    ###########
    @property
    def pathImg(self) -> str:
        return self.__path

    @pathImg.setter
    def pathImg(self, path: str):
        self.__path = path

    @property
    def escala(self) -> int:
        return self.escalaClases

    @escala.setter
    def escala(self, escala: int):
        if escala > 0:
            self.escalaClases = escala
        else:
            print("La escala no puede ser menor a 0")

    @property
    def pathClass(self) -> str:
        return self.class_dir

    @pathClass.setter
    def pathClass(self, path: str):
        self.class_dir = path

    @property
    def cantidadClases(self) -> int:
        return self.numClases

    @cantidadClases.setter
    def cantidadClases(self, num: int):
        if num > 0:
            self.numClases = num + 1
        else:
            print("El número de clases no puede ser menor a 0")

    ##########
    # Métodos NO setters
    ##########
    def cortadoImg(self):  # Abre, corta y modifica la img
        print("Cortando")

    def guardarImg(self, *args, **kwargs):
        print("Guardando")

    def procesar_archivo(self, file, pathdir):
        """Procesa un archivo individual."""
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.JPG') or file.endswith('.PNG'):
            fileName = file.split(".")[0]
            if not fileName.isdigit():  # Verificar que el nombre sea numérico
                print(f"El archivo {file} no es numérico!!")
                return
            clase = int(fileName) // 100  # Número de clase
            if clase > self.numClases or clase < 1:  # Verificar rango de clases
                print(f"El archivo {file} no pertenece a ninguna clase entre 1 y {self.numClases}")
                return
            absSaveDir = os.path.join(self.class_dir, f"clase_{clase}")  # Carpeta de destino
            if not os.path.exists(absSaveDir):
                os.makedirs(absSaveDir)  # Crear carpeta si no existe
            origen = os.path.join(pathdir, file)
            destino = os.path.join(absSaveDir, file)
            shutil.copy(origen, destino)  # Copiar archivo
            print(f"Archivo {file} copiado a {absSaveDir}")

    def parseoImg(self):
        """Paraleliza el procesamiento de imágenes usando ThreadPoolExecutor."""
        self.crearCarpeta()
        with ThreadPoolExecutor() as executor:
            for dir in os.listdir(self.__path):
                pathdir = os.path.join(self.__path, dir)  # Dirección absoluta de la carpeta
                if os.path.isdir(pathdir):  # Asegurarse de que sea un directorio
                    for file in os.listdir(pathdir):
                        executor.submit(self.procesar_archivo, file, pathdir)

    def crearCarpeta(self):
        """Crea las carpetas para las clases."""
        for i in range(1, self.numClases): 
            self.absClassDir = os.path.join(self.class_dir, f"clase_{i}")
            if not os.path.exists(self.absClassDir):
                os.makedirs(self.absClassDir)
            else:
                print(f"La carpeta {self.absClassDir} ya existe.")

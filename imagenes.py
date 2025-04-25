from preTratamiento import ClasificadorImg_cada100 as Img_cada_100

clasif=Img_cada_100()
#definir el número de clases a clasificar
clasif.numClases=41

#definir escala de clasificación. Cada esta escala se separan las clases de img
clasif.escala=100 

#path a donde están las carpetas con las img o donde están las img sueltas
clasif.pathImg="/home/martin/repos/datasets/maderas_macro/clases_parseadas"

#path a donde se guardaran las imagenes clasificadas, se ordenan en carpetas
clasif.class_dir="/home/martin/repos/datasets/maderas_macro/imagenes" 

#inicio del proceso de parseo
clasif.parseoImg()







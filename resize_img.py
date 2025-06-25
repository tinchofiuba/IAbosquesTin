import os
import cv2

#naveo por la direccion ""/home/martin/repos/datasets/maderas_macro/imagenes""

path = "/home/martin/repos/datasets/maderas_macro/imagenes chicas"

#itero en el path para entrar entrar a toda carpeta que haya y a toda imagen que haya le reduzco el tamaño de 2448 x 3264 a un 40% del tamaño
fraccion_resize = 0.1  # 

for root, dirs, files in os.walk(path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(root, file)
            img = cv2.imread(file_path)
            if img is not None:
                # Redimensionar la imagen al 40% de su tamaño original
                new_width = int(img.shape[1] * fraccion_resize)
                new_height = int(img.shape[0] * fraccion_resize)
                resized_img = cv2.resize(img, (new_width, new_height))
                
                # Guardar la imagen redimensionada
                cv2.imwrite(file_path, resized_img)
                print(f"Redimensionada: {file_path} a {new_width}x{new_height}")
            else:
                print(f"Error al leer la imagen: {file_path}")

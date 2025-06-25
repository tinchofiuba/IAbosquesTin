import os
import shutil
import random

# Ruta principal que contiene las carpetas clase_1, clase_2, ..., clase_40
pathClases = "/home/martin/repos/datasets/maderas_macro/imagenes"

# Carpetas destino globales
train_root = os.path.join(pathClases, "train")
test_root = os.path.join(pathClases, "test")
val_root = os.path.join(pathClases, "val")

os.makedirs(train_root, exist_ok=True)
os.makedirs(test_root, exist_ok=True)
os.makedirs(val_root, exist_ok=True)

# Iterar sobre las carpetas clase_1, clase_2, ..., clase_40
for clase in sorted(os.listdir(pathClases)):
    if not clase.startswith("clase_"):
        continue
    clase_path = os.path.join(pathClases, clase)
    
    # Verificar si es un directorio
    if os.path.isdir(clase_path):
        print(f"Procesando {clase}...")
        
        # Crear las carpetas de clase dentro de train, test y val
        train_path = os.path.join(train_root, clase)
        test_path = os.path.join(test_root, clase)
        val_path = os.path.join(val_root, clase)
        os.makedirs(train_path, exist_ok=True)
        os.makedirs(test_path, exist_ok=True)
        os.makedirs(val_path, exist_ok=True)
        
        # Obtener todas las imágenes en la carpeta actual
        images = [img for img in os.listdir(clase_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # Mezclar aleatoriamente las imágenes
        random.shuffle(images)
        
        # Calcular los tamaños de cada conjunto
        total_images = len(images)
        train_size = int(total_images * 0.7)
        test_size = int(total_images * 0.2)
        val_size = total_images - train_size - test_size  # El resto va a val
        
        # Distribuir las imágenes
        train_images = images[:train_size]
        test_images = images[train_size:train_size + test_size]
        val_images = images[train_size + test_size:]
        
        # Mover las imágenes a las carpetas correspondientes
        for img in train_images:
            shutil.move(os.path.join(clase_path, img), os.path.join(train_path, img))
        for img in test_images:
            shutil.move(os.path.join(clase_path, img), os.path.join(test_path, img))
        for img in val_images:
            shutil.move(os.path.join(clase_path, img), os.path.join(val_path, img))
        
        print(f"Distribución completada para {clase}:")
        print(f"  Train: {len(train_images)} imágenes")
        print(f"  Test: {len(test_images)} imágenes")
        print(f"  Val: {len(val_images)} imágenes")

print("Proceso de distribución de imágenes completado.")
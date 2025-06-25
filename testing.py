import tensorflow as tf
import cv2
import numpy as np
import pandas as pd
import os

#importo el modelo "modelo_maderas.h5"
model = tf.keras.models.load_model("modelo_maderas.h5")

#defino la ruta hacia donde estan las imagenes que quiero predecir (testear)
path = "/home/martin/repos/datasets/maderas_macro/imagenes chicas/test"

#lista de clases
lista_de_clases = [f"clase_{i+1}" for i in range(41)]

#voy testeando cada imagen por clase y obtengo la predicción obtendia
def predict_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error al leer la imagen: {image_path}")
        return None
    img = cv2.resize(img, (244, 326))  # (ancho, alto)
    img = img.astype('float32') / 255.0  # Normaliza si tu modelo lo requiere
    img = np.expand_dims(img, axis=0)   # Añade dimensión batch
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=1)[0]
    return predicted_class

#itero por la carpeta de test
results = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(root, file)
            predicted_class = predict_image(file_path)
            if predicted_class is not None:
                results.append((file, predicted_class))
                
print("Resultados de las predicciones:")
for file, predicted_class in results:
    print(f"Archivo: {file}, Clase Predicha: {lista_de_clases[predicted_class]}")
        
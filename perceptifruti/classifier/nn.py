import torch
import os
import torch.nn as nn
import numpy as np
import tensorflow as tf
import h5py as h5
import cv2
from django.conf import settings
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from typing import List, Tuple
from .enums import Ripeness

class RipenessClassifier(nn.Module):
    def __init__(self, filename):
        super().__init__()
        if not os.path.exists('perceptifruti/banana_model.h5'):
            self.train_localy()
        
    def train_localy(self):
        datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=30,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )

        real_train_generator = datagen.flow_from_directory(
            settings.BASE_DIR / 'Real Dataset/train',
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical',
            subset='training',
        )

        val_generator = datagen.flow_from_directory(
            settings.BASE_DIR / 'Real Dataset/validation',
            target_size=(224, 224),
            batch_size=32,
            class_mode='categorical',
        )

        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(128, activation='relu'),
            Dense(4, activation='softmax')
        ])

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        model.summary()

        epochs=22
        history = model.fit(real_train_generator, epochs=epochs, validation_data=val_generator)

        test_loss, test_acc = model.evaluate(val_generator, verbose=2)
        print(f'\mTest accuracy: {test_acc:.4f}')

        model.save('perceptifruti/banana_model.h5')

    def forward(self, x):
        return self.fx(x)
    
    def load_pretrained_model(self):
        return tf.keras.models.load_model('perceptifruti/banana_model.h5')
    
    def classify_image(
            self,
        image_path: str = None,
        image_array: np.ndarray = None,
        target_size: Tuple[int, int] = (224, 224),
        class_labels: List[str] =['A', 'B', 'C', 'D']
    ) -> str:
        image_array = tf.image.resize(image_array, (224, 224)).numpy()
        # Se houver mais de 3 canais, usa apenas os 3 primeiros
        if image_array.shape[-1] > 3:
            image_array = image_array[..., :3]
        # Normaliza e adiciona dimensão extra para batch
        image_array = image_array
        image_array = np.expand_dims(image_array, axis=0)
        #---------------------------------------------------------------------
        prediction = self.load_pretrained_model().predict(image_array)
        predicted_class = np.argmax(prediction)
        print(f'Predicted Class: {class_labels[predicted_class]}')

        return class_labels[predicted_class]

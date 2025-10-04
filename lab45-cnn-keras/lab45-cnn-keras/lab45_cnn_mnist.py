#!/usr/bin/env python3
"""
Lab 45: Introduction to Convolutional Neural Networks using Keras
Headless version for Cloud VM (saves plots instead of displaying).
"""
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("--- Task 2: Build a Basic CNN Model ---")

# Load and preprocess MNIST data
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))
print("✅ Data normalized and reshaped successfully. Train shape:", train_images.shape, "Test shape:", test_images.shape)

# Define CNN architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
print("✅ CNN model architecture defined successfully:")
model.summary()

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("✅ Model compiled successfully.")

# Train the model
print("--- Task 3: Training the Model ---")
history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels), verbose=2)

# Evaluate model
print("--- Task 4: Evaluating Classification Results ---")
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"✅ Test Accuracy: {test_acc:.4f}, Test Loss: {test_loss:.4f}")

# Plot training vs validation accuracy/loss (headless)
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig('screenshots/cnn_training_curves.png')
plt.close()
print("✅ Training curve plot saved successfully at: screenshots/cnn_training_curves.png")

print("\n--- Lab 45 Completed Successfully ---")
print("🎯 Built, trained, and evaluated a CNN on MNIST using Keras (headless mode).")
print("🧠 Figures automatically saved to screenshots folder.")

# lab44_visualize_training_history.py
# Lab 44: Visualizing Neural Network Training History

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

print("\n--- Task 1: Create and Compile the Model ---")
model = Sequential([
    Dense(16, input_dim=8, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
print("✅ Model compiled successfully.")

print("\n--- Task 2: Generate and Split the Dataset ---")
X = np.random.rand(200, 8)
y = np.random.randint(2, size=(200, 1))
X_train, X_val = X[:150], X[150:]
y_train, y_val = y[:150], y[150:]
print("✅ Dataset generated and split into 150 training and 50 validation samples.")

print("\n--- Task 3: Train the Model and Capture History ---")
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=10, verbose=0)
print("✅ Model training completed successfully.")

print("\n--- Task 4: Visualize Training History ---")
# Plot loss curves
plt.figure()
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('figure2.png')
plt.close()

# Plot accuracy curves
plt.figure()
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('training_validation_accuracy.png')
plt.close()

print("✅ Plots saved as figure2.png and training_validation_accuracy.png.")
print("\n--- Lab 44 Completed Successfully ---")
print("🎯 You visualized training and validation metrics using Matplotlib.")

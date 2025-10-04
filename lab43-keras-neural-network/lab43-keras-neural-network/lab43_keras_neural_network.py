#!/usr/bin/env python3
# Lab 43: Working with Neural Networks using Keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

print("\n--- Task 1: Build a Simple Sequential Model in Keras ---")
print("✅ Libraries imported successfully.\n")

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print("✅ Model architecture defined successfully:")
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print("✅ Model compiled successfully.\n")

print("--- Task 2: Train the Model on a Small Dataset ---")
X = np.random.rand(100, 8)
Y = np.random.randint(2, size=(100, 1))
print("✅ Dataset generated successfully: 100 samples, 8 features.\n")

model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
print("✅ Model training completed successfully.\n")

print("--- Task 3: Evaluate Training and Test Performance ---")
loss, accuracy = model.evaluate(X, Y, verbose=0)
print(f"Training Loss: {loss:.4f}, Training Accuracy: {accuracy:.4f}\n")

X_test = np.random.rand(20, 8)
Y_test = np.random.randint(2, size=(20, 1))
test_loss, test_accuracy = model.evaluate(X_test, Y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}\n")

print("--- Lab 43 Completed Successfully ---")
print("🎯 You have built, trained, and evaluated a neural network using Keras.")
print("📊 Model summary, training/test performance metrics displayed successfully.")
print("🧠 This lab forms the foundation for building more complex neural network architectures.\n")

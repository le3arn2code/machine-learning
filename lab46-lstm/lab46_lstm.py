#!/usr/bin/env python3
# ============================================================
# Lab 47: Implementing a Long Short-Term Memory (LSTM) Network
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam

# ---- Task 1: Build LSTM Model ----
model = Sequential()
model.add(LSTM(units=50, activation='tanh', input_shape=(5, 1)))
model.add(Dense(units=1))

model.compile(optimizer=Adam(learning_rate=0.01), loss='mean_squared_error')

# ---- Task 2: Generate Sequential Data ----
X_train = np.array([[[i+j] for i in range(5)] for j in range(1000)], dtype=float)
y_train = np.array([[i+5] for i in range(1000)], dtype=float)

# ---- Task 3: Train Model ----
history = model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)

plt.figure()
plt.plot(history.history['loss'])
plt.title('LSTM Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.tight_layout()
plt.savefig('screenshots/lab47_training_loss.png')
plt.close()

# ---- Evaluate Model ----
X_test = np.array([[[i+j] for i in range(5)] for j in range(100, 110)], dtype=float)
y_test = np.array([[i+5] for i in range(100, 110)], dtype=float)
loss = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {loss:.4f}")

y_pred = model.predict(X_test, verbose=0)
print("Predictions:", y_pred.flatten())

plt.figure()
plt.plot(y_test, label='True', marker='o')
plt.plot(y_pred, label='Predicted', marker='x')
plt.title('LSTM Sequence Prediction')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.savefig('screenshots/lab47_predictions.png')
plt.close()

print("✅ Training complete. All plots saved in /screenshots directory.")

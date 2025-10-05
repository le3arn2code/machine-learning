# Lab 46: Implementing a Long Short-Term Memory (LSTM) Network

## 🎯 Objectives
- Understand the limitations of simple RNNs and how LSTMs overcome them.
- Implement an LSTM using Keras.
- Train the model on sequential data.
- Evaluate predictions visually and numerically.

## 🧠 Prerequisites
- Knowledge of RNNs, sequences, and vanishing gradient problem.
- Python 3 with TensorFlow/Keras, NumPy, and Matplotlib installed.

## ⚙️ Tasks
### Task 1: Build an LSTM Model
Initialize an LSTM network using Keras with 50 units and one Dense output layer.

### Task 2: Train the Model
Generate simple sequential data, compile using Adam optimizer, and train for 100 epochs.

### Task 3: Evaluate and Predict
Evaluate the model on test data, visualize loss and predictions (headless mode).

## 📊 Results
All figures are saved automatically to the `/screenshots/` directory:
- `lab46_training_loss.png`
- `lab46_predictions.png`

## 🏁 Conclusion
This lab demonstrates how LSTMs outperform simple RNNs for sequence learning, capturing both short- and long-term dependencies.

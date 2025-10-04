# Interview Q&A: Neural Network Training Visualization

**1. What does the training loss curve represent?**
It shows how well the model fits the training data over epochs.

**2. What does the validation loss curve indicate?**
It reflects model performance on unseen data — a key for detecting overfitting.

**3. Why does validation loss increase while training loss decreases?**
This is a sign of overfitting — the model memorizes training data but fails to generalize.

**4. What does the accuracy curve help with?**
It helps visualize how well the model predicts labels correctly over time.

**5. How can you identify underfitting from these plots?**
Both training and validation losses remain high and accuracy low across epochs.

**6. What does ‘early stopping’ do in training visualization?**
It halts training when validation loss stops improving to prevent overfitting.

**7. Why is `model.fit()` history useful?**
It returns the `history` object that stores all metrics per epoch for visualization.

**8. What’s the difference between batch size and epoch?**
Batch size defines samples per update; epoch defines full dataset passes.

**9. How can visualization help in tuning model performance?**
By spotting when loss diverges or plateaus, one can adjust learning rates or layers.

**10. How do you handle noisy accuracy curves?**
Use moving averages or more data to stabilize curve fluctuations.

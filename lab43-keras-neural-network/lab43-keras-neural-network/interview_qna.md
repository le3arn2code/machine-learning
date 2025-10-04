# Interview Q&A — Neural Networks with Keras

**Q1:** What is the difference between `Sequential` and `Functional` API in Keras?  
**A1:** Sequential builds models layer-by-layer; Functional API allows complex architectures with branching and shared layers.

**Q2:** Why do we use ReLU activation in hidden layers?  
**A2:** ReLU helps mitigate vanishing gradients and accelerates training convergence.

**Q3:** Why is `sigmoid` used in the output layer for binary classification?  
**A3:** Sigmoid maps outputs between 0 and 1, ideal for predicting probabilities of binary outcomes.

**Q4:** What does the optimizer `Adam` do?  
**A4:** Adam combines momentum and adaptive learning rates, providing fast convergence with low memory requirements.

**Q5:** How do you prevent overfitting in a neural network?  
**A5:** Use dropout layers, early stopping, and more training data to improve generalization.

**Q6:** What’s the difference between `binary_crossentropy` and `categorical_crossentropy`?  
**A6:** Binary is used for two-class problems, while categorical handles multi-class classification.

**Q7:** What’s the role of epochs and batch size?  
**A7:** Epochs are full dataset passes; batch size determines how many samples are processed before weight updates.

**Q8:** Why should data be normalized before feeding to neural networks?  
**A8:** Normalization ensures stable gradients and faster convergence during backpropagation.

**Q9:** Can you explain model evaluation metrics like accuracy, loss, and F1-score?  
**A9:** Accuracy measures correct predictions; loss reflects model error; F1-score balances precision and recall.

**Q10:** What’s the difference between training and validation accuracy?  
**A10:** Training accuracy shows performance on known data; validation accuracy evaluates generalization on unseen data.

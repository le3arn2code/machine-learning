# Interview Q&A - Lab 46 (LSTM Networks)

1. **What problem does an LSTM solve compared to a simple RNN?**
   LSTMs overcome the vanishing gradient problem, enabling learning of long-term dependencies.

2. **What are the main components of an LSTM cell?**
   Input gate, forget gate, output gate, and cell state.

3. **Why is 'tanh' used in LSTMs?**
   It helps keep values in a manageable range and stabilizes training.

4. **How is the 'forget gate' important?**
   It decides which past information should be discarded or retained.

5. **What optimizer is commonly used for training LSTMs?**
   Adam optimizer is popular for its adaptive learning rate.

6. **What kind of data is suitable for LSTM models?**
   Time-series, text sequences, stock prices, or any temporal data.

7. **How can overfitting be reduced in LSTM models?**
   By using dropout layers, reducing complexity, or early stopping.

8. **What is the role of 'input_shape' in Keras?**
   It defines the format of the input sequence for the model.

9. **How do you visualize model performance headlessly?**
   Use `plt.savefig()` and `plt.close()` to generate plots without a GUI.

10. **Can LSTMs be stacked?**
    Yes, multiple LSTM layers can be stacked to learn hierarchical sequence features.

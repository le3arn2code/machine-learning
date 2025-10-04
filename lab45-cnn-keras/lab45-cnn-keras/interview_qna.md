# Interview Q&A: CNNs in Keras

**Q1:** What is a Convolutional Neural Network (CNN)?  
**A1:** A CNN is a type of neural network specialized in processing data with grid-like topology, such as images.

**Q2:** What is the purpose of a Conv2D layer?  
**A2:** It extracts spatial features by applying convolutional filters over the input image.

**Q3:** Why do we use pooling layers?  
**A3:** Pooling reduces spatial dimensions and helps control overfitting by summarizing feature maps.

**Q4:** What is the role of the Flatten layer?  
**A4:** It converts multidimensional feature maps into a 1D vector for the dense layer.

**Q5:** Why is ‘ReLU’ activation widely used in CNNs?  
**A5:** ReLU introduces non-linearity while avoiding vanishing gradient issues.

**Q6:** What does 'softmax' do in the output layer?  
**A6:** It converts logits into probabilities summing to 1 for classification tasks.

**Q7:** What is the advantage of using the Adam optimizer?  
**A7:** Adam combines momentum and adaptive learning rate techniques for faster convergence.

**Q8:** Why do we normalize input images?  
**A8:** It helps the model converge faster by ensuring feature values are in a consistent range.

**Q9:** How can you prevent overfitting in CNNs?  
**A9:** Techniques include dropout, data augmentation, early stopping, and regularization.

**Q10:** What accuracy is expected on MNIST with a simple CNN?  
**A10:** Typically above 98% after 5 epochs with basic architecture.

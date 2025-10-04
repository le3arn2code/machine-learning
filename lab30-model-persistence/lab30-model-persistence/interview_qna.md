# Interview Q&A - Lab 30

1. What is model persistence?
   - The process of saving trained ML models for reuse without retraining.

2. Which library is best for scikit-learn model persistence?
   - Joblib, optimized for large NumPy arrays.

3. What file format is used for saved models?
   - Typically `.pkl` or `.joblib`.

4. How do you save a model with Joblib?
   - `joblib.dump(model, 'model.pkl')`

5. How do you load a model with Joblib?
   - `model = joblib.load('model.pkl')`

6. Why use persistence in production?
   - To avoid retraining every time the service restarts.

7. Can Joblib save large models efficiently?
   - Yes, it’s designed for high-performance I/O with NumPy.

8. What is the key advantage over pickle?
   - Joblib handles array data faster and uses less memory.

9. What happens if the environment differs between save and load?
   - Compatibility issues may occur; use the same scikit-learn version.

10. What is a real-world use case?
    - Deploying pre-trained models in web APIs or ML pipelines.

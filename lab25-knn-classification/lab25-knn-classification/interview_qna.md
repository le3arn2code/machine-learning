# Interview Q&A – Lab 25: Implementing k-Nearest Neighbors for Classification

1️⃣ **What is the main idea behind k-NN?**  
k-NN classifies data points based on the majority label of their k closest neighbors using distance metrics.

2️⃣ **Why is k-NN a lazy learner?**  
It performs no model training; predictions are made directly from stored training data.

3️⃣ **How do you choose the optimal k?**  
By cross-validation. Smaller k increases variance; larger k increases bias.

4️⃣ **What are common distance metrics?**  
Euclidean, Manhattan, Minkowski, Hamming, and Cosine.

5️⃣ **Why is feature scaling important for k-NN?**  
Because distance-based algorithms are sensitive to the range of features.

6️⃣ **How does k-NN handle multi-class classification?**  
It assigns the label based on the majority class among the nearest neighbors.

7️⃣ **Advantages of k-NN:**  
Simple, no training phase, and effective on small datasets.

8️⃣ **Disadvantages of k-NN:**  
Slow prediction, sensitive to irrelevant features, and poor performance with large/high-dimensional data.

9️⃣ **Real-world applications:**  
Recommender systems, medical diagnosis, anomaly detection, and text classification.

🔟 **Optimizations for production:**  
Use KD-Trees, Ball Trees, or Approximate Nearest Neighbors (e.g., FAISS) to improve performance.

# Interview Q&A - Lab 48 (Text Vectorization)

1. **What is text vectorization?**
   Transforming text into numeric form for ML models.

2. **What does CountVectorizer do?**
   Creates a matrix of word counts from documents.

3. **What is TF-IDF used for?**
   Assigns importance to words relative to corpus frequency.

4. **Why prefer TF-IDF over raw counts?**
   It reduces weight of common words, improving signal quality.

5. **What does TF stand for?**
   Term Frequency — how often a word appears in a document.

6. **What does IDF stand for?**
   Inverse Document Frequency — reduces importance of common words.

7. **Which library provides both CountVectorizer and TF-IDF?**
   scikit-learn (`sklearn.feature_extraction.text`).

8. **What is the output of CountVectorizer?**
   A sparse matrix of word frequencies.

9. **What is normalization in TF-IDF?**
   Adjusting word weights to a scale (e.g., unit length).

10. **Where is TF-IDF used in real-world systems?**
    Search engines, recommendation systems, and spam detection.

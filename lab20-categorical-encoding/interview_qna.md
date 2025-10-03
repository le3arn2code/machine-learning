# Interview Q&A - Lab 20

**Q1: Why do we need to encode categorical variables?**
A1: Machine learning models require numerical inputs. Encoding converts text categories into numeric form so they can be used in model training.

**Q2: Difference between Label Encoding and One-Hot Encoding?**
A2: Label Encoding assigns integer values (0,1,2...) to categories, which can imply ordinal relationships. One-Hot Encoding creates binary columns, avoiding unintended ordinal interpretation.

**Q3: Why use Pipelines in scikit-learn?**
A3: Pipelines streamline preprocessing and modeling into a single workflow, reducing errors and improving reproducibility.

**Q4: When should you use One-Hot Encoding vs Label Encoding?**
A4: Use Label Encoding when categories are ordinal (e.g., small/medium/large). Use One-Hot Encoding when categories are nominal (e.g., apple, banana, cherry).

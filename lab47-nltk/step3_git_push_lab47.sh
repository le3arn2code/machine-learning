#!/bin/bash
# ============================================================
# Step 3: Git Automation Script for Lab 47 - NLP Basics with NLTK
# ============================================================

# Step 1: Remove old copy
rm -rf lab47-nltk

# Step 2: Unzip fresh copy
unzip ../lab47-nltk.zip -d lab47-nltk

# Step 3: Verify structure
ls -l lab47-nltk

# Step 4: Stage
git add lab47-nltk

# Step 5: Commit
git commit -m "Added Lab 47: Natural Language Processing Basics with NLTK"

# Step 6: Tag and push
git tag -d lab47 2>/dev/null
git tag lab47
git push origin main
git push origin lab47

echo "✅ Lab 47 successfully pushed and tagged as lab47."

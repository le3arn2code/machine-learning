# Step 1: Make the script executable
chmod +x lab37_custom_transformer.py

# Step 2: Run the lab
python3 lab37_custom_transformer.py

# Step 3: Git Push Script
git add lab37-custom-transformer/
git commit -m "Added Lab 37: Custom Transformer in scikit-learn"
git tag -d lab37 2>/dev/null
git tag lab37
git push origin main
git push origin lab37

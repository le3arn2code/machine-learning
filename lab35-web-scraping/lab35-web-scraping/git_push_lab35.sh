# Step 3: Git Push Script for Lab 35
rm -rf lab35-web-scraping
unzip ../lab35-web-scraping.zip -d lab35-web-scraping

git add lab35-web-scraping
git commit -m "Added Lab 35: Web Scraping for ML Data"
git tag -d lab35 2>/dev/null
git tag lab35
git push origin main
git push origin lab35

name: Daily Price Update

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0   # Full history laayega
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install requests beautifulsoup4

      - name: Configure Git
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"

      - name: Pull latest changes
        run: |
          git pull origin main --rebase || git pull origin main

      - name: Run Scraper
        run: python scraper.py

      - name: Commit and Push changes
        run: |
          # Check if there are any changes
          if [ -n "$(git status --porcelain)" ]; then
            git add products.json
            git commit -m "Auto-update: Latest prices fetched" || exit 0
            
            # Fetch and merge latest changes before pushing
            git fetch origin main
            
            # Try rebase first, if it fails use merge
            if ! git rebase origin/main; then
              echo "Rebase failed, using merge strategy..."
              git rebase --abort 2>/dev/null || true
              git merge origin/main -m "Merge remote changes" || {
                # If merge fails, reset and re-scrape with latest data
                echo "Merge conflict detected, resetting and re-scraping..."
                git merge --abort 2>/dev/null || true
                git reset --hard origin/main
                python scraper.py
                git add products.json
                git commit -m "Auto-update: Latest prices fetched"
              }
            fi
            
            # Push the changes
            git push origin main
          else
            echo "No changes to commit"
          fi

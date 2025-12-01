#!/bin/bash
set -e

echo "Committing and pushing to main"
git add .
git commit -m "updates"
git push origin master

echo "Deployment complete. Pushed to main."
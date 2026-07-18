# Google Cloud Run Deployment Configuration
gcloud config set project tidy-node-494313-j1

# Build and deploy
gcloud run deploy foodguide-ai-meal-planner \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 512Mi \
  --cpu 1 \
  --timeout 3600 \
  --set-env-vars FLASK_ENV=production

#!/bin/bash

# FoodGuide AI - Google Cloud Run Deployment Script
# Prerequisites: gcloud CLI installed, project billing enabled, user authenticated

set -e

PROJECT_ID="tidy-node-494313-j1"
SERVICE_NAME="foodguide-ai-meal-planner"
REGION="us-central1"

echo "🚀 Starting deployment to Google Cloud Run..."
echo "Project: $PROJECT_ID"
echo "Service: $SERVICE_NAME"
echo "Region: $REGION"

# Set project
echo "📋 Setting Google Cloud project..."
gcloud config set project $PROJECT_ID

# Enable APIs
echo "🔧 Enabling required APIs..."
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com containerregistry.googleapis.com

# Deploy to Cloud Run
echo "🐳 Deploying to Google Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --source . \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --port 8080 \
  --memory 512Mi \
  --cpu 1 \
  --timeout 3600 \
  --set-env-vars FLASK_ENV=production \
  --min-instances 0 \
  --max-instances 100

# Get the service URL
echo ""
echo "✅ Deployment successful!"
echo ""
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)')
echo "🌐 Service URL: $SERVICE_URL"
echo ""
echo "📊 View logs:"
echo "   gcloud run logs read $SERVICE_NAME --limit 50"
echo ""
echo "🔍 View metrics:"
echo "   Visit: https://console.cloud.google.com/run/detail/$REGION/$SERVICE_NAME"

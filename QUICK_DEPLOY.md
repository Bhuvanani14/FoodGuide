# 📋 Quick Deployment Checklist

## ✅ Pre-Deployment

- [x] Code pushed to GitHub: https://github.com/Bhuvanani14/FoodGuide.git
- [x] Dockerfile created and tested
- [x] requirements.txt updated with production dependencies (gunicorn)
- [x] run.py updated for PORT environment variable support
- [ ] **Enable billing** on Google Cloud Project `tidy-node-494313-j1`
- [ ] Authenticate with: `gcloud auth login`

## 🚀 Deployment Steps

### Step 1: Enable Billing (One-time)
1. Go to https://console.cloud.google.com
2. Select project: `tidy-node-494313-j1`
3. Click **Billing** in left menu
4. Click **Link Billing Account**
5. Complete billing setup
6. ⏰ Wait 2-3 minutes for billing to activate

### Step 2: Deploy to Cloud Run
```bash
# From project directory
chmod +x deploy-cloud-run.sh
./deploy-cloud-run.sh

# Or manually
gcloud config set project tidy-node-494313-j1
gcloud run deploy foodguide-ai-meal-planner \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 512Mi
```

### Step 3: Get Service URL
```bash
gcloud run services describe foodguide-ai-meal-planner \
  --platform managed --region us-central1 \
  --format 'value(status.url)'
```

### Step 4: Test the Service
```bash
# Replace URL with your service URL
curl https://foodguide-ai-meal-planner-XXXXX.run.app/health
```

## 📍 Expected Deployment URLs

After deployment, your service will be available at:
```
https://foodguide-ai-meal-planner-[random].run.app
```

Example testing:
```bash
# Health check
curl https://foodguide-ai-meal-planner-abc123.run.app/health

# Generate meal plan
curl -X POST https://foodguide-ai-meal-planner-abc123.run.app/api/generate-meal-plan \
  -H "Content-Type: application/json" \
  -d '{"budget": 50, "servings": 2, "dietary_preferences": "none", "cooking_time": "quick"}'
```

## 📊 Monitoring

```bash
# View logs
gcloud run logs read foodguide-ai-meal-planner --limit 50

# View in Cloud Console
# https://console.cloud.google.com/run/detail/us-central1/foodguide-ai-meal-planner
```

## 🔄 Redeploy (Updates)

When you push updates to GitHub:
```bash
# Method 1: From local machine
gcloud run deploy foodguide-ai-meal-planner --source .

# Method 2: Using Cloud Build from GitHub
# (Set up one-time in Cloud Console)
```

## 💰 Cost Tracking

Monitor costs at:
https://console.cloud.google.com/billing/account-selector

## 🎯 Next Steps

1. **Enable billing** first
2. **Run deployment script**
3. **Note the service URL**
4. **Share with users**
5. **Monitor in Cloud Console**

---

**Status**: Ready for Deployment (Pending Billing Activation)
**Repository**: https://github.com/Bhuvanani14/FoodGuide
**Project**: tidy-node-494313-j1

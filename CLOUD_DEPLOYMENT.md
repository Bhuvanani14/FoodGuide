# 🚀 Google Cloud Run Deployment Guide for FoodGuide AI

## ⚠️ Prerequisites Check

Before deploying, ensure:
- [ ] Google Cloud Account created
- [ ] Project created: `tidy-node-494313-j1`
- [ ] **Billing ENABLED** on the project (Required for Cloud Run)
- [ ] Google Cloud SDK (`gcloud`) installed locally
- [ ] Authenticated with: `gcloud auth login`
- [ ] Git repository pushed to: https://github.com/Bhuvanani14/FoodGuide.git

## 💳 Enable Billing

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Select project: `tidy-node-494313-j1`
3. Navigate to **Billing** → **Link Billing Account**
4. Follow the setup wizard
5. **This is required** for Cloud Run deployment

## 📦 Deployment Methods

### Method 1: Automatic Deployment (Recommended)

```bash
# From project root directory
chmod +x deploy-cloud-run.sh
./deploy-cloud-run.sh
```

This script will:
- Set the project
- Enable required APIs
- Build Docker image via Cloud Build
- Deploy to Cloud Run
- Return your service URL

### Method 2: Manual Deployment (Step-by-step)

```bash
# 1. Set the project
gcloud config set project tidy-node-494313-j1

# 2. Enable required APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

# 3. Deploy to Cloud Run
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

# 4. Note the service URL from output
```

### Method 3: GitHub Integration (CI/CD)

```bash
# Deploy from GitHub repository directly
gcloud run deploy foodguide-ai-meal-planner \
  --source https://github.com/Bhuvanani14/FoodGuide.git \
  --source-dir . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```

## 🔍 Post-Deployment Verification

### Get Service URL
```bash
gcloud run services describe foodguide-ai-meal-planner \
  --platform managed \
  --region us-central1 \
  --format 'value(status.url)'
```

### Test the Service
```bash
SERVICE_URL=$(gcloud run services describe foodguide-ai-meal-planner \
  --platform managed --region us-central1 --format 'value(status.url)')

# Test health endpoint
curl $SERVICE_URL/health

# Test meal generation
curl -X POST $SERVICE_URL/api/generate-meal-plan \
  -H "Content-Type: application/json" \
  -d '{
    "budget": 50,
    "servings": 2,
    "dietary_preferences": "none",
    "cooking_time": "quick"
  }'
```

### View Logs
```bash
# Last 50 lines
gcloud run logs read foodguide-ai-meal-planner --limit 50

# Real-time logs
gcloud run logs read foodguide-ai-meal-planner --follow

# With filtering
gcloud run logs read foodguide-ai-meal-planner --limit 100 | grep "ERROR"
```

## 📊 Cloud Run Configuration Details

| Configuration | Value | Reason |
|---------------|-------|--------|
| **Platform** | Managed | No infrastructure to manage |
| **Region** | us-central1 | Best latency & cost coverage |
| **Memory** | 512Mi | Sufficient for Flask app |
| **CPU** | 1 | Standard allocation |
| **Timeout** | 3600s | 1 hour max request time |
| **Min Instances** | 0 | Cost optimization (no idle compute) |
| **Max Instances** | 100 | Auto-scaling capability |
| **Port** | 8080 | Cloud Run default port |

## 🔐 Security & Environment

### Environment Variables
Securely set via `--set-env-vars`:

```bash
gcloud run deploy foodguide-ai-meal-planner \
  --set-env-vars FLASK_ENV=production \
  --set-secrets DATABASE_URL=projects/PROJECT_ID/secrets/db-url/latest
```

### Access Control
- **Public Access**: `--allow-unauthenticated` (current setup)
- **Restricted Access**: Use `--no-allow-unauthenticated` + Cloud IAM

## 💰 Cost Estimation

### Pricing Components
- **Cloud Run Compute**: $0.00001 per CPU-second
- **Build**: First 120 build-minutes/day free
- **Outbound Data**: $0.12 per GB (first 5GB free each month)

### Estimated Monthly Cost
```
Scenario: 100k requests/month, 200ms avg duration, 512Mi memory

Compute Cost:
  100,000 requests × 0.2s × $0.00001/CPU-sec = $0.20

Data Transfer: ~5 GB
  5 GB × $0.12/GB = $0.60

Total Estimated: ~$1-2/month

💡 Tip: Always within free tier for low-traffic apps!
```

## 🐛 Troubleshooting

### Issue: "Billing not enabled"
**Solution**: Enable billing in Google Cloud Console → Billing → Link Account

### Issue: "Permission denied" when deploying
**Solution**: Authenticate again
```bash
gcloud auth login
gcloud auth application-default login
```

### Issue: Service returning 500 error
**Solution**: Check logs
```bash
gcloud run logs read foodguide-ai-meal-planner --limit 50
```

### Issue: High latency on first request
**Solution**: Normal - Cloud Run is cold starting. Set `--min-instances 1` if needed:
```bash
gcloud run update foodguide-ai-meal-planner \
  --min-instances 1 \
  --region us-central1
```

### Issue: Out of memory
**Solution**: Increase memory allocation
```bash
gcloud run update foodguide-ai-meal-planner \
  --memory 1Gi \
  --region us-central1
```

## 📈 Monitoring & Analytics

### Cloud Run Dashboard
https://console.cloud.google.com/run/detail/us-central1/foodguide-ai-meal-planner

**Metrics Available**:
- Request count
- Error rate
- Latency (p50, p95, p99)
- CPU & Memory usage
- Container startup time

### Custom Monitoring
```bash
# View request metrics for last hour
gcloud monitoring time-series list \
  --filter 'resource.type="cloud_run_revision" AND metric.type="run.googleapis.com/request_count"'
```

## 🔄 Continuous Deployment

### Automatic Deployment on Git Push

1. **Create Cloud Build trigger**:
   ```bash
   gcloud builds triggers create github \
     --name=foodguide-deploy \
     --repo-name=FoodGuide \
     --repo-owner=Bhuvanani14 \
     --branch-pattern="^main$"
   ```

2. **Create `cloudbuild.yaml` in repo**:
   ```yaml
   steps:
   - name: 'gcr.io/cloud-builders/gke-deploy'
     args:
     - run
     - --filename=.
     - --image=gcr.io/$PROJECT_ID/foodguide:$COMMIT_SHA
     - --location=us-central1
     - --output=/workspace/output

   - name: 'gcr.io/cloud-builders/run'
     args:
     - deploy
     - foodguide-ai-meal-planner
     - --source=.
     - --region=us-central1
   ```

## ✅ Deployment Checklist

- [ ] Billing enabled on project
- [ ] gcloud CLI installed and authenticated
- [ ] Code pushed to GitHub
- [ ] Dockerfile present in root
- [ ] requirements.txt updated with gunicorn
- [ ] PORT environment variable support (done in run.py)
- [ ] Ran `gcloud services enable run.googleapis.com`
- [ ] Executed deployment script or manual commands
- [ ] Verified service is running
- [ ] Tested API endpoints
- [ ] Noted service URL
- [ ] Set up monitoring/logging

## 🎯 Next Steps

1. **Enable billing** if not already done
2. **Run deployment script**: `./deploy-cloud-run.sh`
3. **Test the service** with provided curl commands
4. **Monitor performance** in Cloud Console
5. **Share the service URL** with users
6. **Set up CI/CD** for automatic deployments

## 📚 Additional Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Deploying Python Apps to Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
- [Cloud Run Pricing](https://cloud.google.com/run/pricing)
- [gcloud run deploy Reference](https://cloud.google.com/sdk/gcloud/reference/run/deploy)

---

**Deploy Status**: Ready (pending billing activation)
**Service Name**: foodguide-ai-meal-planner
**Region**: us-central1
**Repository**: https://github.com/Bhuvanani14/FoodGuide.git

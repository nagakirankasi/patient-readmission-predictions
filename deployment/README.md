# Deployment Guide: Predicting Patient Readmissions

## **1. Overview**
This guide provides step-by-step instructions to deploy the **Predicting Patient Readmissions** solution on **AWS** using a **serverless architecture** with **AWS SageMaker, Lambda, API Gateway, and S3**.

## **2. Prerequisites**
Before deploying, ensure the following are set up:
- AWS account
- AWS CLI installed & configured (`aws configure`)
- Python 3.8+
- Docker (for API containerization)
- Terraform (optional, for infrastructure automation)

## **3. Deployment Steps**

### **Step 1: Upload Data to Amazon S3**
Create an S3 bucket and upload preprocessed datasets:
```bash
aws s3 mb s3://patient-readmission-data
aws s3 cp data/processed/train.csv s3://patient-readmission-data/
aws s3 cp data/processed/test.csv s3://patient-readmission-data/
```

### **Step 2: Train & Deploy ML Model using AWS SageMaker**
#### **2.1 Train Model on SageMaker**
Create a SageMaker training job using the script `sagemaker/train_model.py`:
```python
import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn

sagemaker_session = sagemaker.Session()
sklearn_estimator = SKLearn(
    entry_point="model_training.py",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session
)
sklearn_estimator.fit({"train": "s3://patient-readmission-data/train.csv"})
```

#### **2.2 Deploy the Model as an Endpoint**
```python
predictor = sklearn_estimator.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1
)
print("Model deployed at:", predictor.endpoint_name)
```

### **Step 3: API Deployment using AWS Lambda & API Gateway**
#### **3.1 Package API Code**
Modify `api/app.py`:
```python
from fastapi import FastAPI
import joblib
import boto3

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([data["features"]])
    return {"prediction": int(prediction[0])}
```
Zip the API code:
```bash
zip -r api_lambda.zip api/
```

#### **3.2 Deploy API to AWS Lambda**
```bash
aws lambda create-function \
    --function-name PredictReadmission \
    --runtime python3.8 \
    --role arn:aws:iam::123456789012:role/LambdaExecutionRole \
    --handler api.app.lambda_handler \
    --timeout 15 \
    --memory-size 512 \
    --zip-file fileb://api_lambda.zip
```

#### **3.3 Create API Gateway**
```bash
aws apigateway create-rest-api --name "PatientReadmissionAPI"
```

#### **3.4 Link API Gateway to Lambda**
```bash
aws apigateway put-integration \
    --rest-api-id API_ID \
    --resource-id RESOURCE_ID \
    --http-method POST \
    --integration-http-method POST \
    --type AWS_PROXY \
    --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/PredictReadmission/invocations
```

#### **3.5 Deploy API**
```bash
aws apigateway create-deployment --rest-api-id API_ID --stage-name prod
```
Test API:
```bash
curl -X POST "https://API_ID.execute-api.us-east-1.amazonaws.com/prod/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1, 0, 30, 1, 0.5, 2, 1]}'
```

### **Step 4: Automate Deployment with Terraform (Optional)**
Create `terraform/main.tf`:
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "patient-readmission-data"
}

resource "aws_lambda_function" "predict_lambda" {
  function_name    = "PredictReadmission"
  role            = "arn:aws:iam::123456789012:role/LambdaExecutionRole"
  handler         = "api.app.lambda_handler"
  runtime         = "python3.8"
  filename        = "api_lambda.zip"
}
```
Deploy infrastructure:
```bash
terraform init
terraform apply -auto-approve
```

### **Step 5: CI/CD Automation using GitHub Actions**
Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to AWS

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Deploy to AWS Lambda
        run: |
          zip -r api_lambda.zip api/
          aws lambda update-function-code \
            --function-name PredictReadmission \
            --zip-file fileb://api_lambda.zip
```

### **Step 6: Monitor & Scale Infrastructure**
- **Monitor Model Performance:** Use **Amazon CloudWatch** to track model drift.
- **Enable Auto-Scaling:** Adjust **SageMaker instance types** based on demand.
- **API Scaling:** Configure **API Gateway throttling** to handle large traffic.

---

## **6. Conclusion**
By following this guide, you will have a fully functional **Predictive Readmission API** running on **AWS SageMaker, Lambda, and API Gateway**. The **serverless approach** ensures cost-effectiveness while maintaining **scalability and security**.

For further enhancements, consider implementing **MLOps pipelines** for model retraining and continuous monitoring.

### 📢 **Next Steps**
✅ Integrate API with hospital EHR systems  
✅ Deploy a front-end dashboard for visualization  
✅ Implement an alert system for high-risk patients

---
**Prepared by:**  
*Naga-Kiran Kasi*  




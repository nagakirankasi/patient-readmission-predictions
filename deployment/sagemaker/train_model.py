import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Define SKLearn estimator
sklearn_estimator = SKLearn(
    entry_point="model_training.py",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=sagemaker_session
)

# Train the model
sklearn_estimator.fit({"train": "s3://my-readmissions-bucket/train_data.csv"})

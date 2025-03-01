
# Project Report: Predicting Patient Readmissions

## **1. Introduction**
### **1.1 Project Overview**
The **Predicting Patient Readmissions** project leverages machine learning to identify patients at high risk of hospital readmission within 30 days of discharge. The goal is to assist healthcare providers and insurance companies in reducing readmissions through early interventions, improved discharge planning, and optimized resource allocation.

### **1.2 Objectives**
- Develop a predictive model for patient readmission risk.
- Reduce hospital readmissions and associated costs.
- Improve patient outcomes through targeted interventions.
- Provide a scalable and cost-effective deployment strategy using cloud technologies.

## **2. Problem Definition**
### **2.1 Challenges of Patient Readmissions**
- **Financial Burden:** Readmissions contribute significantly to healthcare costs, exceeding **$26 billion annually** in the U.S.
- **Regulatory Penalties:** Hospitals with high readmission rates face penalties under **CMS HRRP (Hospital Readmission Reduction Program).**
- **Resource Strain:** Increased hospital readmissions place pressure on medical staff and reduce the availability of beds.
- **Gaps in Post-Discharge Care:** Many readmissions result from inadequate follow-up care, poor medication adherence, and social determinants of health.

## **3. Methodology**
### **3.1 Data Collection & Preprocessing**
- **Data Sources:** Open healthcare datasets (e.g., **MIMIC-III, CMS Hospital Data**) and synthetic patient records for privacy compliance.
- **Preprocessing Steps:**
  - Handle missing values and outliers.
  - One-hot encode categorical variables (e.g., diagnosis codes, demographics).
  - Feature engineering (e.g., length of stay, previous admissions, comorbidities).
  - Split data into **training (80%) and testing (20%) sets**.

### **3.2 Model Development**
- **Baseline Models:** Logistic Regression, Decision Trees.
- **Advanced Models:**
  - **Random Forest, XGBoost** – High interpretability, robust results.
  - **Deep Learning (LSTMs, Neural Networks)** – Suitable for sequential patient history.
- **Evaluation Metrics:**
  - **AUC-ROC Score** – Measures model discrimination ability.
  - **Precision-Recall Curve** – Addresses class imbalance.
  - **F1 Score** – Ensures balance between precision and recall.

### **3.3 Model Deployment on AWS**
#### **Infrastructure Components**
- **AWS SageMaker** – Model training and inference.
- **AWS Lambda + API Gateway** – Serverless deployment of the prediction API.
- **Amazon S3** – Storage for preprocessed data and model artifacts.
- **AWS CloudWatch** – Monitoring model performance and data drift.

## **4. Results & Findings**
### **4.1 Model Performance**
| Model | AUC-ROC | Precision | Recall | F1 Score |
|--------|---------|----------|--------|----------|
| Logistic Regression | 0.72 | 0.65 | 0.60 | 0.62 |
| Random Forest | 0.81 | 0.72 | 0.75 | 0.73 |
| XGBoost | **0.85** | **0.78** | **0.79** | **0.78** |
| LSTM | 0.83 | 0.76 | 0.77 | 0.76 |

### **4.2 Key Findings**
- **XGBoost outperformed other models** with the highest AUC-ROC score.
- **Feature Importance:** Previous admissions, length of stay, and chronic conditions were the strongest predictors of readmission.
- **Model deployment on AWS reduced operational costs** by using a serverless architecture.

## **5. Business & Cost Analysis**
### **5.1 Estimated Cost Savings**
- **Reducing readmissions by 15-20%** could lead to **$3.4M - $4.6M in annual savings per hospital**.
- **Projected ROI = 97x** (For every **$1 invested, hospitals save $97**).

### **5.2 Implementation Cost Estimate**
| **Component** | **Estimated Annual Cost** |
|--------------|--------------------------|
| AWS SageMaker Training | $10,000 |
| AWS Lambda + API Gateway | $5,000 |
| Data Storage (S3, RDS) | $3,000 |
| DevOps & MLOps (CI/CD) | $7,000 |
| Integration & Support | $10,000 |
| **Total Investment** | **$35,000** |

## **6. Deployment & Integration Plan**
### **6.1 Phase-Wise Rollout**
| **Phase** | **Key Activities** | **Timeline** |
|----------|--------------------|-------------|
| Phase 1 | Data Collection & Preprocessing | 1 Month |
| Phase 2 | Model Training & Validation | 2 Months |
| Phase 3 | API Deployment on AWS | 1 Month |
| Phase 4 | Integration with Hospital Systems | 2 Months |
| Phase 5 | Model Monitoring & Optimization | Ongoing |

![HL Flow](assets/images/patient_readmission_prediction_HL.png)

### **6.2 CI/CD Integration**
- **GitHub Actions:** Automates deployment of model updates.
- **AWS Step Functions:** Automates batch inference for large datasets.
- **Model Drift Monitoring:** Alerts when model accuracy declines.

## **7. Key Benefits**
### **7.1 For Hospitals**
✅ **Lower Readmission Rates** – Ensures compliance with CMS guidelines.
✅ **Reduced Costs** – Decreases hospital penalties and bed occupancy costs.
✅ **Optimized Resource Allocation** – Reduces unnecessary hospital stays.

### **7.2 For Insurance Companies**
✅ **Lower Claim Payouts** – Fewer readmissions reduce reimbursement claims.
✅ **Better Risk Prediction** – Improves actuarial models for coverage plans.
✅ **Data-Driven Decision Making** – Enhances engagement with high-risk members.

## **8. Risks & Mitigation Strategies**
| **Risk** | **Mitigation Strategy** |
|---------|------------------------|
| **Data Privacy** | Ensure compliance with HIPAA & GDPR. Use de-identified data. |
| **Model Bias** | Perform fairness audits and remove biased features. |
| **System Integration Issues** | Use API-based interoperability with hospital EHR systems. |
| **Adoption Challenges** | Conduct training sessions for healthcare staff. |

## **9. Conclusion & Future Enhancements**
### **9.1 Summary**
The **Predicting Patient Readmissions** project successfully demonstrates how machine learning and cloud computing can be leveraged to improve patient care and reduce healthcare costs. The deployment strategy ensures scalability, cost efficiency, and compliance with industry regulations.

### **9.2 Future Enhancements**
- **Expanding dataset** to include real-world EHR and claims data.
- **Improving interpretability** by integrating SHAP (SHapley Additive exPlanations) for model explainability.
- **Integrating an alert system** to notify healthcare providers of high-risk patients.
- **Enhancing real-time prediction** capabilities with AWS Kinesis or Apache Kafka.

---
### 📢 **Next Steps**
🔹 Deploy a pilot version in selected hospitals.  
🔹 Monitor model performance & fine-tune for specific patient populations.  
🔹 Scale the deployment for broader adoption.  

---

# IDS706_Beibei-Du-Project4
- Create a Microservice that returns a JSON payload and performs a Data Engineering related task
- Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)
- Configure Build Server to Deploy Changes on build (Continuous Delivery)
- Create realistic API (reference here: Data Engineering: Chapter 5 aws chapter for pragmatic ai.)

## Overview
In this project, I am using the `FastAPI` to deploy some data enginerring Tasks. I take a dataset from Kaggle about the fetal health and I want to discover what are the features that will classify/predict the `fetal_health` status and using machine learning to achieve a high accuracy on testing set. I considered the following models: KNN, Random Forest, Logistic regression, XGBoost. In the output that I received, XGBoost performed the best with an accuracy score of 94.13%.
[!alt](https://github.com/nogibjj/IDS706_Beibei-Du-Project4/blob/main/xgboost_confusion%20matrix.png)

## Implementation
- Install the packages in the requirements.txt and set up for FastAPI
- Code for the project and functions to perform the tasks
- Perform Continous Intergration on Github Actions (`main.yml`)
- Deploy Continous Delivery



## How to Use
- Use the command `uvicorn main:app --reload` to run the server

## Reference
https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification

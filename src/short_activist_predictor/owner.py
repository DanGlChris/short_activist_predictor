# ---------------------------------------------------------------
# Project Name: short-activist-report
# Created by: Daglox Kankwanda
# Username: DanGlChris
# Creation Date: October 21, 2023
#
# Copyright: All rights reserved
# ---------------------------------------------------------------
import os
path_topic_model_Data_first_day_predicted_constant_succeed = "/topic_model_Data_first_day_predicted_constant_succeed"
path_topic_model_Data_first_day_predicted_constant_failed = "/topic_model_Data_first_day_predicted_constant_failed"
path_topic_model_Data_first_day_predicted_succeed = "/topic_model_Data_first_day_predicted_succeed"
path_topic_model_Data_first_day_predicted_failed = "/topic_model_Data_first_day_predicted_failed"
path_topic_model_Data_first_day_to_month_predicted_constant_succeed = "/topic_model_Data_first_day_to_month_predicted_constant_succeed"
path_topic_model_Data_first_day_to_month_predicted_constant_failed = "/topic_model_Data_first_day_to_month_predicted_constant_failed"
path_topic_model_Data_first_day_to_week_predicted_constant_succeed = "/topic_model_Data_first_day_to_week_predicted_constant_succeed"
path_topic_model_Data_first_day_to_week_predicted_constant_failed = "/topic_model_Data_first_day_to_week_predicted_constant_failed"
path_topic_model_Data_first_week_predicted_succeed = "/topic_model_Data_first_week_predicted_succeed"
path_topic_model_Data_first_week_predicted_failed = "/topic_model_Data_first_week_predicted_failed"
path_topic_model_Data_first_week_predicted_constant_succeed = "/topic_model_Data_first_week_predicted_constant_succeed"
path_topic_model_Data_first_week_predicted_constant_failed = "/topic_model_Data_first_week_predicted_constant_failed"
path_topic_model_Data_first_week_to_month_predicted_constant_failed = "/topic_model_Data_first_week_to_month_predicted_constant_failed"
path_topic_model_Data_first_week_to_month_predicted_constant_succeed = "/topic_model_Data_first_week_to_month_predicted_constant_succeed"
path_topic_model_Data_first_month_predicted_failed = "/topic_model_Data_first_month_predicted_failed"
path_topic_model_Data_first_month_predicted_succeed = "/topic_model_Data_first_month_predicted_succeed"
path_topic_model_Data_first_month_predicted_constant_failed = "/topic_model_Data_first_month_predicted_constant_failed"
path_topic_model_Data_first_month_predicted_constant_succeed = "/topic_model_Data_first_month_predicted_constant_succeed"

path_on_hugging_face: str = "DanGlChris"
path_data_on_hugging_face: str = "DanGlChris/short-activist-predict-data"

A_ = "Status First Day Low"
B_ = "Status First Day Close"
C_ = "Status First Week"
D_ = "Status First Week Close"
E_ = "Status First Month Max"
F_ = "Status First Month Closed"

Text_entry_token = 'Enter your hugging face token here : '

'''def check_env():
    if 'AZURE_NOTEBOOKS_HOSTING_ENVIRONMENT' in os.environ:
        print("The code is executed in Azure Notebooks.")
    elif 'RUNTIME_ENV_TYPE' in os.environ and os.environ['RUNTIME_ENV_TYPE'] == 'notebook':
        print("The code is executed in IBM Watson Studio.")
    elif 'DATABRICKS_RUNTIME_VERSION' in os.environ:
        print("The code is executed in Databricks.")
    elif 'SHELL' in os.environ and '/home/user/anaconda3/bin/python' in os.environ['SHELL']:
        print("The code is executed in CoCalc.")
    elif 'KAGGLE_KERNEL_RUN_TYPE' in os.environ:
        print("The code is executed in Kaggle Kernels.")
    elif 'DATACAMP_TOKEN' in os.environ:
        print("The code is executed in DataCamp.")
    elif 'DEEPNOTE_PROJECT_ID' in os.environ:
        print("The code is executed in Deepnote.")
    elif 'AI_PLATFORM_NOTEBOOKS_INSTANCE_NAME' in os.environ:
        print("The code is executed in Google Cloud AI Platform Notebooks.")
    elif 'RSTUDIO_SESSION_ID' in os.environ:
        print("The code is executed in RStudio Cloud.")
    elif 'SAGEMATHCLOUD_PROJECT_ID' in os.environ:
        print("The code is executed in SageMathCloud.")
    elif 'TRINKET_PROJECT_ID' in os.environ:
        print("The code is executed in Trinket.")
    elif 'WOLFRAMSCRIPTDIR' in os.environ:
        print("The code is executed in Wolfram Cloud.")
'''


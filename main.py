# filepath: c:\Users\sohai\OneDrive - National University of Sciences & Technology\Desktop\proj\End-to-End-Chest-Cancer-Classification-using-MLflow-DVC\main.py
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:  # ← Fixed indentation
    logger.exception(e)
    raise e
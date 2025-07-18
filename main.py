from dotenv import load_dotenv
load_dotenv()
import os
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/sohjpeg/End-to-End-Chest-Cancer-Classification-using-MLflow-DVC.mlflow"
import mlflow 
import mlflow.keras
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()  
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:  
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"***********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try:
    logger.info(f"***********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"***********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
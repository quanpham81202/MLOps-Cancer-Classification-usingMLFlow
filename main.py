from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTraininigPineline
from cnnClassifier.pipeline.stage_02 import PrepareBaseModelTraininigPineline
from cnnClassifier.pipeline.stage_03 import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = DataIngestionTraininigPineline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    prepare_base_model = PrepareBaseModelTraininigPineline()
    prepare_base_model.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"****************")
    logger.info(f">>> {STAGE_NAME} <<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>> {STAGE_NAME} Completed <<<\n")
    
except Exception as e:
    logger.exception(e)


from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01 import DataIngestionTraininigPineline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = DataIngestionTraininigPineline()
    obj.main()
    logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
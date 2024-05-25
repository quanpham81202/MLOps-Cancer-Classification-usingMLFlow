from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTraininigPineline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepapre_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepapre_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        prepare_base_model = PrepareBaseModelTraininigPineline()
        prepare_base_model.main()
        logger.info(f">>> Stage {STAGE_NAME} completed <<<\n\nx====================x")
    except Exception as e:
        logger.exception(e)
        raise e
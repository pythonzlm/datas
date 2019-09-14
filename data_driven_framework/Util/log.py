#encoding=utf-8
import logging
import logging.config
from ProjectVar.Var import *

logging.config.fileConfig(project_path+"\\Conf\\Logger.conf")
logger = logging.getLogger("example02")

def error(message):
    logger.error(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)
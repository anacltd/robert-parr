import logging
import os.path

from configparser import ConfigParser

config = ConfigParser()
DEFAULT_CONFIG_FILES = []

LOCAL_CONFIG_PATH = "./credentials.conf"

config.read(DEFAULT_CONFIG_FILES + [LOCAL_CONFIG_PATH])

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

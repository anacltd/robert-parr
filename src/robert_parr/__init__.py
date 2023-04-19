import os.path
import logging

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

config = ConfigParser()
DEFAULT_CONFIG_FILES = []

LOCAL_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.realpath(__file__)
    ))),
    "credentials.conf"
)

config.read(DEFAULT_CONFIG_FILES + [LOCAL_CONFIG_PATH])

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

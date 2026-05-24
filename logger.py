import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)s]: %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S"
)

logger = logging.getLogger("CapyUtilities")
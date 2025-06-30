import logging
import time
import random
from typing import Callable, TypeVar
# Set up structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

T = TypeVar("T")



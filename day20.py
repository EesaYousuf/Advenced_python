import logging
import time
import random
from typing import Callable, TypeVar
# Set up structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

T = TypeVar("T")
# Custom exceptions
class APIError(Exception):
    """Raised when the API call fails"""
    pass

class NetworkError(APIError):
    """Specific network-related failure"""
    pass




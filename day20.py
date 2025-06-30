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
# Retry decorator with exponential backoff
def retry_on_failure(retries: int = 3, backoff: float = 0.5):
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args, **kwargs) -> T:
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    logger.warning(f"Attempt {attempt} failed due to network: {e}")
                    if attempt == retries:
                        raise
                    time.sleep(backoff * attempt)
                except Exception as e:
                    logger.error("Non-retryable error occurred", exc_info=True)
                    raise
        return wrapper
    # Simulated API call
@retry_on_failure(retries=4)
def call_api_simulated(endpoint: str) -> str:
    chance = random.random()
    logger.info(f"Calling API at {endpoint}, chance={chance:.2f}")

    if chance < 0.3:
        raise NetworkError("Simulated network timeout")
    elif chance < 0.5:
        raise APIError("API responded with 500 error")
    
    return f"Success response from {endpoint}"

    # Fallback wrapper
def safe_call(func: Callable[[], T], fallback: T) -> T:
    try:
        return func()
    except APIError as e:
        logger.error(f"Falling back due to error: {e}")
        return fallback
# Usage
def main():
    endpoint = "https://fake-api.com/data"
    result = safe_call(lambda: call_api_simulated(endpoint), fallback="Fallback data")
    logger.info(f"Final result: {result}")

if __name__ == "__main__":
    main()



import logging
import time
import sys
import threading
try:
    import thread
except ImportError:
    import _thread as thread
from functools import wraps

logger = logging.Logger(__name__)


def retry_generate(func):
    """ Retry decorator for wrap into generate function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        n_retry = 2
        while n_retry > 0:
            result = func(*args, **kwargs)
            if result:
                return result
            n_retry -= 1
            logger.warn(f"{func.__name__} failed to generate or parse result. Retrying")
        
        logger.warn(f"{func.__name__} failed. Giving up!")
        return result
        
    return wrapper


def latency_benchmark(func):
    """
    Measure the execution time of a function. This is useful for measuring the time it takes to execute an application and print a summary of the execution time to the log

    @param func - function to be benchmarked.

    @return result of the function wrapped in a decorator that logs the execution time of the function and returns the result
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper to log how long the function took. This is useful for unit testing. 
                If you don't want to log the time taken use : func : ` log ` instead.
        
        @return The return value of the function wrapped by this wrapper. 
                It's a convenience wrapper for : func : ` log `
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        logger.warn(f'{func.__name__} took:  {time.time() - start_time} (s)')
        return result

    return wrapper

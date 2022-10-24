import sys
from logging_formatter import getLogger

logger = getLogger("Fibonacci")

def get_nth_fibo_num(n):
    n = int(n)
    if n == 1:
        return 1
    return get_nth_fibo_num(n-1)+get_nth_fibo_num(n-2)

try:
    if len(sys.argv) < 2:
        logger.warning("Usage : python 01_fibo_prob.py <n>")
    else:
        n = sys.argv[1]
        logger.info(f"The {n}th fibonacci number = {get_nth_fibo_num(n)}.")
except Exception as e:
    logger.exception(f"Exception in execution of program - {e}")

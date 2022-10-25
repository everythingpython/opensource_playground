import sys
from logging_formatter import getLogger

logger = getLogger("Fibonacci")

def get_nth_fibo_num(n):
    """
      Objective : Should return the nth fibonacci number
      E.g. If n = 10 
      get_nth_fibo_num(10) should return 55
    """
    n = int(n)
    count = 2
    a = 0
    b = 1
    while count <= n:
        c = a+b
        a = b
        b = c
        count += 1
    return c
    # if n == 1:
    #     return 1
    # return get_nth_fibo_num(n-1)+get_nth_fibo_num(n-2)

try:
    if len(sys.argv) < 2:
        logger.warning("Usage : python 01_fibo_prob.py <n>")
    else:
        n = sys.argv[1]
        logger.info(f"The {n}th fibonacci number = {get_nth_fibo_num(n)}.")
except Exception as e:
    logger.exception(f"Exception in execution of program - {e}")

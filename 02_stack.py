from logging_formatter import getLogger
import strings

logger = getLogger("Fibonacci")

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, n):
        """
            Objective : Should push an element to END of stack (an array)
            E.g. If n = 10 and current stack = [1,2,3]
            the resultant stack = [1,2,3,10]
        """
        self.stack.append(n)
        logger.info(f"Pushed {n} to stack. Current stack contents = {self.stack}")


    def pop(self):
        """
            Objective : Should pop an element from the HEAD of the stack (an array)
            E.g. If current stack = [1,2,3]
            the popped element = 1 and the resultant stack = [2, 3]
        """
        if len(self.stack) > 0:
            n = self.stack.pop(1)
            logger.info(f"Popped {n} from stack. Current stack contents = {self.stack}")
        else:
            logger.info(f"No contents in stack to pop from.")


try:
    stack_obj = Stack()
    method =  None

    while method != "0":
        inputs = input(strings.str_message+"\n").split()
        if len(inputs) < 1:
            logger.error(f"Empty input.\n")
        else:
            method = inputs[0]
            if method == "push":
                if len(inputs) < 2:
                    logger.warning(f"Missing element to push to stack. Enter : <push> <n>\n")
                else:
                    to_be_pushed = inputs[1]
                    element = int(to_be_pushed) if to_be_pushed.isnumeric() else to_be_pushed
                    stack_obj.push(element)
            elif method == "pop":
                stack_obj.pop()
            elif method == "0":
                logger.info(f"Final state of stack = {stack_obj.stack}\n")
                exit
            else:
                logger.error("Method unsupported. Only 'push' or 'pop' supported.\n")

except Exception as e:
    logger.exception(f"Exception in execution of program - {e}")

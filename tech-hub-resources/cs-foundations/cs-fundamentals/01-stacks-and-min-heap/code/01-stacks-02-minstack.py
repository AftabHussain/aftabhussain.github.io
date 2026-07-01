# Stack operations, and get min of stack, using O(1) operations.

class MinStack:

    def __init__(self):
        """
        We create two stacks, the actual stack, s, and a min stack, m.
        The min stack stores the minimum value of the entire stack.
        The min keeps the minimum at every stack depth
        
        say,

        s = [1]
        m = [1]

        s = [1,2]
        m = [1,1]

        This way when we push to s, we push the minimum of the current min of stack m and the input push value.

        When we pop, we just remove the top value of each stack. 
        """

        self.s = []
        self.m = []

    def pop(self) -> int:
        if not self.s:
            raise IndexError("pop from empty stack")
        self.m.pop()
        return(self.s.pop())

    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.m)==0:
            self.m.append(x)
        else:
            self.m.append(min(x, self.m[-1])) # m[-1] indicates the last element of the list, which is the top of the stack.

    def getMin(self) -> int:
        return self.m[-1]

def main():

    ms = MinStack()
    ms.push(5)
    print("pushed 5, Min", ms.getMin())
    ms.push(2)
    print("pushed 2, Min", ms.getMin())
    ms.push(3)
    print("pushed 3, Min", ms.getMin())
    ms.push(-1)
    print("pushed -1, Min", ms.getMin())


    print("Popped", ms.pop())
    print("Min", ms.getMin())

if __name__ == "__main__":
    main()

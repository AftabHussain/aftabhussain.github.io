
def paren_check(inp: str) -> bool:
    """
    Use stack to check parentheses.
    Read the string from left to right.
    Push an opening brace.
    If pushing a closing brace, ensure:
      1. the stack must not be empty, else return False
      2. the top of the stack must be the corresponding closer
    Assumes string only has parentheses
    """

    stack = []
    p_map = {")":"(", "]":"[", "}":"{"}

    if len(inp) <= 1:
        return False

    for ch in inp:
        if ch in p_map: #ch is a closing brace
            if p_map[ch] != stack[-1]: #We don't want to pop, we just want to peek (at top val)
                return False
            else:
                stack.pop()
        else:           #it is an opening brace
            stack.append(ch)

    return len(stack) == 0 


def main():
    sample = "&*(kj)]"
    print (paren_check(sample))



if __name__ == "__main__" :
    main()

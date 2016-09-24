class Stack():
    """
    Class Stack to define the stack datastructure
    """
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[len(self.stack)-1]
    def isEmpty(self):
        return len(self.stack)==0

def main():
    s = Stack()
    print s.isEmpty()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print s.isEmpty()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.isEmpty()

if __name__ == '__main__':
    main()

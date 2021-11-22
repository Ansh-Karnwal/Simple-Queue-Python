class Queue:
    def __init__(self):
        self.__lst = []
    def put(self, val):
        self.__lst.insert(0, val)
    def get(self):
        if len(self.__lst) > 0:
            val = self.__lst[-1]
            del self.__lst[-1]
            return val
    def isempty(self):
        if len(self.__lst) > 0:
            return False
        else:
            return True
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    def put(self, val):
        Queue.put(self, val)
    def get(self):
        return Queue.get(self)
    def isempty(self):
        if Queue.isempty(self):
            return True
        else:
            return False
que = SuperQueue()
que.put(1)
que.put("dog")    #Test Inputs
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

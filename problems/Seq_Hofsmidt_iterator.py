class sequence:
    def __init__(self,start):
        self.seq = start[:]
    def __iter__(self):
        return self
    def __next__(self):
        try:
            Q = self.seq[-self.seq[-1]]+self.seq[-self.seq[-2]]
            self.seq.append(Q)
            return Q
        except:
            exit()


Q = sequence([1, 10])
for i in range(10):
    print(next(Q), end = " ")
class RecentCounter:

    def __init__(self):
        self.queue = []
        
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        while self.queue[0] < t- 3000:
            self.queue.remove(self.queue[0])
            
        return len(self.queue)


s = RecentCounter()
print(s.ping(1))
print(s.ping(100))
print(s.ping(3002))
print(s.ping(4000))

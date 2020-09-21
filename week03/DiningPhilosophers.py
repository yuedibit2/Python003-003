import threading
import time
import queue
class DiningPhilosopher(threading.Thread):
    def __init__(self,index,leftFork,rightFork,q,eatNum=1):
        super(DiningPhilosopher,self).__init__()
        self.index=index
        self.leftFork=leftFork
        self.rightFork=rightFork
        self.q=q
        self.eatNum=eatNum
    def run(self):
        for _ in range(self.eatNum):
            self.leftFork.acquire()
            self.pickLeftFork()
            self.rightFork.acquire()
            self.pickRightFork()
            self.eat()
            self.putLeftFork()
            self.leftFork.release()
            self.putRightFork()
            self.rightFork.release()
    def pickLeftFork(self):
        self.q.put([self.index,1,1])
    def pickRightFork(self):
        self.q.put([self.index,2,1])
    def eat(self):
        time.sleep(1)
        self.q.put([self.index,0,3])
    def putLeftFork(self):
        self.q.put([self.index,1,2])
    def putRightFork(self):
        self.q.put([self.index,2,2])
if __name__=='__main__':
    q=queue.Queue()
    forkLock=[threading.Lock() for _ in range(5)]
    eatNum=input('请输入每个哲学家需要进餐的次数：')
    if int(eatNum)<1 or int(eatNum)>60:
        print('每个哲学家需要进餐的次数在1到60次之间！')
    else:
        philosophers=[]
        for i in range(5):
            if i==0:
                leftFork,rightFork=4,0
            else:
                leftFork,rightFork=i-1,i
            philosophers.append(DiningPhilosopher(i,forkLock[leftFork],forkLock[rightFork],q,int(eatNum)))
        for philosopher in philosophers:
            philosopher.start()
        for philosopher in philosophers:
            philosopher.join()
        print(list(q.queue))



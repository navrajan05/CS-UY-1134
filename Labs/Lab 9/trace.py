from Queues import ArrayQueue

myQ = ArrayQueue()
for i in range(8):
    myQ.enqueue(i)

def mystery(q):
    if q.is_empty():
        return
    else:
        val = q.dequeue()
        mystery(q)
        if val % 2 != 0:
            q.enqueue(val)

mystery(myQ)

while(len(myQ) > 0):
    print(myQ.dequeue())
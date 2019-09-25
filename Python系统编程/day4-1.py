from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
m = QueueManager(address=('192.168.1.165', 5000), authkey=b'horns')
m.connect()
queue = m.get_queue()

print(queue.get())

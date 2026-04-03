import socket
import threading
from queue import Queue
class PortScanner:
    def __init__(self,target,thread=100):
        self.target = target
        self.thread = thread
        self.open_ports = []
    
    def scan_port(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((self.target, port)) == 0:
            self.open_ports.append(port)
        s.close()

    def scan_all_port(self,start=1, end =1025):
        queue = Queue()
        for port in range(start,end):
            queue.put(port)
        
        def thread():
            while not queue.empty():
                port = queue.get()
                self.scan_port(port)
                queue.task_done()
        for i in range(self.thread):
            t = threading.Thread(target=thread)
            t.daemon = True
            t.start()

        queue.join()
        print(f"Open port: {sorted(self.open_ports)}")
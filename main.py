from multiprocessing import Process
from subprocess import call

def det():
    target1 = "getdetails.py"
    call(["python", (target1)])
    
def watch():
    target1 = "watcher.py"
    call(["python", (target1)])
    
if __name__ == '__main__':

    proc1 = Process(target=det)
    proc1.start()

    proc2 = Process(target=watch)
    proc2.start()
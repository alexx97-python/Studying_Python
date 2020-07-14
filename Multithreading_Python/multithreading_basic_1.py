import threading
import os


def task1():
    print(f"Tsk 1 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 1: {os.getpid()}")


def task2():
    print(f"Task 2 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 2: {os.getpid()}")


if __name__ == '__main__':

    print(f'ID of process running main program: {os.getpid()}')

    print(f'Main thread name: {threading.current_thread().name}')

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
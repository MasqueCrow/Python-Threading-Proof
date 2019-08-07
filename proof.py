import multiprocessing
import threading
import time

def function_1():
    for i in range(100000):
        print(i)

def function_2():
    for i in range(100000):
        print(i)

if __name__ == '__main__':
    thread1 = threading.Thread(target = function_1, args = [])
    thread2 = threading.Thread(target = function_2, args = [])

    process1 = multiprocessing.Process(target = function_1, args = [])
    process2 = multiprocessing.Process(target = function_2, args = [])

    #run function 1
    start = time.time()
    function_1()
    end = time.time()

    #run function 2
    start2 = time.time()
    function_2()
    end2 = time.time()


    #run threads
    start3 = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end3 = time.time()

    #run processes
    start4 = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end4 = time.time()

    print("Function 1 runtime:")
    print(end - start)
    print("-------------------")

    print("Function 2 runtime:")
    print(end2 - start2)
    print("-------------------")

    print("Multi-thread runtime:")
    print(end3 - start3)
    print("-------------------")

    print("Multi-process runtime:")
    print(end4 - start4)
    print("-------------------")

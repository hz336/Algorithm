import random
import threading
import time


def list_append(count, id, out_list):
    for i in range(count):
        out_list.append(random.random())


if __name__ == "__main__":
    start_time = time.time()

    for xx in range(0, 50):
        size = 3000000
        threads = 8       # we will run 9 processes

        jobs = []
        for i in range(0, threads):
            out_list = list()
            thread = threading.Thread(target=list_append, args=(size, i, out_list)) # Create a process object and set the constructor
            jobs.append(thread)

        # Start the processes (i.e. calculate the random number lists)
        for j in jobs:
            j.start()

        # Ensure all of the processes have finished
        for j in jobs:
            j.join()

    '''Time the program'''
    print("--- %s seconds ---" % (time.time() - start_time))


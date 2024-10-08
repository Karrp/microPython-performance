# """
# Basic multi thread example
# """

from time import sleep
import _thread


def core0_thread():
    counter = 0
    while True:
        print("0: ", counter)
        counter += 2
        sleep(1)


def core1_thread():
    counter = 1
    while True:
        print("1: ", counter)
        counter += 2
        sleep(2)

        if counter >= 20:
            print("end")
            _thread.exit()


second_thread = _thread.start_new_thread(core1_thread, ())

core0_thread()
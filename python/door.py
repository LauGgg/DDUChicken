from EmuControl2 import Emu
from time import sleep
from threading import Thread

emu = Emu()
emu.start()
ids = emu.scanUnits()

for id in ids:
    print(str(id))

emu.wheelMode(5)
emu.wheelMode(7)


# def open():
#     threads = []
#     for i in range(3):
#         t = Thread(target=emu.moveJoint, args=(ids[i], 200))
#         t.start
#         threads.append(t)
#     for thread in threads:
#         thread.join()

def close():
    pass

if __name__ == "__main__":
    # emu.moveWheel(5, 200)
    # print('moteren kører')
    # print(emu.getTuple(5))

    # run = True
    # while run:
    #     load = emu.getTuple(5)[39][1]
    #     if load > 80:
    #         run = False

    # emu.moveWheel(5, 0)
    # print('moteren er færdig med at køre')
    emu.moveWheel(5, 100)
    emu.moveWheel(7, -100)
    sleep(10)
    emu.moveWheel(5, 0)
    emu.moveWheel(7, 0)   


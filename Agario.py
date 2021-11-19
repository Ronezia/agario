import core
from creep import Creep
from avatar import Avatar

def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [1400, 850]
    core.memory("c",Creep())
    core.memory("a",Avatar())
    core.memory("listCreep",[])
    core.memory("nbrCreep",100)
    for i in range(0,core.memory("nbrCreep")):
        core.memory("listCreep").append(Creep())


def run ():
    core.cleanScreen()

    for moncreep in core.memory("listCreep"):
        moncreep.show(core.screen)
















core.main(setup, run)

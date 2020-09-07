# Gaol: This program has to switch quantum states: z=[x,y], output: z=[y,x].
from projectq.ops import All, CNOT, H, Measure, X, Y
from projectq import MainEngine

stateEngine = MainEngine()
qubitOne = int(input(stateEngine.allocate_qubit()))
qubitTwo = int(input(stateEngine.allocate_qubit()))

def quantum_teleportation(qubitOne, qubitTwo):
    H | qubitOne
    H | qubitTwo
    H | measure
    for stateEngine in (qubitOne and qubitTwo):
        if qubitOne[1] == 1 and qubitTwo[0] == 0:
            return (X | qubitOne, Y | qubitTwo = Y | qubitTwo, X | qubitOne)
        elif qubitOne[1] == 0 and qubitTwo[0] == 1:
            return (Y | qubitOne, X | qubitTwo = X | qubitTwo, Y | qubitTwo)
        else:
            return (qubitOne and qubitTwo)

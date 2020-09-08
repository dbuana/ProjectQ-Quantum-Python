from projectq.ops import All, CNOT, H, Measure, X, Y
from projectq import MainEngine

stateEngine = MainEngine()
qubitOne = int(input(stateEngine.allocate_qubit()))
qubitTwo = int(input(stateEngine.allocate_qubit()))

def quantum_teleportation(qubitOne, qubitTwo):
    # Gaol: This program has to switch quantum states: z=[x,y], output: z=[y,x].

    # Inner Workings: With application of Hadamard's matrix, I can create a quantum program which
    # returns a random quantum state. However, the quantum state needs switches; with quantum teleportation
    H | qubitOne
    H | qubitTwo
    H | measure
    # The main program engine
    for stateEngine in (qubitOne and qubitTwo):
        if qubitOne[1] == 1 and qubitTwo[0] == 0:
            quantum_value = int(qubitOne)
            quantum_value_two = int(qubitTwo)
            X | quantum_value
            Y | quantum_value_two
            return (quantum_value and quantume_value_two)
        elif qubitOne[1] == 0 and qubitTwo[0] == 1:
            X | qubitOne
            result = int(qubitOne)
            return result 
        else:
            quantum = [qubitOne, qubitTwo]
            return quantum

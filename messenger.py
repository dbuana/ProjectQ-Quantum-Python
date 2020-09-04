# Attempting to learn Quantum Computing with Python3.
# Quantum computers - Computer technology with vast association with qubits.

# A basic quantum computer program with application of Hadamard matrix.
# A Random Generator Program
from projectq.ops import H, Measure # ProjectQ is an IBM quantum computer library.
from projectq import MainEngine

# Applying a qubit
engine = MainEngine()
qubit = engine.allocate_qubit()
# Application of Hadamard's matrix to the program

def get_random():
    qubit = engine.allocate_qubit()
    # Applying Hadamard's matrix to the program
    H | qubit
    Measure | qubit
    # After a brief analyzation of the qubit, it will generate a random number.
    random_numbers = int(qubit)
    return random_numbers

numbers = []

for i in range(5):
    numbers.append(get_random())

engine.flush()
print("Hadamard's Matrix: " + str(numbers))
# Result: Based on the Hadamard's matrix, the function will return Hadamard's values; in an array form.

# Second practice-project

# Quantum Teleportation; a texting protocol of teleporting quantum states - basic idea.

# An example of wtiching qunatum sates - input:[0,1] and output: [1,0]. With the application
# of Hadamard's matrix, this is essentially based of each other.

# Quantum teleportation project , the basic program will be about. Person A sending a message to Person B.
from projectq.ops import All, CNOT, H, Measure, X, Y
from projectq import MainEngine

def sending_message(message, qubit_one="", qubit_two=""):
    # For this certain program, the main qubits are...
    qubit_one = eng.allocate_qubit()
    qubit_two = eng.allocate_qubit()
    # Compiling the qubits to create "one" qubit engine.
    qubits = [qubit_one, qubit_two]
    qubit_send = qubits.allocate_qubit(message)
    X | qubit_send # Switches the condition of the qubit.
    # THe message engine

    # Logic gates for qunatum teleportation: Hadamard's gate, CNOT gate, Pauli-x gate and Pauli-y gate are the
    # four main gates of quantum teleportation.

    # CNOT Gate - Works with two conditioned qubits with them being conditioned by one another - basic explanation.

    # Pauli Gates - In correlation to Pauli gates, blochsphere is sphere is a multi-variable representation
    # of a qubit's state. Pauli's gates tracks the certain coordinates of the qubits.

    if message == 1:
        """
        This code switches the quantum condition of The
        code and converts the message into the specified condition.
        """
        x | qubit_send
        CNOT | (qubit_send, qubits)
    elif message == "":
        """
        Translates the messages into a qubit.
        """
        X | qubit_send
        Y | qubit_one
    elif message == 0:
        """
        The code specifically combines the main qubit messages
        with the condition of the message.
        """
        xQubit = X | qubit_send
        yQubit = Y | qubit_send
        return xQubit
    else:
        return None

def messsage_receiver(qubits, message):
    """
    With the application of Hadamard's 
    """
    if message[1] and qubits[1] ==

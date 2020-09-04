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
    
    
# ===================== Under Construction =========================

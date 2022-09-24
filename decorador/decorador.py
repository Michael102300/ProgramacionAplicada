""" import sys
sys.path.insert(0,  "state_machines")

from state_machines.state_machines import state_machine """

""" def decorator(function):
    def intToBinary(intput, state): """
        


def intToBinary(input):
    result = input
    binary = []
    while result > 0:
        binary.append(result % 2)
        result = result // 2
    binary.reverse()
    return binary

print(intToBinary(0b0011))
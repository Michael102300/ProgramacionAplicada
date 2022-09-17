#from state_machines import state_machines

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

print(intToBinary(22))
print(bin(22))
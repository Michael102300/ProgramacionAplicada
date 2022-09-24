def decorator(function):
    def intToBinary(state, input):
        result = input
        binary = []
        output_binary = "0b"
        if result > 32: #Condicion para que el numero no supere los 32 bits 0b11111
            binary = [0,0,0,0,0]
            return binary
        while result > 0: # While para la conversion de binario a array para la maquina de estado
            binary.append(result % 2)
            result = result // 2
        binary.reverse()
        if len(binary) < 6: # Condicion para revisar si estan los 5 datos necesarios para la state machine
            while len(binary) < 5: # While para llenar el array con 0 hacia la izquierda, en lo mas significativo
                binary.insert(0,0)
        state_output, output = function(state, binary)
        for out in output: # For para convertir el arreglo en un binario
            output_binary = output_binary + str(out) # Concatena todo en una string
        return state_output, int(output_binary, 2) # Devuelva y cambia el binario a dec
    return intToBinary

@decorator
def state_machine(state, input):
    if state == "S1":
        output = [1,0,0,0,0]
        if input[0:2] == [0,1]:
            state = "S2"
    elif state == "S2":
        output = [0,0,0,1,1]
        if input[3:] == [1,1]:
            state = "S3"
        elif input[3:] == [0,1]:
            state = "S4"
    elif state == "S3":
        output = [0,0,1,0,0]
        if input[0] == 1:
            state = "S1"
    elif state == "S4":
        output = [0,1,0,0,0]
        if input[0:3] == [0,0,1]:
            state = "S3"
    else:
        output = [0,0,0,0,0]
    return state, output

print(state_machine("S1", 0b0100))
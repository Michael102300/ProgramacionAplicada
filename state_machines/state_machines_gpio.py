from machine import Pin
import time

pin_arr = [6, 7, 8, 9, 11]
pin_arr_2 = [17, 18, 19, 20, 21]
#pin_arr_2.reverse()

pin_input_arr = []
pin_output_arr = []
for pin in pin_arr:
    pin_input_arr.append(Pin(pin, Pin.IN, Pin.PULL_UP))

for pin in pin_arr_2:
    pin_output_arr.append(Pin(pin, Pin.OUT, Pin.PULL_UP))

def state_machine(state, _input):
    if state == "S1":
        output = [1,0,0,0,0]
        if _input[0:2] == [0,1]:
            state = "S2"
    elif state == "S2":
        output = [0,0,0,1,1]
        if _input[3:] == [1,1]:
            state = "S3"
        elif _input[3:] == [0,1]:
            state = "S4"
    elif state == "S3":
        output = [0,0,1,0,0]
        if _input[0] == 1:
            state = "S1"
    elif state == "S4":
        output = [0,1,0,0,0]
        if _input[0:3] == [0,0,1]:
            state = "S3"
    else:
        output = [0,0,0,0,0]
    return state, output

state = 'S1'
while True:
    entrada = []
    for pin in pin_input_arr:
        entrada.append(pin.value())
    print("entrada:"+str(entrada))
    state, output = state_machine(state, entrada)
    print("estado: ", state, "salida: ", output)
    for i in range(len(output)):
        pin_output_arr[i].value(output[i])
    #print("salida:" + str(_salida))
    time.sleep(0.2)

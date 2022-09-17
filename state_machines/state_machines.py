
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

#inputs = [[0,1,0,0,0], [0,0,0,1,1], [1,0,0,0,0]]
inputs = [[0,1,0,0,0], [0,0,0,0,1], [0,0,1,0,0], [1,0,0,0,0]]

state = "S1"
for input in inputs:
    print("input: ", input, ", state: ", state, end=" ")
    state, output = state_machine(state, input)
    print("output: ", output, ", next_state: ", state)


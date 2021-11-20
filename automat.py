#Automat komórkowy jednowymiarowy z jedną komórką żywą na start

rule = int(input("Podaj regułę: "))
automat_length = 81
main_automat = [" " for i in range(automat_length)]
pom_automat = [" " for i in range(automat_length)]

def initial_state(line, line_lenght):
    line[line_lenght//2] = "o"
    for i in range(line_lenght):            
        print(line[i],end=" ")
    print("\n")

def print_line(line, line_lenght=automat_length):
    for i in range(line_lenght):
        print(line[i],end=" ")
    print("\n")

def to_binary(rule):
    rule_list = []
    while rule>0:
        rule_list.insert(0,rule%2)
        rule //= 2
    while len(rule_list)<8:
        rule_list.insert(0,0)
    rule_list.reverse()
    return rule_list

def bin_to_dec(number):
    result = int(number[0])
    for i in range(1,len(number)):
        result = (result*2)+int(number[i])
    return result

def state_of_cell(left,cell,right,index):
    if left == " ": left = 0
    else: left = 1
    if cell == " ": cell = 0
    else: cell = 1
    if right == " ": right = 0
    else: right = 1
    state = str(left)+str(cell)+str(right)
    state_in_deci = bin_to_dec(state)
    if rule[state_in_deci] == 1:
        pom_automat[index] = "o"
    else:
        pom_automat[index] = " "
    
    
def run(automat=main_automat, repeat=40):
    initial_state(automat,automat_length)
    for i in range(repeat):
        state_of_cell(" ",automat[0],automat[1],0)
        for i in range(1,automat_length-1):
            state_of_cell(automat[i-1],automat[i],automat[i+1],i)
        state_of_cell(automat[automat_length-2],automat[automat_length-1]," ",automat_length-1)
        automat = pom_automat[:]
        print_line(automat)



rule = to_binary(rule)
run()

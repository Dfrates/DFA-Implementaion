"""DFA Implementation
    Name: Daniel Frates
    Date: 10/22/2022
    Description: Implementation of a DFA from a file
"""

# initialize the rule set list and states list
rule_set = []
states = []


def strip_list(arr, opt):
    """Strip list of optional characters
    Parameters: list, string (list to be stripped and character to strip)
    Returns: list (stripped list)
    """
    while opt in arr:
        arr.remove(opt)
    return arr


def load_alphabet(symbols):
    """Create a dictionary of the symbols in the alphabet
    Parameters: list (list of characters for alphabet)
    Returns: dict (dictionary of alphabet)
    """
    temp = {}
    for a in range(len(symbols)):
        temp[symbols[a]] = a
    return temp


def read_file(file_name, opt='r'):
    """Read file and load data in rule set list
    Parameters: string, string (filename and option to read)
    """
    with open(file_name, opt) as file:
        for line in file:
            # check if file has comments
            if ';' in line:
                current_line = line.split(';')
            else:
                current_line = line.split('\n')
            instr = current_line[0].split('\t')
            rule_set.append(instr[0])


def next_state(index, char):
    """Update state from given index
    Parameters: int, string (index of last state and char of last state)
    Returns: int (next state)
    """
    return states[int(index)][int(char)]


def check_accept(current_state, accept_list):
    """Checks whether current state is accepted
    Parameters: list, int (list of the accepted states and current state)
    Returns: bool (whether the current state is in the accepted states)
    """
    accepted = False
    if str(current_state) in accept_list:
        accepted = True

    return accepted


def get_user_input():
    """Gets user input and combines the two character end of string
    delimiter with the user input list
    Returns: list (list of user input ending with end character)
    """
    usr_input = []
    done = False
    # get user input
    while not done:

        # input prompt
        raw_input = input('-> ')
        # turns input into a list
        raw_input_list = list(raw_input)

        # separates end of string char and updates input
        end_char = ''.join(raw_input_list[-2:])
        usr_input = raw_input_list[:-2]
        usr_input.append(end_char)

        # end of string character
        stop_char = r'\0'
        if stop_char not in usr_input:
            print(f'Input string must end with "{stop_char}"')
            continue
        done = True

    return usr_input


def run_user_input(symbols, usr_input, end_char, accept_list):
    """Runs user input through the given dfa rule set
    Parameters: list, list, string (alphabet, users input, and end of
    string character
    Returns: bool (whether input is accepted or not)
    """
    # initializes current state and accepted
    curr_state = 0
    accepted = False

    # go through each input character
    for i in range(len(usr_input)):
        # go until end of string
        if usr_input[i] != end_char:
            print(f'Current state: {curr_state}, Current input: {usr_input[i]}')
            # updates current state to the next state
            curr_state = next_state(curr_state, symbols[usr_input[i]])
        else:
            print(f'Current state: {curr_state}, Current input: {usr_input[i]}')
            # checks whether final string is accepted in the language
            accepted = check_accept(curr_state, accept_list)
            break

    return accepted


def fill_states(state_amount):
    """Fills states from rule set and trims whitespace
    Parameters: int (number of states in the rule set)
    """
    # offset for rule_set
    offset = 2

    # sets the values of the raw states list
    for i in range(int(state_amount)):
        states.append(rule_set[i + offset])

    # trims the states list and separates the non empty values and removes them
    for i in range(len(states)):
        states[i] = strip_list(states[i].split(' '), '')


def run_dfa(symbols, state_amount, accept_list):
    """Runs DFA
    Parameters: list, int (alphabet and number of states
    Returns: bool (the solution to the users input)
    """
    # fills state list
    fill_states(state_amount)

    # end of string character
    stop_char = r'\0'

    # formats the initial entry message
    print(f'\nInput a string using alphabet of ', end='[')
    for key in symbols:
        print(f'{key}', end='')
    print(']')
    print(f'\nEnd string with "{stop_char}"')

    # gets the user input and puts it into a list
    user_input = get_user_input()

    # runs the user input list through dfa
    return run_user_input(symbols, user_input, stop_char, accept_list)


def main():
    """Runs everything needed to complete the DFA
    and prints the final solution
    """
    # read file
    read_file('test_files/DFA1.txt')

    # creates the values from the rule set
    letters = strip_list(list(rule_set[0]), ' ')
    alphabet = load_alphabet(letters)
    state_count = rule_set[1]
    accept_states = strip_list(rule_set[len(rule_set) - 1].split(' '), '')

    # runs dfa and determines if the string passed
    passed = run_dfa(alphabet, state_count, accept_states)

    print('String is accepted!') if passed else print('String is rejected!')


if __name__ == '__main__':
    main()
from file_utils.read_file import read_file


def get_network(nodes):
    network = {}

    for line in nodes:
        key, value = line.split(' = ')
        values = tuple(value.strip('()').split(', '))
        network[key] = values

    return network


def main(documents_input):
    instructions, _, *nodes = documents_input.splitlines()
    network = get_network(nodes)

    steps_to_zzz = 0
    instruction_size = len(instructions)
    ins_index = 0
    node = "AAA"

    while node != "ZZZ":
        steps_to_zzz += 1
        curr_node = network[node]

        if ins_index >= instruction_size:
            ins_index = 0

        next_instruction = instructions[ins_index]
        node = curr_node[1] if next_instruction == "R" else curr_node[0]

        ins_index += 1

    return steps_to_zzz


if __name__ == "__main__":
    documents = read_file("day_08_first_input.txt")
    steps_to_reach_zzz = main(documents)
    print(steps_to_reach_zzz)

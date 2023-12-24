from file_utils.read_file import read_file


def get_network(nodes):
    network = {}

    for line in nodes:
        key, value = line.split(' = ')
        values = tuple(value.strip('()').split(', '))
        network[key] = values

    return network


def get_nodes_ending_with_a(network):
    return [node for node in network if node.endswith("A")]


def gcd(x, y):
    """Compute the greatest common divisor of x and y using the Euclidean algorithm."""
    while y:
        temp = x % y
        x = y
        y = temp
    return x


def lcm(x, y):
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // gcd(x, y)


def multiple_lcm(numbers):
    """Compute the least common multiple of a set of numbers."""
    while len(numbers) > 1:
        lcm_value = lcm(numbers[0], numbers[1])
        numbers = [lcm_value] + numbers[2:]

    return numbers[0]


def main(documents_input):
    instructions, _, *nodes = documents_input.splitlines()
    network = get_network(nodes)
    nodes_ending_with_a = get_nodes_ending_with_a(network)

    instruction_size = len(instructions)
    ins_index = 0
    steps = []

    for n in nodes_ending_with_a:
        steps_to_node_ending_with_z = 0
        curr = n
        while not curr.endswith("Z"):
            steps_to_node_ending_with_z += 1
            curr_node = network[curr]

            if ins_index >= instruction_size:
                ins_index = 0

            next_instruction = instructions[ins_index]
            curr = curr_node[1] if next_instruction == "R" else curr_node[0]

            ins_index += 1
        steps.append(steps_to_node_ending_with_z)

    return multiple_lcm(steps)


if __name__ == "__main__":
    documents = read_file("day_08_second_input.txt")
    steps_to_reach_node_ending_with_z = main(documents)
    print(steps_to_reach_node_ending_with_z)

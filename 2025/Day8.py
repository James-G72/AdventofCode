import math

loci = []
for line in open("Day8_input.txt").readlines():
    loci.append([int(x) for x in line.split("\n")[0].split(",")])


def build_dist(loci):
    d = []
    for idx_1, l1 in enumerate(loci):
        dist_temp = []
        for idx_2, l2 in enumerate(loci):
            if idx_1 != idx_2:
                dist_temp.append([math.dist(l1, l2), idx_1, idx_2])
        d.extend(dist_temp)
    return d


distances = build_dist(loci)
sorted_d = sorted(distances)
sorted_unique_d = sorted_d[::2]

circuits = []
for idx in range(0, 1001):
    if idx == 224:
        t = 1
    index_1, index_2 = sorted_unique_d[idx][1:]
    included = False
    merge_circ = []
    remove_idx = []
    for circ_idx, circuit in enumerate(circuits):
        if index_1 in circuit:
            circuit.extend([index_2])
            merge_circ.extend(circuit)
            remove_idx.append(circ_idx)
        elif index_2 in circuit:
            circuit.extend([index_1])
            merge_circ.extend(circuit)
            remove_idx.append(circ_idx)
    for index_to_remove in sorted(remove_idx, reverse=True):
        circuits.pop(index_to_remove)
    if len(merge_circ) > 0:
        circuits.append(list(set(merge_circ)))
    else:
        circuits.append([index_1, index_2])

length_included = sorted([[len(x), x] for x in circuits], reverse=True)

longest_3_prod = math.prod([x[0] for x in length_included[:3]])

print("Part1: The sum of invalid entries is: " + str(longest_3_prod))

# Part 2

istances = build_dist(loci)
sorted_d = sorted(distances)
sorted_unique_d = sorted_d[::2]

circuits = []
final_connection = []
idx = 0
while len(circuits) > 1 or idx < 20:
    index_1, index_2 = sorted_unique_d[idx][1:]
    final_connection = [index_1, index_2]
    included = False
    merge_circ = []
    remove_idx = []
    for circ_idx, circuit in enumerate(circuits):
        if index_1 in circuit:
            circuit.extend([index_2])
            merge_circ.extend(circuit)
            remove_idx.append(circ_idx)
        elif index_2 in circuit:
            circuit.extend([index_1])
            merge_circ.extend(circuit)
            remove_idx.append(circ_idx)
    for index_to_remove in sorted(remove_idx, reverse=True):
        circuits.pop(index_to_remove)
    if len(merge_circ) > 0:
        circuits.append(list(set(merge_circ)))
    else:
        circuits.append([index_1, index_2])
    idx += 1

print("Part2: The product of x values: " + str(final_connection[0]*final_connection[1]))
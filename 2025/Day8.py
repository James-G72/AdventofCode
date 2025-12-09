import math

loci = []
for line in open("Day8_input.txt").readlines():
        loci.append([int(x) for x in line.split("\n")[0].split(",")])

def dist_3d(l1, l2):
    return math.sqrt((l1[0]-l2[0])**2+(l1[1]-l2[1])**2+(l1[2]-l2[2])**2)

def build_dist(loci):
    d= []
    for idx_1, l1 in enumerate(loci):
        dist_temp = []
        for idx_2, l2 in enumerate(loci):
            if idx_1 != idx_2:
                dist_temp.append([dist_3d(l1, l2), idx_1, idx_2])
        d.extend(dist_temp)
    return d

distances = build_dist(loci)
sorted_d = sorted(distances)
sorted_unique_d = sorted_d[::2]

circuits = []
for idx in range(0, 11):
    index_1, index_2 = sorted_unique_d[idx][1:]
    included = False
    out_circuit = []
    merge_circ = []
    for circ_idx, circuit in enumerate(circuits):
        if index_1 in circuit:
            circuit.extend([index_2])
            merge_circ.extend(circuit)
            included = True
        elif index_2 in circuit:
            circuit.extend([index_1])
            merge_circ.extend(circuit)
            included = True
        else:
            out_circuit.append(circuit)
    if len(merge_circ) > 0:
        out_circuit.append(list(set(merge_circ)))

    if not included:
        circuits.append([index_1, index_2])
    else:
        circuits = out_circuit

length_included = sorted([[len(x), x] for x in circuits], reverse=True)

longest_3_prod = math.prod([x[0] for x in length_included[:3]])

print("Part1: The sum of invalid entries is: "+str(longest_3_prod))

# Part 2
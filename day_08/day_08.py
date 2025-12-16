import sys
filename = "input_test.txt" if len(sys.argv) == 2 and sys.argv[1] == "test" else "input.txt"
data = list(open(filename).read().splitlines())
data = [tuple(map(int, line.split(','))) for line in data]

def get_distance(p1, p2):
    return (
        ((p2[0] - p1[0]) ** 2 +
         (p2[1] - p1[1]) ** 2 +
         (p2[2] - p1[2]) ** 2) 
         ** 0.5
    )

def part_one(data):
    distances = []
    for p1i, p1 in enumerate(data):
        for p2i, p2 in enumerate(data):
            if p2i >= p1i: continue
            if p1 is not p2:
                d = get_distance(p1, p2)
                distances.append((p1, p2, d))
    distances.sort(key=lambda x: x[-1])
    distances = distances[:1000]

    circuits = []
    for p1, p2, _ in distances:
        found_circuits = []
        for circuit in circuits:
            if p1 in circuit or p2 in circuit:
                found_circuits.append(circuit)
        if not found_circuits:
            circuits.append(set([p1, p2]))
        else:
            merged = set([p1, p2])
            for circuit in found_circuits:
                merged.update(circuit)
                circuits.remove(circuit)
            circuits.append(merged)

    circuits.sort(key=lambda x: -len(x))
    circuits = circuits[:3]

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part_two(data):
    pass

print("Part 1 -> ", part_one(data))
print("Part 2 -> ", part_two(data))
with open("2024/day23/input.txt") as f:
    lines = f.read().splitlines()

graph = {}

for line in lines:
    A, B = line.split("-")
    graph.setdefault(A, set()).add(B)
    graph.setdefault(B, set()).add(A)

triangle = set()

for p in graph:
    for q in graph[p]:
        for r in graph[q]:
            if r in graph[p]:
                if p.startswith("t") or q.startswith("t") or r.startswith("t"):
                    triangle.add(tuple(sorted([p, q, r])))

print(len(triangle))

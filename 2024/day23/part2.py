with open("2024/day23/input.txt") as f:
    lines = f.read().splitlines()

graph = {}

for line in lines:
    A, B = line.split("-")
    graph.setdefault(A, set()).add(B)
    graph.setdefault(B, set()).add(A)

nodes = set(graph.keys())


def bron_kerbosch(R, P, X, grph, clq):
    if not P and not X:
        clq.append(R)
        return

    for v in list(P):
        bron_kerbosch(R | {v}, P & grph[v], X & grph[v], grph, clq)
        P.remove(v)
        X.add(v)


cliques = []
bron_kerbosch(set(), nodes, set(), graph, cliques)
largest = max(cliques, key=len)

print(",".join(sorted(largest)))

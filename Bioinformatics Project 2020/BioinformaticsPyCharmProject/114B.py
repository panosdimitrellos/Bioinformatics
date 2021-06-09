states = ('a', 'b')

observations = ('G', 'G', 'C', 'T')

start_probability = {'a': 0.6, 'b': 0.4}

transition_probability = {
    'a': {'a': 0.9, 'b': 0.1},
    'b': {'a': 0.1, 'b': 0.9}
}

emission_probability = {
    'a': {'A': 0.4, 'G': 0.4, 'C': 0.1, 'T': 0.1},
    'b': {'A': 0.2, 'G': 0.2, 'C': 0.3, 'T': 0.3}
}


# Μας βοηθάει να οπτικοποιήσουμε τα βήματα του Viterbi
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # V = [{y:(start_p[y] * emit_p[y][obs[0]]) για y στις καταστάσεις a,b}]
    # path = {y:[y] για y στις καταστάσεις a,b}

    # Τρέχουμε τον Viterbi
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Δεν χρειάζεται να θυμόμαστε τα παλιά μονοπάτια.
        path = newpath

    print_dptable(V)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)


print(example())
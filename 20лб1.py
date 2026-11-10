import numpy as np

gamma = 0.8

pi = {
    's1': {'a1': 0.4, 'a2': 0.6},
    's2': {'a2': 1.0},
    's3': {'a1': 0.5, 'a3': 0.5},
    's4': {'a1': 1.0}
}

transitions = {
    's1': {
        'a1': [(0.3, 's2', 2.0), (0.7, 's3', 3.0)],
        'a2': [(1.0, 's3', 1.0)]
    },
    's2': {
        'a2': [(1.0, 's1', 3.0)]
    },
    's3': {
        'a1': [(1.0, 's1', -3.0)],
        'a3': [(0.2, 's3', 1.0), (0.8, 's4', 6.0)]
    },
    's4': {
        'a1': [(0.6, 's1', 5.0), (0.4, 's2', -3.0)]
    }
}

states = ['s1', 's2', 's3', 's4']
state_idx = {s: i for i, s in enumerate(states)}

A = np.zeros((4, 4))
B = np.zeros(4)

for s in states:
    i = state_idx[s]
    A[i, i] = 1.0
    for a, prob_a in pi[s].items():
        expected_reward = 0
        expected_next_value = 0
        
        for p, s_next, r in transitions[s][a]:
            expected_reward += p * r
            A[i, state_idx[s_next]] -= prob_a * p * gamma
            expected_next_value += p * r 
        B[i] += prob_a * expected_reward

solution = np.linalg.solve(A, B)
print("Значения ценности состояний:")
for s in states:
    print(f"V({s}) = {solution[state_idx[s]]:.3f}")
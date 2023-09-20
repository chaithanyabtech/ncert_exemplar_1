import random

# Simulate coin tosses
def simulate_coin_tosses(num_tosses):
    outcomes = []
    for _ in range(num_tosses):
        outcome = random.choice(['Head', 'Tail'])  # Randomly choose 'Head' or 'Tail'
        outcomes.append(outcome)
    return outcomes

# Perform the simulation
num_simulations = 10000
num_tosses = 4
tail_count = 0

for _ in range(num_simulations):
    outcomes = simulate_coin_tosses(num_tosses)
    if outcomes[-1] == 'Tail':
        tail_count += 1

# Calculate the probability of getting a tail in the 4th toss
probability_tail = tail_count / num_simulations

print(f"Probability of getting a tail in the 4th toss: {probability_tail}")


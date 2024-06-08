import numpy as np
import matplotlib.pyplot as plt

# Simulating 1000 rolls of two dice
rolls = np.random.randint(1, 7, size=(1000, 2))
sums = rolls.sum(axis=1)

plt.hist(sums, bins=np.arange(2, 14)-0.5, edgecolor='black')
plt.title('Sum of Rolling Two Dice 1000 Times')
plt.xlabel('Sum')
plt.ylabel('Frequency')
plt.xticks(range(2, 13))
plt.show()

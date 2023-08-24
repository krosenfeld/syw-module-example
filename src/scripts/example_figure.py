import matplotlib.pyplot as plt
import numpy as np
from module.example import generate_random_numbers
import paths

# Generate some data
random_numbers = [generate_random_numbers(100) for i in range(10)]

# Plot and save
fig = plt.figure(figsize=(7, 6))
plt.plot(random_numbers)
plt.xlabel("x")
plt.ylabel("y")
fig.savefig(paths.figures / "random_numbers.pdf", bbox_inches="tight", dpi=300)
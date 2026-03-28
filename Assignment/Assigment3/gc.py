import gc

# Create unused objects
a = [1, 2, 3]
b = [4, 5, 6]

# Delete references
del a
del b

# Manually collect garbage
collected = gc.collect()

print("Garbage objects collected:", collected)
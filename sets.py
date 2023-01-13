# Sets unmutable values
# create an empty set
s = set()

# Add element to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# auto remove dublicate item
s.add(3)

# remove item

s.remove(2)
print(s)


# calculate how many item on set

print(f"The set has {len(s)} element")
data = {"a": 10, "b": 50, "c": 25, "d": 5}
max_key = max(data, key=data.get)
min_key = min(data, key=data.get)

print("Key with max value:", max_key)
print("Key with min value:", min_key)

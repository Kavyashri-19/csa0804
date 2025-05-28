data = {"a": 10, "b": 50, "c": 25, "d": 5}
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_dict)

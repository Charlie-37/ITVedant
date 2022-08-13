a = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}, {'id': 3, 'name': 'C'}]

b = [b['id'] for b in a]
print(b)

c = [b['name'] for b in a ]
c = tuple(c)
print(c)

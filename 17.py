
d1 = {'ab': 100, 'bc': 200}
d2 = {'cd': 300, 'de': 400}
print("dictionary1", d1)
print("dictionary2", d2)
d = d1.copy()
d.update(d2)
print("Merged dictionary:", d)

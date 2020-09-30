d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
​
items = list(d.items())
​
# Sort by key
​
items.sort()
​
for i in items:
	print(f'{i[0]}: {i[1]}')
​
​
print()
​
# Sort by value
​
"""
def sort_by(t):
	#print(f'sort_by({repr(t)}) called!')
	return t[1]
​
items.sort(key=sort_by)
​
# ^^ same as lambda vv
"""
​
items.sort(key=lambda t: t[1])
​
for i in items:
    	print(f'{i[0]}: {i[1]}')
london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco', 'London1': 'name'}
nmap = {}
for key, value in london.items():
    # Один вариант
    if not nmap.get(value) == key:
            nmap[key] = value
# Второй вариант
#    key, value = sorted([key, value])
#    nmap[key] = value
print(nmap)


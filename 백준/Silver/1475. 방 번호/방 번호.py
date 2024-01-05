n = input()
m = {}
result = 0

for i in range(10):
    m[str(i)] = 0

for i in range(len(n)):
    if n[i] == '9':
        m['6'] += 1
    else:
        m[n[i]] += 1

if m['6'] % 2 == 0:
    m['6'] = m['6'] // 2
elif m['6'] % 2 == 1:
    m['6'] = (m['6'] // 2) + 1

print(max(m.values()))
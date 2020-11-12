from random import randint

UZ = [
    [],
    ['K1', 'K1', 'K1'],
    ['K2', 'K2', 'K1'],
    ['K3', 'K3', 'K2']
]

def damage(p, d, s = 0, e = 100):
    k = randint(s, e)
    while p != None and (p - d > k or p + d < k):
        k = randint(s, e)
    return k


print('k experts')
k = int(input())

print('Size IS(0=object, 1=region, 2=federation)')
s = int(input())

print('count experiments')
e = int(input())

d = 15

experiments = []
for i in range(e):
    ex = []
    for j in range(k):
        ek = damage(experiments[i - 1][j] if i else None, d)
        ex.append(ek)
    exa = sum(ex) // len(ex)
    experiments.append(ex)
    experiments[i].append(exa)

[print(l) for l in experiments]

expl = experiments[e-1][k]

uz = 0
if expl > 70:
    uz = 1
elif 20 < expl and expl <= 70:
    uz = 2
elif expl <= 20:
    uz = 3

print(UZ[uz][s])
from random import randint

from numpy.core._multiarray_umath import sign

UZ = [
    [],
    ['K1', 'K1', 'K1'],
    ['K2', 'K2', 'K1'],
    ['K3', 'K3', 'K2']
]


def damage_estimate(experiment, expert_index, max_delta):
    if not experiment:
        return randint(0,100)
    experiment = experiment[0]
    average_esitmate = sum(experiment) // len(experiment)
    last_estimate = experiment[expert_index]
    new_estimate = (average_esitmate+last_estimate)//2

    delta_estimate = (new_estimate - last_estimate)/last_estimate*100
    delta = min(abs(delta_estimate), max_delta)
    return round(last_estimate*(1+sign(delta_estimate)*delta/100))


experts_count = int(input('Enter amount of experts: '))
is_size = int(input('Enter IS size(0=object, 1=region, 2=federation): '))
experiments_count = int(input('Enter count of experiments: '))

estimation_max_delta = 15
experiments = []


for experiment_index in range(experiments_count):
    experiment = [damage_estimate(experiments[-1:], expert_index, estimation_max_delta)
                  for expert_index in range(experts_count)]
    experiments.append(experiment)


[print(l) for l in experiments]

avg_estimate = sum(experiments[-1])/len(experiments[-1])
if avg_estimate > 70:
    uz = 1
elif 20 < avg_estimate and avg_estimate <= 70:
    uz = 2
elif avg_estimate <= 20:
    uz = 3

print(UZ[uz][is_size])
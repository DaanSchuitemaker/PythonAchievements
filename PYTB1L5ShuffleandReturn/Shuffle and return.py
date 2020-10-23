import random

def ShuffledWoord(original):
    randomised = ''.join(random.sample(original, len(original)))
    return randomised

woord1 = ShuffledWoord("Daan")
woord2 = ShuffledWoord("Appelsap")
woord3 = ShuffledWoord("Aansprakelijkheidswaardevaststellingsveranderingen")
print(woord1)

print()

print(woord2)

print()

print(woord3)






import random

with open('637seq', 'r') as file:
    akoluthia = file.read().replace('\n', '')

alhlouxiaList = list(akoluthia)

print("Η αρχικά αλληλουχία είναι: ")
text1 =""
for i in range(akoluthia.__len__()):
    text1 += str(akoluthia[i])

print(text1)

for n, x in enumerate(akoluthia):
    if x == "A":
        alhlouxiaList[n] = "A"+"A"*random.randint(1, 5)
    if x == "C":
        alhlouxiaList[n] = "C"+"C"*random.randint(1, 10)
    if x == "G":
        alhlouxiaList[n] = "G"+"G"*random.randint(1, 100)
    if x == "T":
        alhlouxiaList[n] = "T"+"T"*random.randint(1, 100)

print("Η μολυσμένη έκδοση της αρχικής αλληλουχίας είναι: ")
text2 = ""
for i in range(alhlouxiaList.__len__()):
    text2 += str(alhlouxiaList[i])

print(text2)

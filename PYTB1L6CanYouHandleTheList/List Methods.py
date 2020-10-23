list = ["appel", "peer", 5, 8, 2.4]
print(list)

list.append ("banaan")
print(list)

list.remove ("peer")
print(list)

list.append ("appel")
print(list)
hoeveelAppels = list.count("appel")
print("appel komt", hoeveelAppels, "keer voor in de list")

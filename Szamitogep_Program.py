from Szamitogep import Szamitogep

peldany1 = Szamitogep("Win", 32)
peldany2 = Szamitogep("Mac", 16)
peldany3 = Szamitogep("Win", 16)

szamitogepek = []

szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)

for i in range(len(szamitogepek)):
    op_r = szamitogepek[i].op_r
    ram = szamitogepek[i].ram
    print(f"{op_r} ({ram})")

print("Átlag: ", end="")
ossz = 0
for i in range(len(szamitogepek)):
    ossz += szamitogepek[i].ram
print(round(ossz / len(szamitogepek), 3))


print("Legtöbb ram-ot tartalmazó oprendszer: ", end="")
max_i = 0
for i in range(len(szamitogepek)):
    if szamitogepek[max_i].ram < szamitogepek[i].ram:
        max_i = i
print(szamitogepek[max_i].op_r)

print("Hány windows-os gépünk van? ", end="")
hany = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].op_r == "Win":
        hany += 1
print(f"{hany} db Windows-os számítógépünk van.")


vizsgaltram = 22
print(f"Van-e {vizsgaltram} GB-nál nagyobb Windows? ", end="")

van = False
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > vizsgaltram and szamitogepek[i].op_r == "Win":
        van = True

if van:
    print("Van")
else:
    print("nincs")

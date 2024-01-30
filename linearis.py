def kereses():
    also = 42
    felso = 67
    i = also
    while i <= felso and i % 10 != 0:
        i += 1
    van = i <= felso
    if van:
        return i
    else:
        return -1

print(kereses())
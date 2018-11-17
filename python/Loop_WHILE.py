
i = 0

while i < 10:

    if i == 5:
        i = i + 1
        continue

    if i == 8:
        break

    print(i)
    i = i + 1
#Caso dé o break a interação é finalizada ou seja, não vai executar o else.
else:
    print("Fim do loop")
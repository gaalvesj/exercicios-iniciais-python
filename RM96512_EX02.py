VOTOS_SEG = int(input("Quantos Votos tiveram na segunda-feira?"))
VOTOS_TER = int(input("Quantos Votos tiveram na terça-feira?"))
VOTOS_QUA = int(input("Quantos Votos tiveram na quarta-feira?"))
VOTOS_QUI = int(input("Quantos Votos tiveram na quinta-feira?"))
VOTOS_SEX = int(input("Quantos Votos tiveram na sexta-feira?"))

if VOTOS_SEG > VOTOS_TER and VOTOS_SEG > VOTOS_QUA and VOTOS_SEG > VOTOS_QUI and VOTOS_SEG > VOTOS_SEX:
    print(f"segunda foi o mais votado com {VOTOS_SEG} votos")
elif VOTOS_TER  > VOTOS_SEG and VOTOS_TER > VOTOS_QUA and VOTOS_TER > VOTOS_QUI and VOTOS_TER > VOTOS_SEX :
    print(f"terca foi o mais votado com {VOTOS_TER} votos")
elif VOTOS_QUA  > VOTOS_SEG and VOTOS_QUA > VOTOS_TER and VOTOS_QUA > VOTOS_QUI and VOTOS_QUA > VOTOS_SEX :
    print(f"quarta foi o mais votado com {VOTOS_QUA} votos")
elif VOTOS_QUI  > VOTOS_SEG and VOTOS_QUI > VOTOS_TER and VOTOS_QUI > VOTOS_QUA and VOTOS_QUI > VOTOS_SEX :
    print(f"quinta foi o mais votado com {VOTOS_QUI} votos")
elif VOTOS_SEX  > VOTOS_SEG and VOTOS_SEX > VOTOS_TER and VOTOS_SEX > VOTOS_QUA and VOTOS_SEX > VOTOS_QUI :
    print(f"sexta foi o mais votado com {VOTOS_SEX} votos")



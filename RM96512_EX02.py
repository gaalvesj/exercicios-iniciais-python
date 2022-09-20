VOTOS_SEG = 0
VOTOS_TER = 0
VOTOS_QUA = 0
VOTOS_QUI = 0
VOTOS_SEX = 0

def votoSeg():
    global VOTOS_SEG
    VOTOS_SEG += 1
    return VOTOS_SEG

def votoTer():
    global VOTOS_TER
    VOTOS_TER += 1
    return VOTOS_TER

def votoQua():
    global VOTOS_QUA
    VOTOS_QUA += 1
    return VOTOS_QUA

def votoQui():
    global VOTOS_QUI
    VOTOS_QUI += 1
    return VOTOS_QUI

def votoSex():
    global VOTOS_SEX
    result = VOTOS_SEX + 1
    return result


resposta = int(input("Qual dia voce escolhe para lives:\
 1-Segunda-Feira \
 2-Terca-Feira \
 3-Quarta-Feira \
 4-quinta-feira \
 5-Sexta-Feira"))
if resposta == 1:
        print("voce votou na segunda-feira")
elif resposta == 2:
        print("voce votou na terca-feira")
elif resposta == 3:
        print("voce votou na quarta-feira")

elif resposta == 4:
        print("voce votou na quinta-feira")

elif resposta == 5:
        print("voce votou na sexta-feira")

else:
    print("digite apenas de 1 a 5 para votar")


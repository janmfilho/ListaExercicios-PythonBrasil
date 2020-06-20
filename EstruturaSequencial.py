#### Python Brasil ####
### Lista de Exercícios - Estrutura Sequencial ###

## ES.1
print("#ES.1 \n Alô mundo")

## ES.2
answeres2 = int(input("Qual é o número?"))
print("#ES.2 \n O número infomado é", answeres2)

## ES.3
a1 = int(input("Qual é o primeiro número?"))
b1 = int(input("Qual é o segundo número?"))

def addtwo(a, b):
    added = a + b
    return(added)

answeres3 = addtwo(a1,b1)
print("#ES.3 \n A soma é", int(answeres3))

## ES.4
answeres41 = float(input("Qual foi sua primeira nota bimestral?"))
answeres42 = float(input("Qual foi sua segunda nota bimestral?"))
answeres43 = float(input("Qual foi sua terceira nota bimestral?"))
answeres44 = float(input("Qual foi sua quarta nota bimestral?"))

média = (answeres41 + answeres42 + answeres43 + answeres44) / 4
print("#ES.4 \n Sua média bimestral foi de", média)

## ES.5
metros = float(input("Quantos metros são?"))
print("#ES.5 \n Ok! Esse valor equivale a", (metros * 100), "centímetros")

## ES.6
raio = float(input("Qual é o raio do círculo?"))
print("#ES.6 \n Ok! A área deste círculo é de", ((raio)*(raio))*3.14)

## ES.7
lado = int(input("Qual é o lado do quadrado?"))
print("#ES.7 \n Ok! A área desse quadrado é de", (lado)*(lado), "e seu dobro é de", ((lado)*(lado)*2))

## ES.8
rendimento1 = int(input("Quanto você ganha por hora?"))
horas1 = int(input("Quantas horas você trabalha por mês?"))

def calculo(rendimento, horas):
    salario = rendimento * horas
    return(salario)

answeres8 = calculo(rendimento1, horas1)
print("#ES.8 \n Ok! Você ganha R$", int(answeres8), "por mês")

## ES.9
frnht = int(input("Qual é a temperatura em Farenheit?"))
print("#ES.9 \n Ok! Essa temperatura é equivalente à", ((5*(frnht-32))/9), "celsius")

## ES.10
cls = int(input("Qual é a temperatura em Graus Celsius?"))
print("#ES.10 \n Ok! Essa temperatura é equivalente à", ((9*cls)/4) + 32, "Farenheit")

## ES.11
inteiro1 = int(input("Qual é o primeiro número inteiro?"))
inteiro2 = int(input("Qual é o segundo número inteiro"))
real1 = float(input("Qual é o número real?"))

print("#ES.11 letra a \n Ok! O produto do dobro do primeiro com metade do segundo é", (inteiro1*2)*(inteiro2/2))
print("#ES.11 letra b \n Ok! A soma do triplo do primeiro com o terceiro é", (inteiro1*3)+(real1))
print("#ES.11 letra c \n Ok! O terceiro elevado ao cudo é", (real1)*(real1)*(real1))

## ES.12
answeres12 = float(input("Qual é sua altura?"))
print("#ES.12 \n Ok! Seu peso ideal é de", (72.7 * answeres12) - 58, "kilos.")

## ES.13
answeres13 = input("Você é homem ou mulher?")
answeres131 = float(input("Qual é sua altura?"))

if answeres13 == 'homem':
    print("#ES.13 \n Ok! Seu peso ideal é de", (72.7 * answeres131) - 58)
elif answeres13 == 'mulher':
    print("#ES.13 \n Ok! Seu peso ideal é de", (62.1 * answeres131) - 44.7)
else:
    print("Responda a questão #ES.13 correta")

## ES.14 (The "return" statement only makes sense inside functions)
peso = float(input("João Papo-de-Pescador, Qual é o peso do peixe que pescaste?"))
if peso <= 50:
    print("#ES.14 Muito bom, João! Você trouxe um Peixe que está dentro do regulamento")
elif peso > 50:
    def contaexc(peso):
        excesso = peso - 50
        return (excesso)
    answeres14 = contaexc(peso)
    print("#ES.14 \n João, você trouxe um Peixe que não está dentro do regulamento! Você terá que pagar uma multa de", (4 * answeres14))
else:
    print("#ES.14 \n Então você não pescou peixe nenhum, João!")

## ES.15
rendimento2 = int(input("Quanto você ganha por hora?"))
horas2 = int(input("Quantas horas você trabalha por mês?"))

def calculobruto(rendimenton, horasn):
    salariobruto = rendimenton * horasn
    return(salariobruto)

answeres15 = calculobruto(rendimento2, horas2)
print("#ES.15 \n Ok! O seu salário bruto é de R$", answeres15, "por mês.")
print("Você pagou cerca de R$", answeres15 * 0.08, "ao INSS, cerca de R$", answeres15 * 0.11, "ao IR e cerca de R$", answeres15 * 0.05, "ao sindicato.")
print("Resultando em um salário líquido de", (1 - (0.08 + 0.11 + 0.05)) * answeres15, "por mês.")

## ES.16
litro = int(input("Qual é o tamanho em metros quadrados da área a ser pintada?")) / 3

if litro <= 18:
    print("#ES.16 \n Ok! Você precisará de apenas uma lata e isso lhe custará R$ 80")
elif litro > 18:
    def contalitro(litro):
        latas = litro / 18
        return(latas)
    answer16 = contalitro(litro)
    print("#ES.16 \n Ok! Você precisará de", round(answer16 + 0.5), "latas e isso lhe custará R$", round(answer16 + 0.5) * 80)
else:
    print("#ES.16 \n Então você não me disse o tamanho da área a ser pintada!")

## ES.17
arealitro = int(input("Qual é o tamanho em metros quadrados da área a ser pintada?")) / 6
arealitro2 = arealitro

if arealitro <= 18:
    print("#ES.17 \n Ok! Você precisará de apenas uma lata e isso lhe custará R$ 80")
elif arealitro > 18:
    def contalitro(arealitro):
        latas = arealitro / 18
        return(latas)
    answer17 = contalitro(arealitro)
    print("#ES.17 \n Ok! Você precisará de", round(answer17 + 0.5), "latas e isso lhe custará R$", round(answer17 + 0.5) * 80)
else:
    print("#ES.17 \n Então você não me disse o tamanho da área a ser pintada!")

if arealitro2 <= 3.6:
    print("#ES.17 \n Ok! Você precisará de apenas um galão e isso lhe custará R$ 25")
elif arealitro2 > 3.6:
    def contalitro(arealitro2):
        latas = arealitro2 / 3.6
        return(latas)
    answer171 = contalitro(arealitro2)
    print("#ES.17 \n Ok! Você precisará de", round(answer171 + 0.5), "galões e isso lhe custará R$", round(answer171 + 0.5) * 25)
else:
    print("#ES.17 \n Então você não me disse o tamanho da área a ser pintada!")

## ES.18
arquivo = float(input("Qual é o tamanho do arquivo para download em MB?"))
velocidade = float(input("Qual é a velocidade do link de Internet em Mbps?"))
print("#ES.18 \n O tempo aproximado de download é de", int(arquivo/velocidade) / 60, "minutos.")

### FIM ###

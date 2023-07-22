#Calculo para superficies divididas em 2 quadrantes


tempo = int(input("digite o tempo em segundos"))
velocidade_Q1 = int(input("digite a velocidade média das linhas de força no quadrante 1 em m/s"))
direcao_Q1 = int(int(input("digite o angulo da direção das linhas de força no quadrante 1  em relação  ao norte")))
viscosidade_Q1 = int(input("digite um valor para viscosidade para o quadrante 1, considerando 1 um valor referencial"))
gravidade = int(input("digite um valor para G considerando G da Terra como 1"))


volume_Q1 = int(input("digite um valor para volume do quadrante 1"))
massa_Q1 = int(input("digite um valor para massa em kg do quadrante 1"))

Y1_Q1 = int(input("digite a distancia inicial no quadrante 1"))
Y2_Q1 = int(input("digite a distancia final no quadrante 1"))

densidade_Q1 = massa_Q1/volume_Q1
dissipacao_Q1 = Y1_Q1/Y2_Q1


NB_numero_de_buracos_Q1 = (tempo*velocidade_Q1*direcao_Q1)/(viscosidade_Q1*gravidade*densidade_Q1)


Soma_de_raios_de_buracos_Q1 =(velocidade_Q1*dissipacao_Q1)/(densidade_Q1*gravidade*viscosidade_Q1)

print ("O número de buracos no quadrante 1 será proporcional a {} e a soma des raios dos buracos  no quadrante 1 será a{}" .format(NB_numero_de_buracos_Q1, Soma_de_raios_de_buracos_Q1))


## CALCULO DO QUADRANTE 2



tempo = int(input("digite o tempo em segundos"))
velocidade_Q2 = int(input("digite a velocidade média das linhas de força no quadrante 2 em m/s"))
direcao_Q2 = int(int(input("digite o angulo da direção das linhas de força no quadrante 2  em relação  ao norte")))
viscosidade_Q2 = int(input("digite um valor para viscosidade para o quadrante 2, considerando 1 um valor referencial"))
gravidade = int(input("digite um valor para G considerando G da Terra como 1"))


volume_Q2 = int(input("digite um valor para volume do quadrante 2"))
massa_Q2 = int(input("digite um valor para massa em kg do quadrante 2"))

Y1_Q2 = int(input("digite a distancia inicial no quadrante 2"))
Y2_Q2 = int(input("digite a distancia final no quadrante 2"))

densidade_Q2 = massa_Q2/volume_Q2
dissipacao_Q2 = Y1_Q2/Y2_Q2


NB_numero_de_buracos_Q2 = (tempo*velocidade_Q2*direcao_Q2)/(viscosidade_Q2*gravidade*densidade_Q2)
Soma_de_raios_de_buracos_Q2 =(velocidade_Q2*dissipacao_Q2)/(densidade_Q2*gravidade*viscosidade_Q2)

print ("O número de buracos no quadrante 2 será proporcional a {} e a soma des raios dos buracos  no quadrante 2 será a{}" .format (NB_numero_de_buracos_Q2, Soma_de_raios_de_buracos_Q2))

## CALCULO DA SOME E MÉDIA DOS QUADRANTES

Soma_total_de_buracos = (NB_numero_de_buracos_Q1+NB_numero_de_buracos_Q2)/2
Soma_total_RB = (Soma_de_raios_de_buracos_Q1+Soma_de_raios_de_buracos_Q2)/2

print("O número de buracos em todo o fluido será proporcional a {} e a soma des raios dos buracos em todo o fluido  será a{}" .format (Soma_total_de_buracos,Soma_total_RB))

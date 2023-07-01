# Navier Stokes Project
 pip instal request
from tkinter import*

tempo = int(input(" Digite o tempo em segundos"))
velocidade  = int(input( "digite a velocidade"))
direcao = int(input(" Digite o angulo da direção em relação ao Norte"))
viscosidade = int(input(" Digite um valor para viscosidade, considerando água destilada a 5 graus celsius como 1"))
gravidade = int(input(" Digite um valor para gravidade, considerando Terra como 1"))

massa = int(input(" Digite um valor para massa"))
volume = int(input(" Digite um valor para volume"))

Y1 = int(input(" Digite um valor para distancia inicial"))
Y2 = int(input(" Digite um valor para distancia final"))

densidade = massa/volume
dissipacao = Y1/Y2
numero_de_buracos = (tempo*velocidade*direcao)/(viscosidade*gravidade*densidade)
soma_de_raios_de_buracos = (velocidade*dissipacao)/(densidade*gravidade*viscosidade)

print("O número de buracos será proporcional a {} e a soma dos raios dos buracos serão proporcionais a {}.format(numero_de_buracos, soma_dos_raios_de_buracos)")

janela = tk()
janela.title(Calculadora Navier Stokes)
texto = label(janela, text = "texto introdutório")
texto.orientacao.grid(colunm =  , row =)

#aqui os inputs

botao = button (janela.text = "calular numero de buracos") command nb
botao.grid(column , row = )
textodoresultadonb = label(janela, text = "o resultado é")
textodoresultado.grid(colmn = , row = )
botao = button (janela, text ="calcular a soma dos raios de buracos")
texto_do resultado_soma_dos_raios_de_buracos = label(janela, text "o resultado é")
texto_do_resultado.grid(column = , row =_)

janela.mainloop()

pip install phyton installer
py installer __onefile -w



pip install request
from thinker import*

tempo = int(input("digite o tempo em segundos"))
velocidade = int(input("digite a velocidade em m/s"))
direcao = int(int(input("digite o angulo da direção em relação ao norte")))
viscosidade = int(input("digite um valor para viscosidade, considerando 1 um valor referencial"))
gravidade = int(input("digite um valor para G considerando G da Terra como 1"))


volume = int(input("digite um valor para volume"))
massa = int(input("digite um vaor para massa em kg"))

Y1 = int(input("digite a distancia inicial"))
Y2 = int(input("digite a distancia final"))

densidade = massa / volume
dissipacao = Y1/Y2

NB_numero_de_buracos = (tempo*velocidade*direcao)/(viscosidade*gravidade*densidade)
Soma_de_raios_de_buracos =(velocidade*dissipacao)/(densidade*gravidade*viscosidade)

print "O número de buracos será proporcional a {} e a soma des raios dos buracos será a {}".format(NB_numero_de_buracos, Soma_de_raios_de_buracos)

janela = tk()
janela.title(calculadora de Navier Stokes)
texto = label(janela,text = "texto introdutório")
texto.orientacao.grid(column= 1, row=0)

botao = button(janela.text = "calcular NB", commandNB)
botao.grid(column=2, row=7)
texto_do_resultado_NB = label(janela,text= "O resultado é")

texto_do_resultado_nb.grid(column=1, row =8)

botao = button(janela,text = " Calcule a Soma dos raios dos buracos")
texto_do_resulrado_SRB = label(janela, text = "O resultado é")
texto_do_resultado.grid (column = 1, row =10)

janela.mainloop()
pipinstall phyton installer
py installer --onefile -while

#copiar arquivos dentro do phycharm
#colar em uma pasta no PC, que vai aparecer como executavel
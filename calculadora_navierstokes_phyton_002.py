from tkinter import *



tempo = int(input("digite o tempo em segundos"))
velocidade = int(input("digite a velocidade em m/s"))
direcao = int(int(input("digite o angulo da direção em relação ao norte")))
viscosidade = int(input("digite um valor para viscosidade, considerando 1 um valor referencial"))
gravidade = int(input("digite um valor para G considerando G da Terra como 1"))


volume = int(input("digite um valor para volume"))
massa = int(input("digite um valor para massa em kg"))

Y1 = int(input("digite a distancia inicial"))
Y2 = int(input("digite a distancia final"))

densidade = massa/volume
dissipacao = Y1/Y2


NB_numero_de_buracos = (tempo*velocidade*direcao)/(viscosidade*gravidade*densidade)

Soma_de_raios_de_buracos =(velocidade*dissipacao)/(densidade*gravidade*viscosidade)
print ("O número de buracos será proporcional a {} e a soma des raios dos buracos será a{}" .format (NB_numero_de_buracos , Soma_de_raios_de_buracos))





root=Tk()
root.geometry("300x700")
root.title("Calculadora de Entropia")
root.config(bg="darkblue")

texto = Label(root,text = "Esta é uma calculadora de entropia para fluidos, digite as informações a seguir e obtenha um valor para o número de buracos no fluido e a soma de seus raios. Siga as equações de Navier Stokes para uma interpretação dos resultados")
texto.grid(column= 1, row=0)

botao = Button(root, text = "calcular NB", command= NB_numero_de_buracos)
botao.grid(column=2, row=7)

texto_do_resultado_NB = Label(root,text= "O resultado é")

texto_do_resultado_NB.grid(column=1, row =8)

botao = Button(root,text = " Calcule a Soma dos raios dos buracos", command= Soma_de_raios_de_buracos)
texto_do_resultado_SRB = Label(root, text = "O resultado é")
texto_do_resultado_SRB.grid (column = 1, row =10)



root.mainloop()

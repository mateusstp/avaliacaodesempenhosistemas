#arquivos alterar "," por "." em valor potencial
dados_mva_aproximado = open("mva_aproximado.txt", "w")


Ni = [0 0]

for i in 3
	


#itenr& 0.030 & $0.07875*10^{-3}$ & $30.07875*10^{-3}$ & 5 & 6 & 7\\[3pt]
#conteudo_texto = f_texto.read()
#insere cabecalho
head = potencial_atmega.readline()
novo_potencial_atmega.write(head)

linha = potencial_atmega.readline()

while linha:
    linhaSemAspas = linha.replace("\"","")
    vetor = linhaSemAspas.split(",")
    newLinha = []
    newLinha.append(vetor[0])
    newLinha.append(",")
    newLinha.append(vetor[1])
    newLinha.append(",")
    newLinha.append(vetor[2])
    newLinha.append('.')
    newLinha.append(vetor[3])
    newLinha.append(",")
    newLinha.append(vetor[4])
    newLinha.append(",")
    newLinha.append(vetor[5])
    #newLinha.append('\n')
    newLinha = ''.join(newLinha)
    print(newLinha)
    novo_potencial_atmega.write(newLinha)
    linha = potencial_atmega.readline()


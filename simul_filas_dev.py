taxa_chegada  = 5#6 #taxa de chegada (quantos clientes chegam por minuto?)
taxa_atendimento = 1.24#1 #taxa de atendimento (em quanto tempo os clientes sao atendidos?)
quantidade_caixas = 4 #quantidade de caixas funcionando inicialmente

tempo_corte = 10 # a cada 10 minutos, se a fila nao se dispersou deve-se operar mais um caixa

tempo_min = 0 #tempo em minutos, comecando em zero

fila_dispersou = False #flag para controle do while, se a fila nao dispersou, continuar a simular

chegada_acc = 0 #chegadas acumuladas, inicialmente zero
atendimento_acc = 0 #partidas acumuladas, inicialmente zero

while fila_dispersou == False: #continuar ate a fila dispersar
	tempo_min = tempo_min + 1 # iteracoes de 1 em 1 minutos
	if tempo_min == tempo_corte: #se atingir o tempo de corte
		quantidade_caixas = quantidade_caixas+1 #operar um caixa adicional
		tempo_corte = tempo_corte+10 #incrementar em mais 10 min o tempo de corte
	chegada_acc = chegada_acc + taxa_chegada #acumulador de chegadas
	atendimento_acc = atendimento_acc + (quantidade_caixas*taxa_atendimento) #acumulador de atendimentos
	fila = chegada_acc - atendimento_acc #claculo do tamanho da fila

	## output visual, apenas pra controle ##
	print('Tempo: {} minutos, Fila: {} clientes, caixas operando: {}'.format(tempo_min,fila, quantidade_caixas))

	if fila <= 0: #se a fila for nula, fim da simulação
		fila_dispersou = True

	if tempo_min == 180: # condicao de saida para caso ultrapasse 3 horas de simulação
		print('A fila nao se dispersou no tempo limite de 3 horas')
		break
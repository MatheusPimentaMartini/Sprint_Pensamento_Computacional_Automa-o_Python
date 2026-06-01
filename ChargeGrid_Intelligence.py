nomes = ["carro 1", "carro 2", "carro 3", ]
baterias = [30, 25, 12]
capacidades = [80, 75, 70]
potencias = [30, 20, 25]
potencias_recebidas = []
energias = []
custos = []
potencia_maxima_rede = 50
veiculo_prioritario = ""
soma_prioridades = 0
soma_potencias = 0
tempo_horas = 1
tarifa_kwh = 2.10
nova_bateria = 0
aumento = 0
def calcular_prioridade(bateria):
    return 100 - bateria 


#calculo de prioridade
def mostrar_prioridades(nomes, baterias):
    for i in range(len(baterias)):
        prioridade = calcular_prioridade(baterias[i])
        print(nomes[i], "--> bateria:", baterias[i], "prioridade:", prioridade)
mostrar_prioridades(nomes, baterias)

#potencia solicitada
def calcular_potencia_total(potencias):
    soma = 0
    for i in range(len(potencias)):
        soma += potencias[i]
    return soma
soma = calcular_potencia_total(potencias)
print("Potência total solicitada:", soma)

#soma de prioridades 
def distribuir_potencia(baterias, potencias, potencia_maxima_rede):
    soma_prioridades = 0
    potencias_recebidas = []
    soma = calcular_potencia_total(potencias)
    if soma <= potencia_maxima_rede:
        for i in range(len(potencias)):
            potencias_recebidas.append(potencias[i])
    else:
        soma_prioridades = 0

        for i in range(len(baterias)):
            prioridade = calcular_prioridade(baterias[i])
            soma_prioridades += prioridade

        for i in range(len(baterias)):
            prioridade = calcular_prioridade(baterias[i])
            proporcao = prioridade / soma_prioridades
            potencia_recebida = potencia_maxima_rede * proporcao

            if potencia_recebida > potencias[i]:
                potencia_recebida = potencias[i]

            potencias_recebidas.append(potencia_recebida)

    return potencias_recebidas

potencias_recebidas = distribuir_potencia(baterias, potencias, potencia_maxima_rede)


def verificar_sobrecarga(soma, potencia_maxima_rede, potencias_recebidas):
    if soma > potencia_maxima_rede:
        print("\nDistribuição Inteligente de Potência")

        for i in range(len(nomes)):
            print(nomes[i], "recebeu", round(potencias_recebidas[i], 2), "kW")
        
        return "Sobrecarga detectada. Potência redistribuída com inteligência."
    else:
        return "Rede operando normalmente"
    
mensagem = verificar_sobrecarga(soma, potencia_maxima_rede,potencias_recebidas)
print(mensagem)

#qual deles tem a maior prioridade 
def encontrar_veiculo_prioritario(nomes, baterias):
    maior_prioridade = 0
    for i in range(len(baterias)):
        prioridade = calcular_prioridade(baterias[i])

        if prioridade > maior_prioridade:
            maior_prioridade = prioridade
            veiculo_prioritario = nomes[i]

    return veiculo_prioritario, maior_prioridade
veiculo_prioritario, maior_prioridade = encontrar_veiculo_prioritario(nomes, baterias)
print(f"Veículo prioritário: {veiculo_prioritario} | Prioridade: {maior_prioridade}")



#energia entregue
def calcular_energias(potencias_recebidas, tempo_horas):
    energias = []

    for i in range(len(potencias_recebidas)):
        energia = potencias_recebidas[i] * tempo_horas
        energias.append(energia)

    return energias
energias = calcular_energias(potencias_recebidas, tempo_horas)

#Tarifação

def calcular_custos(energias, tarifa_kwh):
    custos = []

    for i in range(len(energias)):
        custo = energias[i] * tarifa_kwh
        custos.append(custo)

    return custos
custos = calcular_custos(energias, tarifa_kwh)

#Calculo de nova bateria

def calcular_nova_bateria(bateria_atual, capacidade_bateria, energia_entregue):
    aumento_percentual = (energia_entregue / capacidade_bateria) * 100
    nova_bateria = bateria_atual + aumento_percentual
    if nova_bateria > 100:
        nova_bateria = 100
    return nova_bateria

#RELATORIO FINAL
def gerar_relatorio(nomes, baterias, capacidades, potencias_recebidas, energias, custos):
    for i in range(len(nomes)):
        nova_bateria = calcular_nova_bateria(baterias[i],capacidades[i],energias[i])
        print("=================================")
        print("ChargeGrid Intelligence - Simulador de Recarga Inteligente")
        print(f"Veículo: {nomes[i]}")
        print(f"Bateria inicial: {baterias[i]}%")
        print(f"Bateria final: {nova_bateria:.2f}%")
        print(f"Potência recebida: {potencias_recebidas[i]:.2f} kW")
        print(f"Energia entregue: {energias[i]:.2f} kWh")
        print(f"Custo: R$ {custos[i]:.2f}")
        print("=================================")

gerar_relatorio(nomes, baterias, capacidades, potencias_recebidas, energias, custos)
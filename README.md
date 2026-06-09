# ChargeGrid Intelligence

### Integrantes

* Leonardo Soares Rodrigues RM:572986 
* Matheus Pimenta RM:569400
* Rubens Henrique RM 572667
* Guilherme Cedro RM: 571050
* Gabriel Carvalho RM: 571381
* Eduardo dos Reis Santos RM: 572514

---

# Sobre o Projeto

O ChargeGrid Intelligence é uma solução desenvolvida para o EV Challenge 2026 da GoodWe em parceria com a FIAP.

O projeto tem como objetivo transformar uma solução residencial de carregamento de veículos elétricos em uma solução comercial inteligente, capaz de gerenciar múltiplas sessões de recarga simultaneamente, evitando sobrecargas na rede elétrica e otimizando a distribuição de energia.

---

# Problema

Em estações de recarga comerciais, diversos veículos podem solicitar carregamento ao mesmo tempo.

Quando a potência total demandada ultrapassa a capacidade disponível da rede elétrica, podem ocorrer:

* Sobrecarga da infraestrutura;
* Queda de eficiência energética;
* Aumento dos custos operacionais;
* Experiência negativa para os usuários.

---

# Solução Proposta

O ChargeGrid Intelligence implementa uma lógica de gerenciamento inteligente de demanda energética.

O sistema analisa o nível de bateria dos veículos conectados e distribui a potência disponível de forma proporcional à necessidade de cada veículo.

Veículos com menor carga de bateria recebem maior prioridade durante a distribuição da energia.

---

# Funcionalidades Implementadas

## Priorização Inteligente

O sistema calcula uma prioridade para cada veículo com base no nível atual da bateria.

Quanto menor a bateria, maior a prioridade.

## Gerenciamento de Demanda

Quando a potência total solicitada ultrapassa o limite da rede elétrica, o sistema realiza uma redistribuição automática da potência disponível.

## Distribuição Inteligente de Potência

A potência é distribuída proporcionalmente à prioridade calculada para cada veículo.

## Cálculo de Energia Entregue

O sistema calcula a quantidade de energia fornecida para cada veículo durante a sessão de recarga.

## Tarifação

O custo da recarga é calculado automaticamente com base na energia consumida e na tarifa definida.

## Relatório Final

* Veículo atendido;
* Bateria inicial;
* Bateria final;
* Potência recebida;
* Energia entregue;
* Valor da recarga.

---

# Arquitetura da Solução

1. Cadastro dos veículos
2. Leitura do nível de bateria
3. Cálculo das prioridades
4. Verificação da potência total solicitada
5. Identificação de sobrecarga
6. Redistribuição inteligente da potência
7. Cálculo da energia entregue
8. Cálculo da cobrança
9. Geração do relatório final

---

# Tecnologias Utilizadas

* Python
* GitHub
* Trello (Kanban)

---

# Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/ChargeGrid-Intelligence.git
```

Acesse a pasta do projeto:

```bash
cd ChargeGrid-Intelligence
```

Execute o sistema:

```bash
python main.py
```

---

# Diferenciais do Projeto

* Gerenciamento inteligente de demanda energética;
* Priorização automática de veículos;
* Simulação de tarifação;
* Estrutura escalável para eletropostos comerciais;
* Alinhamento com soluções de energia inteligente da GoodWe.

---

# Projeto Desenvolvido para o EV Challenge 2026

Parceria entre FIAP e GoodWe Technologies.

Desafio: Transformar uma solução residencial de carregamento de veículos elétricos em uma solução comercial inteligente com gerenciamento energético eficiente.

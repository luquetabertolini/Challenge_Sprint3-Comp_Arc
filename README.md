Sistema Inteligente de Controle de Sessão de Recarga

Plataforma: Simulador Wokwi  
Disciplina: Computer Organization and Architeture

Integrantes do Grupo
- Lucca Bertolini - RM: 569552
- Cristhian Henrique Clementino - RM: 574117
- Raphaello Caffettani  - RM: 572334
- Diego Brandão de Oliveira - RM: 569773
- Fabio Pena Viera - RM: 570441


Descrição do Projeto
Este projeto consiste no desenvolvimento de um prototipo funcional de gerenciamento e controle inteligente de recarga de veiculos eletricos. O sistema le/simula dados de geracao de energia solar e consumo residencial, calcula a potencia disponivel e determina o status da recarga em tempo real.


Cenarios de Operacao e Saidas (LEDs)
Cenario de Carga Total: Quando a geracao solar supera o consumo da residencia com sobra igual ou superior a 1000W (ex: 4000W gerados para 1500W consumidos), o sistema calcula 2500W disponiveis, aprova o status RECARGA AUTORIZADA e energiza o pino GPIO15 (LED Verde).

Cenario de Carga Parcial: Quando a geracao solar cobre o consumo mas a sobra fica entre 0W e 999W (ex: 1800W gerados para 1500W consumidos), o sistema calcula 300W disponiveis, altera o status para RECARGA REDUZIDA e energiza o pino GPIO14 (LED Amarelo).

Cenario de Interrupcao de Carga: Quando o consumo residencial excede a geracao solar (ex: 1000W gerados para 1800W consumidos), a ULA processa um saldo negativo (-800W), define o status como RECARGA BLOQUEADA e energiza o pino GPIO13 (LED Vermelho).


Mapeamento do Hardware (Pinout)

* LED Verde: Pino GPIO15 (Resistor 220 Ohm)
* LED Amarelo: Pino GPIO14 (Resistor 220 Ohm)
* LED Vermelho: Pino GPIO13 (Resistor 220 Ohm)
* Catodo dos LEDs: Pino GND (Pino 38 da Pico)



Relação com Conceitos de Arquitetura de Computadores

1. Entrada e Saida (E/S):
   - Entrada: Dados simulados de potencia inseridos no sistema.
   - Saida: Sinalizacao fisica via LEDs atraves das portas GPIO e exibicao de logs no Terminal Serial via comunicacao USB.
2. Processamento (CPU e ULA):
   - A Unidade Logica e Aritmetica (ULA) executa o calculo de diferenca energetica (Disponivel = Geracao - Consumo).
   - As estruturas condicionais (if/elif/else) sao processadas via instrucoes de salto condicional (branching) no processador ARM Cortex-M0+.
3. Memoria e Representacao de Dados:
   - Dados numericos processados e armazenados nos registradores e na memoria RAM.
   - Demonstracao da transcodificacao de valores entre Decimal, Binario (representacao nativa em memoria) e Hexadecimal.

---

Links Uteis
- Link da Simulacao no Wokwi: https://wokwi.com/projects/473460269509542913
- Link do Video no YouTube: https://youtu.be/7L5jvjhxZ-I

import time
from machine import Pin

# Configuração dos Pinos de Saída (E/S - Output)
led_verde = Pin(15, Pin.OUT)
led_amarelo = Pin(14, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)


def apagar_leds():
    """Garante apenas um LED aceso por ciclo."""
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)


def exibir_representacao_dados(valor):
    """Demonstra a representação de dados (Decimal, Binário, Hexadecimal)."""
    val_abs = abs(valor)
    bin_str = bin(val_abs)[2:]
    hex_str = hex(val_abs)[2:].upper()

    print(f"--- REPRESENTAÇÃO DE DADOS (Disponível: {valor}W) ---")
    print(f"Decimal:     {valor}")
    print(
        f"Binário:     {'-' if valor < 0 else ''}{bin_str} (base 2 em memória)"
    )
    print(f"Hexadecimal: {'-' if valor < 0 else ''}{hex_str}")
    print("-" * 50)


def processar_recarga(geracao, consumo):
    apagar_leds()

    # Processamento na ULA (Unidade Lógica e Aritmética)
    disponivel = geracao - consumo

    # Formatação de Saída Terminal
    print("\n========================================")
    print(f"GERACAO:    {geracao} W")
    print(f"CONSUMO:    {consumo} W")
    print(f"DISPONIVEL: {disponivel} W")
    print("STATUS:     ", end="")

    # Tomada de Decisão (Desvios Condicionais)
    if disponivel >= 1000:
        print("RECARGA AUTORIZADA")
        led_verde.value(1)
    elif 0 <= disponivel < 1000:
        print("RECARGA REDUZIDA")
        led_amarelo.value(1)
    else:
        print("RECARGA BLOQUEADA")
        led_vermelho.value(1)

    print("========================================")
    exibir_representacao_dados(disponivel)


# --- SIMULAÇÃO DOS TRÊS CENÁRIOS (Loop Principal) ---
cenarios = [
    {"geracao": 4000, "consumo": 1500},  # Situação 1: Suficiente (Verde)
    {"geracao": 1800, "consumo": 1500},  # Situação 2: Limitada (Amarelo)
    {"geracao": 1000, "consumo": 1800},  # Situação 3: Insuficiente (Vermelho)
]

print("Iniciando Sistema Inteligente de Recarga GoodWe (Simulado)...\n")
time.sleep(1)

while True:
    for cenario in cenarios:
        processar_recarga(cenario["geracao"], cenario["consumo"])
        time.sleep(4)  # Espera 4 segundos para cada cenário

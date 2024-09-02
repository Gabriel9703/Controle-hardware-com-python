import psutil
import time

def mapeamento_rede():
    rede = psutil.net_if_addrs()
    for interface, endereco in rede.items():
        print(f'Interface : {interface}')
        for e in endereco:
            print(f'Endereço : {e.address}')
            print(f'Tipo : {e.family}')
            print(f'Máscara : {e.netmask}')
            print(f'Broadcast : {e.broadcast}')
mapeamento_rede()
def pacotes_rede():
    rede = psutil.net_io_counters()
    recebido = rede.bytes_recv / (1024 * 1024)
    print(f'Dados recebidos : {recebido:.2f} MB')
    enviado = rede.bytes_sent / (1024 * 1024)
    print(f'Dados enviados : {enviado:.2f} MB')
    pacotes_recebidos = rede.packets_recv
    print(f'Pacotes recebidos : {pacotes_recebidos}')
    pacotes_enviados = rede.packets_sent
    print(f'Pacotes enviados : {pacotes_enviados}')
    erros_recebidos = rede.errin
    print(f'Erros recebidos : {erros_recebidos}')
    erros_enviados = rede.errout
    print(f'Erros enviados : {erros_enviados}')
    print("-" * 30)
try:
    while True:
        pacotes_rede()
        time.sleep(5)  

except KeyboardInterrupt:
    print('Saindo...')
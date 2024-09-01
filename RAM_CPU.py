import psutil
import time
from datetime import datetime

"""
Monitoramento da RAM e CPU em captura de log quando 
determinado valor de ocupção é atingido

"""
  

def memoria_CPU():
     
    vm = psutil.virtual_memory()
    total_mem_virt = vm.total / (1024**3)
    mem_disponivel = vm.available / (1024**3)
    mem_usada = vm.used / (1024**3)
    perct_memor = vm.percent
    cpu = psutil.cpu_percent(interval=1)

    print("-"* 30)
    print(f"Memoria Total: {total_mem_virt:.2f} GB")
    print(f'Memoria Disponivel: {mem_disponivel:.2f} GB')
    print(f'Memoria Usada: {mem_usada:.2f} GB')
    print(f'Percentual de memoria em uso {perct_memor}%')
    print(f'CPU usado: {cpu}%')
    print("-"* 30)

    if cpu > 90 or perct_memor > 90:
        with open("cpu_mem_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} - CPU: {cpu}% - Memoria: {perct_memor}%\n")

    return True


try:    
    while True:
        uso = memoria_CPU()
        time.sleep(1)
except KeyboardInterrupt:
    print("Controle finalizado")
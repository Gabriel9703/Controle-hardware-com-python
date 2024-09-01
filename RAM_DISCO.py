import psutil
import time
"""
Script para verificar o uso da memoria RAM 
e dos discos em intervalos de 10 segs
"""

  

def memoria():
     
    vm = psutil.virtual_memory()
    total_mem_virt = vm.total / (1024**3)
    mem_disponivel = vm.available / (1024**3)
    mem_usada = vm.used / (1024**3)
    perct_memor = vm.percent

    print("-"* 30)
    print(f"Memoria Total: {total_mem_virt:.2f} GB")
    print(f'Memoria Disponivel: {mem_disponivel:.2f} GB')
    print(f'Memoria Usada: {mem_usada:.2f} GB')
    print(f'Percentual de memoria em uso {perct_memor}%')
    print("-"* 30)

    return True


def info_disco():
    discos = psutil.disk_io_counters(perdisk=True)
    for disco, estatis in discos.items():
        print(f"Disco: {disco}")
        print(f"Bytes Lidos: {estatis.read_bytes / (1024**3):.2f} GB")
        print(f"Bytes Escritos: {estatis.write_bytes / (1024**3):.2f} GB")
        print(f"Contagem de Leitura: {estatis.read_count}")
        print(f"Contagem de Escrita: {estatis.write_count}")
        print(f"Tempo de Leitura: {estatis.read_time} ms")
        print(f"Tempo de Escrita: {estatis.write_time} ms")
        print("-" * 30)

try:    
    while True:
        uso_RAM = memoria()
        uso_disco = info_disco()
        time.sleep(10)
except KeyboardInterrupt:
    print("Controle finalizado")





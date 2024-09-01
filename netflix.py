import psutil
import time

mapeamento = psutil.cpu_times()
print(mapeamento)
# for x in range(3):
#     control = psutil.cpu_percent(interval=1)
  
#     print(control)
# conta = psutil.cpu_count()
# # print(conta)
# print(psutil.swap_memory())
# print(psutil.virtual_memory())
# print(psutil.cpu_times_percent(interval=1))
print(psutil.cpu_count(logical=True))
print(psutil.cpu_count(logical=False))
## CPU utilizaveis
print(len(psutil.Process().cpu_affinity()))
print(psutil.cpu_stats())
print(psutil.cpu_freq(percpu=True))
print(psutil.getloadavg())
mem = psutil.virtual_memory()
mom = psutil.swap_memory()
print(mom)
print(mem)
con = 100 * 1024*1024
if mem.available < con:
    print("Perigo")
import psutil

# Informações sobre a memória virtual (RAM + Swap)
vm = psutil.virtual_memory()
print(f"Total Virtual Memory: {vm.total / (1024**3)}")
nome =  vm.available / (1024**3)
print(f'Disponivel {nome:.2f}GB')
print(f"Used Virtual Memory: {vm.used} GB")
print(f"Memory Usage Percentage: {vm.percent}%")

# Informações sobre a memória swap
swap = psutil.swap_memory()
print(f"Total Swap: {swap.total}")
print(f"Used Swap: {swap.used}")
print(f"Free Swap: {swap.free}")
print(f"Swap Usage Percentage: {swap.percent}%")

# def monitorar_sitema(intervalo=1):
#     try:
#         while True:
#             porcento_cpu = psutil.cpu_percent(interval=1)
#             info_memoria = psutil.virtual_memory()
#             porcento_memoria = info_memoria.percent
#             total_memoria = info_memoria.total / (1024 ** 3)
#             uso_memoria = info_memoria.used / (1024 ** 3)

#             print(f'Uso do CPU: {porcento_cpu}%')
#             print(f'Uso da memoria: {porcento_memoria}% (Usado: {uso_memoria:.2f} GB / Total: {total_memoria:.2f} GB)')
#             print("-"* 40)

#             time.sleep(intervalo)
#     except KeyboardInterrupt:
#         print("Monitoramento encerrado")   


# if __name__ == "__main__":
#     sistema = monitorar_sitema(intervalo=5)
                
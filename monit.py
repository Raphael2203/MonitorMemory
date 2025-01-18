import psutil
import time
import gc
from plyer import notification

def monitor_memory(interval=60, threshold=80):
    print("Iniciando monitoramento de memória em segundo plano...")
    try:
        while True:
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            print(f"Uso da memória: {memory_usage}%")

            if memory_usage >= threshold:
                notification.notify(
                    title='Alerta de memória',
                    message=f'O uso da memória RAM atingiu {memory_usage}%',
                    timeout=10
                )
                print("Limpando a memória...")
                gc.collect()
                memory_info = psutil.virtual_memory()
                memory_usage = memory_info.percent
                print(f"Uso da memória após limpeza: {memory_usage}%")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoramento da memória interrompido.")

if __name__ == "__main__":
    monitor_memory()
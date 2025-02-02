import psutil
import time
import gc
from plyer import notification
import tkinter as tk
from tkinter import messagebox
import threading
import os
import shutil
import getpass

def monitor_memory(interval=60, threshold=80):
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    memory_label.config(text=f"Uso da memória: {memory_usage}%")

    if memory_usage >= threshold:
        notification.notify(
            title='Alerta de memória',
            message=f'O uso da memória RAM atingiu {memory_usage}%',
            timeout=10
        )
        gc.collect()
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        memory_label.config(text=f"Uso da memória após limpeza: {memory_usage}%")

    root.after(interval * 1000, monitor_memory, interval, threshold)

def start_monitoring():
    interval = int(interval_entry.get())
    threshold = int(threshold_entry.get())
    monitoring_thread = threading.Thread(target=monitor_memory, args=(interval, threshold))
    monitoring_thread.daemon = True
    monitoring_thread.start()

def add_to_startup():
    script_path = os.path.abspath("monit.py")
    startup_folder = os.path.join(
        "C:\\", "Users", getpass.getuser(), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup" 
    )
    powershell_script = f"""
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("{os.path.join(startup_folder, 'monit.lnk')}")
    $Shortcut.TargetPath = "{script_path}"
    $Shortcut.Save()
    """

    powershell_path = os.path.join(startup_folder, "add_to_startup.ps1")
    with open(powershell_path, "w") as file:
        file.write(powershell_script)

    os.system(f'powershell --ExecutionPolicy Bypass --File "{powershell_path}"')
    messagebox.showinfo("Sucesso", "O aplicativo foi adicionado à inicialização do sistema.")

root = tk.Tk()
root.title("Monitor de memória")

interval_label = tk.Label(root, text="Intervalo (segundos):")
interval_label.pack()
interval_entry = tk.Entry(root)
interval_entry.pack()
interval_entry.insert(0, "60")

threshold_label = tk.Label(root, text="Limite de uso da memória (%):")
threshold_label.pack()
threshold_entry = tk.Entry(root)
threshold_entry.pack()
threshold_entry.insert(0, "80")

start_button = tk.Button(root, text="Iniciar Monitoramento", command=start_monitoring)
start_button.pack()

memory_label = tk.Label(root, text="Uso da memória: 0%")
memory_label.pack()

startup_button = tk.Button(root, text="Definir Aplicativo em Segundo Plano", command=add_to_startup)
startup_button.pack()

root.mainloop()
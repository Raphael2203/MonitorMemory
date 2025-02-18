# Monitoramento de Memória RAM

## Descrição
Este projeto é um script em Python para monitorar o uso de memória RAM em seu sistema. Quando o uso de memória atinge um limite especificado, o script tenta liberar a memória e notifica o usuário através de uma notificação na área de trabalho.

## Funcionalidades
- Monitora continuamente o uso de memória RAM.
- Notifica o usuário quando o uso de memória atinge o limite especificado.
- Tenta limpar a memória quando o limite é atingido.
- Ajusta automaticamente o intervalo de monitoramento.

## Requisitos
- Python 3.x
- Bibliotecas Python: `psutil`, `plyer`

## Instalação
1. Clone este repositório:
    ```sh
    git clone https://github.com/Raphael2203/MonitorMemory.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd SEU_REPOSITORIO
    ```
3. Instale as dependências:
    ```sh
    pip install psutil plyer
    ```

## Uso
Execute o script `monitor_memory.py` para iniciar o monitoramento de memória:
```sh
python monitor_memory.py

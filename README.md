# Escáner de Puertos en Python

Este es un escáner de puertos básico escrito en Python. Permite verificar si un conjunto específico de puertos en una dirección IP están abiertos o cerrados. El script utiliza sockets para intentar establecer una conexión TCP con cada puerto de la lista predefinida y reportar su estado.

## Características

- Escanea puertos TCP.
- Permite personalizar la dirección IP de destino.
- Indica si los puertos están abiertos o cerrados.
- Fácil de entender y modificar.

## Requisitos

- Python 3.x
- Módulos estándar de Python: `socket`

## Instalación

1. Clona este repositorio en tu máquina local o descarga el archivo `port_scanner.py`:

    ```bash
    git clone https://github.com/mauq91/escaner-de-puertos.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd escaner-puertos
    ```

3. No se necesitan dependencias adicionales, ya que el script solo utiliza módulos estándar de Python.

## Uso

1. Abre el archivo `escaner-puertos.py` y configura la lista de puertos que deseas escanear. Actualmente, los puertos predeterminados son:

    ```python
    puertos = [22, 80, 443]  # Puedes agregar o quitar puertos aquí
    ```

2. Ejecuta el script:

    ```bash
    python3 escaner-puertos.py
    ```

3. Cuando se te solicite, ingresa la dirección IP de destino que deseas escanear:

    ```bash
    Ingrese dirección IP: 192.168.1.1
    ```

4. El escáner intentará conectarse a cada puerto en la lista y te mostrará si está abierto o cerrado.

## Ejemplo de Salida

```bash
Ingrese dirección IP: 192.168.1.1
Puerto Abierto: 22
Puerto Cerrado: 80
Puerto Abierto: 443

Personalización

    Lista de Puertos: Puedes agregar o eliminar puertos de la lista puertos según lo que desees escanear.

    python

puertos = [21, 22, 23, 80, 443]  # Ejemplo con más puertos

Timeout de Conexión: Puedes ajustar el tiempo de espera para cada intento de conexión modificando la línea:

python

    sock.settimeout(5)  # El tiempo de espera actual es de 5 segundos

Mejoras Futuras

Este script es básico, pero puedes añadir más características como:

    Escaneo de rangos de puertos.
    Soporte para escaneo UDP.
    Escaneo de múltiples IPs de manera concurrente.
    Detección del sistema operativo o versión de software detrás de los puertos abiertos (fingerprinting).
    Reportes más detallados o guardados en un archivo.

Contribuciones

Si deseas mejorar este proyecto o añadir nuevas características, sigue estos pasos:

    Haz un fork del repositorio.
    Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
    Realiza los cambios y haz commit (git commit -m 'Añade nueva característica').
    Haz push a la rama (git push origin feature/nueva-caracteristica).
    Abre un Pull Request.

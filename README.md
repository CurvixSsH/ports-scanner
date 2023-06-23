# Actualizacion 
Escanea los 65.535 puertos en menos de 45 segundos. (Imagen 1)

Escaneo de puertos personalizado (imagen 2)

Escaneo de puertos personalizado atraves de un proxy (Imagen 3)

# 1
![imagen_2023-06-23_040643343](https://github.com/CurvixSsH/ports-scanner/assets/127477293/3a75c4c0-1b3b-4522-9faa-5e601c84fb2a)

# 2
![imagen_2023-06-23_033650649](https://github.com/CurvixSsH/ports-scanner/assets/127477293/656996b2-3d07-4502-a2cd-bf68592d634f)

# 3
![por222](https://github.com/CurvixSsH/ports-scanner/assets/127477293/b410e944-9e76-43c2-a506-1126ce89969f)



# Ports-scanner

Este código de escaneo de puertos permite al usuario escanear un rango de puertos en una dirección IP o nombre de host dado. Además, se ha implementado el uso opcional de un proxy para aumentar el anonimato del usuario. Si se utiliza la opción "-pn", el programa no intentará hacer ping a la dirección IP o nombre de host antes de escanear los puertos, lo que puede ser útil en situaciones donde se desea evitar la detección por parte de los sistemas de seguridad. El escaneo de puertos tarda menos de 50 segundos en escanear los 65535 puertos y utiliza subprocesos para escanear múltiples puertos simultáneamente, lo que lo hace más rápido que los escáneres de puertos de un solo subproceso. También arroja el servicio y protocolo de los puertos más conocidos almacenados en un archivo donde puedes agregar mas puertos serv a la lista. En resumen, este escáner de puertos es una herramienta útil y eficiente para aquellos que necesitan escanear múltiples puertos simultáneamente de manera rápida y confiable

# Librerias

pip3 install -r requirements.txt

# Instalacion

git clone https://github.com/CurvixSsH/ports-scanner.git

cd ports-scanner

pip3 install -r requirements.txt

python port.py -h o python3 port.py -h

# Ejemplo

python port.py google.com

python port.py (Target)

python port.py (Target) -pn

python port.py (Target) -px [protocolo://]host[:puerto]

python port.py (Target) -p 1-10467,56888,64344 -t 800 -to 1 -px [protocolo://]host[:puerto]

#PROXY -px

[protocolo://]host[:puerto]

Protocolos: HTTP, HTTPS, SOCKS4 o SOCKS5

Ejemplo= socks5://192.168.1.1:80

Proxys gratis: https://hidemy.name/es/proxy-list/

#COMANDOS
-p : rango de puertos (predeterminado) 65535

-pn : se omite la fase de descubrimiento del host (ping)

-t : número de hilos o threads que se utilizarán para realizar el escaneo de puertos. Especifica la cantidad de hilos simultáneos que se ejecutarán para acelerar el escaneo. (predeterminado) 850 threads

-to : tiempo de espera o timeout de conexión en segundos (predeterminado) 0.5s

-px : se utiliza para especificar un proxy en el escaneo de puertos. [protocolo://]host[:puerto]








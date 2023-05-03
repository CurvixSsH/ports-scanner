![git port 11](https://user-images.githubusercontent.com/127477293/235881118-dfe32068-418a-4e82-ae26-c88916be22dc.png)

![2222333322](https://user-images.githubusercontent.com/127477293/235887436-a01435c0-0a56-4d5d-a28d-f14f9865ce3c.png)


# Ports-scanner

Este código de escaneo de puertos permite al usuario escanear un rango de puertos en una dirección IP o nombre de host dado. Además, se ha implementado el uso opcional de un proxy para aumentar el anonimato del usuario. Si se utiliza la opción "-pn", el programa no intentará hacer ping a la dirección IP o nombre de host antes de escanear los puertos, lo que puede ser útil en situaciones donde se desea evitar la detección por parte de los sistemas de seguridad. El escaneo de puertos tarda menos de 50 segundos en escanear los 65535 puertos y utiliza subprocesos para escanear múltiples puertos simultáneamente, lo que lo hace más rápido que los escáneres de puertos de un solo subproceso. También arroja el servicio y protocolo de los puertos más conocidos almacenados en un archivo donde puedes agregar mas puertos serv a la lista. En resumen, este escáner de puertos es una herramienta útil y eficiente para aquellos que necesitan escanear múltiples puertos simultáneamente de manera rápida y confiable

# Librerias

pip3 install -r requirements.txt

# Instalacion

git clone https://github.com/CurvixSsH/ports-scanner.git

cd ports-scanner

pip3 install -r requirements.txt

python port.py -h

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







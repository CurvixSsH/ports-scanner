# ports-scanner

El código es un programa de escaneo de puertos en Python que utiliza sockets para probar la conectividad a través de los puertos TCP en una dirección ip en alrededor de 50 segundos

#Librerias

pip install argparse socket threading queue time pyfiglet

#INSTALACION

git clone https://github.com/CurvixSsH/ports-scanner.git

cd ports-scanner

python port.py (Host)

#EJEMPLO

python port.py google.com

Al escanner se le añadio una funcion de nmap por defecto -Pn que permite saltar el descubrimiento de host y escanear directamente los puertos de un objetivo especificado mediante su dirección IP o nombre de host. asi el programa no realizará una verificación previa para ver si el host está activo antes de intentar escanear los puertos. Esto puede ahorrar tiempo si ya se sabe que el host está activo y se desea escanear sus puertos abiertos. tambien sirve para no alertar a un servidor que estas escaneando los puertos..

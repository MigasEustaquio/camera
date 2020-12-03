#!/bin/bash

RED='\033[0;31m'
GRE='\033[0;32m'
NC='\033[0m' # No Color

printf "\n${NC}Atualizando repositórios...\n\n"
if ! sudo apt-get update
then
    printf "\n${RED}Não foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}Atualização feita com sucesso.${NC}\n\n"


printf "\n${NC}Atualizando pacotes já instalados.\n\n"
if ! sudo apt-get upgrade
then
    printf "\n${RED}Não foi possível atualizar pacotes.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}Atualização de pacotes feita com sucesso.${NC}\n\n"


printf "\n${NC}Instalando PiCamera\n\n"
if ! pip3 install picamera
then
    printf "\n${RED}Não foi possível instalar o PiCamera.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}PiCamera instalado com sucesso.${NC}\n\n"


printf "\n${NC}Instalando Image${NC}\n\n"
if ! pip install image
then
    printf "\n${RED}Não foi possível instalar o Image.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}Image instalado com sucesso.${NC}\n\n"


printf "\n${NC}Instalando Contrib\n\n"
if ! pip install opencv-contrib-python==4.1.0.25
then
    printf "\n${RED}Não foi possível instalar o Contrib.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}Contrib instalado com sucesso.${NC}\n\n"


printf "\nInstalando pacote gTTS.\n\n"
if ! pip3 install gTTS
then
    printf "\nNão foi possível instalar o pacote gTTS.\n\n"
    exit 1
fi
printf "\nPacote gTTS instalado com sucesso.\n\n"



printf "\n${NC}Instalando GPIO\n\n"
cd gpio
if ! python3 setup.py install
then
    printf "\n${RED}Não foi possível instalar o GPIO.${NC}\n\n"
    exit 1
fi
printf "\n${GRE}GPIO instalado com sucesso.${NC}\n\n"





printf "\n${GRE}Instalação finalizada${NC}\n\n"

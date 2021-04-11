# -*- coding: utf-8 -*-

###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
###SCRIPT FEITO POR FATALSEC###
import os
import time
import random
social = ('\033[31m'+'''
     _______.  ______     ______  __       ___       __      
    /       | /  __  \   /      ||  |     /   \     |  |     
   |   (----`|  |  |  | |  ,----'|  |    /  ^  \    |  |     
    \   \    |  |  |  | |  |     |  |   /  /_\  \   |  |     
.----)   |   |  `--'  | |  `----.|  |  /  _____  \  |  `----.
|_______/     \______/   \______||__| /__/     \__\ |_______|
                                                             '''+'\033[0;0m')
 
tools = ('\033[1;92m'+'''
.___________.  ______     ______    __          _______.
|           | /  __  \   /  __  \  |  |        /       |
`---|  |----`|  |  |  | |  |  |  | |  |       |   (----`
    |  |     |  |  |  | |  |  |  | |  |        \   \    
    |  |     |  `--'  | |  `--'  | |  `----.----)   |   
    |__|      \______/   \______/  |_______|_______/    
                                                    
'''+'\033[0;0m')


print (social + tools)
print ('\033[31m'+'Feito por'+'\033[0;0m', '\033[1;92m'+'FATALSEC'+'\033[0;0m')
print (' ')
print ('\033[1;92m'+'Pressione ENTER para continuar'+'\033[0;0m')

input(' ') 
os.system('clear') #host fatalsec.arch@user/down1111.socketopen
print (social + tools)
print ('\033[31m'+'Ferramenta programada para auxiliar no pentest/engenharia social'+'\033[0;0m')
time.sleep(1)

H = ('\033[30m'+'H'+'\033[0;0m')
A = ('\033[32m'+'A'+'\033[0;0m')
C = ('\033[33m'+'C'+'\033[0;0m')
K = ('\033[34m'+'K'+'\033[0;0m')
I = ('\033[35m'+'I'+'\033[0;0m')
N = ('\033[36m'+'N'+'\033[0;0m')
G = ('\033[37m'+'G'+'\033[0;0m')

um = ('\033[31m'+'[1]'+'\033[0;0m')
dois = ('\033[31m'+'[2]'+'\033[0;0m')
tres = ('\033[31m'+'[3]'+'\033[0;0m')
quatro = ('\033[31m'+'[4]'+'\033[0;0m')
cinco = ('\033[31m'+'[5]'+'\033[0;0m')
seis = ('\033[31m'+'[6]'+'\033[0;0m')
print ('\033[31m'+'GOOD'+'\033[0;0m', H+A+C+K+I+N+G)

time.sleep(1)
os.system("clear")
print (
um, 'EMAIL TEMPORARIO',)

print (" ")

print (
dois, 'GERADOR DE CPF',)

print (" ")

print (
tres, 'GERADOR DE NOMES (FORA DO AR)',)
print (" ")

print (
quatro, 'OBTER INFORMAÇÕES DO IP/DOMÍNIO',)
print (" ")

print (
cinco, 'CONTATO',)
print (" ")
print (seis, 'INFORMAÇÕES',)
print (" ")
while True:
    #trueopen.fatalsec@arch
    option = int(input("digite o numero de alguma opção: "))
    if option == 1: 
      print ("EMAIL TEMPORARIO")
      time.sleep(2)
      os.system('clear')
      from bs4 import BeautifulSoup
      from urllib.request import urlopen
      html = urlopen("https://generator.email/")
      email = BeautifulSoup(html, 'html.parser')
      email1 = (email.find('span', id="email_ch_text").text)
      print ('\033[31m'+'SEU EMAIL:'+'\033[0;0m', email1)
      print (' ')
      print ('\033[31m'+'PARA ACESSAR:'+'\033[0;0m', "https://generator.email/"+ email1)
      break
    if option == 2:
      import random
      print ('GERADOR DE CPF')
      time.sleep(3)
      os.system('clear')
      cpf1=('327.','350.','502.','802.','102.','205.')
      cpf2=('492.','302.','901.','552.','300.','422.','100.')
      cpf3=('604','308','702','008','242','909','105')
      cpf4=('-21','-12','-52','-90','-22','-99','-30','-43',)
      cpf="".join(random.choice(cpf1)+""+random.choice(cpf2)+random.choice(cpf3)+random.choice(cpf4)  for _ in range(1))
      print (' ')
      print ('\033[31m'+'SEU CPF:'+'\033[0;0m', cpf)
      break
    if option == 3:
      print ("está fora do ar!")
      break
    if option == 4:
      from bs4 import BeautifulSoup
      from urllib.request import urlopen
      time.sleep(3)
      os.system('clear')
      url = 'https://api.ipify.org'

      response = urlopen(url)
      html = response.read()
      meuip = BeautifulSoup(html, 'html.parser')
      print (' ')
      print ('\033[31m'+'SEU IP:'+'\033[0;0m', meuip)
      import socket
      import whois
      import os
      from urllib.request import Request, urlopen
      from urllib.error import URLError, HTTPError
      print (" ")
      alvo = input("alvo: ")
      w = whois.whois(alvo)
      time.sleep(2)
      print ("TESTANDO CONEXÃO...")
      print (" ")
      try:
         response = urlopen("https://" + alvo)
      except HTTPError as e:
         print("SERVIDOR ESTÁ", '\033[1;31m'+'FORA DO AR'+'\033[0;0m')
         print ("CÓDIGO DE ERRO: ", e.code)
         break
      except URLError as e:
         print("SERVIDOR ESTÁ", '\033[1;31m'+'FORA DO AR'+'\033[0;0m')
         print ("CÓDIGO DE ERRO: ", e.reason)
         break
      else:
         time.sleep(4)
         print (" ")
         print("SERVIDOR ESTÁ", '\033[1;92m'+'ONLINE'+'\033[0;0m')
         time.sleep(4)
         print ("\033[31mIP: \033[0;0m", (socket.gethostbyname(alvo)))
         print (" ")
         print ("\033[31mPAÍS: \033[0;0m", (w.country))
         print (" ")
         print ("\033[31mDOMÍNIO: \033[0;0m", (w.domain_name))
         print (" ")
         print ("\033[31mDATA DE CRIAÇÃO: \033[0;0m", (w.creation_date))
         print (" ")
         print ("\033[31mDATA DE EXPIRAÇÃO: \033[0;0m", (w.expiration_date))
         print (" ")
         print ("\033[31mSERVERS: \033[0;0m", (w.name_servers))
         print (" ")
         print ("\033[31mEMAILS: \033[0;0m", (w.emails))
         print (" ")
         print ("\033[31mNOME: \033[0;0m", (w.name))
         print (" ")
         print ("\033[31mCEP: \033[0;0m", (w.zipcode))
         print (" ")
         print ("\033[31mESTADO: \033[0;0m", (w.state))
         print (" ")
         print ("\033[31mORG: \033[0;0m", (w.org))
         break
    if option == 5:
      print (" ")
      print ("\033[31mPROTONMAIL: \033[0;0m", "rootfatalsec@protonmail.ch")
      print (" ")
      print ("\033[31mTWITTER: \033[0;0m", "https://twitter.com/F4t4lsec")
      print (" ")
      print ("\033[31mINSTAGRAM: \033[0;0m", "https://www.instagram.com/fatalsec/")
      print (" ")
      print ("\033[31mTELEGRAM \033[0;0m", "https://t.me/fatalsec")
      print (" ")
      print ("\033[31mSITE DA TEAM \033[0;0m", "https://teamroot.tk")
      break
    if option == 6:
      os.system('clear')
      from bs4 import BeautifulSoup
      from urllib.request import urlopen
      html = urlopen("https://raw.githubusercontent.com/FatalS3C/SocialtoolS/main/sobre.txt")
      sobre = BeautifulSoup(html, 'html.parser')
      print (sobre)
      break

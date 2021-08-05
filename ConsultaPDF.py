#https://pypi.org/project/pyinterboleto/
from pathlib import Path
from datetime import date, timedelta
from pprint import pprint
from pyinterboleto import Boleto, RequestConfigs
from unidecode import unidecode


 
# definição da configuração de autenticação
direc = Path('c:\Python\Inter')
cert = direc / 'Inter_API_Certificado.crt'
key = direc / 'Inter_API_Chave.key'
acc = '49041860' # Número da conta PJ
configs = RequestConfigs(conta_inter=acc, certificate=cert, key=key)

#////////////PARA DOWNLOAD DO PDF//////////
from pathlib import Path
boleto = Boleto(configs)
num_boleto = '00702240062'

# Armazenado em um buffer de bytes na memória
pdf = boleto.consulta_pdf(num_boleto)
# salva em um arquivo chamado 'boleto.pdf' no diretório atual
nome_boleto = num_boleto + " - boleto.pdf"
filename = Path().resolve() /nome_boleto
#filename = "c:\Python\Inter\Boletos" /nome_boleto
boleto.consulta_pdf(num_boleto, filename)



       

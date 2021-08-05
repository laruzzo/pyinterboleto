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


from pyinterboleto import Boleto, Emissao, Pagador, RequestConfigs
boleto = Boleto(configs) # configs vem da seção configuração
pagador = Pagador(
tipoPessoa='JURIDICA',
cnpjCpf='29.232.620/0001-38',
nome="P.R DE MORAIS ROSA",
endereco="RUA APARECIDA",
numero='648',
bairro='SANTA ROSALIA',
cidade='Sorocaba',
uf='SP',
cep='18095-000'
)

emissao = Emissao(
pagador=pagador, seuNumero='0543',
cnpjCPFBeneficiario='23.866.944/0001-41',
valorNominal=390,
dataEmissao=date.today(),
dataVencimento=date.today()+timedelta(days=7)
)
result = boleto.emitir(emissao)
print(result)
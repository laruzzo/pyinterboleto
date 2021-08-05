from pathlib import Path
from datetime import date, timedelta
from pprint import pprint
from numpy import iinfo, record
from numpy.lib.index_tricks import ogrid
from pandas.io.formats.style import Styler
from pyinterboleto import Boleto, RequestConfigs
from pyinterboleto.consulta.lista import FiltrarEnum, OrdenarEnum
from unidecode import unidecode
import pandas
from pandas import DataFrame
import json
 
# definição da configuração de autenticação
direc = Path('c:\Python\Inter')
cert = direc / 'Inter_API_Certificado.crt'
key = direc / 'Inter_API_Chave.key'
acc = '49041860' # Número da conta PJ
configs = RequestConfigs(conta_inter=acc, certificate=cert, key=key)

boleto = Boleto(configs)
inicial = '2021-01-01'
final = '2021-12-31'
status = FiltrarEnum.V
    #T = 'TODOS'
    #V = 'VENCIDOSAVENCER'
    #E = 'EXPIRADOS'
    #P = 'PAGOS'
    #TB = 'TODOSBAIXADOS'
order = OrdenarEnum.DVA
    # NN: Nosso número (usado também para consulta do PDF do boleto);
    # SN: Seu número (que você usou na emissão);
    # DVA: Data de vencimento crescente;
    # DVD: Data de vencimento decrescente;
    # NS: Nome do sacado;
    # VA: Valor do título crescente;
    # VD: Valor do título decrescente;
    # SA: Status do título crescente;
    # SD: Status do título decrescente;


lista = boleto.consulta_lista(inicial, final,filtrar=status,ordernar=order,page=0)
#print(lista)

resumo = pandas.DataFrame(lista['summary'])
print(resumo)
boletos = pandas.DataFrame(lista['content'],columns={'nossoNumero', 'seuNumero', 'nomeSacado','situacao','dataVencimento','dataEmissao','valorNominal'})
print(boletos)



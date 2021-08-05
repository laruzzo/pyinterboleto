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

#///////////////PARA DAR BAIXA DE BOLETO///////////
from pyinterboleto import CodigoBaixaEnum
boleto = Boleto(configs)
num_boleto = '00704514449'
# A: Baixa por acertos;
#    - P: Baixado por ter sido protestado;
#    - D: Baixado para devolução;
#    - PAB: Baixado por protesto após baixa;
#    - PDC: Baixado, pago direto ao cliente;
#    - S: Baixado por substituição;
#    - FS: Baixado por falta de solução;
#    - PC: Baixado a pedido do cliente;

boleto.baixar_boleto(num_boleto, CodigoBaixaEnum.PDC)
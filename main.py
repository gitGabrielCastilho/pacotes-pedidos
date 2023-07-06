import pandas as pd
import fdb
from tkinter import *

dst_path = r'MTK:C:/Microsys/MsysIndustrial/Dados/MSYSDADOS.FDB'

TABLE_NAME1 = 'PEDIDOS_VENDAS'

########################################################################
SELECT1 = 'select PDV_CLI_CODIGO, PDV_NUMERO, PDV_CON_CODIGO, PDV_VALORPRODUTOS from %s ' \
          % (TABLE_NAME1)
########################################################################
con = fdb.connect(dsn=dst_path, user='SYSDBA', password='masterkey', charset='UTF8')
cur = con.cursor()
########################################################################
cur.execute(SELECT1)
table_rows1 = cur.fetchall()
########################################################################
df1 = pd.DataFrame(table_rows1)
########################################################################
print("Digite o cód do cliente: ")
cod_cli = int(input())
df1 = df1[df1[0] == cod_cli]
########################################################################
print("Digite o cód do pedido de pacote de Yale: ")
num_pedido_yale = int(input())
df2 = df1.loc[df1[1] == num_pedido_yale]
df2 = df2.reset_index(drop=True)
valor_pedido_yale = df2.iloc[0,3]

########################################################################
dfx = df1[df1[2] == 3]
dfx = dfx.reset_index(drop=True)
total = dfx[3].sum()
########################################################################
valor_restante_yale = valor_pedido_yale - total


if valor_restante_yale > 0:
    print(f"O cliente tem o valor de R${valor_restante_yale:,.2f} para retirar do pacote {num_pedido_yale}")

elif valor_restante_yale < 0:
    print(f"O pacote {num_pedido_yale} do cliente acabou, ele retirou R${valor_restante_yale:,.2f} a mais do pacote")

elif valor_restante_yale == 0:
    print(f"O cliente completou a retirada do pacote {num_pedido_yale}")

print(50*"#")
#########################################################################
print("Digite o cód do pedido de pacote de Tetra, caso não tenha tetra, digite 0: ")

num_pedido_tetra = int(input())

if num_pedido_tetra == 0:
    pass
else:
    df3 = df1.loc[df1[1] == num_pedido_tetra]
    df3 = df3.reset_index(drop=True)
    valor_pedido_tetra = df3.iloc[0,3]
    valor_restante_tetra = valor_pedido_tetra - total

    if valor_restante_tetra > 0:
        print(f"O cliente tem o valor de R${valor_restante_tetra:,.2f} para retirar do pacote {num_pedido_tetra}")

    elif valor_restante_tetra < 0:
        print(
            f"O pacote {num_pedido_tetra} do cliente acabou, ele retirou R${valor_restante_tetra:,.2f} a mais do pacote")

    elif valor_restante_tetra == 0:
        print(f"O cliente completou a retirada do pacote {num_pedido_tetra}")


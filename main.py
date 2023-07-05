import pandas as pd
import fdb

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
print("Digite o cód do pedido de pacote: ")
num_pedido = int(input())
df2 = df1.loc[df1[1] == num_pedido]
df2 = df2.reset_index(drop=True)
valor_pedido = df2.iloc[0,3]
########################################################################
df1 = df1[df1[2] == 3]
df1 = df1.reset_index(drop=True)
total = df1[3].sum()
########################################################################
valor_restante = valor_pedido - total

if valor_restante > 0:
    print(f"O cliente tem o valor de R${valor_restante:,.2f} para retirar do pacote {num_pedido}")

elif valor_restante < 0:
    print(f"O pacote {num_pedido} do cliente acabou, ele retirou R${valor_restante:,.2f} a mais do pacote")

elif valor_restante == 0:
    print(f"O cliente completou a retirada do pacote {num_pedido}")

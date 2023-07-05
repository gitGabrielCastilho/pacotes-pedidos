import pandas as pd
import fdb

dst_path = r'MTK:C:/Microsys/MsysIndustrial/Dados/MSYSDADOS.FDB'

TABLE_NAME1 = 'PEDIDOS_VENDAS'

########################################################################
SELECT1 = 'select PDV_CLI_CODIGO, PDV_NUMERO, PDV_TIPOPAGAMENTO, PDV_VALORPRODUTOS from %s ' \
          % (TABLE_NAME1)
########################################################################
con = fdb.connect(dsn=dst_path, user='SYSDBA', password='masterkey', charset='UTF8')
cur = con.cursor()
########################################################################
cur.execute(SELECT1)
table_rows1 = cur.fetchall()
########################################################################
df1 = pd.DataFrame(table_rows1)
df1 = df1[df1[2] == "B"]
########################################################################
print("Digite o cód do cliente: ")
x = int(input())
df1 = df1[df1[0] == x]
########################################################################
print("Digite o cód do pedido de pacote: ")
y = int(input())
df2 = df1.loc[df1[1] == y]

df2 = df2.rename(index = lambda x: 0)
df2 = df2.rename(index =lambda x: x+1)


print(df2.head(15))
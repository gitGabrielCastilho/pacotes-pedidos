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
#df1 = df1[df1[2] == "B"]
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
df1 = df1.reset_index(drop=True)
total = df1[3].sum()
########################################################################

#print(total_atual)
#print(df1)
import pandas as pd
import fdb
import tkinter
from tkinter import *

def enter_data():
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

    cod_cli = cod_cli_entry.get()
    cod_cli = int(cod_cli)
    df1 = df1[df1[0] == cod_cli]

# ########################################################################
    num_pedido_yale = yale_entry.get()
    num_pedido_yale = int(num_pedido_yale)
    df2 = df1.loc[df1[1] == num_pedido_yale]
    df2 = df2.reset_index(drop=True)
    valor_pedido_yale = df2.iloc[0,3]
# ########################################################################
    dfx = df1[df1[2] == 3]
    dfx = dfx.reset_index(drop=True)
    total = dfx[3].sum()
# ########################################################################

    valor_restante_yale = (valor_pedido_yale - total)

    if valor_restante_yale > 0:
        var_yale.set(f"O cliente tem o valor de {valor_restante_yale:,.2f} para retirar do pacote {num_pedido_yale}")

    elif valor_restante_yale < 0:
        var_yale.set(f"O pacote {num_pedido_yale} do cliente acabou, retirou R${valor_restante_yale:,.2f} a mais do pacote")

    elif valor_restante_yale == 0:
        var_yale.set(f"O cliente completou a retirada do pacote {num_pedido_yale}")


##########################################################################
    num_pedido_tetra = tetra_entry.get()
    num_pedido_tetra= int(num_pedido_tetra)

    if num_pedido_tetra == 0:
        pass
    elif num_pedido_tetra != 0:
        dfy = df1[df1[2] == 3]
        dfy = dfy.reset_index(drop=True)
        total_tetra = dfy[3].sum()

        df3 = df1.loc[df1[1] == num_pedido_tetra]
        df3 = df3.reset_index(drop=True)
        valor_pedido_tetra = df3.iloc[0,3]
        valor_restante_tetra = valor_pedido_tetra - total_tetra

        if valor_restante_tetra == 0:
            var_tetra.set(f"O cliente completou a retirada do pacote {num_pedido_tetra}")

        elif valor_restante_tetra > 0:
            var_tetra.set(f"O cliente tem o valor de R${valor_restante_tetra:,.2f} para retirar do pacote {num_pedido_tetra}")

        elif valor_restante_tetra < 0:
            var_tetra.set(f"O pacote {num_pedido_tetra} do cliente acabou, ele retirou R${valor_restante_tetra:,.2f} a mais do pacote")



window = tkinter.Tk()
window.title('Calculadora de Pacotes')

frame = tkinter.Frame(window)
frame.pack()
window.geometry("400x300")

################################################################################
user_info_frame = tkinter.LabelFrame(frame, text='Informações do Pedido')
user_info_frame.grid(padx=10, pady=10)

cod_cli_label = tkinter.Label(user_info_frame, text ='Código cliente: ')
cod_cli_label.grid(row=0, column=0, pady=5)
cod_cli_entry = tkinter.Entry(user_info_frame)
cod_cli_entry.grid(row=0, column=1, padx=5, pady=5)
##################################################################################
yale_label = tkinter.Label(user_info_frame, text="Pedido Yale:")
yale_label.grid(row=1, column=0, pady = 5)
yale_entry = tkinter.Entry(user_info_frame)
yale_entry.grid(row=1, column=1, padx=5, pady=5)
##################################################################################
tetra_label = tkinter.Label(user_info_frame, text="Pedido Outras chaves:")
tetra_label_info = tkinter.Label(user_info_frame, text="Digite 0 caso não houver ")
tetra_label.grid(row=3, column=0, pady=5)
tetra_label_info.grid(row=4, column=0)
tetra_entry = tkinter.Entry(user_info_frame)
tetra_entry.grid(row=3, column=1, pady=5)


##################################################################################
button = tkinter.Button(frame, text="Confirmar", command=enter_data)
button.grid(row=2, column=0, sticky="news", pady=5, padx=10)

##################################################################################
var_yale = StringVar()
var_yale.set("")

resultado_yale = tkinter.Label(frame, textvariable = var_yale)
resultado_yale.grid(row=3, column=0, padx=10, pady=10)

var_tetra = StringVar()
var_tetra.set("")
resultado_tetra = tkinter.Label(frame, textvariable = var_tetra)
resultado_tetra.grid(row=4, column=0, padx=10, pady=10)
window.mainloop()
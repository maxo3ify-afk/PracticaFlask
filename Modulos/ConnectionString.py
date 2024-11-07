import pyodbc
def Coneccion():
    cnxn_str = ("Driver={SQL Server};"
                    "Server=MAXO3IFY;"
                    "Database=BelencitaDeMujerch;"
                    "Trusted_Connection=yes;")
    cnxn = pyodbc.connect(cnxn_str)
    return cnxn
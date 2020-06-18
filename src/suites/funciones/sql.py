import pyodbc, pytest
Server = "192.168.22.9"
Base = "vfAlfa_Nueva"

def sqlQuery(query):  
    try:        
        conn = pyodbc.connect('Driver={SQL SERVER};'
                      "Server="+Server+";"
                      "Database="+Base+";"
                      'UID=asas;'
                      'PWD=asas;')
                        
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.commit()
        print("SQL Ejecutado correctamente")
        cursor.close()
    except:
        assert False, "Error en SQL"

def sqlSelect(query):
    conn = pyodbc.connect('Driver={SQL SERVER};'
                "Server="+Server+";"
                "Database="+Base+";"
                'UID=UsuarioGenerico;'
                'PWD=vesco;')
                    
    cursor = conn.cursor()
    cursor.execute(query) 
    row = cursor.fetchone() 
    while row: 
        dato =  row[0]
        row = cursor.fetchone()
    cursor.close()
    return dato
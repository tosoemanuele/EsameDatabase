def get_turni_macchinista(matricola):
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="1234", database="nome_del_database")
        cursor = db.cursor()
        
        cursor.callproc('TurniMacchinista', [matricola])
        
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                nome = row[0]
                ora_partenza = row[1].strftime('%Y-%m-%d %H:%M:%S')
                partenza = row[2]
                ora_arrivo = row[3].strftime('%Y-%m-%d %H:%M:%S')
                arrivo = row[4]
                
                print("Nome:", nome, "Partenza:", ora_partenza, partenza, "Arrivo:", ora_arrivo, arrivo)
        
    except:
        print("Errore")

    if db.is_connected():
        cursor.close()
        db.close()

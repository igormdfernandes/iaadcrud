class StartupImpl():
    def create(self, data_id, data_sede, data_nome):
        import mysql.connector

        conn = mysql.connector.connect(host="localhost", user="root", password="iaadcrUD1", db="iaadcrud")

        cursor = conn.cursor()

        sql = "INSERT INTO STARTUP (id_startup, nome_startup, cidade_sede) VALUES (%s, %s, %s)"
        data = (data_id, data_nome, data_sede)

        cursor.execute(sql, data)
        conn.commit()

        userid = cursor.lastrowid

        cursor.close()
        conn.close()

        print("Foi cadastrado o novo usuário de ID:", userid)

    def read(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost", user="root", password="iaadcrUD1", db="iaadcrud")

        cursor = conn.cursor()
        sql = "SELECT * FROM STARTUP"

        cursor.execute(sql)
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        for result in results:
            print(result)

    def update(self, data_id, data_nome, data_sede):
        import mysql.connector

        conn = mysql.connector.connect(host="localhost", user="root", password="iaadcrUD1", db="iaadcrud")

        cursor = conn.cursor()

        sql = "UPDATE STARTUP SET NOME_STARTUP = %s, CIDADE_SEDE = %s WHERE ID_STARTUP = %s"
        data = (data_nome, data_sede, data_id)

        cursor.execute(sql, data)
        conn.commit()

        linhas_alteradas = cursor.rowcount

        cursor.close()
        conn.close()

        print(linhas_alteradas, " registros alterados")

    def delete(self, data_id):
        import mysql.connector

        conn = mysql.connector.connect(host="localhost", user="root", password="iaadcrUD1", db="iaadcrud")

        cursor = conn.cursor()

        sql = "DELETE FROM STARTUP WHERE ID_STARTUP = %s"
        data = (data_id,)

        cursor.execute(sql, data)
        conn.commit()

        linhas_excluidas = cursor.rowcount

        cursor.close()
        conn.close()

        print(linhas_excluidas, " registros excluídos")

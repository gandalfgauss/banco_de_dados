import psycopg2

class Conexao(object):
    _db=None

    def __init__(self, mhost, db, usr, pwd):
        self.mhost = mhost
        self.db = db
        self.usr = usr
        self.pwd = pwd
        self._db = psycopg2.connect(host=mhost, database=db, user=usr,  password=pwd)

    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()

        except:
            cur.close()
            self.fechar()
            self._db = psycopg2.connect(host=self.mhost, database=self.db, user=self.usr, password=self.pwd)
            return False
        return True

    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()

            #print(type(self._db))
        except:
            cur.close()
            self.fechar()
            self._db = psycopg2.connect(host=self.mhost, database=self.db, user=self.usr, password=self.pwd)
            return None
        return rs

    def fechar(self):
        self._db.close()
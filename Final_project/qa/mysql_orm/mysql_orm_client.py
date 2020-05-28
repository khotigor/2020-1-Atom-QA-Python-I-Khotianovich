import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MysqlOrmConnection:
    def __init__(self, user, password, db_name, host, local_host, port):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.local_host = local_host
        self.port = port

        self.connection = self.connect()
        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def get_connection(self, db_created=False, selen=False):
        engine = sqlalchemy.create_engine(
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
                user=self.user,
                password=self.password,
                host=self.local_host if selen else self.host,
                port=self.port,
                db=self.db_name if db_created else ''),
            encoding='utf8'
        )
        return engine.connect()

    def connect(self):
        connection = self.get_connection()
        connection.execute('USE {db};'.format(db=self.db_name))
        connection.close()
        return self.get_connection(db_created=True)

    def execute_query(self, query):
        res = self.connection.execute(query)
        return res.getchall()

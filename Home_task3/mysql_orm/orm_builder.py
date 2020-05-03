from mysql_orm.models import Base, A, B, C, D, E
from mysql_orm.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection, parser):
        self.connection = connection
        self.engine = connection.connection.engine
        self.parser = parser

        self.create_a()
        self.create_b()
        self.create_c()
        self.create_d()
        self.create_e()

    def create_a(self):
        if not self.engine.dialect.has_table(self.engine, 'key_a'):
            Base.metadata.tables['key_a'].create(self.engine)

    def create_b(self):
        if not self.engine.dialect.has_table(self.engine, 'key_b'):
            Base.metadata.tables['key_b'].create(self.engine)

    def create_c(self):
        if not self.engine.dialect.has_table(self.engine, 'key_c'):
            Base.metadata.tables['key_c'].create(self.engine)

    def create_d(self):
        if not self.engine.dialect.has_table(self.engine, 'key_d'):
            Base.metadata.tables['key_d'].create(self.engine)

    def create_e(self):
        if not self.engine.dialect.has_table(self.engine, 'key_e'):
            Base.metadata.tables['key_e'].create(self.engine)

    def add_a(self):
        self.parser.is_file_func()
        self.parser.gen_list()
        """
        Лучше было бы создать один лист на сессию, тогда и использование листа 
        было бы оправдано. Т.е. создавать Parser() выше по иерархии, а сюда 
        передавать готовый лист.  
        Но тесты должны быть независимыми... 
        Вдруг мы изменяли этот лист где-то еще.
        """
        a = A(
            quantity=int(self.parser.count_number_of_requests())
        )
        self.connection.session.add(a)
        self.connection.session.commit()

    def add_b(self):
        self.parser.is_file_func()
        self.parser.gen_list()
        res_list = self.parser.number_of_each_type()
        for i in range(len(res_list)):
            if i % 2 == 0:
                b = B(
                    type=res_list[i],
                    quantity=res_list[i + 1]
                )
            self.connection.session.add(b)
            self.connection.session.commit()

    def add_c(self):
        self.parser.is_file_func()
        self.parser.gen_list()
        res_list = self.parser.top_of_size()
        for i in range(len(res_list)):
            c = C(
                url=res_list[i][6],
                code=int(res_list[i][8]),
                quantity=int(res_list[i][9])
            )
            self.connection.session.add(c)
            self.connection.session.commit()

    def add_d(self):
        self.parser.is_file_func()
        self.parser.gen_list()
        res_list = self.parser.top_of_size()
        for i in range(len(res_list)):
            d = D(
                url=res_list[i][6],
                code=int(res_list[i][8]),
                ip=res_list[i][0]
            )
            self.connection.session.add(d)
            self.connection.session.commit()

    def add_e(self):
        self.parser.is_file_func()
        self.parser.gen_list()
        res_list = self.parser.top_quantity_client_error_by_size()
        for i in range(len(res_list)):
            e = E(
                url=res_list[i][6],
                code=int(res_list[i][8]),
                ip=res_list[i][0]
            )
            self.connection.session.add(e)
            self.connection.session.commit()

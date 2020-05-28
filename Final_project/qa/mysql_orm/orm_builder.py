from mysql_orm.models import Base, TestUsers
from mysql_orm.mysql_orm_client import MysqlOrmConnection


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine

    def create_test_users(self):
        if not self.engine.dialect.has_table(self.engine, 'test_users'):
            Base.metadata.tables['test_users'].create(self.engine)

    def add_user(self, user, password, email):
        create_test_user = TestUsers(
            username=user,
            password=password,
            email=email
        )
        self.connection.session.add(create_test_user)
        self.connection.session.commit()

    def del_user_by_name(self, user):
        self.connection.session.execute(
            "DELETE FROM test_users WHERE username='{user}'".format(user=user))
        self.connection.session.commit()

    def del_user_by_email(self, email):
        self.connection.session.execute(
            "DELETE FROM test_users WHERE email='email'".format(email=email))
        self.connection.session.commit()

    def sel_pass(self, user):
        res = self.connection.session.execute(
            "SELECT password from test_users WHERE username='{user}'".format(
                user=user))
        self.connection.session.commit()
        return res

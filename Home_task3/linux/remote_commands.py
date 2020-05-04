# -*- coding: UTF-8 -*-

from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, \
    SSHException


class SSH:
    def __init__(self, **kwargs):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.kwargs = kwargs

    def __enter__(self):
        kw = self.kwargs
        try:
            self.client.connect(
                hostname=kw.get('hostname'),
                port=int(kw.get('port', 2233)),
                username=kw.get('username'),
                password=kw.get('password'),
            )
        except AuthenticationException:
            print("Authentication failed, please verify your credentials")
        except SSHException as sshException:
            print(f"Could not establish SSH connection {sshException}")

        """
        Возвращение self из метода означает,
        что метод возвращает ссылку на объект экземпляра, для которого он был 
        вызван
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def exec_cmd(self, cmd):
        # все команды будем делать из-под рута
        stdin, stdout, stderr = self.client.exec_command(
            "sudo -S -p '' {cmd}".format(cmd=cmd))
        stdin.write('centos\n')
        stdin.flush()

        data = stdout.read()
        data = data.decode()

        err = stderr.read()
        err = err.decode()
        if err:
            raise Exception(f'Err:{err}')
        return data

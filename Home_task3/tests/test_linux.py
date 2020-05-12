import pytest


class TestLinux:
    @pytest.mark.linux
    def test_root(self, linux_client):
        root = linux_client.exec_cmd('id -u -n')
        assert 'root' == root[:-1]
        assert len(linux_client.exec_cmd('tail /var/log/messages')) > 0

    @pytest.mark.linux
    def test_nginx(self, linux_client):
        firewall_list = linux_client.exec_cmd('firewall-cmd --list-all')
        if '2232/tcp' not in firewall_list:
            linux_client.exec_cmd(
                'firewall-cmd --permanent --zone=public --add-port=2232/tcp')
            linux_client.exec_cmd('firewall-cmd --reload')
            linux_client.exec_cmd('systemctl restart nginx')
        assert '2232' in linux_client.exec_cmd('firewall-cmd --list-all')

    @pytest.mark.linux
    def test_nginx_running(self, linux_client):
        task = linux_client.exec_cmd('systemctl status nginx')
        assert task.find('active (running)') > 0

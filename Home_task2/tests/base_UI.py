from ui.fixtures_UI import *


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.authorization_page: AuthorizationPage = request.getfixturevalue(
            'authorization_page')

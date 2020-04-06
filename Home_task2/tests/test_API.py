from api.fixtures_API import *


class Test:

    # def test_above_the_test_1(self, api_client):
    #     result = api_client.login()
    #     print(result)

    @pytest.mark.API
    def test_create_segment(self, api_client, create_name_of_segment_for_add):
        name = create_name_of_segment_for_add
        assert api_client.create_segment(name).status_code == 200

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        name = create_name_of_segment_for_delete
        assert api_client.delete_segment(
            api_client.create_segment(name).json()['id']).status_code == 204

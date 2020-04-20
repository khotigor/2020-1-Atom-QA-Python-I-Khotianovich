from api.fixtures_API import *
from functions import create_name_of_segment


class Test:

    @pytest.mark.API
    def test_create_segment(self, segment_request):
        assert segment_request.status_code == 200, \
            'Failed to create test segment'

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        name = create_name_of_segment('API', -1000, -1)
        assert api_client.delete_segment(
            api_client.create_segment(name).json()['id']).status_code == 204, \
            'Failed to delete test segment'

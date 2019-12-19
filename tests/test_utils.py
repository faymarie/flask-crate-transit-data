import os
from transitdata.main.utils import parse_header_to_dict


def test_parse_header_to_dict():
    file_path = os.path.join("transitdata", "static", "data", "service_alerts.txt")
    result = parse_header_to_dict(file_path)

    assert result == {'gtfs_realtime_version': '2.0', 
                    'incrementality': 'DIFFERENTIAL', 
                    'timestamp': '1575622745'}
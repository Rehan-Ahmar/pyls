import pytest
import json

from pyls_rehan import *


@pytest.mark.parametrize("nbytes, expected_result", [
    (60, "60B"),
    (1024, "1K"),
    (1030, "1K"),
    (4096, "4K"),
    (1048576, "1M"),
    (1073741824, "1G"),
    (1153434, "1.1M"),
    (26420, "25.8K"),
])
def test_format_size(nbytes, expected_result):
    assert format_size(nbytes) == expected_result


content_list = [
    {
        "name": ".hidden1",
        "size": 227,
        "time_modified": 1699944819,
        "permissions": "-rw-r--r--"
    },
    {
        "name": ".hidden2",
        "size": 2886,
        "time_modified": 1699955487,
        "permissions": "-rw-r--r--"
    },
    {
        "name": "file1",
        "size": 8911,
        "time_modified": 1699941437,
        "permissions": "-rw-r--r--"
    },
    {
        "name": "file2",
        "size": 1071,
        "time_modified": 1699941437,
        "permissions": "-rw-r--r--"
    },
    {
        "name": "dir1",
        "size": 102383,
        "time_modified": 1699941437,
        "permissions": "drwxr-xr-x",
        "contents": []
    },
    {
        "name": "dir2",
        "size": 4096,
        "time_modified": 1700205662,
        "permissions": "drwxr-xr-x",
        "contents": []
    },
    {
        "name": ".hidden-dir",
        "size": 4096,
        "time_modified": 1700205662,
        "permissions": "drwxr-xr-x",
        "contents": []
    }
]


@pytest.mark.parametrize("content_list, filter_file_type, show_all, expected_result", [
    (content_list, "file", True,  [content_list[0], content_list[1], content_list[2], content_list[3]]),
    (content_list, "file", False, [content_list[2], content_list[3]]),
    (content_list, "dir", True, [content_list[4], content_list[5], content_list[6]]),
    (content_list, "dir", False, [content_list[4], content_list[5]]),
    (content_list, None, True, content_list),
    (content_list, None, False, [content_list[2], content_list[3], content_list[4], content_list[5]]),
])
def test_filter_contents(content_list, filter_file_type, show_all, expected_result):
    assert filter_contents(content_list, filter_file_type, show_all) == expected_result


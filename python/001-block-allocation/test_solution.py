import pytest
from solution import calculate storage

@pytest.mark.parametrize("filesize, block_size, expected", [
    (0, 4096, 0),
    (1, 4096, 4096),
    (4096, 4096, 4096),
    (4097, 4096, 8192),
    (4096, 1024, 4096),
    (1025, 1024, 2048),
])
def test_calculate_storage(filesize, block_size, expected):
    assert calculate_storage(filesize, block_size) == expected

@pytest.mark.parametrize("filesize, block_size", [
    (-1, 4096),
    (1, 0),
    (1, -5),
])
def test_invalid_inputs(filesize, block_size):
    with pytest.raises(ValueError):
        calculate_storage(filesize, block_size)

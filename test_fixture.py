import pytest

@pytest.fixture(name="nihao")
def func():
    return 42


def test_func(nihao):
    print(nihao/6)
    assert nihao == 42

if __name__ == "__main__":
    pytest.main()
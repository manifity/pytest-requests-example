import pytest


@pytest.fixture
def select_api_version(version):
    """
    Пример того, как хранить различные версии API для дальнейшего переиспользования,
    а также их вызова при запуске тестов.
    """
    if version == 'v1':
        return '/service/v1'
    elif version == 'v2':
        return '/service/v2'
    else:
        raise TypeError('Unsupported API version')


def pytest_addoption(parser):
    parser.addoption('--api_version', action='store', default='v1')

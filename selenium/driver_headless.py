# режимом запуска без пользовательского интерфейса, с так называемым headless-режимом («без головы»)

import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.set_headless(True)
    return chrome_options
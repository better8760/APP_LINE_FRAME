import pytest


@pytest.fixture(scope='package')
def driverenv():
    des_capabilities={
        'platformName':'Android',
        'platformVersion':'6.0.1',
        'deviceName':'MuMu',
        'udid':'127.0.0.1:7555',
        'appPackage':'com.sky.jisuanji',
        'appActivity':'.JisuanjizixieActivity',
        'noReset':True,
        'unicodeKeyboard':True,
        'resetKeyboard':True,
        'newCommandTimeout':300,
        'noSign':True
    }
    return des_capabilities

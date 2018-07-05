# -*- coding: utf-8 -*-
"""TODO: doc module"""


import pytest
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.utils import settings


CONFIG = settings(
    file_path="testlinktests/configs/",
    file_name="settings.json"
)


class TestMethods(object):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        if 'skipIf' in dir(test_method) and test_method.skipIf.args[0]:
            pytest.skip(test_method.skipIf.args[1])
            return
        self.tlm = TLManager(settings=CONFIG)

    def test_checkdevkey(self):
        """TestCase: test_checkdevkey
            Login success with valid config
        """
        is_logged = self.tlm.api_login()
        if not is_logged:
            raise AssertionError(
                "API_KEY it's invalid when must be valid")

    @pytest.mark.raises(exception=ResponseException)
    def test_raises_checkdevkey(self):
        """TestCase: test_raises_checkdevkey"""
        is_logged = self.tlm.api_login(dev_key='willfail')
        if is_logged:
            raise AssertionError(
                "API_KEY it's invalid when must be valid")

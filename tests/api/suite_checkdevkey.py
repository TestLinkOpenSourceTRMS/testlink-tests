# -*- coding: utf-8 -*-
"""TODO: doc module"""


import pytest
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings as CFG


CONFIG = CFG(
    file_path="testlinktests/configs/",
    file_name="settings.example.json"
)


class TestCheckDevKey(TestInfoBase):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestCheckDevKey, self).setup_method(
            test_method, **{"tlm": TLManager(settings=CONFIG)})

    def test_checkdevkey(self):
        """TestCase: test_checkdevkey
            Login success with valid config
        """
        msg_error = "API_KEY it's invalid when must be valid"
        is_logged = self.tlm.api_login()
        self.assert_true(is_logged, msg=msg_error)

    @pytest.mark.raises(exception=ResponseException)
    def test_raises_checkdevkey(self):
        """TestCase: test_raises_checkdevkey"""
        msg_error = "API_KEY it's invalid when must be valid"
        is_logged = self.tlm.api_login(dev_key='willfail')
        self.assert_false(is_logged, msg=msg_error)

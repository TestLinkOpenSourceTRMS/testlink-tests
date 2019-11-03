# -*- coding: utf-8 -*-
"""TODO: doc module"""


import pytest
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings


SETTINGS = settings(file_path="testlinktests/configs/")
SKIP = SETTINGS['tests']['skip']['api']
SKIP_MSG = 'DISABLED by config file'


class TestCheckDevKey(TestInfoBase):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestCheckDevKey, self).setup_method(
            test_method, **{"tlm": TLManager(config=SETTINGS)})

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_checkdevkey(self):
        """TestCase: test_checkdevkey
            Login success with valid config
        """
        is_logged = self.tlm.api_login()
        self.assert_true(
            is_logged, msg="API_KEY it's invalid when must be valid")

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.raises(exception=ResponseException)
    def test_raises_checkdevkey(self):
        """TestCase: test_raises_checkdevkey"""
        with pytest.raises(ResponseException):
            self.tlm.api_login(dev_key='willfail')

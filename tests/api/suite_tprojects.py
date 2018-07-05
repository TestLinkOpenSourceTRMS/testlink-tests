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

    def test_get_tprojects_minimal_one(self):
        """TestCase: test_get_tprojects_minimal_one
            At least must exist one TestProject
        """
        tprojects = self.tlm.api_tprojects()
        if len(tprojects) < 1:
            raise AssertionError("Not empty Test Projects")

    @pytest.mark.skipIf(True, "Issue oneped at qatestlink library, #52")
    @pytest.mark.raises(exception=ResponseException)
    def test_raises_tprojects_baddevkey(self):
        """TestCase: test_raises_tprojects_baddevkey"""
        tprojects = self.tlm.api_tprojects(dev_key='willfail')
        if len(tprojects) >= 0:
            raise AssertionError("Not empty Test Projects")

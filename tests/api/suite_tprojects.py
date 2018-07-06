# -*- coding: utf-8 -*-
"""TODO: doc module"""


import pytest
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.models.tl_models import TProject
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings as CFG


CONFIG = CFG(
    file_path="testlinktests/configs/",
    file_name="settings.example.json"
)


class TestTProjects(TestInfoBase):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestTProjects, self).setup_method(
            test_method, **{"tlm": TLManager(settings=CONFIG)})

    def test_get_tprojects(self):
        """TestCase: test_get_tprojects
            At least must exist one TestProject
        """
        msg_error = "If empty testlink install, create at least one."
        tprojects = self.tlm.api_tprojects()
        self.assert_greater(len(tprojects), 1, msg=msg_error)
        for tproject in tprojects:
            self.log.debug(repr(tproject))
            self.assert_is_instance(tproject, TProject)

    @pytest.mark.skipIf(True, "Issue oneped at qatestlink library, #52")
    @pytest.mark.raises(exception=ResponseException)
    def test_raises_tprojects_baddevkey(self):
        """TestCase: test_raises_tprojects_baddevkey"""
        msg_error = "With invalid key, must return ResponseException"
        self.tlm.api_tprojects(dev_key='willfail')
        raise AssertionError(msg_error)

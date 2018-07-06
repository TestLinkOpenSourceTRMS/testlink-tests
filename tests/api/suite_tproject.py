# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qatestlink.core.models.tl_models import TProject
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings as CFG


CONFIG = CFG(
    file_path="testlinktests/configs/",
    file_name="settings.example.json"
)


class TestTProject(TestInfoBase):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestTProject, self).setup_method(
            test_method, **{"tlm": TLManager(settings=CONFIG)})

    def test_get_tproject_by_name(self):
        """TestCase: test_get_tproject
            At least must exist this TestProject NAME
        """
        msg_error = ("If empty testlink install, At least"
                     " must exist this TestProject NAME.")
        tproject_name = "testlink-tests"
        tproject = self.tlm.api_tproject(tproject_name)
        self.assert_is_instance(tproject, TProject, msg=msg_error)
        self.assert_equals(tproject.name, tproject_name, msg=msg_error)

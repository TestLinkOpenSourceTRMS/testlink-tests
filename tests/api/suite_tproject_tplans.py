# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qatestlink.core.models.tl_models import TPlan
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings as CFG


CONFIG = CFG(
    file_path="testlinktests/configs/",
    file_name="settings.json"
)


class TestTProjectTPlans(TestInfoBase):
    """TODO: doc class"""

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestTProjectTPlans, self).setup_method(
            test_method, **{"tlm": TLManager(settings=CONFIG)})

    def test_get_tproject_tplans(self):
        """TestCase: test_get_tprojects_minimal_one
            At least must exist one TPlan for this TProject
        """
        tproject_id = 1
        tplans = self.tlm.api_tproject_tplans(tproject_id)
        self.assert_is_instance(tplans, list)
        self.assert_greater(len(tplans), 1)
        for tplan in tplans:
            self.log.debug(repr(tplan))
            self.assert_is_instance(tplan, TPlan)

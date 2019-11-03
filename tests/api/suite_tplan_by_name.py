# -*- coding: utf-8 -*-
"""TODO: doc module"""


import pytest
from qatestlink.core.exceptions.response_exception import ResponseException
from qatestlink.core.models.tl_models import TPlan
from qatestlink.core.testlink_manager import TLManager
from testlinktests.core.test_info import TestInfoBase
from testlinktests.core.utils import settings


SETTINGS = settings(file_path="testlinktests/configs/")
SKIP = SETTINGS['tests']['skip']['api']
SKIP_MSG = 'DISABLED by config file'


class TestTProjects(TestInfoBase):
    """TODO: doc class"""

    tproject_name = None
    tplan_name = None

    def setup_method(self, test_method, **kwargs):
        """TODO: doc method"""
        super(TestTProjects, self).setup_method(
            test_method, **{"tlm": TLManager(config=SETTINGS)})
        # Tplan must be assigned to testproject to get tests working
        self.tproject_name = 'testlink-tests'
        self.tplan_name = 'xmlrpc'

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    def test_get_tplan_by_name(self):
        """TestCase: test_get_tplan_by_name
            At least must exist one TestPlan
            and assigned to TestProject

        Issue opened at main lib because not
            raise nothing if tplanname it's invalid
            https://github.com/netzulo/qatestlink/issues/53
        """
        msg_error = ("If empty testlink install, create at"
                     " least one and assign to testprojectname")
        tplan = self.tlm.api_tplan(self.tproject_name, self.tplan_name)
        self.log.debug(repr(tplan))
        self.assert_is_instance(tplan, TPlan, msg=msg_error)
        self.assert_is_instance(tplan.id, int)
        self.assert_equals(tplan.name, self.tplan_name)

    @pytest.mark.skipIf(True, "Issue opened at qatestlink library, #52")
    @pytest.mark.raises(exception=ResponseException)
    def test_raises_tplan_by_name_baddevkey(self):
        """TestCase: test_raises_tplan_by_name_baddevkey"""
        msg_error = "With invalid key, must return ResponseException"
        self.tlm.api_tplan(
            self.tproject_name,
            self.tplan_name,
            dev_key='willfail')
        raise AssertionError(msg_error)

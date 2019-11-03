# -*- coding: utf-8 -*-
"""package tests.web.suite_login
    Created on 2019-10-27

    @author: netzulo
"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qautils.files import settings
from testlinktests.core.pages.page_index import PageIndex
from testlinktests.core.pages.page_login import PageLogin
from testlinktests.core.specs import req_information


SETTINGS = settings(file_path="testlinktests/configs/")
SKIP = SETTINGS['tests']['skip']['index']
SKIP_MSG = 'DISABLED by config file'


class TestPageIndex(TestInfoBotUnique):
    """TODO: doc class"""

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestPageIndex, cls).setup_class(
            config=SETTINGS, skip_force=SKIP)
        cls.add_property('app', cls.cfg_app('testlink'))
        cls.add_property('cfg_login', cls.cfg_page('login'))
        cls.add_property('cfg', cls.cfg_page('index'))
        # suite preconditions
        try:
            _page = PageLogin(cls.bot, **cls.cfg_login.copy())
            req_information.url("login", _page)
            creeds = cls.app["data"]
            _page.login(creeds["usr"], creeds["pwd"])
        except Exception as err:
            cls.log.error("Bot Fails at precondition: %s", err.message)

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestPageIndex, self).setup_method(
            test_method, config=SETTINGS)
        # testcase preconditions
        try:
            self.page = PageIndex(self.bot, **self.cfg.copy())
        except Exception as err:
            self.log.error("Bot Fails at precondition: %s", err.message)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.dependency(name="loads")
    def test_index_loads(self):
        """Testcase: test_index_loads"""
        try:
            req_information.url("index", self.page)
            self.assert_true(self.page.is_url())
        except AssertionError as err:
            self.log.error("Bot Fails at assert %s", err.message)

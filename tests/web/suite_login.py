# -*- coding: utf-8 -*-
"""package tests.web.suite_login
    Created on 2019-10-27

    @author: netzulo
"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qautils.files import settings
from testlinktests.core.pages.page_login import PageLogin
from testlinktests.core.specs import req_information


SETTINGS = settings(file_path="testlinktests/configs/")
SKIP = SETTINGS['tests']['skip']['login']
SKIP_MSG = 'DISABLED by config file'


class TestPageLogin(TestInfoBotUnique):
    """TODO: doc class"""

    @classmethod
    def setup_class(cls, **kwargs):
        """Setup class (suite) to be executed"""
        super(TestPageLogin, cls).setup_class(
            config=SETTINGS, skip_force=SKIP)
        cls.add_property('app', cls.cfg_app('testlink'))
        cls.add_property('cfg', cls.cfg_page('login'))

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestPageLogin, self).setup_method(
            test_method, config=SETTINGS)
        # page
        self.page = PageLogin(self.bot, **self.cfg.copy())
        req_information.url("login", self.page, go_url=False)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.dependency(name="loads")
    def test_login_loads(self):
        """Testcase: test_login_loads"""
        try:
            req_information.url("login", self.page)
            self.assert_true(self.page.is_url())
        except AssertionError as err:
            self.log.error("Bot Fails at assert %s", err.message)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.dependency(depends=["loads"])
    @pytest.mark.parametrize('username,password', [
        ('admin', 'admin'),
    ])
    def test_login_ok(self, username, password):
        """Testcase: test_login_ok"""
        try:
            req_information.url("login", self.page)
            is_logged = self.page.login(username, password)
            self.assert_true(is_logged)
        except AssertionError as err:
            self.log.error("Bot Fails at assert %s", err.message)

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.dependency(depends=["loads"])
    @pytest.mark.parametrize('username,password', [
        ('notexist', 'notexist'),
        ('admin', ''),
        ('', 'admin'),
        ('|@#~€¬[]{}.-´ç`+', '|@#~€¬[]{}.-´ç`+'),
    ])
    def test_login_ko(self, username, password):
        """Testcase: test_login_ko"""
        try:
            req_information.url("login", self.page)
            is_logged = self.page.login(username, password)
            self.assert_false(is_logged)
        except AssertionError as err:
            self.log.error("Bot Fails at assert %s", err.message)

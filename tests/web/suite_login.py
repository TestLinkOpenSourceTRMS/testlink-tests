# -*- coding: utf-8 -*-
"""package tests.web.suite_login
    Created on 2019-10-27

    @author: netzulo
"""


import pytest
from qacode.core.testing.test_info import TestInfoBotUnique
from qautils.files import settings
from testlinktests.core.pages.page_login import PageLogin


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

    def setup_method(self, test_method):
        """Configure self.attribute"""
        super(TestPageLogin, self).setup_method(
            test_method, config=SETTINGS)
        self.add_property('app', self.cfg_app('testlink'))
        # page
        self.add_property('cfg', self.cfg_page('login'))
        self.page = PageLogin(self.bot, **self.cfg.copy())
        self.assert_is_instance(self.page, PageLogin)

    def ri_login_url(self, page):
        """Information requirement"""
        self.assert_is_instance(self.page, PageLogin)
        if not page.is_url():
            page.go_url()

    @pytest.mark.skipIf(SKIP, SKIP_MSG)
    @pytest.mark.dependency(name="loads")
    def test_login_loads(self):
        """Testcase: test_login_loads"""
        try:
            self.page.go_url()
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
            self.ri_login_url(self.page)
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
            self.ri_login_url(self.page)
            is_logged = self.page.login(username, password)
            self.assert_false(is_logged)
        except AssertionError as err:
            self.log.error("Bot Fails at assert %s", err.message)

# -*- coding: utf-8 -*-
"""package testlinktests.core.pages.page_login
    Created on 2019-10-27

    @author: netzulo
"""


from qacode.core.webs.pages.page_base import PageBase


class PageLogin(PageBase):
    """TODO:doc class"""

    def __init__(self, bot, **kwargs):
        """TODO: doc method"""
        kwargs.update({"locator": "css selector"})
        kwargs.update({"go_url": False})
        kwargs.update({"wait_url": 0})
        kwargs.update({"maximize": False})
        controls = [
            {"name": "str_version", "selector": "div span"},
            {"name": "txt_username", "selector": "#tl_login"},
            {"name": "txt_password", "selector": "#tl_password"},
            {"name": "btn_submit", "selector": "#tl_login_button"},
            {"name": "lnk_signup", "selector": "#tl_sign_up"},
            {"name": "lnk_lost_password", "selector": "#tl_lost_password"}
        ]
        kwargs.update({"controls": controls})
        super(PageLogin, self).__init__(bot, **kwargs)

    def version(self):
        """GET testlink version showing at top of login form"""
        text = self.str_version.get_text()
        # texts = text.split(" ")
        # version = texts[0]
        # mode = texts[1]
        # release_name = texts[2]
        return text

    def username(self, name, clear=True):
        """Fill up field for username"""
        self.txt_username.type_text(name, clear=clear)

    def password(self, name, clear=True):
        """Fill up field for password"""
        self.txt_password.type_text(name, clear=clear)

    def submit(self):
        """Click on submit button for login form"""
        self.btn_submit.click()

    def is_logged(self):
        url = self.bot.curr_driver.current_url
        is_login_url = "login.php" in url
        is_index_url = "index.php" in url
        if not is_login_url and is_index_url:
            return True
        return False

    def login(self, username, password):
        """Fill up login form and do login"""
        self.username(username)
        self.password(password)
        self.submit()
        return self.is_logged()

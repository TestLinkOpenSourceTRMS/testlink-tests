# -*- coding: utf-8 -*-
"""package testlinktests.core.pages.page_login
    Created on 2019-10-27

    @author: netzulo
"""


from qacode.core.webs.pages.page_base import PageBase


class PageIndex(PageBase):
    """TODO:doc class"""

    def __init__(self, bot, **kwargs):
        """
        USAGE:
            on a browser javascript console

            var iframe = document.querySelectorAll("[name='mainframe']")[0]
            var doc = iframe.contentDocument
            var menuRight = doc.querySelectorAll(".vertical_menu:nth-child(1)")
            var menuLeft = doc.querySelectorAll(".vertical_menu:nth-child(3)")
        """
        kwargs.update({"locator": "css selector"})
        kwargs.update({"go_url": False})
        kwargs.update({"wait_url": 0})
        kwargs.update({"maximize": False})
        controls = [
            {"name": "iframe_title", "selector": "[name='titlebar']"},
            {"name": "logo", "selector": "[title='logo']"},
            {"name": "menu_title", "selector": ""},
            {"name": "menu_bar", "selector": ""},
            {"name": "iframe_content", "selector": "[name='mainframe']"},
            {"name": "menu_right", "selector": ".vertical_menu:nth-child(1)"},
            {"name": "menu_left", "selector": ".vertical_menu:nth-child(3)"},
        ]
        kwargs.update({"controls": controls})
        super(PageIndex, self).__init__(bot, **kwargs)

    def menu_right(self):
        return self.iframe_content.find_child(self.menu_right)

    def menu_left(self):
        return self.iframe_content.find_child(self.menu_left)

    def is_iframe_content(self):
        self.menu_right()
        self.menu_left()
        return True

    def logo(self):
        return self.iframe_title.find_child(self.logo)

    def menu_title(self):
        return self.iframe_title.find_child(self.menu_title)

    def menu_bar(self):
        return self.iframe_title.find_child(self.menu_bar)

    def is_iframe_title(self):
        self.logo()
        self.menu_title()
        self.menu_bar()

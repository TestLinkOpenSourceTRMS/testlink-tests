
# -*- coding: utf-8 -*-
"""package testlinktests.core
    Created on 2018-07-03

    @author: netzulo
"""


from qacode.core.testing.test_info import TestInfoBase
from testlinktests.core.pages.page_index import PageIndex
from testlinktests.core.pages.page_login import PageLogin


def url(name, page, go_url=True):
    """Information requirement about URLs

    Arguments:
        name {str} -- Name of a page instance
        page {PageBase} -- Instance of a qacode Page or inherit object

    Keyword Arguments:
        go_url {True} -- Force BOT to navigate at requirement url (default: {True})
    """
    pageType = {
        "login": PageLogin,
        "index": PageIndex,
    }[name]
    TestInfoBase().assert_is_instance(page, pageType)
    if not page.is_url() and go_url:
        page.go_url()

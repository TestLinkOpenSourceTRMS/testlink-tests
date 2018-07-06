# -*- coding: utf-8 -*-
"""Base module for inherit new Test Suites"""


import os
import re
import time
import pytest
from qatestlink.core.testlink_manager import TLManager


ASSERT_MSG_DEFAULT = "Fails at '{}': actual={}, expected={}"
ASSERT_REGEX_URL = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501


class TestInfoBase(object):
    """Base class for inherit new Test classes"""

    tlm = None
    log = None

    @classmethod
    def setup_class(cls, **kwargs):
        """Configure 'cls.attribute'. If name start with 'test_' and have
            decorator skipIf with value True, then not open bot
        """
        tests_methods = []
        skip_methods = []
        skip_force = kwargs.get('skip_force')
        for method_name in dir(cls):
            if method_name.startswith("test_"):
                method = getattr(cls, method_name)
                tests_methods.append(method)
                if 'skipIf' in dir(method) and method.skipIf.args[0]:
                    skip_methods.append(method)
        if tests_methods == skip_methods or skip_force:
            pytest.skip("Testsuite skipped")

    def setup_method(self, test_method, **kwargs):
        """Configure self.attribute.
        If skipIf mark applied and True as first param for args tuple
            then not open bot
        """
        if 'skipIf' in dir(test_method) and test_method.skipIf.args[0]:
            pytest.skip(test_method.skipIf.args[1])
            return
        settings = kwargs.get('settings')
        tlm = kwargs.get('tlm')
        if settings is None and tlm is None:
            raise Exception(
                ("Not settings or TLManager "
                 "instance provided, read README first"))
        if tlm is None:
            tlm = TLManager(settings=settings)
        self.tlm = tlm
        self.log = tlm.log
        self.log.info("Started testcase named='{}'".format(
            test_method.__name__))

    def teardown_method(self, test_method):
        """Unload self.attribute"""
        self.log.info("Finished testcase named='{}'".format(
            test_method.__name__))

    @classmethod
    def add_property(cls, name, value=None):
        """Add property to test instance using param 'name', will setup
            None if any value it's passed by param
        """
        setattr(cls, name, value)

    def timer(self, wait=5, print_each=5):
        """Timer to sleep browser on testcases

        Keyword Arguments:
            wait {int} -- seconds to wait (default: {5})
            print_each {int} -- print message each seconds, must be divisible
                by 5, negatives are accepted (default: {5})

        Raises:
            Exception -- [description]
        """
        msg_err = "Timer can't works if print_each param isn't divisible by 1"
        if (print_each % 1) != 0:
            raise Exception(msg_err)
        while wait > 0:
            self.sleep(print_each)
            wait -= print_each

    def sleep(self, wait=0):
        """Just call to native python time.sleep method

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})
        """
        if wait > 0:
            time.sleep(wait)

    def assert_equals(self, actual, expected, msg=None):
        """Allow to compare 2 values and check if 1st it's equals to
            2nd value
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_equals", actual, expected)
        if actual != expected:
            raise AssertionError(actual, expected, msg)
        return True

    def assert_not_equals(self, actual, expected, msg=None):
        """Allow to compare 2 value to check if 1st isn't equals to
            2nd value
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_equals", actual, expected)
        if actual == expected:
            raise AssertionError(actual, expected, msg)
        return True

    def assert_equals_url(self, actual, expected, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st it's equals to 2nd url

        Arguments:
            actual {type} -- actual value
            expected {type} -- expected value

        Keyword Arguments:
            wait {int} -- Wait time on Runtime execution before execute
                next lane of code (default: {0})

        Raises:
            AssertionError -- [description]
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_equals_url", actual, expected)
        self.sleep(wait)
        if actual != expected:
            raise AssertionError(actual, expected, msg)
        return True

    def assert_not_equals_url(self, actual, expected, msg=None, wait=0):
        """Allow to compare 2 urls to check if 1st isn't equals to 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_equals_url", actual, expected)
        self.sleep(wait)
        if actual == expected:
            raise AssertionError(actual, expected, msg)
        return True

    def assert_contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st contains 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_contains_url", actual, contains)
        self.sleep(wait)
        if actual not in contains:
            raise AssertionError(actual, contains, msg)
        return True

    def assert_not_contains_url(self, actual, contains, msg=None, wait=0):
        """Allow to compare 2 urls and check if 1st not contains 2nd url"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_contains_url", actual, contains)
        self.sleep(wait)
        if actual in contains:
            raise AssertionError(actual, contains, msg)
        return True

    def assert_is_instance(self, instance, class_type, msg=None):
        """Allow to encapsulate method assertIsInstance(obj, cls, msg='')"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_is_instance", instance, class_type)
        if not isinstance(class_type, type):
            class_type = type(class_type)
        if not isinstance(instance, class_type):
            raise AssertionError(instance, class_type, msg)
        return True

    def assert_raises(self, expected_exception, function, *args, **kwargs):
        """Allow to encapsulate pytest.raises method(
            *args=(
                expected_exception,
                function,
            ),
            **kwargs={
                msg: ASSERT_MSG_DEFAULT
            }
        )
        """
        msg = kwargs.get('msg')
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_raises",
                "TODO:not implemented value",
                expected_exception)
        return pytest.raises(expected_exception, function, *args, **kwargs)

    def assert_greater(self, actual, greater, msg=None):
        """Allow to encapsulate method assertGreater(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, greater)
        if actual < greater:
            raise AssertionError(actual, greater, msg)
        return True

    def assert_lower(self, actual, lower, msg=None):
        """Allow to encapsulate method assertLower(a, b, msg=msg)"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_greater", actual, lower)
        if actual > lower:
            raise AssertionError(actual, lower, msg)
        return True

    def assert_in(self, actual, valid_values, msg=None):
        """Allow to compare if value it's in to 2nd list of values"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_in", actual, valid_values)
        if actual not in valid_values:
            raise AssertionError(actual, valid_values, msg)
        return True

    def assert_not_in(self, actual, invalid_values, msg=None):
        """Allow to compare if value it's not in to 2nd list of values"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_in", actual, invalid_values)
        if actual in invalid_values:
            raise AssertionError(actual, invalid_values, msg)
        return True

    def assert_regex(self, actual, pattern, msg=None):
        """Allow to compare if value match pattern"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_regex", actual, pattern)
        is_match = re.match(pattern, actual)
        if not is_match:
            raise AssertionError(actual, pattern, msg)
        return True

    def assert_not_regex(self, actual, pattern, msg=None):
        """Allow to compare if value not match pattern"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_not_regex", actual, pattern)
        is_match = re.match(pattern, actual)
        if is_match:
            raise AssertionError(actual, pattern, msg)
        return True

    def assert_regex_url(self, actual, pattern=None, msg=None):
        """Allow to compare if value match url pattern, can use
            custom pattern
        """
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_regex_url", actual, pattern)
        if not pattern:
            pattern = ASSERT_REGEX_URL
        return self.assert_regex(actual, pattern, msg=msg)

    def assert_path_exist(self, actual, is_dir=True, msg=None):
        """Allow to check if path exist, can check if is_dir also"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_path_exist",
                actual,
                "is_dir={}".format(is_dir))
        if not os.path.exists(actual):
            raise AssertionError(actual, "NEED_PATH_FOUND", msg)
        _is_dir = os.path.isdir(actual)
        if is_dir:
            if not _is_dir:
                raise AssertionError(actual, "NEED_PATH_IS_DIR", msg)
        else:
            if _is_dir:
                raise AssertionError(actual, "NEED_PATH_NOT_DIR", msg)
        return True

    def assert_path_not_exist(self, actual, msg=None):
        """Allow to check if path not exist, can check if is_dir also"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_path_not_exist", actual, "")
        if os.path.exists(actual):
            raise AssertionError(actual, "NEED_PATH_NOT_FOUND", msg)
        return True

    def assert_true(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'True'"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_true", actual, "")
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, True, msg=msg)
        return True

    def assert_false(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'False'"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        self.assert_is_instance(actual, bool)
        self.assert_equals(actual, False, msg=msg)
        return True

    def assert_none(self, actual, msg=None):
        """Allow to compare and check if value it's equals to 'None'"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        return self.assert_equals(actual, None, msg=msg)

    def assert_not_none(self, actual, msg=None):
        """Allow to compare and check if value it's not equals to 'None'"""
        if not msg:
            msg = ASSERT_MSG_DEFAULT.format(
                "assert_false", actual, "")
        return self.assert_not_equals(actual, None, msg=msg)

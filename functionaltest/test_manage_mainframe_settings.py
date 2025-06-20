# Copyright (C) 2022 Hottinger Bruel and Kjaer Benelux B.V.
# Schutweg 15a
# 5145 NP Waalwijk
# The Netherlands
# http://www.hbm.com

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Manage mainframe settings API functional test."""

import os
import sys
import time
import unittest

import HtmlTestRunner

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from src.ghsapi import ghsapi

IP_ADDRESS = "localhost"
PORT_NO = 8006


class TestManageMainframeSettings(unittest.TestCase):
    """Manage mainframe settings API functional test."""

    gen = ghsapi.GHS()

    @classmethod
    def setUpClass(cls):
        # run connect api at start of test file
        cls.gen.ghs_connect(IP_ADDRESS, PORT_NO)

    @classmethod
    def tearDownClass(cls):
        # run disconnect api at end of test file
        cls.gen.ghs_disconnect()

    def setUp(self):
        # runs before each test
        pass

    def tearDown(self):
        # runs after each test
        self.gen.ghs_stop_recording()

    def test_persist_current_settings(self):
        """Test copy of active settings to boot settings."""

        return_var = self.gen.ghs_persist_current_settings()
        self.assertEqual(
            return_var,
            "OK",
            "Failed to persist current settings.",
        )

    # While recording not able to persist setting checked the same in perception
    # def test_persist_current_settings_when_recording(self):
    #     """Test copy of active settings to boot settings when recording."""

    #     return_var = self.gen.ghs_start_recording()
    #     self.assertEqual(
    #         return_var,
    #         "OK",
    #         "Failed on start recording.",
    #     )

    #     return_var = self.gen.ghs_persist_current_settings()
    #     self.assertEqual(
    #         return_var,
    #         "OK",
    #         "Failed to persist current settings.",
    #     )

    #     return_var = self.gen.ghs_stop_recording()
    #     self.assertEqual(
    #         return_var,
    #         "OK",
    #         "Failed on stop recording.",
    #     )

    #     time.sleep(2)

    def test_apply_persisted_settings(self):
        """Test copy of boot settings to active settings."""

        return_var = self.gen.ghs_apply_persisted_settings()
        self.assertEqual(
            return_var,
            "OK",
            "Failed to apply persisted settings.",
        )

    def test_apply_persisted_settings_when_recording(self):
        """Test copy of boot settings to active settings when
        recording."""

        return_var = self.gen.ghs_start_recording()
        self.assertEqual(
            return_var,
            "OK",
            "Failed on start recording.",
        )

        return_var = self.gen.ghs_apply_persisted_settings()
        self.assertEqual(
            return_var,
            "SystemNotIdle",
            "Failed to apply persisted settings.",
        )

        return_var = self.gen.ghs_stop_recording()
        self.assertEqual(
            return_var,
            "OK",
            "Failed on stop recording.",
        )

        time.sleep(2)

    def test_set_get_current_settings(self):
        """Test to set then get current settings."""

        return_var = self.gen.ghs_set_high_low_rate_storage_enabled(
            "SyncChannels", "A", "Enable", "Enable"
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed on set high low storage enabled.",
        )

        return_var, high, low = self.gen.ghs_get_high_low_rate_storage_enabled(
            "SyncChannels", "A"
        )
        self.assertEqual(
            high,
            "Enable",
            "Failed on get high low storage enabled.",
        )
        self.assertEqual(
            low,
            "Enable",
            "Failed on get high low storage enabled.",
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed on get high low storage enabled.",
        )

        (
            return_var,
            blob_enable,
            blob_size_enable,
        ) = self.gen.ghs_get_current_settings()
        self.assertEqual(
            return_var,
            "OK",
            "Failed to get current settings.",
        )

        return_var = self.gen.ghs_set_high_low_rate_storage_enabled(
            "SyncChannels", "A", "Disable", "Disable"
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed on set high low storage disabled.",
        )

        return_var, high, low = self.gen.ghs_get_high_low_rate_storage_enabled(
            "SyncChannels", "A"
        )
        self.assertEqual(
            high,
            "Disable",
            "Failed on get high low storage disabled.",
        )
        self.assertEqual(
            low,
            "Disable",
            "Failed on get high low storage disabled.",
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed on get high low storage disabled.",
        )

        (
            return_var,
            blob_disable,
            blob_size_disable,
        ) = self.gen.ghs_get_current_settings()
        self.assertEqual(
            return_var,
            "OK",
            "Failed to get current settings.",
        )

        return_var = self.gen.ghs_set_current_settings(
            blob_enable, blob_size_enable
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed to set current settings.",
        )

        return_var, high, low = self.gen.ghs_get_high_low_rate_storage_enabled(
            "SyncChannels", "A"
        )
        self.assertEqual(
            high,
            "Enable",
            "Failed on set current settings.",
        )
        self.assertEqual(
            low,
            "Enable",
            "Failed on set current settings.",
        )
        self.assertEqual(
            return_var,
            "OK",
            "Failed on get high low storage enabled.",
        )


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            open_in_browser=True,
            report_name="Manage mainframe settings API Functional Test Report",
            report_title="Manage mainframe settings API Functional Test Report",
        )
    )

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

"""Trigger API test."""

import os
import sys
import time
import unittest
from unittest.mock import patch

import HtmlTestRunner

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

#sys.path.append(parentdir)
sys.path.append(os.path.join(parentdir, "src"))

from ghsapi import connection, ghsapi_states, trigger_api, ghsapi

IP_ADDRESS = "localhost"
PORT_NO = 8006


class TestTrigger(unittest.TestCase):
    """FieldBus Trigger API Unit test."""
    
    con_handle = connection.ConnectionHandler()
    GHSReturnValue = ghsapi_states.GHSReturnValue
    RETURN_KEY = ghsapi_states.RETURN_KEY
    get_trigger_api_list = [("test_get_start_data_recording",trigger_api.get_start_data_recording,"StartMethod","StartDataRecording_OnStartOfAcquisition",None),
                        ("test_get_stop_data_recording",trigger_api.get_stop_data_recording,"StopMethod","StopDataRecording_FirstTrigger",None),
                        ("test_get_number_of_mainframe_sweeps",trigger_api.get_number_of_mainframe_sweeps,"Count",1,None),
                        ("test_get_trigger_arm_enabled",trigger_api.get_trigger_arm_enabled,"Enable",1,None),
                        ("test_get_external_trigger_mode",trigger_api.get_external_trigger_mode,"Mode","ExternalTriggerInMode_RisingEdge",None),
                        ("test_get_external_minimum_pulse_width",trigger_api.get_external_minimum_pulse_width,"DebounceIn","DeBounceFilterTime_2",None),
                        ("test_get_sweep_length",trigger_api.get_sweep_length,"SweepLength",3,"A"),
                        ("test_get_trigger_position",trigger_api.get_trigger_position,"TriggerPosition",6,"A"),
                        ("test_get_continuous_leadout_time",trigger_api.get_continuous_leadout_time,"ContinuousLeadOutTime",5,"A"),]
    set_trigger_api_list =  [("test_set_start_data_recording",trigger_api.set_start_data_recording,"StartMethod","StartDataRecording_OnStartOfAcquisition",None),
                        ("test_set_stop_data_recording",trigger_api.set_stop_data_recording,"StopMethod","StopDataRecording_FirstTrigger",None),
                        ("test_set_number_of_mainframe_sweeps",trigger_api.set_number_of_mainframe_sweeps,"Count",1,None),
                        ("test_set_trigger_arm_enabled",trigger_api.set_trigger_arm_enabled,"Enable",1,None),
                        ("test_set_sweep_length",trigger_api.set_sweep_length,"SweepLength",3,"A"),
                        ("test_set_trigger_position",trigger_api.set_trigger_position,"TriggerPosition",6,"A"),
                        ("test_set_continuous_leadout_time",trigger_api.set_continuous_leadout_time,"ContinuousLeadOutTime",2,"A"),
                        ("test_set_external_trigger_mode",trigger_api.set_external_trigger_mode,"Mode","ExternalTriggerInMode_RisingEdge",None),
                        ("test_set_external_minimum_pulse_width",trigger_api.set_external_minimum_pulse_width,"DebounceIn","DeBounceFilterTime_2",None),]
    
    gen = ghsapi.GHS()

    def setUp(self):
        # runs before each test
        pass

    def tearDown(self):
        # runs after each test

        time.sleep(2)

    # Test cases for all get methods of Trigger FieldBus configuation Functions
    def test_get_fieldbus_trigger_configuration(self):
        """Test get_start_data_recording api with success response"""
        for testname,testcase,paramName,paramvalue,paramSlot in self.get_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
                print(f"\ntest_get_fieldbus_trigger_configuration: {testname} \n")
                with patch(
                    "test_connection_handler.connection.ConnectionHandler.connection_establish"
                ) as mock_con_est:
                    mock_con_est.return_value = self.GHSReturnValue["OK"]

                    with patch(
                        "test_connection_handler.connection.ConnectionHandler.send_request_wait_response"
                    ) as mock_req_ros:
                        mock_req_ros.return_value = {
                            self.RETURN_KEY: self.GHSReturnValue["OK"],
                            paramName: paramvalue,
                        }
                        if paramSlot:
                            self.assertEqual(
                                testcase(self.con_handle,paramSlot),
                                (
                                    "OK",
                                    paramvalue,
                                ),
                                f"\n {testcase} : testname  with slot Id : {paramSlot} failed.\n",
                            )
                        else:
                            self.assertEqual(
                                testcase(self.con_handle),
                                (
                                    "OK",
                                    paramvalue,
                                ),
                                f"\n {testcase} : testname  failed.\n",
                            )

    def test_get_fieldbus_trigger_configuration_neg(self):
        """Test get_start_data_recording api with failure response"""
        for testname,testcase,paramName,paramvalue,paramSlot in self.get_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
              
                with patch(
                    "test_connection_handler.connection.ConnectionHandler.connection_establish"
                ) as mock_con_est:
                    mock_con_est.return_value = self.GHSReturnValue["OK"]
                    
                with patch(
                    "test_connection_handler.connection.ConnectionHandler.send_request_wait_response"
                ) as mock_req_ros:
                    mock_req_ros.return_value = {
                        self.RETURN_KEY: self.GHSReturnValue["NOK"],
                        paramName: paramvalue,
                    }
                    if paramSlot:
                        self.assertEqual(
                            testcase(self.con_handle,paramSlot),
                            (
                                "NOK",
                                None,
                            ),
                            f"\n {testname} : test  with slot Id : {paramSlot} failed.\n",
                        )
                    else:
                        self.assertEqual(
                            testcase(self.con_handle),
                            ("NOK", None),
                            f"\n{testname}: failure response test failed ---1.\n",
                        )
                    mock_req_ros.return_value = {
                        self.RETURN_KEY: self.GHSReturnValue["OK"],
                        paramName: paramvalue,
                    }
                    if paramSlot:
                        self.assertEqual(
                            testcase(self.con_handle, paramSlot),
                            (
                                "OK",
                                paramvalue,
                            ),
                            f"\n {testname} : test  with slot Id : {paramSlot} failed.\n",
                        )
                    else:
                        self.assertEqual(
                            testcase(self.con_handle),
                            ("OK", paramvalue),
                            f"\n{testname}: failure response test failed --- 2.\n",
                        )

                    mock_req_ros.return_value = {
                        self.RETURN_KEY: self.GHSReturnValue["NullPtrArgument"],
                        paramName: None
                    }
                    if paramSlot:
                        self.assertEqual(
                            testcase(self.con_handle, paramSlot),
                            (
                                "NullPtrArgument",
                                 None,
                            ),
                            f"\n {testname} : test  with slot Id : {paramSlot} failed.\n",
                        )
                    else:
                        self.assertEqual(
                            testcase(self.con_handle),
                            ("NullPtrArgument",None),
                            f"\n{testname}: failure response test failed ---3.\n",
                        )

    def test_set_fieldbus_trigger_configuration(self):
        for testname,testcase,paramName,paramvalue,paramSlot in self.set_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
                with patch(
                    "test_connection_handler.connection.ConnectionHandler.connection_establish"
                ) as mock_con_est:
                    mock_con_est.return_value = self.GHSReturnValue["OK"]

            with patch(
                "test_connection_handler.connection.ConnectionHandler.send_request_wait_response"
            ) as mock_req_ros:
                mock_req_ros.return_value = {
                    self.RETURN_KEY: self.GHSReturnValue["OK"],
                }
                if paramSlot:
                    self.assertEqual(
                        testcase(
                            self.con_handle, paramSlot, paramvalue,
                        ),
                        "OK",
                        f"\n{testname}: failure response test failed \n",
                    )
                else:
                    self.assertEqual(
                        testcase(
                            self.con_handle, paramvalue,
                        ),
                        "OK",
                        f"\n{testname}: failure response test failed \n",
                    )
    
    def test_set_fieldbus_trigger_configuration_neg(self):
        for testname,testcase,paramName,paramvalue,paramSlot in self.set_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):

                with patch(
                    "test_connection_handler.connection.ConnectionHandler.connection_establish"
                ) as mock_con_est:
                    mock_con_est.return_value = self.GHSReturnValue["OK"]

            if paramSlot:
                self.assertEqual(
                    testcase(self.con_handle, paramSlot, 0.1),
                    "InvalidDataType",
                    f"\n{testname}: failure response test failed .\n",
                )
            else:
                self.assertEqual(
                    testcase(self.con_handle, 0.1),
                    "InvalidDataType",
                    f"\n{testname}: failure response test failed .\n",
                )  

                    
    def test_set_fieldbus_trigger_configuration_null_args(self):
        """Test set_fieldbus_trigger_configuration with null args"""
        for testname,testcase,paramName,paramvalue,paramSlot in self.set_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
 
                with patch(
                    "test_connection_handler.connection.ConnectionHandler.connection_establish"
                ) as mock_con_est:
                    mock_con_est.return_value = self.GHSReturnValue["OK"]

                if paramSlot:
                    self.assertEqual(
                        testcase(self.con_handle, paramSlot, None),
                        "NullPtrArgument",
                        f"\n{testname}: failure response test failed .\n",
                    )
                else:
                    self.assertEqual(
                        testcase(self.con_handle, None),
                        "NullPtrArgument",
                        f"\n{testname}: failure response test failed .\n",
                    )  

    

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            open_in_browser=True,
            report_name="Field Bus Trigger Configuration API Unittest Report",
            report_title="Field Bus Trigger Configuration API Unittest Report",
        )
    )

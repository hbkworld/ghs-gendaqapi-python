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

"""Trigger API functional test."""

import os
import sys
import time
import unittest

import HtmlTestRunner

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from src.ghsapi import ghsapi

IP_ADDRESS = "10.96.129.185"
PORT_NO = 8006


class TestTrigger(unittest.TestCase):
    """Trigger Field Bus configuration API functional test."""

    gen = ghsapi.GHS()
    get_trigger_api_list = [("get_start_data_recording",gen.ghs_get_start_data_recording,"Method","StartDataRecording_OnStartOfAcquisition",None),
                        ("get_stop_data_recording",gen.ghs_get_stop_data_recording,"Method","StopDataRecording_FirstTrigger",None),
                        ("get_number_of_mainframe_sweeps",gen.ghs_get_number_of_mainframe_sweeps,"Count",1,None),
                        ("get_trigger_arm_enabled",gen.ghs_get_trigger_arm_enabled,"Enable",1,None),
                        ("get_external_trigger_mode",gen.ghs_get_external_trigger_mode,"Mode","ExternalTriggerInMode_RisingEdge",None),
                        ("get_external_minimum_pulse_width",gen.ghs_get_external_minimum_pulse_width,"DebounceIn","DeBounceFilterTime_2",None),
                        ("get_sweep_length",gen.ghs_get_sweep_length,"SweepLength",2,"A"),
                        ("get_trigger_position",gen.ghs_get_trigger_position,"TriggerPosition",6,"A"),
                        ("get_continuous_leadout_time",gen.ghs_get_continuous_leadout_time,"ContinuousLeadOutTime",5,"A"),]
    set_trigger_api_list =  [("set_start_data_recording",gen.ghs_set_start_data_recording,"Method",1,None),
                        #("set_stop_data_recording",gen.ghs_set_stop_data_recording,"Method",3,None),
                        ("set_number_of_mainframe_sweeps",gen.ghs_set_number_of_mainframe_sweeps,"Count",1,None),
                        ("set_trigger_arm_enabled",gen.ghs_set_trigger_arm_enabled,"Enable",1,None),
                        ("set_sweep_length",gen.ghs_set_sweep_length,"SweepLength",4,"A"),
                        ("set_trigger_position",gen.ghs_set_trigger_position,"TriggerPosition",6,"A"),
                        ("set_continuous_leadout_time",gen.ghs_set_continuous_leadout_time,"ContinuousLeadOutTime",2,"A"),
                        ("set_external_trigger_mode",gen.ghs_set_external_trigger_mode,"Mode",1,None), #ExternalTriggerInMode_RisingEdge
                        ("set_external_minimum_pulse_width",gen.ghs_set_external_minimum_pulse_width,"DebounceIn",2,None),] #"DeBounceFilterTime_2"
    
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
        time.sleep(2)
        
    def test_set_fieldbus_trigger_configuration(self):
        for testname,testcase,paramName,paramvalue,paramSlot in self.set_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
                if paramSlot:
                    return_var = testcase(paramSlot,paramvalue)
                else:
                    return_var = testcase(paramvalue)
                    
                print(f"param value :{paramvalue}\n")
                self.assertEqual(
                    return_var,
                    "OK",
                    f"Failed on {testname}\n",
                )

    def test_get_fieldbus_trigger_configuration(self):
        for testname,testcase,paramName,paramvalue,paramSlot in self.get_trigger_api_list:
            with self.subTest(testname = testname, testcase = testcase, paramName = paramName,paramvalue = paramvalue,paramSlot = paramSlot):
                if paramSlot:
                    return_var, paramValue = testcase(paramSlot)
                else:
                    return_var, paramValue = testcase()
                    
                print(f"param value :{paramValue}\n")
                self.assertEqual(
                    isinstance(paramValue, int | str | float |
                               None),
                    True,
                    f"1 Failed on {testname}\n",
                )
                self.assertEqual(
                    return_var,
                    "OK",
                    f"2 Failed on {testname}\n",
                )
                
    def test_stop_data_recording(self):
        #gen = ghsapi.GHS()
        return_var = self.gen.ghs_set_stop_data_recording(1)
        self.assertEqual(
                return_var,
                "OK",
                f"Failed on set_stop_data_recording\n",
            )
        return_var, stop_data_recording = self.gen.ghs_get_stop_data_recording()
        self.assertEqual(isinstance(stop_data_recording, int | str),
            True,
            f"1 Failed on get_stop_data_recording\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_stop_data_recording\n",
            )

    def test_start_data_recording_NullPtr(self):
            return_var = self.gen.ghs_set_start_data_recording(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting null nu\n",
                )
            return_var, start_data_recording = self.gen.ghs_get_start_data_recording()
            self.assertEqual(isinstance(start_data_recording, int | str),
                True,
                f"1 Failed on get_start_data_recording\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_start_data_recording\n",
            )
            
    def test_start_data_recording_InvalidDataType(self):
            return_var = self.gen.ghs_set_start_data_recording(5) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "InvalidDataType",
                    f"Failed on setting Invalid Data Type\n",
                )
            return_var, start_data_recording = self.gen.ghs_get_start_data_recording()
            self.assertEqual(isinstance(start_data_recording, int | str),
                True,
                f"1 Failed on get_start_data_recording\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_start_data_recording\n",
            )
            
    def test_stop_data_recording_NullPtr(self):
            return_var = self.gen.ghs_set_stop_data_recording(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting stop_data_recording null nu\n",
                )
            return_var, stop_data_recording = self.gen.ghs_get_stop_data_recording()
            self.assertEqual(isinstance(stop_data_recording, int | str),
                True,
                f"1 Failed on get_stop_data_recording\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_stop_data_recording\n",
            )
            
    def test_stop_data_recording_InvalidDataType(self):
            return_var = self.gen.ghs_set_stop_data_recording(5) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "InvalidDataType",
                    f"Failed on setting Invalid Data Type\n",
                )
            return_var, stop_data_recording = self.gen.ghs_get_stop_data_recording()
            self.assertEqual(isinstance(stop_data_recording, int | str),
                True,
                f"1 Failed on get_stop_data_recording\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_stop_data_recording\n",
            )
            
    def test_number_of_mainframe_sweeps_data_recording_NullPtr(self):
            return_var = self.gen.ghs_set_number_of_mainframe_sweeps(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting number of mainframe sweeps null \n",
                )
            return_var, number_of_mainframe_sweeps = self.gen.ghs_get_number_of_mainframe_sweeps()
            self.assertEqual(isinstance(number_of_mainframe_sweeps, int | str),
                True,
                f"1 Failed on get_number_of_mainframe_sweeps\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_number_of_mainframe_sweeps\n",
            )
            
    def test_trigger_arm_enabled_NullPtr(self):
            return_var = self.gen.ghs_set_trigger_arm_enabled(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting NullPtrArgument\n",
                )
            return_var, trigger_arm_enabled = self.gen.ghs_get_trigger_arm_enabled()
            self.assertEqual(isinstance(trigger_arm_enabled, int | str),
                True,
                f"1 Failed on get_trigger_arm_enabled\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_trigger_arm_enabled\n",
            )
            
    def test_trigger_arm_enabled_InvalidDataType(self):
            return_var = self.gen.ghs_set_trigger_arm_enabled("Invalid") #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "InvalidDataType",
                    f"Failed on setting InvalidDataType\n",
                )
            return_var, trigger_arm_enabled = self.gen.ghs_get_trigger_arm_enabled()
            self.assertEqual(isinstance(trigger_arm_enabled, int | str),
                True,
                f"1 Failed on get_trigger_arm_enabled\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_trigger_arm_enabled\n",
            )

    def test_external_trigger_mode_NullPtr(self):
            return_var = self.gen.ghs_set_external_trigger_mode(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting NullPtrArgument\n",
                )
            return_var, external_trigger_mode = self.gen.ghs_get_external_trigger_mode()
            self.assertEqual(isinstance(external_trigger_mode, int | str),
                True,
                f"1 Failed on get_external_trigger_mode\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_external_trigger_mode\n",
            )
            
    def test_external_trigger_mode_InvalidDataType(self):
            return_var = self.gen.ghs_set_external_trigger_mode("Invalid") 
            self.assertEqual(
                    return_var,
                    "InvalidDataType",
                    f"Failed on setting external trigger mode as InvalidDataType\n",
                )
            return_var, external_trigger_mode = self.gen.ghs_get_external_trigger_mode()
            self.assertEqual(isinstance(external_trigger_mode, int | str),
                True,
                f"1 Failed on get_external_trigger_mode\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_external_trigger_mode\n",
            )

    def test_external_minimum_pulse_NullPtr(self):
            return_var = self.gen.ghs_set_external_minimum_pulse_width(0) #NullPtrArgument
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting external minimum pulse width NullPtrArgument\n",
                )
            return_var, external_minimum_pulse_width = self.gen.ghs_get_external_minimum_pulse_width()
            self.assertEqual(isinstance(external_minimum_pulse_width, int | str),
                True,
                f"1 Failed on get_external_minimum_pulse_width\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_external_minimum_pulse_width\n",
            )
            
    def test_sweep_Length_NullPtr(self):
            return_var = self.gen.ghs_set_sweep_length("A",0) 
            self.assertEqual(
                    return_var,
                    "NullPtrArgument",
                    f"Failed on setting sweep length as Null pointer\n",
                )
            return_var, external_trigger_mode = self.gen.ghs_get_sweep_length("A")
            self.assertEqual(isinstance(external_trigger_mode, int | str),
                True,
                f"1 Failed on get_sweep_length\n",
                )
            
            self.assertEqual(
                return_var,
                "OK",
                f"2 Failed on get_sweep_length\n",
            )
            
    def test_sweep_length_InvalidDataType(self):
        return_var = self.gen.ghs_set_sweep_length("A","Invalid") #setting out of range/invalid value
        self.assertEqual(
                return_var,
                "InvalidDataType",
                f"Failed on setting sweep length as InvalidDataType\n",
            )
        return_var, sweep_length = self.gen.ghs_get_sweep_length("A")
        self.assertEqual(isinstance(sweep_length, int | str),
            True,
            f"1 Failed on get_sweep_length\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_sweep_length\n",
        )
        
    def test_trigger_position_Nullptr(self):
        return_var = self.gen.ghs_set_trigger_position("A",0) 
        self.assertEqual(
                return_var,
                "NullPtrArgument",
                f"Failed on setting trigger position as Null pointer\n",
            )
        return_var, trigger_position = self.gen.ghs_get_trigger_position("A")
        self.assertEqual(isinstance(trigger_position, int | None),
            True,
            f"1 Failed on get_trigger_position\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_trigger_position\n",
        )
        
    def test_trigger_position_InvalidDataType(self):
        return_var = self.gen.ghs_set_trigger_position("A",10.7) #setting out of range/invalid value
        self.assertEqual(
                return_var,
                "InvalidDataType",
                f"Failed on setting trigger position as InvalidDataType\n",
            )
        return_var, trigger_position = self.gen.ghs_get_trigger_position("A")
        self.assertEqual(isinstance(trigger_position, int | None),
            False,
            f"1 Failed on get_trigger_position\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_trigger_position\n",
        )
     
    def test_continuous_leadout_time_Nullptr(self):
        return_var = self.gen.ghs_set_continuous_leadout_time("A",0) #setting null
        self.assertEqual(
                return_var,
                "NullPtrArgument",
                f"Failed on setting continuous_leadout_time as Null pointer\n",
            )
        return_var, continuous_leadout_time = self.gen.ghs_get_continuous_leadout_time("A")
        self.assertEqual(isinstance(continuous_leadout_time, int | None),
            False,
            f"1 Failed on get_continuous_leadout_time\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_continuous_leadout_time\n",
        )
        
    def test_continuous_leadout_time_InvalidDataType(self):
        return_var = self.gen.ghs_set_continuous_leadout_time("A","Invalid") #setting out of range/invalid value
        self.assertEqual(
                return_var,
                "InvalidDataType",
                f"Failed on setting continuous_leadout_time as InvalidDataType\n",
            )
        return_var, continuous_leadout_time = self.gen.ghs_get_continuous_leadout_time("A")
        self.assertEqual(isinstance(continuous_leadout_time, int | None),
            False,
            f"1 Failed on get_continuous_leadout_time\n",
            )
        
        self.assertEqual(
            return_var,
            "OK",
            f"2 Failed on get_continuous_leadout_time\n",
        )         
             
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            open_in_browser=True,
            report_name="FieldBus Trigger configuration API Functional Test Report",
            report_title="FieldBus Trigger configuration API Functional Test Report",
        )
    )
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
# LIABILITY, WHETHER IN AN fv  fv  v     ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""The GEN DAQ Channel API code examples.

This is to help you get started with Field Bus Trigger configuration  API"""

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from src.ghsapi import ghsapi

IP_ADDRESS = "10.96.129.129"
PORT_NO = 8006


def main():
    """Code example to use Channel API."""

    gen = ghsapi.GHS()

    # Connect to the mainframe "localhost" is also possible.
    return_var = gen.ghs_connect(IP_ADDRESS, PORT_NO)
    if return_var == "APIMismatch":
        print("Failed on GHSConnect. Client API version mismatch")
        sys.exit()
    if return_var != "OK":
        print(f"Failed on GHSConnect. Return Status: {return_var}")
        sys.exit()
    print(f"GHSConnect - Return Status: {return_var}")

    # Set Start Data Recording
    #return_var = gen.ghs_set_start_data_recording("A","StartDataRecording_OnStartOfAcquisition")
    # masking as it is under development 
    """ return_var = gen.ghs_set_start_data_recording(3)
    if return_var != "OK":
        print(f"Failed on GHSSetStartDataRecording. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetStartDataRecording - Return Status: {return_var}")
    """
    # Get start data Recording
    return_var, start_data_recording = gen.ghs_get_start_data_recording()
    if return_var != "OK":
        print(f"Failed on GHSGetStartDataRecordingMethod. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetStartDataRecordingMethod - Return Status: {return_var}\
        start_data_recording: {start_data_recording}"
    )
    # masking as it is under development 
    # Set Stop Data Recording
    """ return_var = gen.ghs_set_stop_data_recording(2)
    #return_var = gen.ghs_set_stop_data_recording("A",2)
    if return_var != "OK":
        print(f"Failed on GHSSetStopDataRecording. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetStopDataRecording - Return Status: {return_var}")
    """
    # Get stop data Recording
    return_var, stop_data_recording = gen.ghs_get_stop_data_recording()
    if return_var != "OK":
        print(f"Failed on GHSGetStopDataRecordingMethod. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetStopDataRecordingMethod - Return Status: {return_var}\
        stop_data_recording: {stop_data_recording}"
    )
    # masking as it is under development 
    """
    # Set Number of Mainframe sweeps
    return_var = gen.ghs_set_number_of_mainframe_sweeps(1)
    if return_var != "OK":
        print(f"Failed on GHSSetNumberofMainframeSweeps. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetNumberofMainframeSweeps - Return Status: {return_var}")
    """
    # Get Number of Mainframe sweeps
    return_var, number_of_mainframe_sweep = gen.ghs_get_number_of_mainframe_sweeps()
    if return_var != "OK":
        print(f"Failed on GHSGetNumberofMainframeSweep. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetNumberofMainframeSweep - Return Status: {return_var}\
        number_of_mainframe_sweep: {number_of_mainframe_sweep}"
    )
    # masking as it is under development 
    # Set Number of Mainframe sweeps
    """ return_var = gen.ghs_set_sweep_count_status(1)
    if return_var != "OK":
        print(f"Failed on GHSSetSweepCountStatus. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetSweepCountStatus - Return Status: {return_var}")
    """
    # Get sweep count status
    return_var, sweep_count_status = gen.ghs_get_sweep_count_status()
    if return_var != "OK":
        print(f"Failed on GHSGetSweepCountStatus. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetSweepCountStatus - Return Status: {return_var}\
        sweep_count_status: {sweep_count_status}"
    )
    
    # Get arm trigger enable type
    return_var, trigger_arm_enable = gen.ghs_get_trigger_arm_enabled()
    if return_var != "OK":
        print(f"Failed on GHSGetTriggerArmEnabled. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetTriggerArmEnabled - Return Status: {return_var}\
        trigger_arm_enable: {trigger_arm_enable}"
    )
    # masking as it is under development 
    # Set arm trigger enable type
    """ return_var = gen.ghs_set_trigger_arm_enabled(1)
    if return_var != "OK":
        print(f"Failed on GHSSetTriggerArmEnabled. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSSetTriggerArmEnabled - Return Status: {return_var}\
        trigger_arm_enable: {trigger_arm_enable}"
    )
    """
    # Get External Trigger Mode
    return_var, external_trigger_mode = gen.ghs_get_external_trigger_mode()
    if return_var != "OK":
        print(
            f"Failed on GHSGetExternalTriggerMode. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSGetExternalTriggerMode - Return Status: {return_var}\
          external_trigger_mode: {external_trigger_mode}")
    # masking as it is under development     
    # Set External Trigger Mode
    """ return_var = gen.ghs_set_external_trigger_mode(2)
    if return_var != "OK":
        print(
            f"Failed on GHSSetExternalTriggerMode. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetExternalTriggerMode - Return Status: {return_var}")
    """
    # Get External minimum Trigger pulse width
    return_var, external_min_pulse_width = gen.ghs_get_external_minimum_pulse_width()
    if return_var != "OK":
        print(
            f"Failed on GHSGetDebounceFilterTime. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSGetDebounceFilterTime(Get External Minimum Pulse width) - Return Status: {return_var}\
          external_min_pulse_width: {external_min_pulse_width}")
    # masking as it is under development     
    # Set External minimum Trigger pulse width
    """return_var = gen.ghs_set_external_minimum_pulse_width(3)
    if return_var != "OK":
        print(
            f"Failed on GHSSetDebounceFilterTime. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetDebounceFilterTime - Return Status: {return_var}")
    """

    # Determine the sweep length.
    return_var, sweep_length = gen.ghs_get_sweep_length("A")

    if return_var != "OK":
        print(
            f"Failed on GHSGetSweepLength. Return Status: {return_var}"
        )
        sys.exit()
    print(
        f"GHSGetSweepLength - Return Status: {return_var}\
        sweep length: {sweep_length}"
      )
    # masking as it is under development  
    # Set the sweep length.
    """ return_var = gen.ghs_set_sweep_length("A",1)
    if return_var != "OK":
        print(f"Failed on GHSSetSweepLength. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetSweepLength - Return Status: {return_var}")
    """
    # Determine the trigger position.
    return_var, trigger_position = gen.ghs_get_trigger_position("A")
    if return_var != "OK":
        print(f"Failed on GHSGetTriggerPosition. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetTriggerPosition - Return Status: {return_var}\
        trigger_position: {trigger_position}")
    # masking as it is under development  
    # Set the trigger position.
    """ return_var = gen.ghs_set_trigger_position("A", 1)
    if return_var != "OK":
        print(f"Failed on GHSSetTriggerPosition. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetTriggerPosition - Return Status: {return_var}")
    """
    # Determine the continuous_leadout_time.
    return_var, continuous_leadout_time = gen.ghs_get_continuous_leadout_time("A")
    if return_var != "OK":
        print(f"Failed on GHSGetContinuousLeadOutTime. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetContinuousLeadOutTime - Return Status: {return_var}\
       continuous_leadout_time: {continuous_leadout_time}"
    )
    # masking as it is under development  
     # set the continuous_leadout_time.
    """ return_var = gen.ghs_set_continuous_leadout_time("A", 23)
    if return_var != "OK":
        print(f"Failed on GHSSetContinuousLeadOutTime return Status: {return_var}")
        sys.exit()
    print(f"GHSSetContinuousLeadOutTime - Return Status: {return_var}")
    """
    # Disconnect
    return_var = gen.ghs_disconnect()
    if return_var != "OK":
        print(f"Failed on GHSDisconnect. Return Status: {return_var}")
        sys.exit()
    print(f"GHSDisconnect - Return Status: {return_var}")


if __name__ == "__main__":
    main()

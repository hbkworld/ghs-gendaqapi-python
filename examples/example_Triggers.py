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

IP_ADDRESS = "10.96.129.102"
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
    return_var = gen.ghs_set_start_data_recording(3)
    if return_var != "OK":
        print(f"Failed on GHSSetStartDataRecording. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetStartDataRecording - Return Status: {return_var}")

    # Get start data Recording
    return_var, start_data_recording = gen.ghs_get_start_data_recording()
    if return_var != "OK":
        print(f"Failed on GHSGetStartDataRecordingMethod. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetStartDataRecordingMethod - Return Status: {return_var}\
        start_data_recording: {start_data_recording}"
    )

    # Set Stop Data Recording
    return_var = gen.ghs_set_stop_data_recording(2)
    #return_var = gen.ghs_set_stop_data_recording("A",2)
    if return_var != "OK":
        print(f"Failed on GHSSetStopDataRecording. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetStopDataRecording - Return Status: {return_var}")

    # Get stop data Recording
    return_var, stop_data_recording = gen.ghs_get_stop_data_recording()
    if return_var != "OK":
        print(f"Failed on GHSGetStopDataRecordingMethod. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetStopDataRecordingMethod - Return Status: {return_var}\
        stop_data_recording: {stop_data_recording}"
    )
    
  # Set Number of Mainframe sweeps
    return_var = gen.ghs_set_number_of_mainframe_sweeps(1)
    if return_var != "OK":
        print(f"Failed on GHSSetNumberofMainframeSweeps. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetNumberofMainframeSweeps - Return Status: {return_var}")

    # Get Number of Mainframe sweeps
    return_var, number_of_mainframe_sweep = gen.ghs_get_number_of_mainframe_sweeps()
    if return_var != "OK":
        print(f"Failed on GHSGetNumberofMainframeSweep. Return Status: {return_var}")
        sys.exit()
    print(f"GHSGetNumberofMainframeSweep - Return Status: {return_var}\
        number_of_mainframe_sweep: {number_of_mainframe_sweep}"
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

    # Set arm trigger enable type
    return_var = gen.ghs_set_trigger_arm_enabled(1)
    if return_var != "OK":
        print(f"Failed on GHSSetTriggerArmEnabled. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSSetTriggerArmEnabled - Return Status: {return_var}\
        trigger_arm_enable: {trigger_arm_enable}"
    )
    
    # Get External Trigger Mode
    return_var, external_trigger_mode = gen.ghs_get_external_trigger_mode()
    if return_var != "OK":
        print(
            f"Failed on GHSGetExternalTriggerMode. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSGetExternalTriggerMode - Return Status: {return_var}\
          external_trigger_mode: {external_trigger_mode}")
    
    # Set External Trigger Mode
    return_var = gen.ghs_set_external_trigger_mode(2)
    if return_var != "OK":
        print(
            f"Failed on GHSSetExternalTriggerMode. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetExternalTriggerMode - Return Status: {return_var}")
    
        # Get External minimum Trigger pulse width
    return_var, external_min_pulse_width = gen.ghs_get_external_minimum_pulse_width()
    if return_var != "OK":
        print(
            f"Failed on GHSGetDebounceFilterTime. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSGetDebounceFilterTime(Get External Minimum Pulse width) - Return Status: {return_var}\
          external_min_pulse_width: {external_min_pulse_width}")
    
    # Set External minimum Trigger pulse width
    return_var = gen.ghs_set_external_minimum_pulse_width(3)
    if return_var != "OK":
        print(
            f"Failed on GHSSetDebounceFilterTime. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetDebounceFilterTime - Return Status: {return_var}")


    # Determine the sweep length.
    return_var, sweep_length = gen.ghs_get_sweep_length()

    if return_var != "OK":
        print(
            f"Failed on GHSGetSweepLength. Return Status: {return_var}"
        )
        sys.exit()
    print(
        f"GHSGetSweepLength - Return Status: {return_var}\
        sweep length: {sweep_length}"
      )

    # Set the excitation type and value for an analog channel.
    return_var = gen.ghs_set_sweep_length("A", 1, "Voltage", 15.0)
    if return_var != "OK" and return_var != "Adapted":
        print(f"Failed on GHSGetSweepLength. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetExcitation - Return Status: {return_var}")

    # Determine the excitation type and value for an analog channel.
    return_var, excitation_type, excitation_value = gen.ghs_get_excitation(
        "A", 1
    )
    if return_var != "OK":
        print(f"Failed on GHSGetExcitation. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetExcitation - Return Status: {return_var}\
        Excitation Type: {excitation_type}\
        Excitation Value: {excitation_value}"
    )

    # Set the amplifier mode for an analog channel.
    return_var = gen.ghs_set_amplifier_mode("A", 1, "Basic")
    if return_var != "OK":
        print(f"Failed on GHSSetAmplifierMode. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetAmplifierMode - Return Status: {return_var}")

    # Determine the amplifier mode for an analog channel.
    return_var, amplifier_mode = gen.ghs_get_amplifier_mode("A", 1)
    if return_var != "OK":
        print(f"Failed on GHSGetAmplifierMode. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetAmplifierMode - Return Status: {return_var}\
        Amplifier Mode: {amplifier_mode}"
    )

    # Set the technical units, unit multiplier and unit offset for an analog channel.
    return_var = gen.ghs_set_technical_units("A", 1, "KGS", 10.0, 20.0)
    if return_var != "OK":
        print(f"Failed on GHSSetTechnicalUnits. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetTechnicalUnits - Return Status: {return_var}")

    # Determine the technical units, unit multiplier and unit offset for an analog channel.
    return_var, units, multiplier, offset = gen.ghs_get_technical_units("A", 1)
    if return_var != "OK":
        print(f"Failed on GHSGetTechnicalUnits. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetTechnicalUnits - Return Status: {return_var}\
        Units: {units}\
        Multiplier: {multiplier}\
        Offset: {offset}"
    )

    # Set Auto range settings for analog channels.
    return_var = gen.ghs_set_auto_range("A", 1, "Enable", 10.0)
    if return_var != "OK":
        print(f"Failed on GHSSetAutoRange. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetAutoRange - Return Status: {return_var}")

    # Determine Auto range settings for analog channels.
    return_var, auto_range_enabled, auto_range_time = gen.ghs_get_auto_range(
        "A", 1
    )
    if return_var != "OK":
        print(f"Failed on GHSGetAutoRange. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetAutoRange - Return Status: {return_var}\
        Auto Range Enabled: {auto_range_enabled}\
        Auto Range Time: {auto_range_time}"
    )

    # Set Command a single shot for auto range.
    return_var = gen.ghs_cmd_auto_range_now("A", 1, 20.0)
    if return_var != "OK":
        print(f"Failed on GHSCmdAutoRangeNow. Return Status: {return_var}")
        sys.exit()
    print(f"GHSCmdAutoRangeNow - Return Status: {return_var}")

    # Determine calibration information for an analog channel.
    (
        return_var,
        calibration_date_time,
        verification_date_time,
        power_verification_date_time,
        calibration_lab,
        verification_lab,
        power_verification_lab,
    ) = gen.ghs_get_channel_cal_info("A", 1)
    if return_var != "OK":
        print(
            f"Failed on GHSGetChannelCalibrationInformation. Return Status: {return_var}"
        )
        sys.exit()
    print(
        f"GHSGetChannelCalibrationInformation - Return Status: {return_var}\
        Calibration Date Time: {calibration_date_time}\
        Verification Date Time: {verification_date_time}\
        Power Verification Date Time: {power_verification_date_time}\
        Calibration Lab: {calibration_lab}\
        Verification Lab: {verification_lab}\
        Power Verification Lab: {power_verification_lab}"
    )

    ## NOTE: Enter valid timer/counter channel slot ID and index
    # Set the gate time for a timer/counter channel.
    return_var = gen.ghs_set_timer_counter_gate_time("A", 1, 23.0)
    if return_var != "OK":
        print(
            f"Failed on GHSSetTimerCounterGateTime. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetTimerCounterGateTime - Return Status: {return_var}")

    # Determine the gate time for a timer/counter channel.
    return_var, gate_time = gen.ghs_get_timer_counter_gate_time("A", 1)
    if return_var != "OK":
        print(
            f"Failed on GHSGetTimerCounterGateTime. Return Status: {return_var}"
        )
        sys.exit()
    print(
        f"GHSGetTimerCounterGateTime - Return Status: {return_var}\
        Gate Time: {gate_time}"
    )

    # Set the mode for a timer/counter channel.
    return_var = gen.ghs_set_timer_counter_mode("A", 1, "CountQuadrature")
    if return_var != "OK":
        print(f"Failed on GHSSetTimerCounterMode. Return Status: {return_var}")
        sys.exit()
    print(f"GHSSetTimerCounterMode - Return Status: {return_var}")

    # Determine the mode for a timer/counter channel.
    return_var, mode = gen.ghs_get_timer_counter_mode("A", 1)
    if return_var != "OK":
        print(f"Failed on GHSGetTimerCounterMode. Return Status: {return_var}")
        sys.exit()
    print(
        f"GHSGetTimerCounterMode - Return Status: {return_var}\
        Timer/counter mode: {mode}"
    )

    # Set the range for a timer/counter channel.
    return_var = gen.ghs_set_timer_counter_range("A", 1, 10.0, 20.0)
    if return_var != "OK":
        print(
            f"Failed on GHSSetTimerCounterRange. Return Status: {return_var}"
        )
        sys.exit()
    print(f"GHSSetTimerCounterRange - Return Status: {return_var}")

    # Determine the range for a timer/counter channel.
    return_var, lower, upper = gen.ghs_get_timer_counter_range("A", 1)
    if return_var != "OK":
        print(
            f"Failed on GHSGetTimerCounterRange. Return Status: {return_var}"
        )
        sys.exit()
    print(
        f"GHSGetTimerCounterRange - Return Status: {return_var}\
        Lower value: {lower}\
        Upper value: {upper}"
    )

    # Disconnect
    return_var = gen.ghs_disconnect()
    if return_var != "OK":
        print(f"Failed on GHSDisconnect. Return Status: {return_var}")
        sys.exit()
    print(f"GHSDisconnect - Return Status: {return_var}")


if __name__ == "__main__":
    main()

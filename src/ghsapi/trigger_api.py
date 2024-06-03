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

"""Trigger module interface."""

from .connection import ConnectionHandler
from .ghsapi_states import (
    RETURN_KEY,
    GHSReturnValue,
    GHSStartDataRecordingMethod,
    GHSStopDataRecordingMethod,
    from_string,
    to_string,
)


def get_start_data_recording(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    
    """Determine the start data recording.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Returns:
        * GHSReturnValue - API return values
        * GHSStartDataRecording - Start Data Recording
    """
    response_json = con_handle.send_request_wait_response (
       "GetStartDataRecordingMethod", None
    )

    if ("Method" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["Method"]
    )

def set_start_data_recording(
    con_handle: ConnectionHandler,
    start_data_recording: str | int,
) -> str:
    """Set the start data recording.

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        slot_id: The slot containing the recorder
        start_data_recording: data recording

    Returns:
        * GHSReturnValue - API return values
    """
    start_data_recording_dict = {
        "Method": start_data_recording,
    }

    if not start_data_recording:
        return "NullPtrArgument"

    if isinstance(start_data_recording, str) and start_data_recording in GHSStartDataRecordingMethod:
        start_data_recording = from_string(start_data_recording, GHSStartDataRecordingMethod)

    elif isinstance(start_data_recording, int) and start_data_recording in GHSStartDataRecordingMethod.values():
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetStartDataRecordingMethod", start_data_recording_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)


def get_stop_data_recording(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    """Determine the name of a channel.

     The channel name is UTF-8 encoded.

     Read - This method can be called by multiple connected clients at
     same time.

    Args:
        con_handle: A unique identifier per mainframe connection.
        slot_id: The slot containing the recorder to get number of
        channels for (e.g. 'A' for the first slot).
        channel_index: The one-based index of the specified channel type to determine
        the name for.
        channel_type: The specific channel type.

    Returns:
       Tuple with status and name of the channel.
    """
    response_json = con_handle.send_request_wait_response (
       "GetStopDataRecordingMethod", None
    )

    if ("Method" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["Method"]
    )
    
def set_stop_data_recording(
    con_handle: ConnectionHandler,
    stop_data_recording: str | int,
) -> str:
    """Set the stop data recording.

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * stop_data_recording: stop data recording

    Returns:
        * GHSReturnValue - API return values
    """
    stop_data_recording_dict = {
        "Method": stop_data_recording,
    }

    if not stop_data_recording:
        return "NullPtrArgument"

    if isinstance(stop_data_recording, str) and stop_data_recording in GHSStopDataRecordingMethod:
        stop_data_recording = from_string(stop_data_recording, GHSStopDataRecordingMethod)

    elif isinstance(stop_data_recording, int) and stop_data_recording in GHSStopDataRecordingMethod.values():
        pass
    
    else:
        return "InvalidDataType"

    response_json = con_handle.send_request_wait_response(
        "SetStopDataRecordingMethod", stop_data_recording_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)

def get_number_of_Mainframe_sweeps(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    """Determine the number of mainframe sweeps.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Returns:
        * GHSReturnValue - API return values
        * number_of_mainframe_sweeps - number of mainframe sweeps
    """
    response_json = con_handle.send_request_wait_response (
       "GetNumberOfMainframeSweeps", None
    )

    if ("Count" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["Count"]
    )

def set_number_of_Mainframe_sweeps(
    con_handle: ConnectionHandler,
    number_of_Mainframe_sweeps: int,
) -> str:
    """Set the mainframe sweeps.

    *The system needs to be idle before calling this function.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * number_of_mainframe_sweeps - number of mainframe sweeps

    Returns:
        * GHSReturnValue - API return values
    """
    Mainframesweeps_dict = {
        "Count": number_of_Mainframe_sweeps,
    }

    if not number_of_Mainframe_sweeps:
        return "NullPtrArgument"


    if isinstance(number_of_Mainframe_sweeps, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetNumberOfMainframeSweeps", Mainframesweeps_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)

def get_trigger_arm_enabled(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    """Determine the trigger arm enable.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Returns:
        * GHSReturnValue - API return values
        * trigger_arm_enabled: trigger arm enable
    """
    response_json = con_handle.send_request_wait_response (
       "GetTriggerArmEnabled", None
    )

    if ("Enable" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["Enable"]
    )

def set_trigger_arm_enabled(
    con_handle: ConnectionHandler,
    trigger_arm_enable: bool,
) -> str:
    """Set the trigger arm enable.

    *The system needs to be idle before calling this function.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * trigger_arm_enabled: trigger arm enable

    Returns:
        * GHSReturnValue - API return values
    """
    trigger_arm_enable_dict = {
        "Enable": trigger_arm_enable,
    }

    if not trigger_arm_enable:
        return "NullPtrArgument"


    if isinstance(trigger_arm_enable, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetTriggerArmEnabled", trigger_arm_enable_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)

def get_external_trigger_mode(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    """Determine the external trigger mode.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Returns:
        * GHSReturnValue - API return values
        * external_trigger_mode: external trigger mode
    """
    response_json = con_handle.send_request_wait_response (
       "GetExternalTriggerMode", None
    )

    if ("Mode" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["Mode"]
    )

def set_external_trigger_mode(
    con_handle: ConnectionHandler,
    external_trigger_mode: str | int,
) -> str:
    """Set the external trigger mode.

    *The system needs to be idle before calling this function.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * external_trigger_mode: external trigger mode

    Returns:
        * GHSReturnValue - API return value
    """
    external_trigger_mode_dict = {
        "Mode": external_trigger_mode,
    }

    if not external_trigger_mode:
        return "NullPtrArgument"

    if isinstance(external_trigger_mode, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetExternalTriggerMode", external_trigger_mode_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)

def get_external_minimum_pulse_width(
    con_handle: ConnectionHandler,
) -> tuple[str, int | None]:
    """Determine the external minimum pulse width or debounce filter time.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Returns:
        * GHSReturnValue - API return values
        * external minimum pulse width - Debounce filter time
    """
    response_json = con_handle.send_request_wait_response (
       "GetDebounceFilterTime", None
    )

    if ("DebounceIn" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["DebounceIn"]
    )

def set_external_minimum_pulse_width(
    con_handle: ConnectionHandler,
    debounce_filter_time: str | int,
) -> str:
    """Set the external minimum pulse width or debounce filter time.

    *The system needs to be idle before calling this function.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * number_of_mainframe_sweeps - number of mainframe sweeps
    Returns:
        * GHSReturnValue - API return values
    """
    debounce_filter_time_dict = {
        "DebounceIn": debounce_filter_time,
    }

    if not debounce_filter_time:
        return "NullPtrArgument"


    if isinstance(debounce_filter_time, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetDebounceFilterTime", debounce_filter_time_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)


def get_sweep_length(
    con_handle: ConnectionHandler,
    slot_id: str
) -> tuple[str, int | None]:
    """Determine the sweep length.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Args:
        * slot_id: The slot containing the recorder
 
    Returns:
        * GHSReturnValue - API return values
        * Sweep Length - Sweep length
    """

    sweepLengthParamDict = {
        'SlotId': slot_id,
    }
    response_json = con_handle.send_request_wait_response (
       "GetSweepLength", sweepLengthParamDict
    )

    if ("SweepLength" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["SweepLength"]
    )

def set_sweep_length(
    con_handle: ConnectionHandler,
    slot_id: str,
    sweep_length: str | int,
) -> str:
    """Set the sweep length.

    *The system needs to be idle before calling this function.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * slot_id: The slot containing the recorder
        * sweep_length: length of the sweep

    Returns:
        * GHSReturnValue - API return values
    """
    sweep_length_dict = {
        "SlotId":slot_id,
        "SweepLength": sweep_length,
    }

    if not slot_id or not sweep_length:
        return "NullPtrArgument"

    if isinstance(sweep_length, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetSweepLength", sweep_length_dict
    )

    return to_string(response_json[RETURN_KEY], GHSReturnValue)


def get_trigger_position(
    con_handle: ConnectionHandler,
    slot_id: str
) -> tuple[str, int | None]:
    """Determine the trigger position.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Args:
        * slot_id: The slot containing the recorder

    Returns:
        * GHSReturnValue - API return values
        * trigger_position - trigger position
    """
    TriggerPosition_ParamDict = {
        'SlotId': slot_id,
    }
    response_json = con_handle.send_request_wait_response (
       "GetTriggerPosition", TriggerPosition_ParamDict
    )

    if ("TriggerPosition" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["TriggerPosition"]
    )

def set_trigger_position(
    con_handle: ConnectionHandler,
    slot_id: str,
    trigger_position: str | int,
) -> str:
    """Set the trigger position.

    *The system needs to be idle before calling this function.*

    *If the specified timer/counter mode is not supported by the recorder, the
    timer/counter mode remains unchanged.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * slot_id: The slot containing the recorder
        * trigger_position: trigger position

    Returns:
        * GHSReturnValue - API return values
    """
    trigger_position_dict = {
        "SlotId":slot_id,
        "TriggerPosition": trigger_position,
    }

    if not slot_id or not trigger_position:
        return "NullPtrArgument"


    if isinstance(trigger_position, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetTriggerPosition", trigger_position_dict
    )
    return to_string(response_json[RETURN_KEY], GHSReturnValue)


def get_continuous_leadout_time(
    con_handle: ConnectionHandler,
    slot_id: str
) -> tuple[str, int | None]:
    """Determine the  continuous lead out time.

    *Read - This method can be called by multiple connected clients at same
    time.*

    Args:
        * slot_id: The slot containing the recorder

    Returns:
        * GHSReturnValue - API return values
        * continuous_leadout_time - continuous leadout time
    """
    continuous_leadout_time_paramDict = {
        'SlotId': slot_id,
    }
    response_json = con_handle.send_request_wait_response (
       "GetContinuousLeadOutTime", continuous_leadout_time_paramDict
    )

    if ("ContinuousLeadOutTime" not in response_json) or (
        response_json[RETURN_KEY] != GHSReturnValue["OK"]
    ):
        return to_string(response_json[RETURN_KEY], GHSReturnValue), None
    return (
        to_string(response_json[RETURN_KEY], GHSReturnValue),
        response_json["ContinuousLeadOutTime"]
    )

def set_continuous_leadout_time(
    con_handle: ConnectionHandler,
    slot_id: str,
    continuous_leadout_time: str | int,
) -> str:
    """Set the continuous lead out time.

    *The system needs to be idle before calling this function.*

    *If the specified timer/counter mode is not supported by the recorder, the
    timer/counter mode remains unchanged.*

    *ReadWrite - This method will only process requests from the
    connected client with the most privileges order (Privileges
    order: 1- Perception, 2- GenDaq, 3- Other)*

    Args:
        * slot_id: The slot containing the recorder
        * continuous_leadout_time: continuous lead out time

    Returns:
        * GHSReturnValue - API return values
    """
    continuous_leadout_time_dict = {
        "SlotId":slot_id,
        "ContinuousLeadOutTime": continuous_leadout_time,
    }

    if not slot_id or not continuous_leadout_time:
        return "NullPtrArgument"

    if isinstance(continuous_leadout_time, int):
        pass

    else:
        return "InvalidDataType"
    
    response_json = con_handle.send_request_wait_response(
        "SetContinuousLeadOutTime", continuous_leadout_time_dict
    )
    return to_string(response_json[RETURN_KEY], GHSReturnValue)

def calculate_latency(transmit_time: float, receive_time: float) -> float:
    """
    Calculates the network latency of a telemetry packet in milliseconds.
    """
    if receive_time < transmit_time:
        raise ValueError("Receive time cannot be before transmit time.")
    return (receive_time - transmit_time) * 1000
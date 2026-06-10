# data/stream_simulator.py

import time
import random
from datetime import datetime
from collections import deque

class StreamSimulator:
    """
    Simulates live hospital events coming from:
    - ER
    - ICU
    - General Ward

    Can be plugged into the Digital Twin engine.
    """

    def __init__(self, max_history=100):

        self.history = deque(maxlen=max_history)

        self.state = {
            "er": 20,
            "icu": 8,
            "general": 35
        }

    def generate_event(self):

        hour = datetime.now().hour

        # ER demand pattern
        if hour >= 18 or hour <= 6:
            er_delta = random.randint(0, 6)
        else:
            er_delta = random.randint(-2, 4)

        # ICU changes slowly
        icu_delta = random.randint(-1, 2)

        # General ward more stable
        general_delta = random.randint(-2, 3)

        self.state["er"] = max(
            0,
            self.state["er"] + er_delta
        )

        self.state["icu"] = max(
            0,
            self.state["icu"] + icu_delta
        )

        self.state["general"] = max(
            0,
            self.state["general"] + general_delta
        )

        total_load = (
            self.state["er"] +
            self.state["icu"] +
            self.state["general"]
        )

        event = {
            "timestamp": datetime.now(),
            "er": self.state["er"],
            "icu": self.state["icu"],
            "general": self.state["general"],
            "total_load": total_load
        }

        self.history.append(event)

        return event

    def get_recent_events(self):

        return list(self.history)

    def stream(self, interval=1):

        while True:
            yield self.generate_event()
            time.sleep(interval)


if __name__ == "__main__":

    simulator = StreamSimulator()

    for event in simulator.stream(interval=2):
        print(event)

from circular_buffer import CircularBuffer


class DelayLine(CircularBuffer):
    def __init__(self, sampling_rate: int, max_delay, delay=1):
        super().__init__(sampling_rate, delay)
        self.out = 0
        self.sampling_rate = sampling_rate
        self.max_delay = max_delay

    def process_signal(self, buffer_input: float) -> float:
        self.out = self.buffer[self.read_index]
        self.buffer[self.write_index] = buffer_input
        return self.out

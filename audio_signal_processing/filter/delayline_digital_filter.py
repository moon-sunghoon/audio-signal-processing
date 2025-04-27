from circular_buffer import CircularBuffer


class OnePoleFilter(CircularBuffer):
    def __init__(
        self, sampling_rate: int, gain: float, cutoff_frequency: float
    ):
        super().__init__(sampling_rate)
        self.out = 0
        self.sampling_rate = sampling_rate
        self.gain = gain
        self.cutoff_frequency = cutoff_frequency

    def process_signal(self, buffer_input: float) -> float:
        self.out = self.buffer[self.read_index]
        self.buffer[self.write_index] = buffer_input
        return self.out

from abc import ABC, abstractmethod

class CircularBuffer(ABC):
    def __init__(self, size):
        self.buffer = [0] * size
        self.index = 0
        self.write_index = 0
        self.read_index = 0
        self.out = 0.0
        self.delay = 1

    def process_frame(self, input, delay):
        self.read_index = self.write_index - delay
        if self.read_index < 0 :
            self.read_index = self.buffer

        self.process_buffer(input, delay)

        self.write_index += 1
        if write_index > self.buffer:
            write_index = 0

    @abstractmethod
    def process_buffer(self, input, delay):
        pass

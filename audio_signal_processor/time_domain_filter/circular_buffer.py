from abc import ABC, abstractmethod

class CircularBuffer(ABC):
    """
        This class represents a circular buffer

        Properties:
            buffer (list) : a buffer with the given size
            write_index (int) : write index for the buffer
            read_index (int) : read index for the buffer

    """
    def __init__(self, size, delay = 1):
        self.buffer = [0] * size
        self.write_index = 0
        self.read_index = 0
        self.delay = delay
        self.buffer_size = size

    def set_delay(self, delay: int) -> None:
        self.delay = delay

    def get_delay(self) -> int:
        return self.delay    

    def run_buffer(self, buffer_input: float) -> float:
        """
        This function process a frame of coming input using a processing line

        Parameters:
            buffer_input (float): input signal
        Returns:
            buffer_ouput (float): output signal

        """
        self.read_index = self.write_index - self.delay
        if self.read_index < 0 :
            self.read_index += self.buffer_size

        buffer_output = self.process_signal(buffer_input)

        self.write_index += 1
        if self.write_index > self.buffer_size:
            self.write_index = 0

        return buffer_output

    @abstractmethod
    def process_signal(self, buffer_input : float) -> float:
        """
        abtract method for processing line, implement a filter here.

        Parameters:
            buffer_input (float): input signal

        Returns:
            buffer_ouput (float): output signal

        """
from abc import ABC, abstractmethod

class CircularBuffer(ABC):
    """
        This class represents a circular buffer

        Properties:
            buffer (list) : a buffer with the given size
            write_index (int) : write index for the buffer
            read_index (int) : read index for the buffer

    """
    def __init__(self, size):
        self.buffer = [0] * size
        self.write_index = 0
        self.read_index = 0

    def process_frame(self, buffer_input: float, delay: int) -> float:
        """
        This function process a frame of coming input using a processing line

        Parameters:
            buffer_input (float): input signal
            delay: amount of sample delayed

        Returns:
            buffer_ouput (float): output signal

        """
        self.read_index = self.write_index - delay
        if self.read_index < 0 :
            self.read_index = self.buffer

        buffer_output = self.process_buffer(buffer_input, delay)

        self.write_index += 1
        if write_index > self.buffer:
            write_index = 0

        return buffer_output

    @abstractmethod
    def process_buffer(self, buffer_input : float, delay: int) -> float:
        """
        abtract method for processing line, implement a filter here.

        Parameters:
            buffer_input (float): input signal
            delay: amount of sample delayed

        Returns:
            buffer_ouput (float): output signal

        """
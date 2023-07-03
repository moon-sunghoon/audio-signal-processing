import sys
sys.path.append('..')
from delayline import DelayLine

import unittest

class DelayLineTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sampling_rate = 48000
        self.max_delay = 1000
        self.test_input = [1.5, 2.0, 2.5, 3.0]

    def test_output_default_delayed_sampe(self):
        delay_line = DelayLine(self.sampling_rate, self.max_delay)
        expected_output = [0.0, 1.5, 2.0, 2.5]
        output = []
        for input_frame in self.test_input:
            output.append(delay_line.run_buffer(input_frame))
        self.assertEqual(output, expected_output)

    def test_output_non_default_delayed_sampe(self):
        delay_line = DelayLine(self.sampling_rate, self.max_delay, delay = 3)
        expected_output = [0.0, 0.0, 0.0, 1.5]
        output = []
        for input_frame in self.test_input:
            output.append(delay_line.run_buffer(input_frame))
        print(output)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
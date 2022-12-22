from util import Input

def unique_seq_end(stream, sequence_length=4):
    for i in range(0, len(stream) - sequence_length):
        if len(set(stream[i:i+sequence_length])) == sequence_length:
            return i + sequence_length

test_input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
real_input = Input(6).read()

assert unique_seq_end(test_input) == 10
print("Part 1:", unique_seq_end(real_input))

assert unique_seq_end(test_input, sequence_length=14) == 29
print("Part 2:", unique_seq_end(real_input, sequence_length=14))

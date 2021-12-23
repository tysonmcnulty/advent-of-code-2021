from itertools import islice

def load_transmission(bits_transmission_file):
    with open(bits_transmission_file, "r") as file:
        return next(file).strip()

class EndOfBits(Exception): pass

def read_bits(bits, n):
    try:
        next_bits = []
        for _ in range(n): next_bits.append(next(bits))
        return ''.join(next_bits)
    except StopIteration:
        raise EndOfBits()

class Packet:
    def __init__(self, bits, exhaust = True):
        self._bits = ''
        self._suffix = None
        self._value = None
        self._sub_packets = []

        def advance_bits(n):
            self._bits += read_bits(bits, n)
            return self._bits[-n:]

        self._version = int(advance_bits(3), 2)
        self._type_id = int(advance_bits(3), 2)

        if self._type_id == 4:  # literal packet
            literal = []
            while True:
                block = advance_bits(5)
                literal += block[1:]
                if block[0] == "0": break

            self._value = int(''.join(literal), 2)

        else:
            length_type_id = int(advance_bits(1))
            if length_type_id == 0:

                sub_packets_length = int(advance_bits(15), 2)
                self._sub_packets += Packets.from_bits(
                    islice(bits, sub_packets_length),
                    exhaust = False)
            elif length_type_id == 1:
                sub_packets_count = int(advance_bits(11), 2)
                self._sub_packets += (
                    Packet(bits, exhaust=False) for _ in range(sub_packets_count))

        if exhaust:
            self._suffix = read_bits(bits, -len(self.bits) % 8)
            assert not any(b == "1" for b in self._suffix), f"Encountered nonzero padding at end of packet: {self._bits[:-len(self._suffix)]}[{self._suffix}]"


    @property
    def version(self): return self._version

    @property
    def type_id(self): return self._type_id

    @property
    def value(self): return self._value

    @property
    def sub_packets(self): return self._sub_packets

    @property
    def bits(self):
        return ''.join((
            self._bits,
            ''.join(p.bits for p in self._sub_packets),
            self._suffix or ''
        ))

    def __repr__(self):
        return ''.join([
            "Packet(",
            f"iter(\"{self.bits}\"),",
            f"exhaust={(self._suffix != None)}",
            ")"
        ])

class Packets:
    @staticmethod
    def from_bits(bits, **kwargs):
        while True:
            try:
                yield Packet(bits, **kwargs)
            except EndOfBits:
                break

    @staticmethod
    def from_transmission(bits_transmission):
        nibbles = (bin(int(hex_char, 16))[2:].zfill(4) for hex_char in bits_transmission if not hex_char.isspace())
        bits = (b for n in nibbles for b in n)

        yield from Packets.from_bits(bits)

    @staticmethod
    def traverse(packets, key=lambda p: p):
        for p in packets:
            yield key(p)
            yield from Packets.traverse(p.sub_packets, key)

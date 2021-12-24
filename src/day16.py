from enum import Enum
from itertools import islice
from functools import reduce

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
    class Type(Enum):
        SUM = 0
        PRODUCT = 1
        MINIMUM = 2
        MAXIMUM = 3
        LITERAL = 4
        GREATER_THAN = 5
        LESS_THAN = 6
        EQUAL = 7

    class LengthType(Enum):
        SUB_PACKET_LENGTH = 0
        SUB_PACKET_COUNT = 1

    def __init__(self, bits, exhaust = True):
        self._bits = ''
        self._suffix = None
        self._value = None
        self._sub_packets = []

        def advance_bits(n):
            self._bits += read_bits(bits, n)
            return self._bits[-n:]

        self._version = int(advance_bits(3), 2)
        self._type = Packet.Type(int(advance_bits(3), 2))

        if self._type == Packet.Type.LITERAL:
            literal = []
            while True:
                block = advance_bits(5)
                literal += block[1:]
                if block[0] == "0": break

            self._value = int(''.join(literal), 2)

        else:
            self._length_type = Packet.LengthType(int(advance_bits(1)))
            if self._length_type == Packet.LengthType.SUB_PACKET_LENGTH:
                sub_packets_length = int(advance_bits(15), 2)
                self._sub_packets += Packets.from_bits(
                    islice(bits, sub_packets_length),
                    exhaust = False)
            elif self._length_type == Packet.LengthType.SUB_PACKET_COUNT:
                sub_packets_count = int(advance_bits(11), 2)
                self._sub_packets += (
                    Packet(bits, exhaust=False) for _ in range(sub_packets_count))

        if exhaust:
            self._suffix = read_bits(bits, -len(self.bits) % 8)
            assert not any(b == "1" for b in self._suffix), f"Encountered nonzero padding at end of packet: {self._bits[:-len(self._suffix)]}[{self._suffix}]"

    @property
    def version(self): return self._version

    @property
    def type(self): return self._type

    @property
    def value(self):
        if self._type == Packet.Type.LITERAL:
            return self._value
        else:
            return reduce({
                Packet.Type.SUM: lambda acc, curr: acc + curr,
                Packet.Type.PRODUCT: lambda acc, curr: acc * curr,
                Packet.Type.MINIMUM: lambda acc, curr: min(acc, curr),
                Packet.Type.MAXIMUM: lambda acc, curr: max(acc, curr),
                Packet.Type.GREATER_THAN: lambda x1, x2: int(x1 > x2),
                Packet.Type.LESS_THAN: lambda x1, x2: int(x1 < x2),
                Packet.Type.EQUAL: lambda x1, x2: int(x1 == x2)
            }[self._type], map(lambda p: p.value, self._sub_packets))

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

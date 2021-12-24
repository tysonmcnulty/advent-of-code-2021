import os
import unittest

from src.day16 import load_transmission, Packets, Packet

class Day16Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.packets_test = list(Packets.from_transmission(' '.join((
            "D2FE28",
            "38006F45291200",
            "EE00D40C823060",
            "8A004A801A8002F478",
            "620080001611562C8802118E34",
            "C0015000016115A2E0802F182340",
            "A0016C880162017C3686B18A3D4780"
        ))))
        cls.packets_tm = list(Packets.from_transmission(
            load_transmission('data/day16_bits_transmission_tm.txt')))

    def test_literal_packet(self):
        packet = self.packets_test[0]

        self.assertEqual(6, packet.version)
        self.assertEqual(Packet.Type.LITERAL, packet.type)
        self.assertEqual(2021, packet.value)

    def test_operator_packet_with_length_type_0(self):
        packet = self.packets_test[1]

        self.assertEqual(1, packet.version)
        self.assertEqual(Packet.Type.LESS_THAN, packet.type)
        self.assertEqual(1, packet.value)

        self.assertEqual(2, len(packet.sub_packets))
        self.assertEqual(Packet.Type.LITERAL, packet.sub_packets[0].type)
        self.assertEqual(10, packet.sub_packets[0].value)
        self.assertEqual(Packet.Type.LITERAL, packet.sub_packets[1].type)
        self.assertEqual(20, packet.sub_packets[1].value)

    def test_operator_packet_with_length_type_1(self):
        packet = self.packets_test[2]

        self.assertEqual(7, packet.version)
        self.assertEqual(Packet.Type.MAXIMUM, packet.type)
        self.assertEqual(3, packet.value)

        self.assertEqual(3, len(packet.sub_packets))
        self.assertEqual(Packet.Type.LITERAL, packet.sub_packets[0].type)
        self.assertEqual(1, packet.sub_packets[0].value)
        self.assertEqual(Packet.Type.LITERAL, packet.sub_packets[1].type)
        self.assertEqual(2, packet.sub_packets[1].value)
        self.assertEqual(Packet.Type.LITERAL, packet.sub_packets[2].type)
        self.assertEqual(3, packet.sub_packets[2].value)

    def test_version_sums(self):
        version_sum = lambda packets: \
            sum(Packets.traverse(packets, key=lambda p: p.version))

        self.assertEqual(16, version_sum([self.packets_test[3]]))
        self.assertEqual(12, version_sum([self.packets_test[4]]))
        self.assertEqual(23, version_sum([self.packets_test[5]]))
        self.assertEqual(31, version_sum([self.packets_test[6]]))

        self.assertEqual(901, version_sum(self.packets_tm))

    def test_value(self):
        packets = list(Packets.from_transmission(' '.join((
            "C200B40A82",
            "04005AC33890",
            "880086C3E88112",
            "CE00C43D881120",
            "D8005AC2A8F0",
            "F600BC2D8F",
            "9C005AC2F8F0",
            "9C0141080250320F1802104A08",
        ))))
        self.assertEqual(3, packets[0].value)
        self.assertEqual(54, packets[1].value)
        self.assertEqual(7, packets[2].value)
        self.assertEqual(9, packets[3].value)
        self.assertEqual(1, packets[4].value)
        self.assertEqual(0, packets[5].value)
        self.assertEqual(0, packets[6].value)
        self.assertEqual(1, packets[7].value)

        self.assertEqual(1, len(self.packets_tm))
        self.assertEqual(110434737925, self.packets_tm[0].value)

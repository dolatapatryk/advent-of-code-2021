from abc import abstractmethod
import math

PACKET_VER_START_IDX = 0
PACKET_VER_END_IDX = 3
PACKET_TYPE_START_IDX = 3
PACKET_TYPE_END_IDX = 6
LITERAL_PACKET_TYPE = 4
LITERAL_PACKET_GROUP_LEN = 5
HEADER_SIZE = 6

class Packet:

    @classmethod
    def from_bits(cls, bits):
        packet_type = int(bits[PACKET_TYPE_START_IDX:PACKET_TYPE_END_IDX], 2)
        if packet_type == LITERAL_PACKET_TYPE:
            return LiteralPacket(bits)
        else:
            return OperatorPacket(bits)


    def cut_header(self):
        return self.bits[HEADER_SIZE:]

    @abstractmethod
    def get_result(self):
        pass
    
    @abstractmethod
    def calculate_version(self):
        pass

class LiteralPacket(Packet):

    def __init__(self, bits):
        self.bits = bits
        self.packet_ver = int(bits[PACKET_VER_START_IDX:PACKET_VER_END_IDX], 2)
        self.packet_type = LITERAL_PACKET_TYPE
        self.literal_value = self.__get_literal_value()

    def __get_literal_value(self):
        # for literal packet first bit determine if it's last group or not - 0 = last group
        groups = []
        processed_bits = 0
        bits_without_header = self.cut_header()
        while True:
            offset = processed_bits + LITERAL_PACKET_GROUP_LEN
            group = bits_without_header[processed_bits:offset]
            groups.append(group)
            processed_bits += LITERAL_PACKET_GROUP_LEN
            if group[0] == '0':
                break
        literal_value = int(''.join([group[1:] for group in groups]), 2)
        self.bits = self.bits[:HEADER_SIZE+processed_bits]
        return literal_value

    def get_result(self):
        return self.literal_value

    def calculate_version(self):
        return self.packet_ver
    
    def __len__(self):
        return len(self.bits)

class OperatorPacket(Packet):

    def __init__(self, bits):
        self.bits = bits
        self.packet_ver = int(bits[PACKET_VER_START_IDX:PACKET_VER_END_IDX], 2)
        self.packet_type = int(bits[PACKET_TYPE_START_IDX:PACKET_TYPE_END_IDX], 2)
        self.subpackets = self.__get_subpackets()

    def __get_subpackets(self):
        bits_without_header = self.cut_header()
        length_type = int(bits_without_header[0], 2)
        binary_without_length_type = bits_without_header[1:]
        subpackets = []
        counter = 0
        if length_type == 0:
            total_subpackets_bits = int(binary_without_length_type[:15], 2)
            subpackets_binary = binary_without_length_type[15:15+total_subpackets_bits]
            while counter < total_subpackets_bits:
                subpacket = Packet.from_bits(subpackets_binary[counter:])
                subpackets.append(subpacket)
                counter += len(subpacket)
            counter += 15 + 1
        else:
            number_of_subpackets = int(binary_without_length_type[0:11], 2)
            subpackets_binary = binary_without_length_type[11:]
            processed_subpackets = 0
            while processed_subpackets < number_of_subpackets:
                subpacket = Packet.from_bits(subpackets_binary[counter:])
                subpackets.append(subpacket)
                processed_subpackets += 1
                counter += len(subpacket)
            counter += 11 + 1
        self.bits = self.bits[:HEADER_SIZE+counter]
        return subpackets

    def get_result(self):
        if self.packet_type == 0:
            return sum([sub.get_result() for sub in self.subpackets])
        elif self.packet_type == 1:
            return math.prod([sub.get_result() for sub in self.subpackets])
        elif self.packet_type == 2:
            return min([sub.get_result() for sub in self.subpackets])
        elif self.packet_type == 3:
            return max([sub.get_result() for sub in self.subpackets])
        elif self.packet_type == 5:
            return 1 if self.subpackets[0].get_result() > self.subpackets[1].get_result() else 0
        elif self.packet_type == 6:
            return 1 if self.subpackets[0].get_result() < self.subpackets[1].get_result() else 0
        elif self.packet_type == 7:
            return 1 if self.subpackets[0].get_result() == self.subpackets[1].get_result() else 0

    def calculate_version(self):
        result = self.packet_ver
        for sub in self.subpackets:
            result += sub.calculate_version()
        return result

    def __len__(self):
        return len(self.bits)
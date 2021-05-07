from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.util.ints import uint64
from chia.util.hash import std_hash
import io


class TestCoin:
    def test_coin_serialization(self):

        c = Coin(bytes32(b"a" * 32), bytes32(b"b" * 32), uint64(0xFFFF))
        expected = (b"a" * 32) + (b"b" * 32) + bytes([0, 0xFF, 0xFF])
        expected2 = (b"a" * 32) + (b"b" * 32) + bytes([0, 0, 0, 0, 0, 0, 0xFF, 0xFF])
        assert c.get_hash() == std_hash(expected)
        assert c.name() == std_hash(expected)
        f = io.BytesIO()
        c.stream(f)
        assert bytes(f.getvalue()) == expected2

        c = Coin(bytes32(b"a" * 32), bytes32(b"b" * 32), uint64(1337000000))

        expected = (b"a" * 32) + (b"b" * 32) + bytes([0x4F, 0xB1, 0x00, 0x40])
        expected2 = (b"a" * 32) + (b"b" * 32) + bytes([0, 0, 0, 0, 0x4F, 0xB1, 0x00, 0x40])
        assert c.get_hash() == std_hash(expected)
        assert c.name() == std_hash(expected)
        f = io.BytesIO()
        c.stream(f)
        assert bytes(f.getvalue()) == expected2

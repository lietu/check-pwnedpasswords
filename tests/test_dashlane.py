from __future__ import unicode_literals
from snapshottest import TestCase
from os.path import realpath, dirname, join
from check_pwnedpasswords import DashlaneJsonReader, PasswordEntry


class TestDashlane(TestCase):
    source = None

    @classmethod
    def setUpClass(cls):
        path = join(dirname(realpath(__file__)), "DashlaneExport.json")
        cls.source = DashlaneJsonReader(path)
        super(cls, TestDashlane).setUpClass()

    def test_file(self):
        with self.source as s:
            for entry in s:
                self.assertMatchSnapshot(entry.name)
                self.assertMatchSnapshot(entry.password)

    def test_error(self):
        src_path = join(dirname(realpath(__file__)), "DashlaneError.json")
        src = DashlaneJsonReader(src_path)

        with self.assertRaises(KeyError):
            with src as s:
                for _ in s:
                    raise ValueError("Should never reach this")

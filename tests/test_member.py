import unittest
from task_package import member



class TestMemberMethods(unittest.TestCase):

    def test_get_channels(self):


        m=member.Member();
        m.add_channel("asd");
        self.assertEqual(m.get_channels(), ["asd"]);        
        m.add_channels(["asd1", "asd2"]);
        self.assertEqual(m.get_channels(), ["asd", "asd1", "asd2"]);

        m = member.Member()
        m.add_channel("asd")
        self.assertEqual(m.get_channels(), ["asd"])
        m.add_channels(["asd1", "asd2"])
        self.assertEqual(m.get_channels(), ["asd", "asd1", "asd2"])


    def test_get_region(self):
        m = member.Member()
        m.set_region("test")
        self.assertEqual(m.get_region(), "test")

    def test_get_date(self):
        m = member.Member()
        m.set_date("29.11.1233")
        self.assertEqual(m.get_date(), "29.11.1233")

    def test_get_time(self):

        m = member.Member();
        m.set_time("12:00", "13:00");
        self.assertEqual(m.get_start_time(), "12:00");
        self.assertEqual(m.get_end_time(), "13:00");
        self.assertRaises(Exception, m.set_time, "22:22", "11:11");

        m = member.Member()
        m.set_time("12:00", "13:00")
        self.assertEqual(m.get_start_time(), "12:00")
        self.assertEqual(m.get_end_time(), "13:00")
        self.assertRaises(Exception, m.set_time, "22:22", "11:11")


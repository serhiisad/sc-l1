import unittest
from task_package import request


class TestRequestMethods(unittest.TestCase):
    

    def test_set_get_methods(self):
        r = request.Request();
        r.set_date("12.12.1222");
        r.set_region("asd");
        r.set_time("12:00", "13:00");
        self.assertEqual(r.get_date(), "12.12.1222");
        self.assertEqual(r.get_region(), "asd");
        self.assertEqual(r.get_start_time(), "12:00");
        self.assertEqual(r.get_end_time(), "13:00");

    def test_clear_fields(self):
        r = request.Request();
        r.clear_fields();
        self.assertEqual(r.get_date(), "");
        self.assertEqual(r.get_region(), "");
        self.assertEqual(r.get_start_time(), "");
        self.assertEqual(r.get_end_time(), "");

    def test_exception(self):
        r = request.Request();
        self.assertRaises(Exception, r.set_time, "23:23", "22:22");
        
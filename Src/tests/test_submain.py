import unittest
from unittest.mock import patch
import freezegun
import datetime
from src.submain import SingleSession, Buffer


class TestSingleSession:
    @freezegun.freeze_time("2023-11-01 12:00:00")
    def test_should_create_single_session_with_four_parameters_and_right_timestamp(
        self,
    ):
        # given
        text_before_operation = "text before operation"
        text_after_operation = "text after operation"
        operation = "operation"
        expected_dict = {
            "text_before_operation": text_before_operation,
            "text_after_operation": text_after_operation,
            "operation": operation,
            "session_time_stamp": datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S"),
        }
        # when
        actual = SingleSession(
            text_before_operation=text_before_operation,
            text_after_operation=text_after_operation,
            operation=operation,
            session_time_stamp=datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S"),
        )
        # then
        assert actual.get_data_for_buffer() == expected_dict


class TestBuffer(unittest.TestCase):
    def setUp(self) -> None:
        self.buffer = Buffer()

    def test_add_to_buffer(self):
        session = SingleSession("before", "after", "operation")
        self.buffer.add_to_buffer(session)
        self.assertEqual(len(self.buffer.get_buffer_data()), 1)

    def test_clear_buffer(self):
        session = SingleSession("before", "after", "operation")
        self.buffer.add_to_buffer(session)
        self.buffer.clear_buffer()
        self.assertEqual(len(self.buffer.get_buffer_data()), 0)

    def test_get_buffer_data(self):
        session1 = SingleSession("before1", "after1", "operation1")
        session2 = SingleSession("before2", "after2", "operation2")

        self.buffer.add_to_buffer(session1)
        self.buffer.add_to_buffer(session2)

        expected_data = [session1.get_data_for_buffer(), session2.get_data_for_buffer()]
        self.assertEqual(self.buffer.get_buffer_data(), expected_data)

    @patch("builtins.print")
    def test_str_method(self, mock_print):
        session1 = SingleSession("before1", "after1", "operation1")
        session2 = SingleSession("before2", "after2", "operation2")

        self.buffer.add_to_buffer(session1)
        self.buffer.add_to_buffer(session2)

        expected_output = (
            "text_before_operation: before1\n"
            "text_after_operation: after1\n"
            "operation: operation1\n"
            f"session_time_stamp: {session1.session_time_stamp}\n\n"
            "text_before_operation: before2\n"
            "text_after_operation: after2\n"
            "operation: operation2\n"
            f"session_time_stamp: {session2.session_time_stamp}\n\n"
        )
        print(self.buffer.__str__())
        mock_print.assert_called_with(expected_output)

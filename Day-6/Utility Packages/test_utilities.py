
import unittest
import tempfile
import io
import time
from pathlib import Path
from contextlib import redirect_stdout

from context_manager import MyContext
from generator import file_generator
from retry_decorator import retry
from timing_decorator import timer


class TestMyContext(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.filename = str(Path(self.temp_dir.name) / "test.txt")

    def test_opens_file_and_writes_content(self):
        with MyContext(self.filename, "w") as file:
            file.write("Hello, world!")

        with open(self.filename, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "Hello, world!")

    def test_file_is_closed_after_context(self):
        with MyContext(self.filename, "w") as file:
            file.write("Test")

        self.assertTrue(file.closed)

    def test_file_closes_when_exception_occurs(self):
        with self.assertRaises(ValueError):
            with MyContext(self.filename, "w") as file:
                raise ValueError("Test error")

        self.assertTrue(file.closed)

    def test_reading_missing_file_raises_error(self):
        missing_file = str(Path(self.temp_dir.name) / "missing.txt")

        with self.assertRaises(FileNotFoundError):
            with MyContext(missing_file, "r"):
                pass


class TestFileGenerator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.filename = str(Path(self.temp_dir.name) / "lines.txt")

    def test_yields_all_lines(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write("First\nSecond\nThird\n")

        result = list(file_generator(self.filename))

        self.assertEqual(result, ["First\n", "Second\n", "Third\n"])

    def test_empty_file_returns_no_lines(self):
        Path(self.filename).write_text("", encoding="utf-8")

        self.assertEqual(list(file_generator(self.filename)), [])

    def test_missing_file_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            list(file_generator(self.filename))

    def test_yields_one_line_at_a_time(self):
        Path(self.filename).write_text("One\nTwo\n", encoding="utf-8")

        generator = file_generator(self.filename)

        self.assertEqual(next(generator), "One\n")
        self.assertEqual(next(generator), "Two\n")

        with self.assertRaises(StopIteration):
            next(generator)


class TestRetry(unittest.TestCase):
    def test_returns_result_on_first_attempt(self):
        @retry(attempts=3)
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_retries_until_function_succeeds(self):
        calls = 0

        @retry(attempts=3)
        def flaky_function():
            nonlocal calls
            calls += 1

            if calls < 3:
                raise ValueError("Temporary error")

            return "Success"

        self.assertEqual(flaky_function(), "Success")
        self.assertEqual(calls, 3)

    def test_raises_error_after_all_attempts_fail(self):
        calls = 0

        @retry(attempts=3)
        def failing_function():
            nonlocal calls
            calls += 1
            raise ValueError("Always fails")

        with self.assertRaisesRegex(ValueError, "Always fails"):
            failing_function()

        self.assertEqual(calls, 3)

    def test_attempts_one_calls_function_once(self):
        calls = 0

        @retry(attempts=1)
        def failing_function():
            nonlocal calls
            calls += 1
            raise ValueError("Failed")

        with self.assertRaises(ValueError):
            failing_function()

        self.assertEqual(calls, 1)

    def test_zero_attempts_does_not_call_function(self):
        calls = 0

        @retry(attempts=0)
        def my_function():
            nonlocal calls
            calls += 1
            return "Done"

        self.assertIsNone(my_function())
        self.assertEqual(calls, 0)


class TestTimer(unittest.TestCase):
    def test_returns_function_result(self):
        @timer()
        def my_function():
            return 42

        output = io.StringIO()

        with redirect_stdout(output):
            result = my_function()

        self.assertEqual(result, 42)
        self.assertIn("Execution Time:", output.getvalue())

    def test_passes_arguments_correctly(self):
        @timer()
        def multiply(a, b):
            return a * b

        with redirect_stdout(io.StringIO()):
            result = multiply(4, 5)

        self.assertEqual(result, 20)

    def test_prints_elapsed_time(self):
        @timer()
        def slow_function():
            time.sleep(0.02)
            return "Done"

        output = io.StringIO()

        with redirect_stdout(output):
            slow_function()

        self.assertIn("Execution Time:", output.getvalue())
        self.assertIn("sec", output.getvalue())

    def test_function_exception_propagates(self):
        @timer()
        def failing_function():
            raise ValueError("Timer test error")

        with redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, "Timer test error"):
                failing_function()


if __name__ == "__main__":
    unittest.main()

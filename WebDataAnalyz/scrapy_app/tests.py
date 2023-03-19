from django.test import TestCase

from .tasks import run_example_spider

class ExampleFunctionTests(TestCase):
    def test_example_function(self):
        input_value = 5
        expected_value = 25
        result = run_example_spider(input_value)
        self.assertEqual(result, expected_value)
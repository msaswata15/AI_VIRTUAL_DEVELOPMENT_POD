import unittest
from interfaces.streamlit_app import main

class TestStreamlitUI(unittest.TestCase):
    def test_streamlit_app_runs(self):
        """
        Basic test to ensure that the Streamlit main function executes without errors.
        Note: This test does not simulate full Streamlit interactivity.
        """
        try:
            main()
        except Exception as e:
            self.fail(f"Streamlit app main() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()

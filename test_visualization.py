import unittest
from autoxplainai.visualization import plot_feature_importance

class TestVisualization(unittest.TestCase):
    def test_plot_feature_importance(self):
        # Mock test to ensure plot_feature_importance does not raise exceptions
        try:
            plot_feature_importance([0.1, 0.2, 0.3], ['Feature1', 'Feature2', 'Feature3'])
        except Exception as e:
            self.fail(f"plot_feature_importance raised an exception: {e}")
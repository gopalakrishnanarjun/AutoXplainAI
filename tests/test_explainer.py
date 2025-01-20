import unittest
from autoxplainai.explainer import Explainer

class TestExplainer(unittest.TestCase):
    def test_explainer_initialization(self):
        model = object()  # Mock model
        explainer = Explainer(model)
        self.assertEqual(explainer.model, model)
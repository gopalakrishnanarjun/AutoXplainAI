# AutoXplainAI

AutoXplainAI is an Automatic Model Explanation Framework that simplifies the process of interpreting machine learning models. It provides tools for generating explanations and visualizing them in an intuitive way.

## Features
- Automatic generation of model explanations
- Visualization of feature importances
- Support for multiple explanation methods

## Installation
```
pip install autoxplainai
```

## Usage
```python
from autoxplainai.explainer import Explainer
explainer = Explainer(model)
explanations = explainer.explain(X_test)
```

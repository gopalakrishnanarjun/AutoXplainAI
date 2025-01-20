import matplotlib.pyplot as plt

def plot_feature_importance(importances, feature_names):
    plt.barh(feature_names, importances)
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.show()
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    wine_data = os.path.join(root, 'data', 'wine.data')
    wine = pd.read_csv(wine_data,
                       names=["Cultivator", "Alchol", "Malic_Acid", "Ash",
                              "Alcalinity_of_Ash", "Magnesium",
                              "Total_phenols", "Falvanoids",
                              "Nonflavanoid_phenols", "Proanthocyanins",
                              "Color_intensity", "Hue", "OD280", "Proline"])

    # Set up data
    X = wine.drop('Cultivator', axis=1)
    y = wine['Cultivator']

    pass

if __name__ == "__main__":
    main()


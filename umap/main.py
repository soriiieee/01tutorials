import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from umap import UMAP


def main() -> None:
    # Load the digits dataset
    digits = load_digits()
    data = digits.data
    labels = digits.target

    print(data.shape)
    print(data)

    return None



if __name__ == "__main__":
    main()


    # # Initialize UMAP with desired parameters
    # umap_model = UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)

    # # Fit and transform the data to 2D
    # embedding = umap_model.fit_transform(data)

    # # Plot the results
    # plt.figure(figsize=(10, 8))
    # scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='Spectral', s=5)
    # plt.colorbar(scatter, label='Digit Label')
    # plt.title('UMAP projection of the Digits dataset')
    # plt.xlabel('UMAP 1')
    # plt.ylabel('UMAP 2')
    # plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Noise Level / dB': [61.5, 64.9, 65.9, 59.7, 69.8, 69.7, 63.9, 65.9, 64.7, 62.3, 54.8, 54.7],
    'Distance from the CBD / m': [445.38, 176.67, 0, 342.14, 835.71, 99.89, 399.27, 205.07, 514.47, 895.84, 1278.35, 1600],
}

df = pd.DataFrame(data)
corr_matrix = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Noise Level (dB) vs. Distance from the CBD (m)")
plt.show()
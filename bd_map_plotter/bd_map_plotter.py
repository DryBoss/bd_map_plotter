# Dependency import
try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
except ImportError as e:
    print("Missing dependencies! Please install them using:\n  pip install geopandas matplotlib")
    raise e

bangladesh = gpd.read_file("https://raw.githubusercontent.com/DryBoss/map-visualization/main/datas/whole_bangladesh_outline.json")

fig,ax = plt.subplots(figsize=(5,5))
ax = bangladesh.plot(ax=ax, edgecolor='red', color='blue', linewidth=2)
ax.set_title('Bangladesh')
plt.show()
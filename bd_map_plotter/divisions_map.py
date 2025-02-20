import os

try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Missing dependencies! Install with:\n  pip install geopandas matplotlib")
    raise e

class DivisionsMap:
    def __init__(self):
        """Initialize and load map data from a local file."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "data", "divisions_map.json")

        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Map data file not found: {json_path}")

        self.data = gpd.read_file(json_path)

    def plot(self, figureSize=(5,5),title="Divisions of Bangladesh", edgeColor="black", fillColor="lightcyan", lineWidth=2):
        fig, ax = plt.subplots(figsize=figureSize)
        self.data.plot(ax=ax, edgecolor=edgeColor, color=fillColor, linewidth=lineWidth)
        ax.set_title(title)
        plt.show()

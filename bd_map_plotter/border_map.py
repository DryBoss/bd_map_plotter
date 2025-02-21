import os

try:
    import numpy as np
    import geopandas as gpd
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Missing dependencies! Install with:\n  pip install geopandas matplotlib")
    raise e

class BorderMap:
    def __init__(self):
        """Initialize and load map data from a local file."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "data", "border_map.json")

        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Map data file not found: {json_path}")

        self.data = gpd.read_file(json_path)

    def draw(self, figureSize=(5,5), title="Bangladesh", edgeColor="black", fillColor="lightcyan", lineWidth=2):
        fig, ax = plt.subplots(figsize=figureSize)
        self.ax = ax 
        self.data.plot(ax=ax, edgecolor=edgeColor, color=fillColor, linewidth=lineWidth)
        ax.set_title(title)
        plt.draw()

    def markPoint(self, latitudeLongitude, label=False, color="red", size=10, marker="o"):
        if isinstance(latitudeLongitude[0], (float, int)):
                latitudeLongitude = [latitudeLongitude]
        
        for latlon in latitudeLongitude:
            # Handle cases where latlon might be a tuple/list or just a single pair
            if isinstance(latlon, (list, tuple)) and len(latlon) == 2:
                lat, lon = latlon
                self.ax.scatter(lon, lat, color=color, s=size, label=label if label else f"({lat}, {lon})")
            else:
                raise ValueError("Each item in latitudeLongitude should be a (lat, lon) pair.")
        
        self.ax.legend()
        plt.draw()



    def show(self):
        plt.show()

# Run the code
if __name__ == "__main__":
    border_map = BorderMap()
    border_map.draw()
    border_map.markPoint((22.342218, 91.836653))
    border_map.show()
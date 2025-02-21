import os

try:
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
        self.data.plot(ax=ax, edgecolor=edgeColor, color=fillColor, linewidth=lineWidth)
        ax.set_title(title)
        plt.draw()  # You could use plt.show() here, but plt.draw() updates the plot if necessary.

    def show(self):  # Added self parameter
        plt.show()  # Use plt.show() to display the plot

# Run the code
if __name__ == "__main__":
    border_map = BorderMap()
    border_map.draw()
    border_map.show()
    border_map.draw(fillColor='red')
    border_map.show()
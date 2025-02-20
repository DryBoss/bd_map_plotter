from setuptools import setup, find_packages

setup(
    name="bd_map_plotter",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "geopandas",
        "matplotlib"
    ],
    description="A simple Bangladesh map plotting library.",
    author="DryBoss",
    license="MIT",
    package_data={
        "bd_map_plotter": ["data/*.json"],  # Ensures JSON files are included
    },
)

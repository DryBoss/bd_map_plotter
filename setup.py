from setuptools import setup, find_packages

setup(
    name="bd_map_plotter",
    version="0.2",
    description="A package to plot Bangladesh map",
    author="DryBoss",
    url="https://github.com/DryBoss/bd_map_plotter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "geopandas",
        "matplotlib",
    ],
)

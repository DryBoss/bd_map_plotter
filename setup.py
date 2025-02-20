from setuptools import setup, find_packages

setup(
    name="bd_map_plotter",
    version="0.1",
    description="A package to plot Bangladesh map",
    author="DryBoss",
    author_email="your-email@example.com",  # Your email address
    url="https://github.com/DryBoss/bd_map_plotter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "geopandas",
        "matplotlib",
    ],
    classifiers=[            # Optional, helps users discover your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

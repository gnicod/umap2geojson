import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "umap2geojson",
    version = "0.0.1",
    author = "Gaétan NICOD",
    author_email = "",
    description = ("Export a umap url to geojson"),
    license = "BSD",
    keywords = "umap geojson",
    url = "https://github.com/gnicod/umap2geojson",
    packages=['umap2geojson'],
    long_description=read('README')
)

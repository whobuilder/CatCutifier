# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "CatCutifier"
copyright = "2021, whobuilder"
author = "whobuilder"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ "breathe", "exhale" ]

# Configuration for the breathe extension
# Which directory to read the Doxygen output from
breathe_projects = {"CatCutifier":"xml"}
breathe_default_project = "CatCutifier"

# Configuration for the exhale extensions
exhale_args = {
    "containmentFolder": "./api",
    "doxygenStripFromPath": "../src",
    "rootFileName": "library_root.rst",
    "rootFileTitle": "Library API",
}

# Configuration for the theme
html_theme = "sphinx_book_theme"
html_theme_options = {
    "use_repository_button": False}


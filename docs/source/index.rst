Welcome to pyTSPA's documentation!
============================

A Toolbox for Analyzing and Visualizing Team Sports Performance, with a particular focus on Football Match Data.
The toolbox includes modules for data processing, statistical analysis, match outcome prediction, and result visualization.

Current version: 0.1.0

Planned release: May 2025

Introduction
------------
pyTSPA was developed to support coaches, analysts, and sports scientists in extracting actionable insights from football match data. Designed with a football-centric approach, the toolbox facilitates data handling, statistical analysis, match outcome prediction using machine learning, and comprehensive data visualization.

Description
-----------
The toolbox is divided into the following modules:

- **Data Handling:** Data input/output, cleaning, and profiling (CSV, Excel).
- **Metrics:** Calculation of match and team statistics (Win Percentage, Pythagorean Expectation) and predictive models using logistic regression.
- **Visualization:** Graphical representation of match data, statistical summaries, and prediction results using bar charts, scatter plots, and pie charts.

Datasets
--------
The datasets used for testing and demonstration purposes are primarily sourced from public football datasets.  
For a comprehensive collection of football datasets, visit:  
https://www.football-data.co.uk/data.php

Installation
------------
pip project: https://pypi.org/project/pyTSPA-toolbox/

git repository: https://github.com/vargaheni05/pyTSPA-toolbox

For comprehensive installation instructions and usage guidelines, please refer to the documentation:  
https://pytspa-toolbox.readthedocs.io/en/latest/usage.html

Requirements
------------

Python Requirements:
~~~~~~~~~~~~~~~~~~~~

Python >= 3.10

pandas >= 2.2.2

numpy >= 1.26.4

matplotlib >= 3.9.2

seaborn >= 0.13.2

scikit-learn >= 1.5.2

All the python requirements are installed when the toolbox is installed, so there is no need for any additional commands.

Documentation
--------------

https://pytspa-toolbox.readthedocs.io/en/latest/

.. toctree::
   usage
   io
   data
   metrics
   visualization
   :maxdepth: 2
   :caption: Contents:

.. toctree::
   :caption: Tutorials:
   :maxdepth: 1

Correspondence
--------------
Henrietta Varga PPCU-ITK, Budapest, Hungary

varga.henrietta.julianna@hallgato.ppke.hu

Marcell Szögi PPCU-ITK, Budapest, Hungary

szogi.marcell@hallgato.ppke.hu

Benedek Kardos PPCU-ITK, Budapest, Hungary

kardos.benedek.zoltan@hallgato.ppke.hu

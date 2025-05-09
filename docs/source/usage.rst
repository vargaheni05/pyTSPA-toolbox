Usage
=====
Installation
------------

**From PyPi**

Install `pyTSPA` using pip:

.. code-block:: bash

    pip install pyTSPA-toolbox

**From source**

Clone the git repository:

.. code-block:: bash

    git clone https://github.com/vargaheni05/pyTSPA-toolbox.git

Change directory to the cloned repository:

.. code-block:: bash

    cd pyTSPA-toolbox

Install with pip:

.. code-block:: bash

    pip install .

For validating the installation, check the version of the toolbox:

.. code-block:: python3

    >>> import pyTSPA
    >>> print(pyTSPA.__version__)
    '0.1.1'

Example
-------
The following code will load the specified match data file and display a basic profiling summary of the data.

.. code-block:: python3

    >>> import pyTSPA
    >>> df = pyTSPA.load_match_data("example.csv")
    >>> print(pyTSPA.data_profiling(df))

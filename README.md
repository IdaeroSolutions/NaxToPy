[![Idaero](https://img.shields.io/badge/powered%20by-Idaero%20Solutions-299797)](https://idaerosolutions.com)
[![PyPi](https://img.shields.io/pypi/v/NaxToPy?color=ffd500)](https://pypi.org/project/NaxToPy/)
[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-00699d)](https://www.python.org/downloads/)
![License](https://img.shields.io/badge/license-proprietary-red)
[![MicrosoftStore](https://img.shields.io/badge/Microsoft%20Store-NaxTo-blue?logo=microsoftstore&logoColor=blue&labelColor=lightgrey)](https://apps.microsoft.com/detail/XP9MMH0KDKGRJN?hl=en-US&gl=US)
[![PyPi - Downloads](https://img.shields.io/pypi/dm/NaxToPy?color=dgreen)](https://pypi.org/project/NaxToPy/#files)

![](https://idaerosolutions.com/images/icons/Logo_NaxToPy_Black.svg "NaxToPy")

# NaxToPy

**NaxToPy** is the [**NaxTo**](https://apps.microsoft.com/detail/XP9MMH0KDKGRJN?hl=en-US&gl=US)
library designed for Python, which allows reading and manipulating FEM
analysis results files from the most common tools: Nastran (.op2, .xdb, .h5), Abaqus (odb), Optistruct
(.h3d, .op2) and Ansys (.rst); and stores them in a user-friendly Python structure. Additionally, it
can read input files from Nastran (.bdf, .fem) and change their contents.

It could be easily combined with other Python packages as Matplotlib or Pandas. This provides access
to the full coding power of Python to interpret and process the results, without the need to install
any additional software other than having NaxTo already installed (see the _Download_ and _Homepage_
links on the left).

**NaxToPy** is a powerful tool for FEM analysis post-processing!

**CAUTION:** To use NaxToPy, [**NaxTo**](https://apps.microsoft.com/detail/XP9MMH0KDKGRJN?hl=en-US&gl=US) must be installed.
This version is compatible with **NaxTo 2024.2**. It is compatible with all the steps of this version (2024.2.0, 2024.2.1, 2024.2.2, etc.).
Check in _Programs and Features_ the NaxTo version that is installed. 

## Installation

If python is installed and `pip` is added to the PATH:

`pip install NaxToPy`

An alternative, if Python is callable from the command line:

`python -m pip install NaxToPy`

For **Visual Studio** users:
- Open "Python Environments" window
- Change the "general information" label to "Packages(Pypi)"
- Write the name of the package and press enter:

- `NaxToPy` + enter

For **Spyder** users:
- If pip is installed: `!pip install NaxToPy`
- If pip is not installed, download and run `get-pip.py` located in  https://bootstrap.pypa.io/get-pip.py . Then, run the
`!pip ...` command
- If no method worked, download the sorce ditribution of the package *NaxToPy* from Test PyPi and the source
distribution of the packages from PyPi *pythonnet*, *clr-loader*, *cffi*, *pycparser*. Copy and paste the five folder in the 
same directory. When ever you want to use the NaxToPy package add the following lines to your script:

      import sys
      sys.path.append("...\directory")
      import NaxToPy as n2p
## Updating NaxToPy

If python is callable from the command line:

`python -m pip install -U NaxToPy`

For Visual Studio users:
- Open "Python Environments" window
- Change the "general information" label to "Packages(Pypi)"
- Write the following command on the search bar and press enter:

  `-U NaxToPy` + enter


## Version updates:

To see previous version see the pre-release versions in https://test.pypi.org/project/NaxToPy/

### v.1.0.1
1. Bug Fix: A new dependece is added to support python 3.12
2. Bug Fix: N2PLog.set_directory now works correctly
3. New download page for NaxTo and NaxToPy

### v.1.1.0
1. Bug Fix: PSOLID with material coordinate = -1 is now suppported
2. Now, it is possible to modify the BDF data from Nastran and rewrite the files.

### v.1.1.1
1. New property for the class N2PLoadCase: Solver
2. New fille that allows the user to call the N2P classes. Useful for typing
3. N2PCoord don't have the property PartID any more, as it is considered that Coordinates systems don't have parts/superelements 
4. Method for the connectivity property of N2PNode have been optimized

### v.1.2.0
1. Bug Fix: Property IsTransformable of the N2PComponent class is now right.
2. Bug Fix: When calling the methods .get_nodes(), get_elements(), etc from a Nastran Input File, the user don't have to specify the part.

### v.1.2.1
1. New method to create N2PLoadCase as envelope load case of the selected load cases.
2. The name for derivated load cases is now checked to avoid a repeated name 

### v.1.3.0
1. New class N2PReport. This class allow to create tables of data with the components, incremenets, load cases, etc to generate big reports.
2. Improvement in typing
3. Small changes in the core of the package related to libraries finding and loading.

### v.1.4.0
1. Bug correction for N2PReport. Now it sorts correctly by "LC" or "IDS"
2. N2PLoadCase has a new property: PathFile.

### v.1.5.0
1. A bug is fixed that prevented requesting results on global axes.
2. The typing of some functions is improved.

### v.1.5.1
1. Bug Fix. If the name for a derivated load case is repeated for a second time, the name is changed. 
2. Bug Fix. Now is possible to change the criteria for a new envelope load case.

### v.1.5.2
1. Bug fix: A bug has been resolved that previously prevented the generation of a .log file while executing the N2PtoEXE module.
2. Bug fix: An internal error related to finding the libraries has been resolved.
3. The option to include a splash image in an executable has been added.

### v.1.5.3
1. Bug fix for the EXE generation.
2. Updates in the log messages.

### v.1.5.4
1. Bug Fix: After calling the method get_load_cases(), the new derived cases weren't found. Now they does.
2. N2PLoadCase has now two properties for the ID: OriginalID, that was in the files readed and ID that is the one that is used in NaxToPy. Usually, they are the same.
3. New method new_derived_component() in the class N2PResult that allows to create new N2PComponent based on the original components.
4. New module N2PUpdateFastener. This module updates the stiffness of the CBUSH and CFAST acordint to their properties and shells properties.

### v.1.5.5
1. Bug Fix: Now is possible to call the module N2PUpdateFastener

### v.1.5.6
1. The method new_envelope_loadcase() now has the option to choose the envelope group. Which means the user can ask for
the LoadCases that are critical or the Increment that is critical instead of the value.

### v.2.0.0
1. Changes made to align the library with updates in lower-level dependencies.
2. New internal methods to look for the compatibility with low-level dependencies.
3. The name of the .log is now NaxToPy_Year-Month-Day.log.

### v.2.0.1
1. The compatibility is extended to all NaxTo steps of the same version.
2. The property N2PLoadCase.ActiveIncrement is subtitued by N2PLoadCase.ActiveN2PIncrement.
It uses an object instaed of an int.
3. Update of the examples of some docstrings.

### v.2.1.0
1. Reading a Natran Input File: SPC and SCP1 are now supported.
2. Bug fix. The order in the components in new_report() does not affect now.
3. Formula check in new_derived_loadcase(), new_enevelope_loadcase() and new_derived_component().
4. New optional arguments if n2ptoexe() to add extra libaries, packages or files.

# Documentation

**NaxToPy** is a package developed by Idaero Solutions© as a part of the **NaxTo** software.

NaxToPy only use three dependeces:
- NumPy: https://numpy.org/
- PythonNET: https://pythonnet.github.io/
- Setuptools: https://setuptools.pypa.io/en/latest/index.html

## Supported Files

### Result files:
- **Nastran:** .op2, .h5, .xdb
- **Optistruct:** .op2, .h3d
- **Abaqus:** .odb
- **Ansys:** .rst, .rth(beta)

### Input files:
- **Nastran** (bdf)

## Initialize your model

Load your model:

```python
# results_fem.py
import NaxToPy as N2P

path = "results_fem.op2"

model = N2P.load_model(path)
```

## Load mesh items

```python
# results_fem.py

# Load a list with all the nodes (as N2PNode object) of the model
nodes = model.get_nodes()

# Load the nodes in the list [1, 2, 3] (as a list of N2PNode objects)
nodelist = model.get_nodes([1, 2, 3]) 

# Load the node with the id 1000 (as a N2PNode object)
node1000 = model.get_nodes(1000)

# Load a list with all the elements (as N2PElement object) of the model
element = model.get_elements()

# Load the elements in the list [10, 20, 30] (as a list of N2PElement objects)
elementlist = model.get_nodes([10, 20, 30])

# Load the connectors as N2PConnector:
connectorslist = model.get_connectors()

# Load the coordinate systems of the model:
coordslist = model.get_coords()
```
## Add your own messages to the .log

```python
# results_fem.py

N2P.N2PLog.Info.user("INFO-1000: Running results_fem.py")
```

## Look for LoadCases, Results and Components

```python
# results_fem.py

# Load the list of load cases as N2PLoadCase object
loadcaseslist = model.LoadCases

# Look for the Load Case with the name pressure
pressure_lc = model.get_load_case("pressure")

# Change the active increment (by default is the last one):
pressure_lc.ActiveN2PIncrement = pressure_lc.get_increment(10)

# Look for all results
all_results = pressure_lc.Results

# Look for the Result with the name DISPLACEMENT
displacement = pressure_lc.get_result("DISPLACEMENT")

# Load all the components of the result
all_components = displacement.Components

# Look for the component X:
x_coord = displacement.get_component("X")
```

## Load the result data as a list

```python
# results_fem.py

# Obtain the result array as a list for a component
x_list = x_coord.get_result_list()[0]
```

## Load the result data as a NumPy array

```python
# results_fem.py

# Call the get_result_ndarray method of a N2PComponent to obtain a numpy array
# with the results of the component.
x_df = x_coord.get_result_ndarray()
```

## Create an executable file of your code
Using a different script:
```python
# extra_script.py

import NaxToPy as N2P
path1 = "results_fem.py"
path2 = "results_fem_abaqus.py"

N2P.n2ptoexe(path1, console=True, solver="NASTRAN")
N2P.n2ptoexe(path2, console=True, solver="ABAQUS", abaqusversion=["2021", "2022"])
```

## Create your own functions to work with other python packages:
Private function that generates the proper index for a data frame using the elemnts or nodes ids:
```python
# results_fem.py

import pandas as pd

def _index_dataframe(model: "N2PModelContent", component: "N2PComponent", sections, aveSections, cornerData, aveNodes,
                     variation, realPolar, coordsys, v1, v2) -> pd.Index:
    """ Function that returns the proper index for each component asked
    """
    # It is look if there is one part or several's:
    parts = len(model.Parts) - (model.Solver == "Abaqus")

    # Then the result array and where there results are placed is obtained
    on_items = component.get_result_ndarray(sections, aveSections, cornerData, aveNodes,
                                            variation, realPolar, coordsys, v1, v2)[1]

    # The ids and the index are selected. It takes into account where the results are and the number of parts
    if on_items == "NODES":
        nodes = model.get_nodes()
        ids = [(nodo.PartID, nodo.ID) if parts > 1 else nodo.ID for nodo in nodes]
        indexname = ["Part", "Grid"] if parts > 1 else ["Grid"]

    elif on_items == "ELEMENTS":
        elements = model.get_elements()
        connectors = model.get_connectors()
        ids = [(element.PartID, element.ID) if parts > 1 else element.ID for element in elements] + \
              [(co.PartID, co.ID) if parts > 1 else co.ID for con in connectors for co in (con if isinstance(con, list) else [con])]
        indexname = ["Part", "Element"] if parts > 1 else ["Element"]

    elif on_items == "ELEMENT NODAL":
        ids = model.elementnodal().values()
        indexname = ["Part", "Grid", "Element"]

    else:
        return None

    # If there are several parts, or it is corner data, MultiIndex is used:
    if isinstance(ids[0], tuple):
        index = pd.MultiIndex.from_tuples(ids, names=indexname)
    else:
        index = ids

    return index
```
Function that generates a DataFrame with the results of a component
```python
# results_fem.py

def dataframe_result(model: "N2PModelContent", component: "N2PComponent",sections=None, aveSections=-1, cornerData=False,
                     aveNodes=-1, variation=100, realPolar=0, coordsys: int = -1000,
                     v1: tuple = (1,0,0), v2: tuple = (0,1,0)) -> pd.DataFrame:
    """Function that returns as a dataframe of pandas the result array of a component
    """

    # DataFrame generation
    return pd.DataFrame(data={component.Name:
                              component.get_result_ndarray(sections, aveSections, cornerData, aveNodes, variation,
                                                           realPolar, coordsys, v1, v2)[0]},
                        index=_index_dataframe(model, component, sections, aveSections, cornerData, aveNodes, variation,
                                               realPolar, coordsys, v1, v2),
                        columns=[component.Name])
```
Function that generates a DataFrame for all the components of a result
```python
# results_fem.py

def dataframe_results(model: "N2PModelContent", result: "N2PResult", sections=None, aveSections=-1, cornerData=False,
                     aveNodes=-1, variation=100, realPolar=0, coordsys: int = -1000,
                     v1: tuple = (1,0,0), v2: tuple = (0,1,0)) -> pd.DataFrame:
    """Function that generates a DataFrame of pandas with all the components of a result. It uses dataframe_result.
    It uses sequential computing.
    """
    return pd.DataFrame(data={component.Name:
                                  component.get_result_ndarray(sections, aveSections, cornerData, aveNodes, variation,
                                                               realPolar, coordsys, v1, v2)[0]
                                                               for component in result.Components.values()},
                        index=_index_dataframe(model, next(iter(result.Components.values())), sections, aveSections,
                                               cornerData, aveNodes, variation, realPolar, coordsys, v1, v2),
                        columns=[component.Name for component in result.Components.values()])
```

##
For more documentation visit https://idaerosolutions.com/Home/NaxToPy

Reference Guide at: https://www.idaerosolutions.com/NaxToPyDoc/NaxToPy.html


# License

Copyright is owned by Idaero Solutions©

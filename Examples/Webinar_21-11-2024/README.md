# <strong>Post-processing Finite Element Analysis in Python: Use Case.</strong>

In this session, we will explore a simple use case to demonstrate the advantages of using Python for post-processing finite element analysis (FEA) results. We will see how easy and efficient it is to extract the mesh structure, access results, manipulate data, combine load cases, generate a CSV file for plotting, and visualize the post-processed results.

**Table of Contents:**
1. [Why Python](#1-why-python-)
2. [Tools Introduction](#2-tools-introduction-)
3. [Working with the Mesh](#3-working-with-the-mesh-️)
4. [The Results](#4-the-results-)
5. [Writing the Results](#5-writing-the-results)

## 1. Why-Python 🐍

Python is a user-friendly programming language with a gentle learning curve. This means that anyone, with minimal effort, can learn the basics and automate tasks with just a few lines of code. The Python community is extensive, and there is a wealth of information available on the internet. Additionally, tools like ChatGPT can assist in generating high-quality Python code with clear instructions.

For engineers, Python is an invaluable tool that helps improve productivity and eliminates repetitive, tedious tasks.

Compared to batch files, CMD scripts, or PowerShell (PS1) scripts, Python is easier to use for automating tasks within the operating system. For data analysis, Python is significantly more powerful and intuitive than Excel and VBA macros.

## 2. Tools Introduction 🔧

We are using VS Code to work with Jupyter Notebooks. As you will see, Notebooks are useful for explain code as it allow to run Python code in a cool format document. The python version is the 3.11.7 as you can see in the top right corner. As external package we are using [NaxToPy](<https://pypi.org/project/NaxToPy/>), a package that will allow as to open and load imput mesh files (.inp, .bdf, .fem) and binary result files (.op2, .odb, .h3d, .xdb, .rst). The commands and almost all the code is the same for every solver supported (Nastran, Abaqus, Optistruct and Ansys). For using this package it is necessary to have [NaxTo](<https://www.idaerosolutions.com/Home/NaxTo>) instaled. NaxTo is a trusted post-processing suite, validated by Tier 1 aeronautical companies and in use since 2017. It offers seamless integration with Excel, Python, Word, and its dedicated visualizer, NaxToView.

There are other Python packages for post-processing FEA results files, but they are not as easy or straightforward to use as NaxToPy, as we will see. Once installed, using NaxToPy is as simple as importing it:

```python
import NaxToPy as n2p
n2p.__version__
```

## 3. Working with the Mesh ✈️

In order to work with the mesh is as easy as use the coman `load_model()` and the path to the mesh. A python object is created with all the information of the model. Modern IDEs and editors (PyCharm, VSCode, Spyder, etc) allow us to debug the variables and see what there is inside the objects.

```python
path = r"C:\Webinar\model\SUBCASE_17500.dat"
model = n2p.load_model(path)
```

Objects in Python have methods that allow us to query information. These methods are suggested by modern IDEs and editors, and their details can be accessed simply by hovering the cursor over the method.

```python
element = model.get_elements(39800000)
element
element.Nodes
```

The simple and powerful syntax of Python allows us to write efficient code, sometimes in just a single line.

```python
cquads = [cuad for cuad in model.get_elements() if cuad.TypeElement == "CQUAD4"]
element_types = {ele.TypeElement for ele in cquads}
element_types
```

## 4. The Results 📊

Loading results into the mesh is straightforward. It only requires a single function.

```python
print(model.LoadCases)

model.import_results_from_files([
    r"C:\Webinar\model\subcase_17500.op2",
    r"C:\Webinar\model\subcase_17501.op2",
    r"C:\Webinar\model\subcase_17502.op2",
    r"C:\Webinar\model\subcase_17503.op2",
    r"C:\Webinar\model\subcase_17504.op2"]
)

print(model.LoadCases)
```

Imagine that the first load case is thermal, and the others are mechanical load cases. These can be combined using a formula defined as a string.

```python
for lc in model.LoadCases[1:]:
    formula = f"1.5*<LC{lc.ID}:FR1>+<LC17500:FR1>"
    model.new_derived_loadcase(f"{lc.ID}+17500", formula)
print(model.LoadCases)
```

Next, the envelope load case is generated.

```python
formula_env = ",".join([f"<LC{lc.ID}:FR0>" for lc in model.LoadCases if lc.TypeLC == "DERIVED"])
print(formula_env)
env_ct = model.new_envelope_loadcase("envelope contour", formula=formula_env, criteria="ExtremeMax", envelgroup="ByContour")
env_lc = model.new_envelope_loadcase("envelope loadcase", formula=formula_env, criteria="ExtremeMax", envelgroup="ByLoadCaseID")
print(model.LoadCases)
```

At this point, the results have not been extracted yet. This can be done using several methods:

### 4.1 Simple Results Extraction 📉

```python
fx = env_ct.get_result("FORCES").get_component("FX").get_result_ndarray()[0][:len(model.get_elements())]
fx

fx_lc = env_lc.get_result("FORCES").get_component("FX").get_result_ndarray()[0][:len(model.get_elements())]
```

### 4.2 Parallel Results Extraction 📈

```python
fx_parallel = model.get_result_by_LCs_Incr([(env_ct, env_ct.ActiveN2PIncrement)], "FORCES", "FX")[(-5, 0)][:len(model.get_elements())]
fx_parallel
```

### 4.3 Working with the Results 🔨

```python
cquads_internal_ids = [cquad.InternalID for cquad in cquads]
cquads_internal_ids

fx_cquads = fx[cquads_internal_ids]
fx_lc_cquads = fx_lc[cquads_internal_ids]


max_fx = fx_cquads.argmax()
max_fx

fx_cquads[max_fx]
```

## 5. Writing the Processed Results 📝

The results can be printed in the format specified by the user. In this case, we will use the format required by the NaxTo visualizer, NaxToView. At the end, we will see how to achieve this. The output format is a CSV file with two mandatory columns: "ID_E" and "PARTS_E". Therefore, we need to prepare the CQUAD4 IDs, the CQUAD4 Part IDs, and two result columns: the FX envelope and the load case where the maximum value was found.

```python
import csv

id_e = [cquad.ID for cquad in cquads]
part_e = [cquad.PartID for cquad in cquads]

with open(".\\fx_cquad_envelope.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID_E", "PARTS_E", "FX", "LoadCase"])  # Write header
    writer.writerows(zip(id_e, part_e, fx_cquads, fx_lc_cquads))  # Write data rows
```

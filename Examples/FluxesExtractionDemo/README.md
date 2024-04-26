# FluxesExtractionDemo

Script for an application demonstration using the NaxToPy package and Tkinter.

This script provides an easy-to-use graphical user interface (GUI) built with Tkinter.

NaxToPy is used to extract fluxes from multiple .op2 files, generate envelopes and derived cases, and print the fluxes (FX, FY, FXY) in both the analysis system and the material system to a CSV file.

## Instructions

1. Select Model: The model can be either a Nastran Input File (.bdf) or a binary file (.op2).

2. Select Results: You can select one or several results files.

3. Import Data

4. Generate Load Cases (Optional):
   - Envelope Load Cases: Enter the formula with the desired load cases.
       - Example: "<LC1:FR1>,<LC2:FR1>,<LC100:FR10>"
	
   - Derived Load Cases: Enter the formula with the desired load cases.
       - Example: "2*<LC1:FR1>+0.5*<LC2:FR1>-<LC100:FR10>"
	
5. Select Element IDs: Select several IDs separated by commas or use "ALL".
	- Example: 1000, 1001, 1002, 1003
	- Example: ALL
	
6. Select Load Cases for CSV Output:
	- Example: ALL
	- Example: "<LC1:FR1>,<LC-1:FR0>"
	
7. Material Axis (Optional): Click this option if you want the fluxes written in the material coordinate system. Otherwise, they will be written in the analysis system.

8. Click Generate Report
"""Script for an example tool using NaxToPy

Copyright (c) 2024 Idaero Solutions
"""
import NaxToPy as n2p
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import os
import time
# import pyi_splash  # Uncomment when using executable Tool


class FolderFileSelectorApp:
    """Main class of App"""

    def __init__(self, master):
        """
        Initialize the application.

        Args:
            master (tk.Tk): The root Tkinter window.
        """
        self.master = master
        self.master.title("NaxToPy Simple Tool")

        if os.path.exists('.\\logo.ico'):
            self.master.iconbitmap('.\\logo.ico')
        elif os.path.exists('.\\bin\\logo.ico'):
            self.master.iconbitmap('.\\bin\\logo.ico')

        self.master.geometry("550x650")
        self.master.wm_minsize(550, 650)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(3, weight=1)

        # Variable to store the selected model path
        self.model_path = ""
        # List to store the selected results paths
        self.result_paths = list()

        self.create_widgets()

    def create_widgets(self):
        """Method that generates the application interface"""

        tk.Label(self.master, text="Selected Model:").grid(row=0, column=0, pady=5)
        self.folder_entry = tk.Entry(self.master, textvariable=self.model_path)
        self.folder_entry.grid(row=0, column=1, pady=5, sticky='ew')

        tk.Button(self.master, text="Select Model", command=self.import_model).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.master, text="Selected Results:").grid(row=1, column=0, pady=5)
        self.file_entry = tk.Entry(self.master, textvariable=self.result_paths)
        self.file_entry.grid(row=1, column=1, pady=5, sticky='ew')

        tk.Button(self.master, text="Select Results", command=self.import_results).grid(row=1, column=2, pady=5)

        tk.Button(self.master, text="Import Data", command=self.import_data).grid(row=2, column=1, pady=5, sticky='ew')
        self.is_parallel_checked = tk.BooleanVar()
        tk.Checkbutton(self.master, text="Parallel", variable=self.is_parallel_checked).grid(row=2, column=2, pady=5)

        tk.Label(self.master, text="Model Data:").grid(row=3, column=0, pady=5)
        self.data_text = tk.Text(self.master, width=40, height=5)
        self.data_text.grid(row=3, column=1, columnspan=2, padx='0 15', pady=5, sticky='nsew')

        # ############################### ENVELOPE LOADCASE #########################################
        tk.Label(self.master, text="Create Envelope LC\n <LC#:FR#>:").grid(row=4, column=0, pady=5)
        # Create the entry for inputting numbers
        self.env_entry = tk.Entry(self.master)
        self.env_entry.grid(row=4, column=1, pady=5, sticky='ew')
        # Create the button to parse the input and save the list
        tk.Button(self.master, text="Create", command=self.create_env).grid(row=4, column=2, pady=5)
        # Create a label to display the saved list
        self.saved_env_formula = tk.Label(self.master, text="")
        self.saved_env_formula.grid(row=5, column=0, columnspan=2, pady=5)

        # ############################### DERIVED LOADCASE #########################################
        tk.Label(self.master, text="Create Derived LC\n <LC#:FR#>:").grid(row=6, column=0, pady=5)
        # Create the entry for inputting numbers
        self.dev_lc_entry = tk.Entry(self.master)
        self.dev_lc_entry.grid(row=6, column=1, pady=5, sticky='ew')
        # Create the button to parse the input and save the list
        tk.Button(self.master, text="Create", command=self.create_derived_lc).grid(row=6, column=2, pady=5)
        # Create a label to display the saved list
        self.saved_dev_lc_formula = tk.Label(self.master, text="")
        self.saved_dev_lc_formula.grid(row=7, column=0, columnspan=2, pady=5)

        # ################################ IDS SELECTION ###########################################
        tk.Label(self.master, text="Select Ids:").grid(row=8, column=0, pady=5)
        # Create the entry for inputting numbers
        self.ids_entry = tk.Entry(self.master)
        self.ids_entry.grid(row=8, column=1, pady=5, sticky='ew')
        # Create the button to parse the input and save the list
        tk.Button(self.master, text="Select", command=self.save_ids).grid(row=8, column=2, pady=5)
        # Create a label to display the saved list
        self.saved_ids = tk.Label(self.master, text="")
        self.saved_ids.grid(row=9, column=0, columnspan=3, pady=5)

        # ############################### LOADCASE SELECTION #########################################
        tk.Label(self.master, text="Select LC:FR\n<LC#:FR#>:").grid(row=10, column=0, pady=5)
        # Create the entry for inputting numbers
        self.numbers_entry = tk.Entry(self.master)
        self.numbers_entry.grid(row=10, column=1, pady=5, sticky='ew')
        # Create the button to parse the input and save the list
        tk.Button(self.master, text="Select", command=self.save_lcs).grid(row=10, column=2, pady=5)
        # Create a label to display the saved list
        self.saved_lcs = tk.Label(self.master, text="")
        self.saved_lcs.grid(row=11, column=0, columnspan=3, pady=5)

        # Create a label widget to display "Main Menu" with bold font
        tk.Label(self.master, text="N2PReport", font=font.Font(weight="bold")).grid(row=12, column=1, pady=5)

        tk.Label(self.master, text="Result: FORCES\nComponents: FX, FY, FXY").grid(row=13, column=0, pady=5)
        self.is_material_axis_checked = tk.BooleanVar()
        tk.Checkbutton(self.master, text="Material Axis", variable=self.is_material_axis_checked).grid(row=13, column=1, pady=5)
        tk.Button(self.master, text="Generate Report", command=self.generate_report).grid(row=13, column=2, padx='0 5', pady=5)

    def import_model(self):
        """Method that opens a window to select the model file and save the path"""

        model_selected = filedialog.askopenfilename(filetypes=[("Nastran Input File", "*.bdf"),
                                                               ("Nastran Input File", "*.dat"),
                                                               ("Output Nastran", "*.op2"),
                                                               ("All Files", "*.*")])
        if model_selected:
            self.model_path = os.path.abspath(model_selected)
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(tk.END, model_selected)

    def import_results(self):
        """Method that opens a window to select the results files and save the paths in a list"""

        results_selected = filedialog.askopenfilenames(filetypes=[("Output Nastran", "*.op2"),
                                                                  ("All Files", "*.*")])
        if results_selected:
            self.result_paths = list(results_selected)
            self.update_file_listbox()

    def update_file_listbox(self):
        self.file_entry.delete(0, tk.END)
        for file_path in self.result_paths:
            self.file_entry.insert(tk.END, file_path)

    def import_data(self):
        """Method that calls the NaxToPy functions that load the model and the results"""
        try:
            if self.model_path:

                parallel = False
                if self.is_parallel_checked.get():
                    parallel = True

                # load_model() is the NaxToPy function that read mesh (.bdf files) or mesh and results (.op2 files).
                # Is the same function for other solvers.
                ti = time.time()
                self.model = n2p.load_model(str(self.model_path), parallelprocessing=parallel)
                tf = time.time() - ti
                n2p.N2PLog.Info.user(f"I1000: Time to load the Mesh: {tf} seconds")

                if self.result_paths and self.model != self.result_paths:

                    # import_results_from_files() is the NaxToPy the results (.op2 files). Is the same function for other solvers.
                    ti = time.time()
                    self.model.import_results_from_files(self.result_paths)
                    tf = time.time() - ti
                    n2p.N2PLog.Info.user(f"I1001: Time to load the Results: {tf} seconds")

                self.print_model_data()
        except Exception:
            messagebox.showerror("Error Loading File", "An error ocurred when loadig the file. Please make sure the paths are correct and try again.")

    def print_model_data(self):
        """This method extracts some information to make a summary of the model content. It uses NaxToPy properties"""
        n_lc = len(self.model.LoadCases)
        n_elements = len(self.model.ElementsDict)
        n_connectors = len(self.model.ConnectorsDict)
        n_nodes = len(self.model.NodesDict)
        n_coords = len(self.model.get_coords())

        self.print_text(f"Elements: {n_elements}\n" + \
                        f"Nodes: {n_nodes}\n" + \
                        f"Connectors: {n_connectors}\n" + \
                        f"Coordinate Systems: {n_coords}\n" + \
                        f"Load Cases: {n_lc} -> {[lc.ID for lc in self.model.get_load_case()]}\n")

    def print_text(self, text):
        self.data_text.config(state="normal")
        self.data_text.delete('1.0', tk.END)
        self.data_text.insert(tk.END, text + "\n")
        self.data_text.config(state="disabled")

    def create_env(self):
        """Method that creates a new case as an envelope of the cases selected"""
        try:
            formula = self.env_entry.get()
            if formula is None or formula.strip() == '':
                return
            
            # new_envelope_loadcase() is a method of an N2PModelContent object that generate the load case as an envelope
            ti = time.time()
            n2p_env_vase = self.model.new_envelope_loadcase("ENV-CASE", formula)
            self.env_case = f"<LC{n2p_env_vase.ID}:FR0>"
            tf = time.time() - ti
            n2p.N2PLog.Info.user(f"I1002: Time to generate the loadcase enevelopes: {tf} seconds")
            self.saved_env_formula.config(text=self.env_case)

            self.print_model_data()
        except Exception:
            messagebox.showerror("Error Creating Envelope",
                                 "An error ocurred when creating the envelope. Please make sure the parameters are correct and try again.")

    def create_derived_lc(self):
        """Method that creates a new case as combination of the cases selected"""
        try:
            formula = self.dev_lc_entry.get()
            if formula is None or formula.strip() == '':
                return
            
            # new_envelope_loadcase() is a method of an N2PModelContent object that generate the load case as combination of
            # the original. The formula for the combination must be included.
            ti = time.time()
            n2p_dev_lc = self.model.new_derived_loadcase("DEV-CASE", formula)
            self.dev_lc_case = f"<LC{n2p_dev_lc.ID}:FR0>"
            tf = time.time() - ti
            n2p.N2PLog.Info.user(f"I1002: Time to generate derived load case: {tf} seconds")
            self.saved_dev_lc_formula.config(text=self.dev_lc_case)

            self.print_model_data()
        except Exception:
            messagebox.showerror("Error Creating Derived LC",
                                 "An error ocurred when creating the derived load case. Please make sure the parameters are correct and try again.")

    def save_ids(self):
        try:
            # Get the input text from the entry widget
            input_text = self.ids_entry.get()

            # Parse the input string to create a list of integers
            if input_text == 'ALL':
                self.ids_list = 0
            else:
                self.ids_list = [int(num.strip()) for num in input_text.split(",") if num.strip()]

            # Update the label to display the saved list
            if type(self.ids_list) is int:
                self.saved_ids.config(text="ALL")
            else:
                if len(self.ids_list) < 8:
                    self.saved_ids.config(text=str(self.ids_list))
                else:
                    self.saved_ids.config(text=str(self.ids_list[:8])[:-1] + "...")
        except Exception:
            messagebox.showerror("Error Selecting IDs",
                                 "An error ocurred when saving the selected IDs. Please make sure the parameters are correct and try again.")

    def save_lcs(self):
        try:
            # Get the input text from the entry widget
            self.lcs_formula = self.numbers_entry.get()

            if self.lcs_formula == "ALL":
                self.lcs_formula = ",".join(f"<LC{lc.ID}:FR{lc.ActiveIncrement}>" for lc in self.model.LoadCases)

            self.lcs_formula = self.lcs_formula.replace("LCD", "LC-")
            number_list = [num.strip() for num in self.lcs_formula.split(",") if num.strip()]

            # Update the saved list variable

            # Update the label to display the saved list
            if len(number_list) < 5:
                self.saved_lcs.config(text=str(number_list))
            else:
                self.saved_lcs.config(text=str(number_list[:5])[:-1] + "...")
        except Exception:
            messagebox.showerror("Error Selecting LCs",
                                 "An error ocurred when saving the selected LCs. Please make sure the parameters are correct and try again.")

    def generate_report(self):
        """Method of the app that calls the NaxToPy functions that create a report and write it in a CSV file"""
        try:
            coordsys = -1000
            if self.is_material_axis_checked.get():
                coordsys = -1

            # new_report() is the method of a N2PModelContent that generates a N2PReport. It contains the input information
            # but the data is not generated until the method calculate() is called
            n2p_report = self.model.new_report(self.lcs_formula, False, "FORCES", "<FX:NONE#>,<FY:NONE#>,<FXY:NONE#>",
                                               False, self.model.get_elements(self.ids_list), "LC", coordsys=coordsys)
            t1 = time.time()
            # Method of the N2PReport that calculate the data acording to the properties of the object.
            n2p_report.calculate()
            n2p.N2PLog.Info.user(f"I1003: Time to calculate the report: {time.time()-t1}")
            
            t1 = time.time()
            # Method that writes the data. Must be called after using calculate()
            n2p_report.to_csv("NaxToPy_report.csv")
            n2p.N2PLog.Info.user(f"I1004: Time to print the report: {time.time()-t1}")
        except Exception:
            messagebox.showerror("Error Generating Report",
                                 "An error ocurred when generating the report. Please make sure the parameters are correct and try again.")


def main():
    """Main function of the app"""
    root = tk.Tk()
    app = FolderFileSelectorApp(root)
    root.mainloop()


if __name__ == "__main__":
    
    # pyi_splash.close()  # Uncomment when using executable Tool

    # Select the output error level written in the .log file
    n2p.N2PLog.set_file_level("DEBUG")
    main()

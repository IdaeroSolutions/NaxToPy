"""This script has a basic example of how to post-process finite element models in Python.

The use of python code can help engineers to automate recursive task and work with a few lines. 
The FE models have now lots of load case and to process all this data new tools are needed.

This script uses two external packages:
    - NaxToPy: https://pypi.org/project/NaxToPy/
    - numpy: https://pypi.org/project/numpy/

The package and this script is build by Manuel Sanchez. You can contact me at manuel.sanchez@idaerosolutions.com .
"""

import NaxToPy as n2p
import numpy as np
import csv

def combine_loadcases(n2pmodel: n2p.AllClasses.N2PModelContent) -> tuple[n2p.AllClasses.N2PLoadCase, n2p.AllClasses.N2PLoadCase]:
    """Combine the load cases and generate the enevlope load cases.
    
    Returns:
        out:
            - env_ct: Load Case with the extrem values of the FX.
            - env_lc: Load Case with the id of the combiend load case that is critical.
    """
   
    # Combine linearly the load cases, the thermal (17500) with the mechanicals (the remain)
    for lc in n2pmodel.LoadCases[1:]:
        # Create the formula using a formated (f"") string
        formula = f"1.5*<LC{lc.ID}:FR1>+<LC17500:FR1>"
        # Call no the NaxToPy method for derived load case creation
        n2pmodel.new_derived_loadcase(f"{lc.ID}+17500", formula)

    # Formula to create a envelope load case
    formula_env = ",".join([f"<LC{lc.ID}:FR0>" for lc in n2pmodel.LoadCases if lc.TypeLC == "DERIVED"])

    # Creation of the two envelope load cases, the first for the values and the second for the load cases
    env_ct = n2pmodel.new_envelope_loadcase("envelope contour", formula=formula_env, criteria="ExtremeMax", envelgroup="ByContour")
    env_lc = n2pmodel.new_envelope_loadcase("envelope loadcase", formula=formula_env, criteria="ExtremeMax", envelgroup="ByLoadCaseID")

    return env_ct, env_lc


def writer(path: str, id_e: list[int], part_e: list[int], fx_cqudas: np.ndarray, fx_lc_cquads: np.ndarray) -> None:
    """Writes the output in the NaxToView format"""

    with open(".\\fx_cquad_envelope.csv", "w", newline="") as f:
        writer = csv.writer(f)  # Creates the csv writer
        writer.writerow(["ID_E", "PARTS_E", "FX", "LoadCase"])  # Write header
        writer.writerows(zip(id_e, part_e, fx_cqudas, fx_lc_cquads))  # Write data rows


def main() -> None:
    """Main function of the script"""
    
    path = r"C:\Webinar\model\SUBCASE_17500.dat"
    model = n2p.load_model(path)

    cquads = [cuad for cuad in model.get_elements() if cuad.TypeElement == "CQUAD4"]

    model.import_results_from_files([
        r"C:\Webinar\model\subcase_17500.op2",
        r"C:\Webinar\model\subcase_17501.op2",
        r"C:\Webinar\model\subcase_17502.op2",
        r"C:\Webinar\model\subcase_17503.op2",
        r"C:\Webinar\model\subcase_17504.op2"]
    )

    # Combine the load cases and generate the enevlope load cases.
    # Call to the combine_loadcases function definded above. Modular structure helps to reuse and debug code.
    env_ct, env_lc = combine_loadcases(model)

    # Get the results for FX
    fx = env_ct.get_result("FORCES").get_component("FX").get_result_ndarray()[0][:len(model.get_elements())]

    # Get the critical load cases
    fx_lc = env_lc.get_result("FORCES").get_component("FX").get_result_ndarray()[0][:len(model.get_elements())]

    # Map of the ids that we need to search in the results
    cquads_internal_ids = [cquad.InternalID for cquad in cquads]

    # In numpy you can access an array with a int:
    #     arr = [1, 4, 8, 12, 15] ; arr[2] -> 8
    # and with a list of ints:
    #     arr = [1, 4, 8, 12, 15] ; arr[[2,3]] -> [8, 12]
    fx_cqudas = fx[cquads_internal_ids]
    fx_lc_cquads = fx_lc[cquads_internal_ids]

    # Comprehension list to save the CQUAD4 ids and parts
    id_e = [cquad.ID for cquad in cquads]
    part_e = [cquad.PartID for cquad in cquads]

    out_path = ".\\cquad_results.csv"

    # Call to the writer function defined above. Modular structure helps to reuse and debug code
    writer(out_path, id_e, part_e, fx_cqudas, fx_lc_cquads)


# Entrance to the program. 
if __name__ == "__main__":
    main()
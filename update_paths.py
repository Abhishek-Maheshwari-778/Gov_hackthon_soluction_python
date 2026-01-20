import nbformat as nbf
import os

target_file = r"e:\3rd_year\hackthon\work.ipynb"

def update_paths():
    if not os.path.exists(target_file):
        print("Notebook not found!")
        return

    ntbk = nbf.read(target_file, nbf.NO_CONVERT)
    
    found = False
    for cell in ntbk.cells:
        if cell.cell_type == 'code' and 'PATHS =' in cell.source:
            print("Found PATHS definition cell.")
            # Replace the old path structure with the new one
            new_source = cell.source.replace('"api_data_aadhar_enrolment", "api_data_aadhar_enrolment")', '"api_data_aadhar_enrolment")')
            new_source = new_source.replace('"api_data_aadhar_demographic", "api_data_aadhar_demographic")', '"api_data_aadhar_demographic")')
            new_source = new_source.replace('"api_data_aadhar_biometric", "api_data_aadhar_biometric")', '"api_data_aadhar_biometric")')
            
            if new_source != cell.source:
                cell.source = new_source
                found = True
                print("Updated paths in cell.")
            else:
                print("Paths already updated or not matching expected pattern.")
            break
            
    if found:
        nbf.write(ntbk, target_file)
        print("Notebook updated successfully!")
    else:
        print("Could not find the PATHS definition to update.")

if __name__ == "__main__":
    update_paths()

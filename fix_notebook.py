import nbformat as nbf
import os

target_file = r"e:\3rd_year\hackthon\folder\work.ipynb"

# The missing code cell content
missing_code = """from sklearn.ensemble import IsolationForest

# Feature Selection for Anomaly Detection
# We use Migration Volume and Digital Compliance as key proxies
features = ['Migration_Volume', 'Digital_Compliance', 'New_Births']
X = master_df[features].fillna(0)

# Training the Model
# Contamination = 0.02 means we expect ~2% of districts to be outliers
iso = IsolationForest(contamination=0.02, random_state=42)
master_df['Is_Anomaly'] = iso.fit_predict(X)

# -1 indicates Anomaly, 1 indicates Normal
anomalies = master_df[master_df['Is_Anomaly'] == -1]
print(f"Detected {len(anomalies)} Anomalous Districts.")
display(anomalies[['Migration_Volume', 'Digital_Compliance', 'Is_Anomaly']].head())"""

def fix_notebook():
    if not os.path.exists(target_file):
        print("Notebook not found!")
        return

    ntbk = nbf.read(target_file, nbf.NO_CONVERT)
    
    # Find insertion point (before visualization)
    insert_idx = -1
    for idx, cell in enumerate(ntbk.cells):
        if "Visualization of Anomalies" in cell.source:
            insert_idx = idx
            break
            
    if insert_idx != -1:
        print(f"Found target at cell {insert_idx}. Inserting fix...")
        
        # Create new cells
        md_cell = nbf.v4.new_markdown_cell("## Phase 7: Anomaly Detection (Isolation Forest)\nWe use an Unsupervised Learning algorithm to detect districts that behave 'strangely' (Outliers).")
        code_cell = nbf.v4.new_code_cell(missing_code)
        
        # Insert them
        ntbk.cells.insert(insert_idx, md_cell)
        ntbk.cells.insert(insert_idx + 1, code_cell)
        
        nbf.write(ntbk, target_file)
        print("Notebook fixed successfully!")
    else:
        print("Could not find the visualization cell to insert before.")

if __name__ == "__main__":
    fix_notebook()

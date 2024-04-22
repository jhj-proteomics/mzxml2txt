import os
from pyteomics import mzxml
import csv

# Path to your mzXML file
mzxml_path = r'C:\Users\[username]\Desktop\[path to .mzXML file]'

# Directory to store output TXT files
output_directory = r'C:\Users\[username]\Desktop\[path to output directory]'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the mzXML file
with mzxml.read(mzxml_path) as reader:
    for i, spectrum in enumerate(reader):
        # Create a unique filename for each spectrum using the spectrum ID
        txt_path = f'{output_directory}\\spectrum_{spectrum["id"]}.txt'

        # Open the output TXT file for writing for the current spectrum
        with open(txt_path, 'w', newline='') as txtfile:
            tsv_writer = csv.writer(txtfile, delimiter='\t')
            
            # Data for the current spectrum
            mzs = spectrum['m/z array']
            intensities = spectrum['intensity array']
            charges = spectrum.get('charge array', [None] * len(mzs))

            # Write each peak to the TXT for the current spectrum without headers
            for mz, intensity, charge in zip(mzs, intensities, charges):
                tsv_writer.writerow([mz, intensity, charge])

print("Conversion of all spectra completed and saved in separate TXT files.")

import zipfile
import os
import pandas as pd

def csv_to_zip(csv_file_path, zip_file_path=None):
    """
    Convert a CSV file to a ZIP file
    
    Parameters:
    csv_file_path (str): Path to the input CSV file
    zip_file_path (str): Path for the output ZIP file (optional)
    """
    
    # Check if CSV file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found!")
        return False
    
    # If no zip file path provided, create one based on CSV filename
    if zip_file_path is None:
        base_name = os.path.splitext(csv_file_path)[0]
        zip_file_path = f"{base_name}.zip"
    
    try:
        # Create a ZIP file
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add the CSV file to the ZIP
            csv_filename = os.path.basename(csv_file_path)
            zipf.write(csv_file_path, csv_filename)
        
        print(f"Successfully converted '{csv_file_path}' to '{zip_file_path}'")
        print(f"ZIP file size: {os.path.getsize(zip_file_path)} bytes")
        return True
        
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        return False

def convert_multiple_csv_to_zip(csv_files, zip_file_path):
    """
    Convert multiple CSV files to a single ZIP file
    
    Parameters:
    csv_files (list): List of CSV file paths
    zip_file_path (str): Path for the output ZIP file
    """
    
    try:
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for csv_file in csv_files:
                if os.path.exists(csv_file):
                    csv_filename = os.path.basename(csv_file)
                    zipf.write(csv_file, csv_filename)
                    print(f"Added '{csv_file}' to ZIP")
                else:
                    print(f"Warning: File '{csv_file}' not found, skipping...")
        
        print(f"Successfully created ZIP file: '{zip_file_path}'")
        return True
        
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Method 1: Convert a single CSV file
    # print("=== Single CSV to ZIP ===")
    # csv_to_zip("Movie-dataset.csv")

    print("\n=== Single CSV to ZIP with custom name ===")
    csv_to_zip("food_dataset.csv", "Food_dataset.zip")

    # # Method 2: Convert multiple CSV files to one ZIP
    # print("\n=== Multiple CSV files to single ZIP ===")
    # csv_files_list = [
    #     "StressLevelDataset.csv",
    #     "Student_Marks.csv", 
    #     "Iris.csv",
    #     "Cars_Datasets_2025.csv"
    # ]
    # convert_multiple_csv_to_zip(csv_files_list, "all_datasets.zip")
    
    # # Method 3: Interactive mode
    # print("\n=== Interactive Mode ===")
    # user_csv = input("Enter CSV file path: ")
    # user_zip = input("Enter ZIP file name (or press Enter for auto-name): ")
    
    # if user_zip.strip() == "":
    #     user_zip = None
    
    # csv_to_zip(user_csv, user_zip)

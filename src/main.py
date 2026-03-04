#import packages
import os
import pandas as pd

from dotenv import load_dotenv
from os import getenv

from utils.snowflake_ncl import upload_df
from utils.snowflake_ncl import create_connection

#load .env 
load_dotenv(override=True)

#get qof raw data files from project folder
def get_files(data_dir, file_ext=""):
    """
    Get a list of data files at the listed data_dir location.
    Args:
        data_dir: Path to data files
        file_ext (optional): Limit data files to a specific extension
    Returns:
        list(str): List of file names
    """
    dir_list = [x for x in os.listdir(data_dir) if x.endswith(file_ext)]

    #Cleanse the list
    if dir_list == []:
        e_message = f"No files were found in {data_dir}" 
        raise Exception(e_message)

    return dir_list

data_dir = getenv("RAW_DATA")
files = get_files(data_dir, file_ext="csv")

#establish snowflake connection
ctx = create_connection(
        account=getenv("SNOWFLAKE_ACCOUNT"), 
        user=getenv("SNOWFLAKE_USER"), 
        role=getenv("SNOWFLAKE_ROLE"),
        warehouse=getenv("SNOWFLAKE_WAREHOUSE"))

#upload files to snowflake
for f in files:

    # Build full file path automatically
    file_path = os.path.join(data_dir, f)

    # Extract filename without extension and get table name
    filename = os.path.basename(file_path)
    
    #remove _v2 from file name for cleanliness
    if filename.endswith("_v2.csv"):    
        filename = filename.replace("_v2", "")

    table_name = os.path.splitext(filename)[0].upper()

    # Load CSV
    df = pd.read_csv(file_path)

    # Upload to snowflake
    upload_df(
        ctx=ctx,
        df=df,
        table_name=table_name,
        replace=True,
        table_columns=list(df.columns)
    )

    print(f"Uploaded {file_path} to table {table_name}")


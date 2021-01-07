import tabula
import os
import re
import openpyxl

import pandas as pd

def merge_cols_to_str(df):
    str_output = ""
    
    for i in range(df.shape[1]):
        str_output += str(df.iloc[0][i])
    
    return str_output

def fix_date(str):
    str_new = re.findall(r"[\d]+", str)
    str_new = "".join(str_new)
    str_new = str_new.replace(" ", "")
    
    return str_new

def scrape_vat_return(fp):
    result = {}

    for key, val in coordinates.items():
        df = tabula.read_pdf(fp,
                             pages=1,
                             stream=True,
                             area=val,
                             pandas_options={'header': None})

        result[key] = merge_cols_to_str(df[0])
    
    result["date_from"] = fix_date(result["date_from"])
    result["date_to"] = fix_date(result["date_to"])
    result["code"] = int(result["code"])
    result["vat_receivable_payable"] = float(result["vat_receivable_payable"])

    return result

def scrape(filepaths):
    results = []
    
    for fp in filepaths:
        vat_return = scrape_vat_return(fp)
        results.append(vat_return)
    
    df = pd.DataFrame(vat_returns)

    df["date_from"] = pd.to_datetime(df["date_from"])
    df["date_to"] = pd.to_datetime(df["date_to"])

    df = df.sort_values(by=["code", "date_from"])

    df.to_excel("output.xlsx") 

    return "Success!"
    

coordinates = {
    "name": (101.248, 112.111, 129.928, 570.117),
    "code": (129.058, 115.588, 154.262, 279.844),
    "vat_code": (129.928, 347.632, 160.345, 566.64),
    "date_from": (260.29, 98.206, 286.362, 250.295),
    "date_to": (261.159, 268.546, 284.624, 423.242),
    "vat_receivable_payable": (697.437, 465.827, 727.855, 572.724)    
}


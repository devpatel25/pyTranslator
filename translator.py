import pandas as pd
from googletrans import Translator
import time
import xlrd

def translate_file(input_file,output_file):
    start_time=time.time()      #start the timer
    df= pd.read_excel(input_file)
    translator=Translator()
    for col in df.columns:
        df[col]=df[col].apply(lambda x: translator.tranlate(x).text)

    df.to_excel(output_file,index=False)

    run_time = time.time() - start_time     #get the run time
    print(f"Translation and saving completed in {run_time: .2f} sec.")

if __name__=="__main__":
    input_file="OrderExport.xls"
    output_file="TranslatedOrderExport.xls"
    translate_file(input_file,output_file)
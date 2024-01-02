import pandas as pd
from googletrans import Translator
import time
import xlrd

def translate_file(input_file,output_file):
    start_time=time.time()      #start the timer
    # Load the file
    try:
        df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error: {e}")
        return

    translator=Translator()
    for col in df.columns:
        df[col]=df[col].apply(lambda x: translator.translate(x).text if not translator.translate(x).text == "error" else x)

    # Save the translated data to a new file
    try:
        df.to_excel(output_file, index=False)
    except Exception as e:
        print(f"Error: {e}")
        return

    run_time = time.time() - start_time     #get the run time
    print(f"Translation and saving completed in {run_time: .2f} sec.")

if __name__=="__main__":
    input_file="OrderExport.xls"
    output_file="TranslatedOrderExport.xls"
    translate_file(input_file,output_file)
import tkinter as tk
from tkinter import filedialog
import os.path

"""
Requirements: Python 3.8+
python -m pip install tkinter
"""

def Main():
    print("Download and save images back into the zip of Medium.com backup zip file.")
    root = tk.Tk()
    root.withdraw()
    zipfile = filedialog.askopenfilename(title = "Select the Medium.com backup zip file",filetypes = (("zip files","*.zip"),("all files","*.*")))
    if not os.path.isfile(zipfile):
        logging.error("No valid file selected")
        raise Exception() 
    logging.info(f"Selected zip: {zipfile}")

### set up logging
import logging, sys, socket
machinename = socket.gethostname()
logging.basicConfig(
    level=logging.INFO,
    format=f"%(message)s\t%(asctime)s\t{machinename}\t%(threadName)s\t%(levelname)s",
    handlers=[
        #logging.FileHandler(f"{logfile}.txt"),
        logging.StreamHandler(sys.stdout)
    ]
)

### doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# main run
try:
    Main()
except Exception:
    logging.exception("Fatal error")


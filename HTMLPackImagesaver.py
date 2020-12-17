import tkinter as tk
from tkinter import filedialog
import os.path
import tempfile
import zipfile
from bs4 import BeautifulSoup
"""
Requirements: Python 3.8+
python -m pip install tkinter pyttsx3 html5lib
"""
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            ziph.write(filename=filepath, arcname=filepath.replace(path, ""))

def Main():
    print("Download and save images back into the zip of Medium.com backup zip file.")
    root = tk.Tk()
    root.withdraw()
    zipfilename = filedialog.askopenfilename(title = "Select the Medium.com backup zip file",filetypes = (("zip files","*.zip"),("all files","*.*")))
    if not os.path.isfile(zipfilename):
        logging.error("No valid file selected")
        raise Exception() 
    logging.info(f"Selected zip: {zipfile}")

    with tempfile.TemporaryDirectory() as tempdir:
        logging.info(f"Tempdir: {tempdir}")

        with zipfile.ZipFile(zipfilename, 'r') as zipf:
            logging.info(f"Unzip: {zipfilename}")
            zipf.extractall(tempdir)
        
        for root, dirs, files in os.walk(tempdir):
            for file in files:
                filepath = os.path.join(root, file)
                logging.info(f"Search images in {file}")

                soup = None
                with open(filepath, "rb") as f:
                    try:
                        soup = BeautifulSoup(f, "html5lib")
                    except:
                        logging.debug(f"This is not a html file: {file}")
                
                if soup:
                    imgfound = False
                    links = soup.find_all('img')
                    for i in links:
                        print(i['src'])
                        imgfound = True

                    if imgfound:
                        logging.info("Saving changes...")
                        with open(filepath, "w", encoding="utf-8") as file:
                            file.write(str(soup))
                    

        outfile = zipfilename+"2.zip"
        if os.path.isfile(outfile):
            logging.info(f"Delete existing file: {outfile}")
            os.remove(outfile)
            
        with zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED) as zipf:
            logging.info(f"Compress files to zip")
            zipdir(tempdir, zipf)

### set up logging
import logging, sys, socket
import pyttsx3

class TalkerHandler(logging.StreamHandler):
    """
    A logging handler class which talks the output
    """
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def emit(self, record):
        try:
            msg = self.format(record).split("\t")[0]
            self.engine.say(msg)
            self.engine.runAndWait()
        except:
            self.handleError(record)

machinename = socket.gethostname()
logging.basicConfig(
    level=logging.INFO,
    #format=f"%(message)s\t%(asctime)s\t{machinename}\t%(threadName)s\t%(levelname)s",
    format=f"%(message)s",
    handlers=[
        #logging.FileHandler(f"{logfile}.txt"),
        logging.StreamHandler(sys.stdout)
        #TalkerHandler()
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


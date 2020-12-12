
"""
Requirements: Python 3.8+
python -m pip install 
"""

def Main():
    pass

### set up logging
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format=f"%(message)s\t%(asctime)s\t%(threadName)s\t%(levelname)s",
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


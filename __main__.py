
# __main__.py

import sys
import os

# Add the parent directory of the current script to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

print("Current Python Path:", sys.path)  # Utskrift for å se banen


#from .main import main
from main import main


if __name__ == "__main__":
    main()

import os
import sys

# General Config         

# prices Config
Prices = [
    ("Letter / Short and A4 paper per page", 2),    # Default : 2
    ("Legal / Long paper per page", 3),             # Default : 3
    ("Photo Paper per page", 25),                   # Default : 25
    ("Black and White print per page", 2),          # Default : 2
    ("Full Color print per page", 3),               # Default : 3
    ("Binding", 30),                                # Default : 30
    ("Lamination", 15),                             # Default : 15
]

import sys

# Folder of the .exe when packaged, otherwise the project folder
if getattr(sys, "frozen", False):
    appFolder = os.path.dirname(sys.executable)    # next to PrintSync.exe (saved data)
    bundleDir = sys._MEIPASS                    # inside the exe (default files)
else:
    appFolder = bundleDir = os.path.dirname(os.path.abspath(__file__))

pricesFile = os.path.join(appFolder, "prices.json")

# Use the saved prices if they exist, otherwise the bundled defaults
for path in (pricesFile, os.path.join(bundleDir, "prices.json")):
    try:
        with open(path, "r") as file:
            saved = file.read().split()
        Prices = [(label, int(saved[i])) for i, (label, value) in enumerate(Prices)]
        break
    except Exception:
        continue

# Status
Statuses = [
    "Pending",
    "Printing",
    "Ready for Pickup",
    "Completed",
    "Cancelled",
]
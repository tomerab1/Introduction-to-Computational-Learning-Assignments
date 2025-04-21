import nbformat
from nbformat import NO_CONVERT
import sys

if len(sys.argv) != 2:
    print("Usage: python strip_widget.py <notebook.ipynb>")
    sys.exit(1)

nb = nbformat.read(sys.argv[-1], as_version=NO_CONVERT)

nb.metadata.pop("widgets", None)

for cell in nb.cells:
    cell.metadata.pop("widgets", None)

nbformat.write(nb, sys.argv[-1])

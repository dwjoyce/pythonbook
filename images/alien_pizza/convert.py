import subprocess
import pathlib


for i in pathlib.Path(__file__).parent.glob("*.svg"):
    new = i.with_suffix(".pdf")
    subprocess.call("inkscape -D -z --file={} --export-pdf={}".format(i, new).split())
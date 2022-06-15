# cellfinder-ROI-validation
Script to allow manual cell counting in an anatomically restricted ROI


## To install
```bash
conda create --name cellfinder-ROI-validation python=3.9
conda activate cellfinder-ROI-validation
pip install napari[all] cellfinder
git clone https://github.com/adamltyson/cellfinder-ROI-validation
```

## To use
To run the software, you need to provide:
* The path to `main.py` (e.g. `cellfinder-ROI-validation/main.py`)
* The path to the raw data to be visualised (e.g. `/data/ch2`)
* The path to the cellfinder output directory (e.g. `analysis/cellfinder_output`)
* The acronym of the region to be analysed (e.g. `VISp`)

```bash
python cellfinder-ROI-validation/main.py /data/ch2 analysis/cellfinder_output VISp
```
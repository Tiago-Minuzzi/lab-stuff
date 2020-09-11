# NCBI SCRAPING
Batch download genomes/genes from [NCBI - Nucleotide](https://www.ncbi.nlm.nih.gov/nucleotide) using its IDs. Script written in Python, using Selenium module for the task.
## Installation
Download [get_genome_by_id.py](https://raw.githubusercontent.com/Tiago-Minuzzi/lab-stuff/master/ncbi-scraping/get_genome_by_id.py) script and install dependencies.
## Dependencies
- Python version 3.x;
- Selenium module (Can be installed via pip install or conda install);
- Chromium/Google chrome browser;
- Selenium [chrome driver](https://chromedriver.chromium.org/downloads) (needs to match your Chromium/Google Chrome browser version).
## Usage
Change paths for chrome driver and files inside the script, either make it executable (using chmod +x) or run it by calling python3.

**Note of interest:** Tested with mitochondrial genome ids ('sample.txt' file).

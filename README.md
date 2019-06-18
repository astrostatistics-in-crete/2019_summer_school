# Project Title

Notebooks from the teaching sessions and the workshops of the
[2019 Summer School for Astrostatistics in Crete](
https://astro.physics.uoc.gr/Conferences/Astrostatistics_School_Crete_2019)

## Getting Started

The repository is organized in one folder per subject.
You will have to download the notebooks as well as the data
(which are on an other server).
See "Installing" below.

### Prerequisites 

```
Python v3.6
Jupyter notebook
```
Instructions on retrieveing Jupyter notebook are here: https://jupyter.org

### Installing

First download or clone this repository on your machine:

```
git clone https://github.com/astrostatistics-in-crete/2019_summer_school.git
```

Then download the data. 
From within the repository folder, run:

```
python get_data.py
```
This will automatically create the "data" subfolders within each 
subject folder, and download the data.
It will also try to run jupyter notebook: ignore that. 

## Running the notebooks

```
jupyter-notebook <notebook_name>.ipynb
```
## Authors

* **Andrew, Jeff** - University of Copenhagen

* **Bonfini, Paolo** - University of Crete and National Observatory of Athens

* **Kovlakas, Kostantinos** - University of Crete

## References

All the material provided (notebooks and scripts) are licenced
under the [Creative Commons BY-SA](https://creativecommons.org/licenses/by-sa/3.0/)
licence.

The notebooks have adopted publicly available material from
several sources, most notably [AstroML](http://www.astroml.org).
All the references to published papers, data, and software tools are
properly addressed within each notebook.


## Acknowledgments

If the material you learned through this summer school directly
and significantly contributed to your work, we invite you to
include the following acknowledge in your manuscript:

```
We wish to thank the "2019 Summer School for Astrostatistics in Crete" for providing training on the statistical methods adopted in this work.
```

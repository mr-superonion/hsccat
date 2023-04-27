# DOWNLOAD HSC CATALOG

+ Make an account on the [HSC
  website](https://hsc-release.mtk.nao.ac.jp/datasearch/)
+ Use [this sql](sqls/pdr3_shape.sql) to download the galaxy catalog.
+ Get a galaxy catalog (see [this catalog](./example_catalog/dr3.fits) for
  example)

# ANALYSIS

+ install the code in your computer by `pip instll -e .` under this directory;
+ Selection of galaxies since we need to select galaxies with high-SNR and
  resolution for accurate shape and magnitude estimation (see [this
  notebook]());
+ Derive inclination angle from the galaxy shapes (see [this notebook]()).

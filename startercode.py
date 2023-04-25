# Run the following in Colab to get the data.

# Set up environment
!pip install scanpy
!python -m pip uninstall -y matplotlib
!pip install matplotlib==3.1.3
import scanpy as sc
import pandas as pd

# PIP-seq barnyard data
!wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE202nnn/GSE202911/suppl/GSE202911_JZ20210405_FR_3_filtered_matrix.zip
!unzip GSE202911_JZ20210405_FR_3_filtered_matrix.zip
barnyard     = sc.read_mtx("2_001_filtered_matrix/matrix.mtx").T
barnyard.obs = pd.read_csv("2_001_filtered_matrix/barcodes.tsv", header = None, sep = "\t")
barnyard.var = pd.read_csv("2_001_filtered_matrix/genes.tsv",    header = None, sep = "\t")
barnyard

# Breast 10x data
!wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7074nnn/GSM7074403/suppl/GSM7074403_KP_cDNA_3_barcodes.tsv.gz
!wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7074nnn/GSM7074403/suppl/GSM7074403_KP_cDNA_3_features.tsv.gz
!wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM7074nnn/GSM7074403/suppl/GSM7074403_KP_cDNA_3_matrix.mtx.gz
breast_10x     = sc.read_mtx("GSM7074403_KP_cDNA_3_matrix.mtx.gz").T
breast_10x.obs = pd.read_csv("GSM7074403_KP_cDNA_3_barcodes.tsv.gz", header = None, sep = "\t")
breast_10x.var = pd.read_csv("GSM7074403_KP_cDNA_3_features.tsv.gz", header = None, sep = "\t")
breast_10x

# Breast PIP-seq data
!wget https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6620nnn/GSM6620702/suppl/GSM6620702_JZ_20211118_FR_1.zip
!unzip GSM6620702_JZ_20211118_FR_1.zip
breast_pip     = sc.read_mtx("force_17691/matrix.mtx").T
breast_pip.obs = pd.read_csv("force_17691/barcodes.tsv", header = None, sep = "\t")
breast_pip.var = pd.read_csv("force_17691/genes.tsv",    header = None, sep = "\t")
breast_pip

# PIP-seq barcoding data
!rm -r ./*
!wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE215nnn/GSE215165/suppl/GSE215165_TS20220816_FR_6.zip
!unzip GSE215165_TS20220816_FR_6.zip
pip_barcoded     = sc.read_mtx("filtered_matrix_with_adt/matrix.mtx").T
pip_barcoded.obs = pd.read_csv("filtered_matrix_with_adt/barcodes.tsv", header = None, sep = "\t")
pip_barcoded.var = pd.read_csv("filtered_matrix_with_adt/genes.tsv",    header = None, sep = "\t")
pip_barcoded

# The sample barcodes (hashtags) are extra non-gene features starting with "HTO". 
pip_barcoded.var.tail()

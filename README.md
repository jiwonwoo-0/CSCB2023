### CSCB final project

In class, we discussed a recent droplet-based technology for single-cell genomics called "PIP-seq". Here's the [paper](https://www.nature.com/articles/s41587-023-01685-z) and some additional resources on their startup company's [website](https://www.fluentbio.com/resources/). This technology seems to promise an unprecedented combination of traits: easy, cheap, and scalable. The data also seem to be of comparable quality to the current casual-consumer favorite, which is 10X Genomics. However, it is common for scientists to downplay the weaknesses of their own methods. Before adopting PIP-seq, your lab wants you to investigate the quality of the data and do a detailed comparison to 10X data. 

* Component 1: Read the PIP-seq paper. Discuss the evidence they present on common pitfalls of scRNA tech: doublets, ambient RNA, and depth/capture efficiency. Download the species-mixing experiment data from the record labeled [GSE202911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202911) on the Gene Expression Omnibus website (or obtain it using the starter code below). What fraction of cells have substantial RNA from both species? What fraction of UMIs in each cell are from the wrong species? What does this imply about the doublet rate and the ambient RNA fraction?

* Component 2: barcoding accuracy. Download the multiplexed PIP-seq data from GEO record [GSE215165](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE215165) or use the starter code below. Determine how easy or hard it is to separate the two barcoded samples. What percentage of cells do you think are mis-classified or cannot be classified?

* Component 3: PIP-seq involves a vortexing step that seems like it may damage cells. Compare the PIP-seq breast tissue data against the 10X breast tissue data. What are the main differences in cell counts and gene expression in each population? Is any cell population especially strongly affected? You can get the data from GEO records [GSM7074401](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM7074403) (10X) and [GSM6620702](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6620702) (PIP-seq), or you can use the starter code below. 

* Component 4: Some teams may not need to complete this component; see below. Using each of the methods we tested in class, integrate the 10X and PIP-seq breast datasets. Compare the results to a simple baseline using scanpy's `sc.pp.regress_out`. How does each method affect the cell type proportions, the differential expression results, and the overall interpretation from component 3?

* Component 5: Some teams may not need to complete this component; see below. This component is an experimental design task. Suppose your team has been hired as genomics consultants by a lab pioneering directed differentiation protocols for production of kidney organoids from pluripotent stem cells. They have a budget of $50,000, and using single-cell -omics, they want to create a detailed molecular profile of their protocol that will yield insights about the identity of the resulting cell types and the lineage relationships among them. How would you design the experiments? Please specify the technologies you will use, the number of cells you will sequence, the amount and type of biological replication, the days/times that samples will be collected, and plans for analysis or follow-up experiments. Describe how the new data will relate to existing kidney scRNA datasets. Suppose their protocol is the one documented by Takasato et al. in ["Kidney organoids from human iPS cells contain multiple lineages and model human nephrogenesis"](https://www.nature.com/articles/nature15695). You can use 10X, PIP-seq, or any other tech, or a combination. 


#### Deliverables

- Submit all code that you used for the project in a zipped folder. At the top level of the folder, include a README file that explains how you set up your computing environment and what each file or folder in your repo is for. For instance, "On a Dell laptop running Ubuntu 20.04, we installed python 3.9, scanpy version 17.6, and matplotlib version 3.14159. The folder `breast_comparison` contains our code for comparing the 10X vs PIP-seq breast data and the folder `barnyard` contains our code for analyzing doublets."
- Submit a 5 to 15 page written report explaining your approach for each component and your findings. Include figures to support key claims: for instance, "At high depths, PIP-seq is roughly 60% as efficient as 10X" should be supported by a figure. It's okay to copy-paste relevant figures from the PIP-seq paper or other sources as long as you clearly describe the source and the methods.
- Submit a 5 - 10 minute video summary of your findings. Video summaries should assume we know the problem, and do not have to spend time explaining the background. 

### Administrative aspects and grading

- This project will be done by teams made up of 2-3 students. Please form a team with students registered in the same section as you.
- Link for form teams: [Sign Up Sheet](https://docs.google.com/spreadsheets/d/1vPozvjjv46b1W3qAWPoNLTwIRprNR8MIuqSTa8vWIu0/edit?usp=sharing)  
- If you are in 447 instead of 647, you may skip component 5.
- Teams with members in both 447 and 647 will be treated as 647. 
- If you have a team with only 2 people instead of 3, you may skip component 4.
- The project is due May 12. No late days are allowed.
- TA's will announce office hours to help people get support during the project. 


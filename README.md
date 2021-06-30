# alpha_flops_dataset
A dataset comparing flops and execution time for different Convolutional layers

This repository contains the data used in the article "Dissecting FLOPs along input dimensions for GreenAI cost estimations", accepted for presentation at the 7th International Conference on Machine Learning, Optimization and Data Science (LOD 2021), October 4 – 8, 2021 Grasmere, Lake District, England – UK. It is a joint work between me, Davide Evangelista and Moreno Marzolla.

Raw data are tuples of the form [H,W,Cin,Cout,K1,K2,T] where H is the Height, W is the Width, Cin is the number of input channels, Cout is the number of output channels, K1 and K2 are the kernel dimensions, and T is the execution time. The exection time has been measured as an average over 2000 different executions.

These data are organized in "PLOTS", in order to allow a simple generation of relevant diagrams. The plots correspond to the figures in the article.
Typically each plot is a collection of "lines", growing along a specific dimension (or a combination of them). Along the y-axes we always have time.
The precise structure of each plot is detailed in the following section.


# the strucure of plots
Each plot is a python dictionary composed by the following entries:

- 

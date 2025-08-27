---
paper: https://arxiv.org/abs/2107.11949
repository: https://github.com/asperti/alpha_flops_dataset/
---

# alpha_flops_dataset
A dataset comparing flops and execution time for different Convolutional layers

This repository contains the data used in the article "Dissecting FLOPs along input dimensions for GreenAI cost estimations", accepted for presentation at the 7th International Conference on Machine Learning, Optimization and Data Science (LOD 2021), October 4 – 8, 2021 Grasmere, Lake District, England – UK. It is a joint work between me, Davide Evangelista and Moreno Marzolla.

Raw data are tuples of the form [H,W,Cin,Cout,K1,K2,T] where H is the Height, W is the Width, Cin is the number of input channels, Cout is the number of output channels, K1 and K2 are the kernel dimensions, and T is the execution time. The exection time has been measured as an average over 2000 different executions.

These data are organized in "PLOTS", in order to allow a simple generation of relevant diagrams. The plots correspond to the figures in the article.
Typically each plot is a collection of "lines", growing along a specific dimension (or a combination of them). Along the y-axis we always have time.
All plots are contained in data.pickle. The precise structure of each plot is detailed in the following section.


# The structure of plots
Each plot is a python dictionary composed by the following entries:

- name: a short descriptive name of the plot
- no_lines: number of lines composing the plot
- axis: this could either be a number, specifing the growing dimension among [H,W,Cin,Cout,K1,K2] or the special keyword 'progressive'.
 - x_axis_name: the name to associate with the x-axis
 - ylim: the limit fot the y-axis (could be None)
 - text: a list of textual informations to be added to the drawing. Each textual info is a tuple (x,y,s) where x and y are the coordinate and s is the string
 - lines: this is a list of "lines", with a number equal to no_lines. Each line, is an ordered list of tuples of the kind described in the previous section, typically increasing along the specified 'axis'of the second point 
 - hardware: this field contains informations about the hardware used to acquire data. In particular, we give the GPU type (e.g. 'Quadro T2000'), its computeCapability, the coreClock frequency (in GHz), and the coreCount.

# Plotting facilities
In addition to PLOTS we also provide a simple plotting code to draw diagrams starting form the plot infromations desscribed above. The plotting function also accept as
inut an additional "predict" argument, that can be instantiated with your own prediction, and will be depicted with a black dashed line.

# Just data
This repository only contains data and plotting facilities. We do not provide the obvious code for timing execution, of for regression over data.

import numpy as np
import matplotlib.pyplot as plt
import pickle

##############################

data_file = 'data.pickle'

def data_load():
    with open(data_file, 'rb') as f:
        return pickle.load(f)

data = data_load()

def print_plots_names():
    for pl in data['plots']:
        print(pl['name'])

def plot_plot(p,lines=None,predict=None, save_as=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    if p['ylim']:
        plt.ylim(0, p['ylim'])

    if not(lines):
        lines = list(range(p["no_lines"]))
    for line in lines:
        vals = p['lines'][line]
        if p['axis']=='progressive':
            x_vals = np.sqrt(np.prod(vals[:,0:6],axis=1)/10000)
        else:
            x_vals = vals[:,p['axis']]
        y_vals = vals[:, 6]
        ax.plot(x_vals, y_vals)
        if predict:
            p_vals = predict(vals)
            ax.plot(x_vals, p_vals,"k--")
    for (xs,ys,s) in p['text']:
        plt.text(xs,ys,s)
    ax.set_xlabel(p['x_axis_name'])
    ax.set_ylabel('Milliseconds')
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
    plt.show()

################## alpha flops ######################

# The function mypredict compute the alpha-flops correction accoridng to the formula given in the article
# "Dissecting FLOPs along input dimensions for GreenAI cost estimations" accepted for presentation at the
# the 7th International Online & Onsite Conference on Machine Learning, Optimization, and Data Science –
# October 4 – 8, 2021 – Grasmere, Lake District, England – UK

# we distinguish only two cases for K, namely K=1 and K>1.
# if K=1, beta is 0.02 and gamma is .99
# if K>1, then beta is 0.001 and gamma is .56
# This values have been obtained by regression over the dataset

def beta_gamma(K):
    Kis1 = K == 1
    beta = Kis1 * 0.02 + (1 - Kis1) * 0.001
    gamma = Kis1 * .99 + (1 - Kis1) * .56
    return beta,gamma

final = 0.0375

def mypredict(vals,print_prediction=False):
    D = np.prod(vals[:,0:2],axis=1)
    K = np.prod(vals[:,4:6],axis=1)
    C = np.prod(vals[:,2:4],axis=1)
    beta,gamma = beta_gamma(K)
    FLOPS = C * K * D / 1000000
    #logK = tf.math.log(K) + 1
    logK = np.log(K) +1
    x = beta * (D - logK)
    x = (logK + x) / D
    #x = tf.math.log(x)
    x = np.log(x)
    x = gamma * x
    #x = final * tf.math.exp(x)
    x = final * np.exp(x)
    Ypred = x * FLOPS
    if print_prediction:
        for i in range(0,Ypred.shape[0]):
            print("predicted = {}; actual = {}".format(Ypred[i],vals[i,6]))
    return(Ypred)

#################################################################
# Actual plotting.
# Predictions are plotted with dashed lines

plots = data["plots"]

plot_plot(plots[0],predict=mypredict) #av,se_as="PLOTS/plot1")
plot_plot(plots[1],predict=mypredict) #,save_as="PLOTS/plot2")
plot_plot(plots[2],predict=mypredict) #,save_as="PLOTS/plot3")
plot_plot(plots[3],predict=mypredict) #,save_as="PLOTS/plot4")  #K=1
plot_plot(plots[4],predict=mypredict) #,save_as="PLOTS/plot5")
plot_plot(plots[5],predict=mypredict) #,save_as="PLOTS/plot6_K1") #K=1
plot_plot(plots[6],predict=mypredict) #,save_as="PLOTS/plot11")
plot_plot(plots[7],predict=mypredict) #,save_as="PLOTS/dense_vs_batch") #K = 1





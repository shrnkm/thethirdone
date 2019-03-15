Statistical Dependence
----------------------
If a random variable, called X, could give any information about another random variable, say Y, we consider them dependent. The dependency of two random variables means knowing the state of one will affect the probability of the possible states of the other one. In the same way, the dependency of a random variable could be passed and also defined for a probability distribution.
Investigating a possible dependancy between two random variables is a difficult task. A more specific and more difficult task is to determine the level of that dependency. There are two main categories of techniques for measuring statistical dependency between two random variables. The first category mainly deals with the linear dependency and includes basic techniques like the Pearson Correlation and the Spearman’s Measure. But these techniques do not have a good performance measuring nonlinear dependencies which are more frequent in data.
The second category, however, include general techniques that cover nonlinear dependencies, as well.
</br> 
</br> 
</br> 

**1. Distance Correlation**

Distance correlation (dCor) is a nonlinear dependence measure and it can handle random variables with arbitrary dimensions. Not surprisingly, dCor works with the distance; the Euclidean distance. Assume we have two random variables X and Y. The first step is to form their corresponding transformed matrices, TMx and TMy. Then we calculate the distance covariance:

![](https://user-images.githubusercontent.com/27868570/51983505-1ad0d280-2499-11e9-9890-bfaf186753c3.png)

</br> 

And finally, we calculate the squared dCor value as follows:

![](https://user-images.githubusercontent.com/27868570/51983850-0e00ae80-249a-11e9-9751-908f8e677a49.png)
</br> 


The dCor value is a real number between 0 and 1 (inclusively), and 0 means that the two variables are independent.

</br> 
</br> 
</br> 

**2. Mutual Information**

Mutual information (MI) is a general measure of dependance based on the core concept of information theory, 'entropy.' Entropy is a measure of uncertainty, and is formulated based on the average 'information content' of a set of possible outcomes of an event, which is in turn, a measure of information.

Information content of the outcome x with probability P(x):

![](https://user-images.githubusercontent.com/27868570/52379671-6c65f800-2a6b-11e9-97b2-0dd7e05b510c.png)
</br> 


Entropy of an event with N outcomes with pribabilities P1...Pn:

![](https://user-images.githubusercontent.com/27868570/52380294-87396c00-2a6d-11e9-8d82-acba394783db.png)
</br> 

Mutual information is a symmetric relation between two variables and it indicates the amount of information that one random variable reveals about the other. Or in other words the reduction of uncertainty about a variable, resulted from our knowledge about another one:

![](https://user-images.githubusercontent.com/27868570/52527839-a0d9ee00-2ccf-11e9-9d48-e29b53a1f688.png)


Mutual information is a symmetric and non negative value. And a zero MI means two independent variables.
</br> 



Calculating MI for discrete valued variables is somewhat easy, the problem arises when we try to calculate MI, or in fact the entropy itself, for variables with real, continuous values. For working under this condition, we use the other version of MI formula which is a specific form of the more general form of Kullback-Leibler divergence and works on Probability Density Function (PDF) of joint probabilities:

![](https://user-images.githubusercontent.com/27868570/52519670-42752700-2c5f-11e9-97f6-7630757d8bff.png)
</br> 

 
However, the need for knowing PDF is another problem. In practice, we usually have access to a finite set of data spamles, and not the PDF they are representing. So before being able to calculate MI, or in essence entropy, we need to approximate the PDF itself. In this sense, the problem of estimating MI reduces to the problem of estimating PDF. In fact, most of MI estimators start with PDF estimation procedure. There are two main groups of MI estimators: parametric and non-parametric estimators. Parametric estimators are the ones that assume the probability density could be modelled with one of the most frequent distributions like Gaussian. Non-parametric estimators assume nothing about the hidden PDF.

The main approaches for estimating MI, in a non-parametric way, are methods based on histogram, adaptive partitioning, kernel density, k-nearest neighbor, B-spline, wavelet density, and nonlinear correlation coefficient.
</br> 
</br> 
</br> 

**2.1. Histogram-based Estimation**

Using a histogram is a simple, neat, and popular approach for MI estimation, which is computationally easy and efficient: we discretize the distribution into *N* number of bins, count the number of occurrences of smaples per bin. The number of bins is an arbitrary option, best decided on, cosidering the nature of our data. Using bins with constant width make our estimation too senstivie to the that arbitrary number of *N* which could lead ignoring some meaningful patterns in our data, only because some samples were interpreted within two neighboring, instead of one single bin. That is, constant bins number or their width is not sensitive to the changes in data stream, and therfore, not as efficient as the histogram estimation could potentially be. So another way is to focus on the bins width ratehr than their number and try to define them variably. This approach will reduce the estimation error, but would increase the complexity of the computation by adding a new probelm of how to dicide about the changing bin-width and how to implement the decision.

![](https://media.springernature.com/original/springer-static/image/art%3A10.1007%2Fs10700-014-9178-0/MediaObjects/10700_2014_9178_Fig10_HTML.gif)

*An example of using histogram estimation. Haeri, M. A., & Ebadzadeh, M. M. (2014). Estimation of mutual information by the fuzzy histogram. Fuzzy Optimization and Decision Making, 13(3), 287-318.*
</br> 
</br> 
</br> 


**2.2. Adaptive Partitioning**

Adaptive partitioning, as it is clear from its name, is another way of dividing data space into subsets and subsequent counting of the covered occurrences. The new thing about adaptive partitioning is that it does not confine itself to classic histogram bins, rather it feels free to use different-sized rectangular tiles to cover the data space in a way that increase the conditional independance between partitions. Partitioning is done through an iterative procedure in which after each step, the conditional independence of each tile regarding the other partitions will be examined using Chi-square statistical test.

![](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2Fs12918-017-0458-5/MediaObjects/12918_2017_458_Fig1_HTML.gif)

*An example of adaptive partitioning procedure. He, J., Zhou, Z., Reed, M., & Califano, A. (2017). Accelerated parallel algorithm for gene network reverse engineering. BMC systems biology, 11(4), 83.*

</br> 
</br> 
</br> 

**2.3. Kernel Density Estimation (KDE)**

Kernel density estimation, outperforms both histogram and adaptive partitioning methods, in accuracy. But, not surprisingly, it is computationally a heavier and slower method. The main difference and advantage of KDE is its tolerance in partitioning. KDE not only does not restrict itself to rectangular, so to say, bins or any specific point in data space as the origin, and it also does not use strict lines at borders. What it uses is a kernel with an arbitrary width. This arbitrariness, again, is a weakness and makes the resulted PDF sensitive to the decision on the kernel width.
In the next step, KDE calculates one of different possible probability densities including Gaussian, Rectangualr, and Epanechnikov around each data samples, add them up together to obtain a smooth PDF over all data samples from the superposition of these kernels. The resulted PDF is of high quality because of a smaller MSE rate.

![](http://4.bp.blogspot.com/-WIaKAWGI5eY/UVl2EufeQLI/AAAAAAAAAPQ/OocN9rEiCh0/s1600/KDEWIKI.png)

*Implementing KDE. http://daveakshat.blogspot.com/2013/04/convolution-probabilty-density.html)*

</br> 
</br> 
</br> 


**2.4. B-Spline**
</br> 
</br> 
</br> 

**2.5. K-Nearest Neighbor (KNN)**
</br> 
</br> 
</br> 

**2.6. Wavelet Density Estimator (WDE)**
</br> 
</br> 
</br> 

**2.7. Nonlinear Correlation Coefficient (NCC)**
</br> 
</br> 
</br> 



**3. Maximal Information Coefficient**
</br> 
</br> 
</br> 




How does 'Statistical Dependance' help understanding deep learning?
-------------------------------------------------------------------------------- 

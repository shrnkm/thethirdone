Statistical Dependence
----------------------
If a random variable, called X, could give any information about another random variable, say Y, we consider them dependent. The dependency of two random variables means knowing the state of one will affect the probability of the possible states of the other one. In the same way, the dependency of a random variable could be passed and also defined for a probability distribution.
Investigating a possible dependancy between two random variables is a difficult task. A more specific and more difficult task is to determine the level of that dependency. There are two main categories of techniques for measuring statistical dependency between two random variables. The first category mainly deals with the linear dependency and includes basic techniques like the Pearson Correlation and the Spearman’s Measure. But these techniques do not have a good performance measuring nonlinear dependencies which are more frequent in data.
The second category, however, include more general techniques that also cover nonlinear dependencies.
</br> 
</br> 
</br> 

**Distance Correlation**

Distance correlation (dCor) is a nonlinear dependence measure and it can handle random variables with arbitrary dimensions. Not surprisingly, dCor works with the distance; the Euclidean distance. Assume we have two random variables X and Y. The first step is to form their corresponding transformed matrices, TMx and TMy. Then we calculate the distance covariance:

![](https://user-images.githubusercontent.com/27868570/51983505-1ad0d280-2499-11e9-9890-bfaf186753c3.png)

</br> 
</br> 
</br> 

And finally, we calculate the squared dCor value as follows:

![](https://user-images.githubusercontent.com/27868570/51983850-0e00ae80-249a-11e9-9751-908f8e677a49.png)
</br> 
</br> 
</br> 

The dCor value is a real number between 0 and 1 (inclusively), and 0 means that the two variables are independent.

</br> 
</br> 
</br> 

**Mutual Information**

Mutual information (MI) is a measure of dependance based on the core concept of information theory, 'entropy.' Entropy is a measure of uncertainty, and is formulated based on the average 'information content' of a set of possible outcomes of an event, which is, in turn, a measure of information.

Information content of the outcome x with probability P(x):

![](https://user-images.githubusercontent.com/27868570/52379671-6c65f800-2a6b-11e9-97b2-0dd7e05b510c.png)
</br> 
</br> 
</br> 

Entropy of an event with N outcomes with pribabilities P1...Pn:

![](https://user-images.githubusercontent.com/27868570/52380294-87396c00-2a6d-11e9-8d82-acba394783db.png)
</br> 
</br> 
</br> 

Mutual information between two random variables is defined as follows:

![](https://user-images.githubusercontent.com/27868570/52519670-42752700-2c5f-11e9-97f6-7630757d8bff.png)
</br> 
</br> 
</br> 

Mutual information is a symmetric relation between two variables and it indicates the amount of information that one random variable reveals about the other. Or in other words:

![](https://user-images.githubusercontent.com/27868570/52527839-a0d9ee00-2ccf-11e9-9d48-e29b53a1f688.png)
</br> 
</br> 
</br> 

Mutual information is a symmetric and non negative value. And a zero MI means two independent variables.
</br> 
</br> 
</br> 
 
Calculating MI for discrete variables is somewhat easy, the problem arises when we try to calculate MI for a continuous variable; when we need to work with probability density function.
</br> 
</br> 
</br> 
 

**Estimating Mutual Information for ** 
</br> 
</br> 
</br> 
 
**Maximal Information Coefficient**
</br> 
</br> 
</br> 




How does 'Statistical Dependance' help understanding deep learning?
-------------------------------------------------------------------------------- 

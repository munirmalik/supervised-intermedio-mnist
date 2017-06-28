#MNIST
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from time import time
from sklearn import datasets, svm, metrics
from sklearn.datasets import fetch_mldata
from numpy import arange
from sklearn.model_selection import train_test_split
from dataget import data
#Read image input as vector or matrix

#Train algorithm using data from data/training-set

#Get data
dataset = data("mnist").get()
#Format training_set
features_train, labels_train = dataset.training_set.arrays()
features_train = features_train.reshape((60000, 28*28))
#print("Features shape: {} \nLabels shape: {}".format(features_train.shape, labels_train.shape))

#Format test_set
features_test, labels_test = dataset.test_set.arrays()
features_test = features_test.reshape((10000, 28*28))
#print("Features shape: {} \nLabels shape: {}".format(features_test.shape, labels_test.shape))


def kClassify(features_train,labels_train):
	clf=KNeighborsClassifier(n_neighbors=2,algorithm='brute',leaf_size=7)
	t0 = time()
	clf.fit(features_train,labels_train)
	print "training time:", round(time()-t0, 3), "s"

	return clf

t0=time()
#print features_train.shape, labels_train.shape
clf=kClassify(features_train,labels_train)


pred= clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"



#accuracy
accuracy = metrics.accuracy_score(labels_test,pred)
print "Accuracy is", accuracy

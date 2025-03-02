import numpy as np 
import pandas as pd
from .models import Myrating
import scipy.optimize 


def Myrecommend():
	def normalizeRatings(myY, myR):
	   	# The mean is only counting books that were rated
		# np.seterr(divide='ignore', invalid='ignore')
		Ymean = np.sum(myY,axis=1)/np.sum(myR,axis=1)
		Ymean = Ymean.reshape((Ymean.shape[0],1))
		return myY-Ymean, Ymean
			
	def flattenParams(myX, myTheta):
		return np.concatenate((myX.flatten(),myTheta.flatten()))

    
	def reshapeParams(flattened_XandTheta, mynm, mynu, mynf):
		assert flattened_XandTheta.shape[0] == int(mynm*mynf+mynu*mynf)
		reX = flattened_XandTheta[:int(mynm*mynf)].reshape((mynm,mynf))
		reTheta = flattened_XandTheta[int(mynm*mynf):].reshape((mynu,mynf))
		return reX, reTheta

	def cofiCostFunc(myparams, myY, myR, mynu, mynm, mynf, mylambda = 0.):
		myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
		term1 = myX.dot(myTheta.T)
		term1 = np.multiply(term1,myR)
		cost = 0.5 * np.sum( np.square(term1-myY) )
    	# for regularization
		cost += (mylambda/2.) * np.sum(np.square(myTheta))
		cost += (mylambda/2.) * np.sum(np.square(myX))
		return cost

	def cofiGrad(myparams, myY, myR, mynu, mynm, mynf, mylambda = 0.):
		myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
		term1 = myX.dot(myTheta.T)
		term1 = np.multiply(term1,myR)
		term1 -= myY
		Xgrad = term1.dot(myTheta)
		Thetagrad = term1.T.dot(myX)
    	# Adding Regularization
		Xgrad += mylambda * myX
		Thetagrad += mylambda * myTheta
		return flattenParams(Xgrad, Thetagrad)

	df = pd.DataFrame(list(Myrating.objects.all().values('id', 'user_id', 'product_id', 'rating')))
	if df.empty:
		return np.array([]), np.array([])  # Return empty arrays if no ratings exist

	mynu = df['user_id'].nunique()

	mynm = df['product_id'].nunique()
	
	mynf=8
	
	Y=np.zeros((mynm,mynu))	
	
	for row in df.itertuples():
		Y[row.product_id - 1, row.user_id - 1] = row.rating

	R=np.zeros((mynm,mynu))

	R = (Y != 0).astype(int)  # More efficient way to create R matrix


	Ynorm, Ymean = normalizeRatings(Y,R)
	X = np.random.rand(mynm,mynf)
	Theta = np.random.rand(mynu,mynf)
	myflat = flattenParams(X, Theta)
	mylambda = 12.2
	result = scipy.optimize.fmin_cg(cofiCostFunc,x0=myflat,fprime=cofiGrad,args=(Y,R,mynu,mynm,mynf,mylambda),maxiter=40,disp=True,full_output=True)
	resX, resTheta = reshapeParams(result[0], mynm, mynu, mynf)
	prediction_matrix = resX.dot(resTheta.T)
	return prediction_matrix,Ymean
	





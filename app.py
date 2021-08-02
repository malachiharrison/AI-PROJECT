# core pkgs
import streamlit as st 

# EDA pkgs
import pandas as pd
import numpy as np

# pickle pkg
import pickle

# main function
def main():
	pickle_in = open('sickness_classifier.pkl', 'rb')
	classifier = pickle.load(pickle_in)

	st.title('Artificial Intelligence End of Semester Project')
	menu = ['Tutorial','Model']
	choice = st.sidebar.selectbox('Main Menu',menu)

	if choice == 'Tutorial':
		st.header('Welcome to the Web Application Tutorial')
		st.write('''
			Hello everyone welcome to my web application which
			''')
	elif choice == 'Model':
		st.header('Welcome to (Project Purpose)')
		age = st.number_input('age',1)
		sex = st.number_input('sex',1)
		cp = st.number_input('cp',1)
		trestbps = st.number_input('trestbps',1)
		chol = st.number_input('chol',1)
		fbs = st.number_input('fbs',1)
		restecg = st.number_input('restecg',1)
		thalach = st.number_input('thalach',1)
		exang = st.number_input('exang',1)
		oldpeak = st.number_input('oldpeak',1)
		slope = st.number_input('slope',1)
		ca = st.number_input('ca',1)
		thal = st.number_input('thal',1)


		arr = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
		prediction = classifier.predict(arr)
		if st.button('Predict'):
			if prediction == 1:
				st.success('According to the given symptoms the patient in question has a DISEASE')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))
				# st.
			elif prediction == 0:
				st.success('According to the given symptoms the patient in question has NO DISEASE')
				accuracy = classifier.score(arr,prediction)
				st.success('Accuracy is {}'.format(accuracy))

if __name__ == '__main__':
	main()




# 	Pkl_Filename = "Customer_churn_classifier.pkl"  

# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(model, file)

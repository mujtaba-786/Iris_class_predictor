import streamlit as st
import pickle
from PIL import Image



lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svm=pickle.load(open('svm.pkl','rb'))

def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Virginica'
def main():
    img=Image.open('iris.jpg')
    slt.sidebar.image(img)


    slt.title('IRIS CLASS PREDICTOR')
    activities=['Linear Regression','Logistic Regression','SVM']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    slt.sidebar.info('Below is the link for wikipedia of iris')
    slt.sidebar.success('https://en.wikipedia.org/wiki/Iris_(plant)')

    sepal_length=slt.number_input('LENGTH OF SEAL',  min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    sepal_width=slt.number_input('WIDTH OF SEPAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    petal_length=slt.number_input('LENGTH OF PETAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    petal_width=slt.number_input('WIDTH OF PETAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    inputs=[[sepal_length,sepal_width,petal_length,petal_width]]
    if st.button('Classify'):
        if option=='Linear Regression':
            st.success(classify(lin_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))
        else:
           st.success(classify(svm.predict(inputs)))


if __name__=='__main__':
    main()

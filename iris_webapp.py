import streamlit as slt
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
#     slt.markdown('<style>body{background-color: Green;}</style>',unsafe_allow_html=True)
    img=Image.open('irisImage.jpg')
    slt.sidebar.image(img)
#     img1=Image.open('diabetesimage.jpg')
#     slt.sidebar.image(img1)
    


    slt.title('1. IRIS CLASS PREDICTOR')
    activities=['Linear Regression','Logistic Regression','SVM']
    option=slt.sidebar.selectbox('Which model would you like to use?',activities)
    slt.sidebar.info('Below is the link for wikipedia of iris')
    slt.sidebar.success('https://en.wikipedia.org/wiki/Iris_(plant)')
    img1=Image.open('diabetesimage.jpg')
    slt.sidebar.image(img1)

    sepal_length=slt.number_input('LENGTH OF SEPAL',  min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    sepal_width=slt.number_input('WIDTH OF SEPAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    petal_length=slt.number_input('LENGTH OF PETAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    petal_width=slt.number_input('WIDTH OF PETAL', min_value=0.0, max_value=20.0,value=4.0, step=0.1)
    inputs=[[sepal_length,sepal_width,petal_length,petal_width]]
    if slt.button('Classify'):
        if option=='Linear Regression':
            slt.success(classify(lin_model.predict(inputs)))
            classIris=classify(lin_model.predict(inputs))
            if classIris=='Setosa':
                slt.text('BELOW IS THE IMAGE OF IRIS SETOSA')
                img1=Image.open('irisSetosa.jpeg')
                slt.image(img1)
                slt.text('Iris setosa, the bristle-pointed iris, is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada (including British Columbia, Newfoundland, Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, Korea and southwards to Japan. The plant has tall branching stems, mid green leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. There are also plants with pink and white flowers.')
            elif classIris=='Versicolor':
                slt.text('BELOW IS THE IMAGE OF IRIS VERSICOLOR')
                img1=Image.open('irisVersicolor.jpg')
                slt.image(img1)
                slt.text('Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris. It is a species of Iris native to North America, in the Eastern United States and Eastern Canada.')
            else:
                slt.text('BELOW IS THE IMAGE OF IRIS VIRGINICA')
                img1=Image.open('irisVirginica.jpg')
                slt.image(img1)
                slt.text('Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America. It is common along the coastal plain from Florida to Georgia in the Southeastern United States.')
                
        elif option=='Logistic Regression':
            slt.success(classify(log_model.predict(inputs)))
            classIris=classify(lin_model.predict(inputs))
            if classIris=='Setosa':
                slt.text('BELOW IS THE IMAGE OF IRIS SETOSA')
                img1=Image.open('irisSetosa.jpeg')
                slt.image(img1)
                slt.text('Iris setosa, the bristle-pointed iris, is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada (including British Columbia, Newfoundland, Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, Korea and southwards to Japan. The plant has tall branching stems, mid green leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. There are also plants with pink and white flowers.')
            elif classIris=='Versicolor':
                slt.text('BELOW IS THE IMAGE OF IRIS VERSICOLOR')
                img1=Image.open('irisVersicolor.jpg')
                slt.image(img1)
                slt.text('Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris. It is a species of Iris native to North America, in the Eastern United States and Eastern Canada.')
            else:
                slt.text('BELOW IS THE IMAGE OF IRIS VIRGINICA')
                img1=Image.open('irisVirginica.jpg')
                slt.image(img1)
                slt.text('Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America. It is common along the coastal plain from Florida to Georgia in the Southeastern United States.')
        else:
            
            slt.success(classify(svm.predict(inputs)))
            classIris=classify(lin_model.predict(inputs))
            if classIris=='Setosa':
                slt.text('BELOW IS THE IMAGE OF IRIS SETOSA')
                img1=Image.open('irisSetosa.jpeg')
                slt.image(img1)
                slt.text('Iris setosa, the bristle-pointed iris, is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada (including British Columbia, Newfoundland, Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, Korea and southwards to Japan. The plant has tall branching stems, mid green leaves and violet, purple-blue, violet-blue, blue, to lavender flowers. There are also plants with pink and white flowers.')
            elif classIris=='Versicolor':
                slt.text('BELOW IS THE IMAGE OF IRIS VERSICOLOR')
                img1=Image.open('irisVersicolor.jpg')
                slt.image(img1)
                slt.text('Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris. It is a species of Iris native to North America, in the Eastern United States and Eastern Canada.')
            else:
                slt.text('BELOW IS THE IMAGE OF IRIS VIRGINICA')
                img1=Image.open('irisVirginica.jpg')
                slt.image(img1)
                slt.text('Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America. It is common along the coastal plain from Florida to Georgia in the Southeastern United States.')
    
#         slt.sidebar.image(img)
    slt.title('2. DIABETES PREDICTION')
    age =           slt.number_input("Age in Years", 1, 150, 25, 1)
    pregnancies =   slt.number_input("Number of Pregnancies", 0, 20, 0, 1)
    glucose =       slt.slider("Glucose Level", 0, 200, 25, 1)
    skinthickness = slt.slider("Skin Thickness", 0, 99, 20, 1)
    bloodpressure = slt.slider('Blood Pressure', 0, 122, 69, 1)
    insulin =       slt.slider("Insulin", 0, 846, 79, 1)
    bmi =           slt.slider("BMI", 0.0, 67.1, 31.4, 0.1)
    dpf =           slt.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)
#     row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]
    if (slt.button('Find Health Status')):
#             feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
#             sc, model = load('models/scaler.joblib', 'models/model.joblib')
#             result = inference(row, sc, model, feat_cols)
#             if int(result)==0:
#                 slt.success('You do not have diabetes')
#             else:
        slt.success('You have diabetes')

    
        
        

if __name__=='__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

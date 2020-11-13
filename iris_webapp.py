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
    img=Image.open('irisImage.jpg')
    slt.sidebar.image(img)


    slt.title('IRIS CLASS PREDICTOR')
    activities=['Linear Regression','Logistic Regression','SVM']
    option=slt.sidebar.selectbox('Which model would you like to use?',activities)
    slt.sidebar.info('Below is the link for wikipedia of iris')
    slt.sidebar.success('https://en.wikipedia.org/wiki/Iris_(plant)')

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
        slt.sidebar.image(img)
        slt.title('DIABETES PREDICTION')
        
        

if __name__=='__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

import pandas as pd


file = pd.read_csv('C:\\Users\\ASUS\\Desktop\\samplecsvdata.csv')
dataframe1 = pd.DataFrame(file,columns=['col1','col2','col3','col4','col5','col6','col7','col8','col9'])
data_as_dict = dataframe1.to_dict(orient='list')

print(data_as_dict.keys())
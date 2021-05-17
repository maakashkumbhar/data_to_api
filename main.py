import pandas as pd
import xlrd as xs
import os
import openpyxl
from flask import Flask,jsonify
app = Flask(__name__)



def convert_data(data):
    pass



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/excel_data_api')
def excelDataToAPI():
    ##Reading the exccel file and extracting the data
    file = pd.ExcelFile('C:\\Users\\ASUS\\Desktop\\Book1.xlsx')

    # print(file.sheet_names)

    df1 = file.parse('Sheet1')
    # print(df1)

    #########################
    dataf1 = pd.DataFrame(df1)
    data_as_a_dict = dataf1.to_dict(orient='list')
    convert_data(data_as_a_dict)
    return jsonify(data_as_a_dict)



@app.route('/csv_data_api')
def csv_data_api():
    file = pd.read_csv('C:\\Users\\ASUS\\Desktop\\samplecsvdata.csv')
    dataframe1 = pd.DataFrame(file)
    data_as_dict = dataframe1.to_dict(orient='list')
    json_csv = jsonify(data_as_dict)

    return json_csv

if __name__ == '__main__':
    app.run(debug=True)
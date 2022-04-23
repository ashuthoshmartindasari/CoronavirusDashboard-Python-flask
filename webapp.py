#importing libraries
from flask import Flask, render_template, request, jsonify
import json
import requests
import certifi
from pymongo import MongoClient
import time
import pandas as pd


app = Flask(__name__)
summary_url_temp="https://api.covid19api.com/summary" #api link


client = MongoClient("mongodb+srv://ashuthosh:test@ashuthoshcluster.wzfht.mongodb.net", tlsCAFile=certifi.where())
db = client.get_database('db')
records = db.data
x = records.find()


# def sort_dict_by_value(d, reverse = False):
#     return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse)[:10])



# @app.route('/home', methods=['GET','POST'])
# def home():
    
#     while True:
#         for stats in x:
#             Global=stats["Global"]
#             new_deaths= Global["NewDeaths"]
#             total_deaths=Global["TotalDeaths"]
#             new_cases= Global["NewConfirmed"]
#             total_cases=Global["TotalConfirmed"]
#             new_recovered= Global["NewRecovered"]
#             total_recovered=Global["TotalRecovered"]
#             updated=stats["Date"]

#             return render_template("index.html", date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)

@app.route('/', methods=['GET','POST'])
def home():
    
    data = {'Task' : 'Hours per Day', 
    'Work' : 22, 'Eat' : 4, 'Commute' : 6, 
    'Watching TV' : 5, 'Sleeping' : 15}
    
    for stats in x:
        Global=stats["Global"]
        new_deaths=Global["NewDeaths"]
        total_deaths=Global["TotalDeaths"]
        new_cases=Global["NewConfirmed"]
        total_cases=Global["TotalConfirmed"]
        new_recovered=Global["NewRecovered"]
        total_recovered=Global["TotalRecovered"]
        updated=stats["Date"]

    # for dataset in x:
    #     dataset_list.append(dataset)  
    # for data in dataset_list:
    #     final_data = data['Countries']
    #     for i, record in enumerate(final_data):
    #         inner_dict[record['Country']] = record['TotalConfirmed']
    #         outer_dict[i] = inner_dict

    # needed_data = sort_dict_by_value(inner_dict, True)
    
    # #converts dictionary to list
    # finalresultlist = []
    # for key, value in needed_data.items():
    #     temp = [key,value]
    #     finalresultlist.append(temp)

    
    return render_template('index.html', date=updated, nd_n=new_deaths, td_n=total_deaths,nc_n=new_cases,tc_n=total_cases,nr_n=new_recovered, tr_n=total_recovered)


# @app.route('/bar')
# def for_bar_chart():
    
#     for dataset in x:
#         dataset_list.append(dataset)  
#     for data in dataset_list:
#         final_data = data['Countries']
#         for i, record in enumerate(final_data):
#             inner_dict[record['Country']] = record['TotalConfirmed']
#             outer_dict[i] = inner_dict

#     # needed_data = sort_dict_by_value(inner_dict, True)
#     # needed_data['Country'] = 'TotalConfirmed'

#     return render_template('index.html', rates=inner_dict)


    
if __name__=="__main__":
    dataset_list = list()
    inner_dict = {}
    outer_dict = {}
    app.run(port=5085, debug="true")


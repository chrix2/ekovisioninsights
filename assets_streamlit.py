from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('ocrekomerciolog-26e07a31b8f7.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ocrekomerciolog-default-rtdb.firebaseio.com/'
})

import pandas as pd
from datetime import datetime


def get_data():
    ref = db.reference('barcodes')
    data_dict={}
    snapshot = ref.order_by_child('barcodes').get()
    for key, val in snapshot.items():
        val['date']=datetime.fromtimestamp(val['timestamp']).strftime("%m/%d/%Y")
        data_dict[key]=val

    log_dataframe = pd.DataFrame.from_dict(data_dict, orient='index')



    ref = db.reference('tickets')
    data_dict2={}
    snapshot = ref.order_by_child('ocr_acc').get()
    for key, val in snapshot.items():
        val['date']=datetime.fromtimestamp(val['timestamp']).strftime("%m/%d/%Y")
        data_dict2[key]=val

    log_dataframe2 = pd.DataFrame.from_dict(data_dict2, orient='index')

    return log_dataframe, log_dataframe2
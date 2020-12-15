import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
from assets_streamlit import get_data

log_dataframe, log_dataframe2 = get_data()
st.title('METRICS & INSIGHTS')
st.sidebar.text("""p.- precision\n
r.- recall\n
f.- f1-score\n\n\n
Valores de 0-100 mientras mas alto mejor""")


col1, col2, col3= st.beta_columns(3)

with col1:
    st.header("NER metrics")
    datos = """{"NETO": {"PROVEEDOR": {"p": 78.84615384615384, "r": 80.3921568627451, "f": 79.61165048543688}, "ORDEN": {"p": 0.0, "r": 0.0, "f": 0.0}, "FECHA": {"p": 88.0, "r": 86.27450980392157, "f": 87.12871287128714}, "SUCURSAL": {"p": 3.6363636363636362, "r": 3.9215686274509802, "f": 3.7735849056603774}, "FOLIO": {"p": 0.0, "r": 0.0, "f": 0.0}}, "FRANCISCOASIS": {"FOLIO": {"p": 94.23076923076923, "r": 95.14563106796116, "f": 94.68599033816425}, "CADENA": {"p": 91.34615384615384, "r": 92.23300970873787, "f": 91.78743961352657}, "TOTAL": {"p": 99.02912621359224, "r": 100.0, "f": 99.51219512195122}, "FECHA": {"p": 97.11538461538461, "r": 97.11538461538461, "f": 97.11538461538461}, "PROVEEDOR": {"p": 92.15686274509804, "r": 91.2621359223301, "f": 91.70731707317074}, "SUCURSAL": {"p": 86.27450980392157, "r": 86.27450980392157, "f": 86.27450980392157}, "NOTA": {"p": 0.9708737864077669, "r": 0.9708737864077669, "f": 0.9708737864077669}}, "BENAVIDES": {"CADENA": {"p": 27.27272727272727, "r": 25.0, "f": 26.08695652173913}, "FOLIO": {"p": 95.18072289156626, "r": 94.04761904761905, "f": 94.61077844311376}, "PROVEEDOR": {"p": 83.15789473684211, "r": 84.94623655913979, "f": 84.04255319148936}, "SUCURSAL": {"p": 18.072289156626507, "r": 17.857142857142858, "f": 17.964071856287426}, "NOTA": {"p": 12.903225806451612, "r": 13.48314606741573, "f": 13.186813186813188}, "FECHA": {"p": 68.83116883116884, "r": 69.73684210526315, "f": 69.28104575163398}}, "DUNOSUSA": {"FOLIO": {"p": 3.0303030303030303, "r": 2.9850746268656714, "f": 3.007518796992481}, "FECHA": {"p": 84.28571428571429, "r": 85.5072463768116, "f": 84.89208633093526}, "CADENA": {"p": 1.4084507042253522, "r": 1.4492753623188406, "f": 1.4285714285714286}, "TOTAL": {"p": 84.05797101449275, "r": 85.29411764705883, "f": 84.67153284671534}, "PROVEEDOR": {"p": 98.55072463768117, "r": 95.77464788732394, "f": 97.14285714285714}, "SUCURSAL": {"p": 88.73239436619718, "r": 92.64705882352942, "f": 90.6474820143885}, "NOTA": {"p": 100.0, "r": 98.55072463768117, "f": 99.27007299270075}, "ORDEN": {"p": 94.20289855072464, "r": 97.01492537313433, "f": 95.58823529411764}}, "7ELEVEN": {"CADENA": {"p": 100.0, "r": 98.30508474576271, "f": 99.14529914529915}, "FOLIO": {"p": 88.13559322033898, "r": 91.22807017543859, "f": 89.6551724137931}, "FECHA": {"p": 93.22033898305084, "r": 87.3015873015873, "f": 90.1639344262295}, "PROVEEDOR": {"p": 84.7457627118644, "r": 84.7457627118644, "f": 84.7457627118644}, "SUCURSAL": {"p": 10.526315789473683, "r": 10.16949152542373, "f": 10.344827586206899}, "NOTA": {"p": 84.48275862068965, "r": 83.05084745762711, "f": 83.76068376068375}, "TOTAL": {"p": 69.0909090909091, "r": 73.07692307692307, "f": 71.02803738317756}}, "FARMACIASGUADALAJARA": {"CADENA": {"p": 100.0, "r": 100.0, "f": 100.0}, "TOTAL": {"p": 75.0, "r": 75.0, "f": 75.0}, "FOLIO": {"p": 100.0, "r": 100.0, "f": 100.0}, "FECHA": {"p": 100.0, "r": 100.0, "f": 100.0}, "PROVEEDOR": {"p": 100.0, "r": 100.0, "f": 100.0}, "SUCURSAL": {"p": 60.0, "r": 60.0, "f": 60.0}, "NOTA": {"p": 100.0, "r": 100.0, "f": 100.0}, "ORDEN": {"p": 100.0, "r": 100.0, "f": 100.0}}, "CASALEY": {"FOLIO": {"p": 100.0, "r": 98.88888888888889, "f": 99.44134078212291}, "FECHA": {"p": 97.77777777777777, "r": 98.87640449438202, "f": 98.32402234636872}, "CADENA": {"p": 56.52173913043478, "r": 57.14285714285714, "f": 56.83060109289616}, "PROVEEDOR": {"p": 94.25287356321839, "r": 94.25287356321839, "f": 94.25287356321839}, "SUCURSAL": {"p": 50.54945054945055, "r": 51.68539325842697, "f": 51.11111111111112}, "NOTA": {"p": 96.875, "r": 96.875, "f": 96.875}, "ORDEN": {"p": 96.07843137254902, "r": 96.07843137254902, "f": 96.07843137254902}, "TOTAL": {"p": 0.0, "r": 0.0, "f": 0.0}}, "CHEDRAUI": {"CADENA": {"p": 100.0, "r": 100.0, "f": 100.0}, "FECHA": {"p": 75.0, "r": 66.66666666666666, "f": 70.58823529411765}, "FOLIO": {"p": 100.0, "r": 100.0, "f": 100.0}, "PROVEEDOR": {"p": 100.0, "r": 100.0, "f": 100.0}, "SUCURSAL": {"p": 88.88888888888889, "r": 88.88888888888889, "f": 88.88888888888889}, "ORDEN": {"p": 100.0, "r": 100.0, "f": 100.0}, "TOTAL": {"p": 0.0, "r": 0.0, "f": 0.0}}}
    """

    datos_dict = json.loads(datos)

    for key, value in datos_dict.items():
        st.write(key)
        st.write(pd.DataFrame.from_dict(value).sort_index(axis=1))

with col2:
    st.header("OCR Insights  ")

    df2 = log_dataframe2.groupby("date").count()
    st.subheader("Receipts Processed Daily")
    st.line_chart(df2)

    import matplotlib.pyplot as plt
    import numpy as np
    # arr = log_dataframe2['ocr_acc']
    # fig, ax = plt.subplots()
    # ax.hist(arr, bins=200)
    # ax.set_xlabel('OCR accuracy')
    # ax.set_ylabel('Frequency')
    # st.subheader("OCR Accuracy Histogram")
    # st.pyplot(fig)
    # st.subheader("OCR Accuracy Stats")
    # st.write(arr.describe(include='all'))

    # import streamlit as st
    # import plotly.figure_factory as ff
    #
    # hist_data = [arr.values.tolist()]
    # group_labels = ['Group 1']
    # fig2 = ff.create_distplot(hist_data, group_labels, bin_size = [1])
    # st.plotly_chart(fig2, use_container_width=True)

    log_dataframe3= log_dataframe2[log_dataframe2.timestamp > 1607800861.025552]

    arr = log_dataframe3['ocr_acc']
    fig, ax = plt.subplots()
    ax.hist(arr, bins=200)
    ax.set_xlabel('OCR accuracy V2')
    ax.set_ylabel('Frequency')
    st.subheader("OCR Accuracy V2 Histogram")
    st.pyplot(fig)
    st.subheader("OCR Accuracy V2 Stats")
    st.write(arr.describe(include='all'))



with col3:
    st.header("Barcode insights")
    df = log_dataframe.groupby("date").count()
    print(df.head)
    st.subheader("Receipts with Barcode Processed Daily")
    st.line_chart(df)

    fig, ax = plt.subplots()
    data = log_dataframe['barcodes'].value_counts()
    points = data.index
    frequency = data.values
    ax.bar(points, frequency)
    ax.set_title('Barcodes')
    ax.set_xlabel('Barcodes found')
    ax.set_ylabel('Frequency')
    st.subheader("Barcodes Detected Distribution")
    st.pyplot(fig)
    st.subheader("Barcodes found Stats")
    st.write(data.describe(include='all'))


















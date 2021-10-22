# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:04:05 2021

@author: 20804
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('AndroApp')


st.markdown('[Zepeng Cui](https://github.com/MichaelCui233?tab=repositories)')

uploaded_file=st.file_uploader('Upload a .csv file',type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    df=df.applymap(lambda x: np.nan if x==' ' else x)
    
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
        
    good_cols=[c for c in df.columns if can_be_numeric(c)]
    
    df[good_cols]=df[good_cols].apply(pd.to_numeric,axis=0)
    
    x_axis=st.selectbox('Choose an x-value',good_cols)
    y_axis=st.selectbox('Choose an y-value',good_cols)
    
    values=st.slider('select the range of rows you would like to plot',0, len(df.index)-1,(0,len(df.index)-1))
    
    st.write(f'Plotting ({x_axis},{y_axis}) with range of rows in {values}')
    
    a=values[0]
    b=values[1]
  
    
    chart=alt.Chart(df.iloc[a:b]).mark_circle().encode(
        x=x_axis,
        y=y_axis,
        #size=values,
        tooltip=[x_axis,y_axis])
    
    st.altair_chart(chart)
    
    if st.button('I like this app'):
        st.write('Thank you!')
    
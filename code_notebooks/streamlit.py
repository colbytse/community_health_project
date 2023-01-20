import pandas as pd
import streamlit as st

fi_f = pd.read_csv('../results/feature_importance_f.csv')
fi_m = pd.read_csv('../results/feature_importance_m.csv')

def feature_lookup(x, gender):
    '''fn takes specific mortality feature "x" and gender to lookup 
    feauture importance with the associated mortality '''
    gender = gender.lower()
    
    if gender == 'male' or gender =='m':
        return fi_m[[x, 'description']][fi_m[x]>0]\
                .sort_values(by=x,ascending=False).head(5)
    elif gender == 'female' or gender == 'f':
        return fi_f[[x, 'description']]\
                [np.abs(fi_f[x])>0]\
                .sort_values(by=x,ascending=False).head(5)
    else:
        return print(f"Please enter a valid input")
    

corr_f = pd.read_csv('../results/mort_full_corrs_df_female.csv')
corr_m = pd.read_csv('../results/mort_full_corrs_df_male.csv')

sex = st.selectbox(
    'For which gender would you like to know more about mortalities?',
    ('Male','Female')
)
mortalities_f = corr_f.columns
mortalities_m = corr_m.columns
    
if sex == 'Male':  
    mort = st.selectbox(
        'Which mortality would you like to investigate?',
        (mortalities_m)
                       )
imp = feature_lookup(mort,sex)
st.dataframe(imp)
# if sex == 'Female':  
#     mort = st.selectbox(
#         'Which mortality would you like to investigate?',
#         (mortalities_f)
#     )
#     imp = feature_lookup(mortalities_f,sex)
#     st.dataframe(imp)





st.write(feature_lookup())
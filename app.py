import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os

#title
st.title("Aadhar Card Data EDA App")

#Sidebar
st.sidebar.header("About App")
st.sidebar.info("This is simple app on EDA of Aadhar Card Data")

st.sidebar.header("Get in touch")
st.sidebar.info("contacttorahulmane@gmail.com")

my_data = 'aadhar.csv' #reading path

#function to load data
@st.cache(persist=True)
def explore_data(data):
    df = pd.read_csv(os.path.join(data), low_memory=True)
    return df

df = explore_data(my_data)

#preview Dataset
if st.checkbox("Preview Dataset"):
    
    if st.button("Head"):
        st.write(df.head())
    if st.button("Tail"):
        st.write(df.tail())


#Show column names
if st.checkbox("Show All Column Names"):
    st.write(df.columns)

#show dimension
df_dim = st.radio("What dimensions do you want to see?", ("Rows", "Columns", "All"))
if df_dim == 'Rows': #for rows
    st.text("Showing all rows")
    st.write(df.shape[0])
if df_dim == 'Columns': #for columns
    st.text("Showing all columns")
    st.write(df.shape[1])
if df_dim == 'All': #for all
    st.text("Shape of Dataset")
    st.write(df.shape)
 

#select column
col_option = st.selectbox("Select column", ('S_District','Rejected','Registrar','Pin Code','Mobile','Generated','Gender','Email','District','Agency','Age', 'State'))

if col_option == 'S_District':
    if st.checkbox("Show unique sub district"):
        st.write(df['S_District'].unique())
    st.write(df['S_District'])

if col_option == 'District':
    if st.checkbox("Show unique District"):
        st.write(df['District'].unique())
    st.write(df['District'])

if col_option == 'State':
    if st.checkbox("Show unique State"):
        st.write(df['State'].unique())
    st.write(df['State'])

if col_option == 'Registrar':
    if st.checkbox("Show unique Registarar"):
        st.write(df['Registrar'].unique())
    st.write(df['Registrar'])

if col_option == 'Pin Code':
    if st.checkbox("Show unique Pin Code"):
        st.write(df['Pin Code'].unique())
    st.write(df['Pin Code'])
    
if col_option == 'Rejected':
    st.write(df['Rejected'])
if col_option == 'Mobile':
    st.write(df['Mobile'])
if col_option == 'Generated':
    st.write(df['Generated'])
if col_option == 'Gender':
    st.write(df['Gender'])
if col_option == 'Email':
    st.write(df['Email'])
if col_option == 'Agency':
    st.write(df['Agency'])
if col_option == 'Age':
    st.write(df['Age'])


#check is there any null values
if st.checkbox("How many null values dataset has?"):
    st.write(df.isnull().sum().sum(),"Null values are in the dataset.")

explode=(0.2, 0.0) #explode values for pie chart

if st.checkbox("What percentage of aadhar card generated?"):
    plt.figure()
    percent_of_aadhar_generated = np.round((df[df['Generated'] == 1]['Generated'].sum() / df['Generated'].count()) * 100)                       
    values = [percent_of_aadhar_generated, 100-percent_of_aadhar_generated]
    labels = ['Generated', 'Not Generated']
    a = plt.pie(values, autopct='%1.1f%%', explode=explode,labels=labels)
    plt.title("What percentage of aadhar card generated?")
    st.write(a)
    st.pyplot()

if st.checkbox("What Percentage of aadhar card Rejected?"):
    rejected_percent = np.round((df[df['Rejected'] == 1]['Rejected'].sum() / df['Rejected'].count())*100)
    plt.figure()
    colors = ['black', 'c']
    rej_values = [rejected_percent, 100-rejected_percent]
    rej_label = ['Rejected', 'Not Rejected']
    plt.axis('equal')
    plt.title("What Percentage of aadhar card Rejected?")
    st.write(plt.pie(rej_values, labels=rej_label, explode=explode, autopct='%1.1f%%', colors=colors))
    st.pyplot()

if st.checkbox("Age Ditribution"):
    # plt.figure()
    st.write(plt.hist(df['Age'], 50, normed=1, alpha=0.7, edgecolor = [1,1,1]))
    plt.title("Age Distribution")
    plt.xlabel("Age in years")
    st.pyplot()
    


if st.checkbox("Number of Male and Female applied for Aadhar Card"):
    Male = df[df['Gender'] == 1]['Gender'].count()
    Female = df[df['Gender'] == 0]['Gender'].count()
    mf_values = [Male, Female]
    mf_label = ['Male', 'Female']
    st.write(plt.pie(mf_values, labels=mf_label, autopct='%1.1f%%'))
    plt.title("Number of Male and Female applied for Aadhar Card")
    st.pyplot()

if st.checkbox("How many people's provided Email? and How many people provided Mobile Number ?"):
    email = df[df['Email'] == 1]['Email'].count()
    not_provided = df[df['Email'] == 0]['Email'].count()

    mobile = df[df['Mobile'] == 1]['Mobile'].count()
    mob_not_provided = df[df['Mobile'] == 0]['Mobile'].count()

    fig = plt.figure()
    ax1, ax2 = fig.subplots(nrows=2)

    #plotting email
    email_values=[email, not_provided]
    email_labels = ['Provided', 'Not Provided']
    colors = ['c', 'r']
    st.write(ax1.pie(email_values, labels=email_labels, autopct='%1.1f%%', explode=explode, colors=colors))
    plt.setp(ax1, title = ("Number of peoples provided email"))
    

    #plotting Mobile
    mob_values = [mobile, mob_not_provided]
    st.write(ax2.pie(mob_values, labels=email_labels, autopct='%1.1f%%', explode=explode, colors=colors))
    plt.setp(ax2, title = ("Number of peoples provided Mobile Number"))
    st.pyplot()


if st.checkbox("How much aadhar cards generated per district ?"):
    per_district_aadhar_generated = df[df['Generated'] == 1].groupby('District')['District'].count()
    plt.figure()
    st.write(plt.bar(df['District'].unique()[:20],per_district_aadhar_generated[:20]))
    plt.xticks(rotation=70)
    plt.title('How much aadhar card generated per district')
    st.pyplot()
    
if st.checkbox("How much aadhar card generated by per state?"):
    per_state_aadhar_card_generated = df[df['Generated'] == 1].groupby('State')['State'].count()
    st.write(plt.barh(df['State'].unique(), per_state_aadhar_card_generated))
    plt.title('How much aadhar cards generated per state')
    st.pyplot()
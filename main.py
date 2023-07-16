import streamlit as st

st.title(' Backtest Portfolio Asset Class Allocation :sunglasses:')

st.write("เครื่องมือ backtesting พอร์ตโฟลิโอนี้ช่วยให้คุณสร้างพอร์ตโฟลิโอ ตามการจัดสรรระดับสินทรัพย์ที่เลือก เพื่อวิเคราะห์และทดสอบผลตอบแทนพอร์ตโฟลิโอย้อนหลัง ลักษณะความเสี่ยง Characteristics, และผลตอบแทนย้อนหลัง")



years = list(range(1995, 2023))
year_range = st.slider(label="Start Year", min_value=1958, max_value=2022, value=(2010, 2022))

Initial_Amount = st.number_input('Initial Amount')



withdrawal = st.selectbox(
    'Withdrawal:',
    ('None', 'fixed amount', 'fixed %'))

#st.write('You selected:', withdrawal)
if withdrawal == 'fixed amount' :
    withdrawal_Amount = st.number_input('Withdrawal Amount')
    
if withdrawal == 'fixed %' :
    withdrawal_Per = st.number_input('Withdrawal %')
    


Saving = st.selectbox(
    'Saving:',
    ('None', 'fixed amount', 'fixed %'))

#st.write('You selected:', withdrawal)
if Saving == 'fixed amount' :
    Saving_Amount = st.number_input('Saving Amount')
    
if withdrawal == 'fixed %' :
    Saving_Per = st.number_input('Saving %')
    


Rebalancing  = st.selectbox(
    'Rebalancing ',
    ('No', 'Yes'))



st.subheader('Asset Allocation ')


col1, col2, col3 = st.columns(3)


with col2:
    st.subheader('')
    

with col1:
    Asset_1 = st.selectbox('Asset class1:',('US Equity', 'EU Equity', 'Bond'))

    Asset_2 = st.selectbox('Asset class2:',('US Equity', 'EU Equity', 'Bond'))
    
    Asset_3 = st.selectbox('Asset class3:',('US Equity', 'EU Equity', 'Bond'))
    Asset_4 = st.selectbox('Asset class4:',('US Equity', 'EU Equity', 'Bond'))
    
    Asset_5 = st.selectbox('Asset class5:',('US Equity', 'EU Equity', 'Bond'))   

    Asset_6 = st.selectbox('Asset class6:',('US Equity', 'EU Equity', 'Bond'))
    Asset_7 = st.selectbox('Asset class7:',('US Equity', 'EU Equity', 'Bond'))
    
    Asset_8 = st.selectbox('Asset class8:',('US Equity', 'EU Equity', 'Bond'))
    Asset_9 = st.selectbox('Asset class9:',('US Equity', 'EU Equity', 'Bond'))
    
    Asset_10 = st.selectbox('Asset class10:',('US Equity', 'EU Equity', 'Bond'))  
    
        
with col3:
    Aweight_1 = st.number_input('weight 1', min_value=0, max_value=100)
    Aweight_2 = st.number_input('weight 2', min_value=0, max_value=100)
    Aweight_3 = st.number_input('weight 3', min_value=0, max_value=100)
    Aweight_4 = st.number_input('weight 4', min_value=0, max_value=100)
    Aweight_5 = st.number_input('weight 5', min_value=0, max_value=100)
    Aweight_6 = st.number_input('weight 6', min_value=0, max_value=100)
    Aweight_7 = st.number_input('weight 7', min_value=0, max_value=100)
    Aweight_8 = st.number_input('weight 8', min_value=0, max_value=100)
    Aweight_9 = st.number_input('weight 9', min_value=0, max_value=100)
    Aweight_10 = st.number_input('weight 10', min_value=0, max_value=100)










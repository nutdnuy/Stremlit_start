import streamlit as st
st.title ("Backtest Portfolio Asset Class Allocation")
st.write("This portfolio backtesting tool allows you to construct one or more portfolios based on the selected asset class level allocations in order to analyze and backtest portfolio returns, risk characteristics, drawdowns, and rolling returns. You can compare up to three different portfolios against the selected benchmark, and you can also specify any periodic contribution or withdrawal cashflows and the preferred portfolio rebalancing strategy.  You can also use the portfolio backtesting tool to build and compare portfolios based on specific mutual funds, ETFs, and stocks.")



col = st.columns(2)
code = "test"


with col[0]:
    show_btn = st.button("run")



    if show_btn:
            st.code(code, language='python')


with col[1]:
    show_btn2 = st.button("run 2")


    if show_btn2 :
            st.code(code, language='python')
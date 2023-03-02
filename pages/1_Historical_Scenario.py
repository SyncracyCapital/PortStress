import pandas as pd
import streamlit as st
from utils import add_row_to_asset_df, clear_assets, formatter_pct_value, df_style

# --------------------------------- Application Config --------------------------------- #
st.set_page_config(
    page_title="Scenario Stress Test",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

# --------------------------------- Global Variables --------------------------------- #

SCENARIOS = {'Terra/Luna Collapse': 'scenario_1',
             'FTX Collapse': 'scenario_2',
             'Black Thursday': 'scenario_3',
             '2017-18 Crypto Winter': 'scenario_4',
             '2013-14 Crypto Winter': 'scenario_5'}

ASSET_CG_MAP = {'lido-dao': 'LDO',
                'uniswap': 'UNI',
                'ethereum': 'ETH',
                'arweave': 'AR',
                'maker': 'MKR',
                'solana': 'SOL',
                'synapse-2': 'SYN',
                'canto': 'CANTO',
                'maple': 'MAPLE',
                'blockstack': 'STX',
                'render-token': 'RNDR'}

# --------------------------------- Application Layout --------------------------------- #
st.title('Historical Scenario Stress Tester')
st.write('#### Portfolio stress testing based on pre-defined historical scenarios')

st.write('#### Select Scenario')
scenario = st.selectbox(label=' ', options=(SCENARIOS.keys()))
scenario_date_range = SCENARIOS[scenario]
st.session_state['scenario_name'] = scenario

# Create an empty string for each column (alternatively could use lists)
# Create an empty dataframe on first page load, will skip on page reloads
if 'data' not in st.session_state:
    data = pd.DataFrame({'Asset Name': [], 'Asset Weight': []})
    st.session_state.data = data

st.write('#### Portfolio Composition')

portfolio_table, portfolio_chart = st.columns(2)

with portfolio_table:
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(df_style(st.session_state.data))

# TODO: Make the chart prettier
with portfolio_chart:
    st.bar_chart(data=st.session_state.data,
                 y='Asset Weight',
                 x='Asset Name')


# Inputs listed within a form
st.write('#### Add Assets to Portfolio')
df_table_form = st.form(key='df_form')
with df_table_form:
    df_columns = st.columns(2)
    with df_columns[0]:
        st.selectbox('Asset Name', options=list(ASSET_CG_MAP.values()), key='asset_name_input')
    with df_columns[1]:
        st.number_input('Asset Weight', step=0.1, key='asset_weight_input')
    st.form_submit_button(label='Add Asset', on_click=add_row_to_asset_df)
    st.form_submit_button(label='Clear Assets', on_click=clear_assets)

# --------------------------------- Application Logic --------------------------------- #
run_scenario = st.button('Run Scenario')
if run_scenario:
    st.write(st.session_state)
    print(type(df_table_form))
    st.write(f'Running scenario {scenario}')

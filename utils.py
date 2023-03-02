import pandas as pd
import streamlit as st


# TODO: align values in table to center
def df_style(df):
    """
    Style the dataframe
    :param df: dataframe to style
    :return: styled dataframe
    """
    df = df.reset_index(drop=True)
    return df.style\
        .format({'Asset Weight': '{:.1f}%'})\
        .set_properties(**{'text-align': 'center', 'padding': '6px'})


def add_row_to_asset_df():
    """
    Add a row to the asset dataframe
    :return: session_state.data
    """
    row = pd.DataFrame({'Asset Name': [st.session_state['asset_name_input']],
                        'Asset Weight': [st.session_state['asset_weight_input']]})
    st.session_state.data = pd.concat([st.session_state.data, row])


def clear_assets():
    """
    Clear the assets from the portfolio table
    :return: session_state.data
    """
    st.session_state.data = pd.DataFrame(columns=['Asset Name', 'Asset Weight'])


def formatter_pct_value(value):
    """
    Format the value as a percentage
    :param value: value to format
    :return: pct value
    """
    return f'{value:.2f}%'

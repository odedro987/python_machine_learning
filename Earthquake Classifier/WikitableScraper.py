import pandas as pd

def get_table_dataframe_from_url(url, table_id):
    return pd.read_html('https://en.wikipedia.org/wiki/List_of_tornadoes_and_tornado_outbreaks_in_Asia')[table_id]
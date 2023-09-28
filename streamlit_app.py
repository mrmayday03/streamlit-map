import streamlit as st
import pandas as pd
import pydeck as pdk

# Load the data
df = pd.read_csv('./threat.csv')

# Set up the Streamlit app
st.title("Threat Map")
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v9",  # You can change the map style
        initial_view_state=pdk.ViewState(
            latitude=12.971298,
            longitude=80.043749,
            pitch=50,
            zoom=15,
        ),
        layers=[
            pdk.Layer(
                'ColumnLayer',
                data=df,
                get_position=['longitude', 'latitude'],
                get_elevation='threat_score',
                elevation_scale=100,
                radius=50,
                get_fill_color=[255, 0, 0, 80],
                pickable=True,
                auto_highlight=True,
            ),
            pdk.Layer(
                "TextLayer",
                data=df,
                get_position=["longitude", "latitude"],
                get_text="name",
                get_color=[255, 255, 255],
                get_size=10,
                get_offset=[0, 20],
            ),
        ],
    )
)

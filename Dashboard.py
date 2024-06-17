import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import toml

# ---- PAGE CONFIG ----

st.set_page_config(
    page_title="Superstore",
    page_icon=':bar_chart:',
    layout="wide",
)

# ---- READ DATA ----

@st.cache_resource
def load_data():
    df = pd.read_csv('clean_data.csv')
    return df

df = load_data()

# ---- THEMES ----

def update_theme_toml(theme_colors):
    config_path = ".streamlit/config.toml"

    with open(config_path, "r") as file:
        config = toml.load(file)
    
    config['theme']['primaryColor'] = theme_colors['primaryColor']
    config['theme']['backgroundColor'] = theme_colors['backgroundColor']
    config['theme']['secondaryBackgroundColor'] = theme_colors['secondaryBackgroundColor']
    config['theme']['textColor'] = theme_colors['textColor']
    
    with open(config_path, "w") as file:
        toml.dump(config, file)

color_side = '#232323'
color_accent_1 = '#6D87BD'
color_accent_2 = '#B6C4DE'
color_accent_3 = '#D7DEE5'

# ---- FUNCTIONS ----

#Summary plots
def plot_metric(label, value, prefix="", suffix="", show_graph=False, graph_x="", graph_y="", color_graph=""):

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": prefix,
                "suffix": suffix,
                "font.size": 28,
                'valueformat':',.0f'
            },
            domain={'x': [0, 1], 'y': [0.9, 1]}
            #title={
            #    "text": label,
            #    "font": {"size": 24},
            #}
        )
    )
    
    if show_graph:
        fig.add_trace(
            go.Scatter(
                x=graph_x,
                y=graph_y,
                #hoverinfo="skip",
                fill="tonexty",
                fillcolor=color_graph,
                line={
                    "color": color_graph,
                },
            )
        )

    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        margin=dict(t=20, b=0),
        showlegend=False,
        height=120,
    )
    
    st.plotly_chart(fig, use_container_width=True)

#Top10 plots
def plot_top10(label, df, x_data:str, y_data:str, marker_color:str):
    
    fig = px.bar(
        data_frame=df,
        x=x_data,
        y=y_data,
        #title=label,
        text_auto='.2s'
    )
    
    fig.update_traces(marker_color=marker_color, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_layout(
        yaxis={'categoryorder':'total ascending'}
        )
    st.plotly_chart(fig, use_container_width=True)

#AVG days shipping
def plot_avg(value, min, max, suffix, color):
    
    fig = go.Figure(
        go.Indicator(
            value = value,
            mode = "number+gauge",
            number={
                "font.size": 28,
                "suffix": suffix,
                'valueformat':'.2f'
            },
            gauge={
                'shape': "bullet",
                'axis': {
                    'range': [min, max],
                    'tickmode': 'linear',
                    'tick0': 1,
                    'dtick': 1
                },
                'bar': {'color': color}
            },
            domain={'x': [0, 1], 'y': [0.15, 0.7]}
        )
    )
    
    fig.update_layout(
        margin=dict(t=10, b=10),
        showlegend=False,
        height=120,
    )


    st.plotly_chart(fig,use_container_width=True,)

#Sales plot
def plot_sales(label, df, x_data:str, y_data:str, color, color_map,):
    fig = px.bar(
    data_frame=df,
    x=x_data,
    y=y_data,
    color=color,
    color_discrete_map=color_map,
    #title=label,
    text_auto='.2s'
)
    fig.update_layout(barmode='stack', font_color='white', yaxis=dict(gridcolor=color_side))
    fig.update_traces(textangle=0, textposition="outside", cliponaxis=False)
    fig.update_xaxes(tickmode='linear', tick0=2018, dtick=1)
    st.plotly_chart(fig, use_container_width=True)

# ---- SIDEBAR/FILTERING ----
all_value = 'All'

st.sidebar.header('Years', divider='grey')

year = sorted(df['year'].unique())
year.append(all_value)
years = st.sidebar.multiselect('Select year:', options=year, default='All')
if "All" in years or len(years) == 0:
    years = sorted(df['year'].unique())

st.sidebar.write("")
st.sidebar.write("")

st.sidebar.header('Locations', divider='grey')

region = sorted(df.loc[df['year'].isin(years), 'Region'].unique())
region.append(all_value)
regions = st.sidebar.multiselect('Select region:', options=region, default='All')
if "All" in regions or len(regions) == 0:
    regions = sorted(df['Region'].unique())
    
state = sorted(df.loc[df['Region'].isin(regions), 'State'].unique())
state.append(all_value)
states = st.sidebar.multiselect('Select state:', options=state, default='All')
if "All" in states or len(states) == 0:
    states = sorted(df['State'].unique())

st.sidebar.write("")
st.sidebar.write("")

st.sidebar.header('Categories', divider='grey')

category = sorted(df.loc[df['State'].isin(states), 'Category'].unique())
category.append(all_value)
categories = st.sidebar.multiselect('Select category:', options=category, default='All')
if "All" in categories or len(categories) == 0:
    categories = sorted(df['Category'].unique())
    
subcategory = sorted(df.loc[df['Category'].isin(categories), 'subcategory'].unique())
subcategory.append(all_value)
subcategories = st.sidebar.multiselect('Select sub-category:', options=subcategory, default='All')
if "All" in subcategories or len(subcategories) == 0:
    subcategories = sorted(df['subcategory'].unique())

selected_df = df[
    (df['year'].isin(years)) &
    (df['Region'].isin(regions)) &
    (df['State'].isin(states)) &
    (df['Category'].isin(categories)) &
    (df['subcategory'].isin(subcategories))
]

st.sidebar.write("")
st.sidebar.write("")

st.sidebar.header('Theme', divider='grey')

tcol1, tcol2 = st.sidebar.columns((1,1))

if tcol1.button("Light", use_container_width=True, type='primary'):
    theme_colors = {
        'primaryColor': '#6D87BD',
        'backgroundColor': "#D1D1D1",
        'secondaryBackgroundColor': "#C1C1C1",
        'textColor': '#292929',
    }
    update_theme_toml(theme_colors)

if tcol2.button("Dark", use_container_width=True, type='primary'):
    theme_colors = {
        'primaryColor': '#6D87BD',
        'backgroundColor': '#4A4A4A',
        'secondaryBackgroundColor': '#232323',
        'textColor': "#F4F4F4",
    }
    update_theme_toml(theme_colors)

# ---- MAIN PAGE ----

st.title('Superstore')

## -- Summary data --

st.write('')
st.write('')

sletft, scol1, smid, scol2, sright = st.columns((1,10,1,10,1))

#Total sales and total profit
with scol1:
    st.subheader('Total sales', divider='gray')
    
    sales_df = selected_df.groupby(['month_year'], as_index=False)['Sales'].sum()
    sales = int(selected_df['Sales'].sum())
    
    plot_metric(
        label='Total sales',
        value=sales,
        prefix="$ ",
        suffix="",
        show_graph=True,
        graph_x=sales_df['month_year'],
        graph_y=sales_df['Sales'],
        color_graph=color_accent_1,
    )
    st.write('')
    st.write('')
    
    st.subheader('Total profit', divider='gray')
    
    profit_df = selected_df.groupby(['month_year'], as_index=False)['Profit'].sum()
    profit = int(selected_df['Profit'].sum())
    
    plot_metric(
        label='Total profit',
        value=profit,
        prefix="$ ",
        suffix="",
        show_graph=True,
        graph_x=profit_df['month_year'],
        graph_y=profit_df['Profit'],
        color_graph=color_accent_1,
    )

#Order number and AVG plot
with scol2:
    st.subheader('Total number of orders', divider='gray')
    
    order_df = selected_df.groupby(['month_year'], as_index=False)['Order ID'].count()
    orders = len(selected_df['Order ID'].unique())
    
    plot_metric(
        label='Number of orders',
        value=orders,
        prefix="",
        suffix=" pcs",
        show_graph=True,
        graph_x=order_df['month_year'],
        graph_y=order_df['Order ID'],
        color_graph=color_accent_1,
    )
    st.write('')
    st.write('')
    
    st.subheader('Average shipping days', divider='gray')
    
    average_days_to_ship = selected_df['days to ship'].mean()
    min_days_to_ship = selected_df['days to ship'].min()
    max_days_to_ship = selected_df['days to ship'].max()

    plot_avg(
        value=average_days_to_ship,
        min=min_days_to_ship,
        max=max_days_to_ship,
        suffix=' days',
        color=color_accent_1
    )

st.write('')
st.write('')
st.write('')
st.write('')

## -- Charts --

bleft, bmid, bright = st.columns((1,21,1))

with bmid:

    #Top10 profit
    st.subheader('Top 10 products by sales', divider='gray')

    top10_sales = selected_df[['Product Name', 'Sales']].groupby('Product Name', as_index=False).sum().sort_values('Sales',ascending=False).head(10)

    plot_top10(
        label='Top 10 product by sales',
        df=top10_sales,
        x_data='Sales',
        y_data='Product Name',
        marker_color=color_accent_1
    )

    #Top10 profit
    st.subheader('Top 10 products by profit', divider='gray')

    top10_profit = selected_df[['Product Name', 'Profit']].groupby('Product Name', as_index=False).sum().sort_values('Profit',ascending=False).head(10)

    plot_top10(
        label='Top 10 product by profit',
        df=top10_profit,
        x_data='Profit',
        y_data='Product Name',
        marker_color=color_accent_1
    )

    #Sales plot
    st.subheader('Sales trends', divider='gray')

    sales_trend_df = selected_df[['year', 'Category', 'Sales']].groupby(['year','Category']).sum().reset_index()

    sales_color_map = {
        'Furniture': color_accent_1,
        'Office Supplies': color_accent_2,
        'Technology': color_accent_3
    }

    plot_sales(
        label='Sales',
        df=sales_trend_df,
        x_data='year',
        y_data='Sales',
        color='Category',
        color_map=sales_color_map,
    )
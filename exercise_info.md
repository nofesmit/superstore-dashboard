## Superstore

Imagine you’re a Data Scientist, Analyst, Machine Learning Engineer, or a Web Developer, and you want to transform your Python data script into a quick actionable insight. Streamlit is your answer. Streamlit is an open-source Python framework that allows you to effortlessly create web applications. With Streamlit, you can turn your data scripts into shareable web apps in minutes, not weeks, and it’s absolutely free to use. In this project, you will have opportunity to build an analytics dashboard using the Streamlit Python package.

For this project, you’ll use the Superstore Sales dataset available on Superstore Sales 2023 — dataset by ehughes | data.world. Analyze the dataset with using the learnt pandas and numpy functions. Clean the dataset and create the needed dataframes to create basis of requested plots. The tasks below descibe the obectives are need to be achieved through the dashboard.


##### 1. Import data
Import the Superstore Sales 2023 is attached to the projects!

1. Dataset is imported and asigned to a dataframe.

2. A new year column is created with value extracted from Order Date.

3. A days to ship column is added with value is calculated from Ordeer date and Ship date.

4. Dataset is cleaned as needed


##### 2. Dashboard layout
Plan the dashboard layout. Based on the following excpectations create a wireframe of about the dashboard and its layout. Arrange the individual diagrams to taste, try to create a uniform look for the colors.

1. Wireframe is created.

2. Dashboard contains a Superstores tiitle

3. Colour usage and appearance are uniformed

##### 3. Summary data
The first section need to contain summaried data. Visualize the total sales, how much profit was made and how many distinct orders did the store receive? You can use Streamlite metric visualizer for show data.

1. Total sales data is millified format, the shown value is $2.3M without filtering.

2. Total profit is $286.4k without filtering. The shown data is millified.

3. Number of orders is 5009 without filtering


##### 4. Top 10 products by sales
Visualize the top 10 products by sales. Use bar chart to show the products and their total sales value!

1. Horizontal bar chart is used to visualize top 10 products.

2. Products are ordered by sales, most frequented product is located at the top of chart


##### 5. Top 10 products by profit
Visualize the top 10 products by profit. Use bar chart to show the products and their sum of profit value.

1. Horizontal bar chart is used to visualize top 10 products

2. Products are ordered by profit, most frequented product is located at the top of chart


##### 6. Average shipping days
Visualize the average number of days it takes to ship an Order.

1. Plotly indicator is used for visualization.

2. The displayable range of indicator chart is the minimum and maximum value of Days to ship column.


##### 7. Sales trends
Visualize the sales trends for different product categories over the year. Show the annual sum of sales values per product groups, broken down by year.

1. Stacked bar chart is used, where the years are shown on the x axis and sales value is on y axis.

2. Product categories are furniture, office suppliers and technology.


##### 8. Filtering
Give a sidebar to the dashboarn and locate a dropdown control, which contains possible years are extracted from Order date column. Make the dashboard interactive with giving capability of filtering with year selection.

1. Year selector contains an All value which tuns off filtering

2. On selection change the every chart displays filtered values of data table.

3. Selectable years are 2020, 2021, 2022, 2023. Years are extracted from data table.


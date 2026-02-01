# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: HARSHITA GOUD

*INTERN ID*: CTIS4088

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


📌 Project Overview

This project was developed during my CODTECH IT SOLUTIONS internship as part of the API Integration and Data Visualization task. The objective of this project is to fetch real-time COVID-19 data for Indian states using a public API and transform that raw data into meaningful visual insights that help in understanding the impact of the pandemic across different regions of India.

In today’s data-driven world, public health organizations rely heavily on live data to monitor outbreaks, allocate medical resources, and make informed policy decisions. This project replicates that real-world workflow by using live COVID-19 data and Python-based analytics tools.


🔍 How the Project Works

The application connects to the COVID-19 India Public API, which provides updated statewise pandemic data in JSON format. Using the requests library, the program sends an HTTP request to the API endpoint and retrieves the latest COVID-19 statistics.

This data is then processed using the pandas library, which converts the raw JSON into a structured DataFrame. From this dataset, the confirmed COVID-19 cases for each Indian state are extracted. The national total row is removed to ensure only individual states are included in the analysis.

The states are sorted in descending order based on confirmed cases, and the Top 10 most affected Indian states are selected. This ranking highlights the regions that were most impacted by the pandemic.

To make the insights easy to understand, a bar chart is created using the matplotlib library. The chart visually compares the confirmed COVID-19 cases across the top 10 states. The generated visualization is automatically saved as an image file, making it suitable for reports, documentation, and presentations.


🚀 Key Features

-Public API Integration :-
Fetches live COVID-19 data from an official Indian COVID-19 API without requiring any authentication or API keys.

-Statewise Data Analysis :-
 Processes COVID-19 statistics for all Indian states and extracts confirmed case counts.

-Top-10 Ranking System :-
 Identifies and ranks the 10 most affected Indian states based on confirmed COVID-19 cases.

-Visual Analytics :-
 Generates a bar chart that clearly compares COVID-19 case counts between states.

-Exportable Output :-
 Automatically saves the visualization as an image file for reporting and documentation.


🛠 Technologies Used

-Python 3.x

-Requests :– For API communication and data retrieval

-Pandas :– For data cleaning, filtering, and analysis

-Matplotlib :– For graphical data visualization


🌐 Data Source

COVID-19 India Public API
Provides up-to-date statewise COVID-19 statistics in JSON format.


🎯 Use Cases

-Public health monitoring

-COVID-19 trend analysis

-Data science and analytics practice

-Government and healthcare reporting

-Academic and internship projects


📊 Project Output

<img width="1228" height="737" alt="Image" src="https://github.com/user-attachments/assets/aa8e67cc-e84e-4a9b-a3d9-3a0f09dbe143" />

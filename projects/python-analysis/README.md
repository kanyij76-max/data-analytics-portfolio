# 🐍 Python Deployment Efficiency Analysis

## Project Overview
This Python script utilizes the Pandas library to analyze network deployment schedules and measure technician efficiency. It tracks Service Level Agreement (SLA) turnaround times for regional deployment tickets.

## Technical Skills Demonstrated
* **Data Manipulation (Pandas):** Created DataFrames and handled missing values for pending deployments.
* **Feature Engineering:** Cleaned datetime formats and calculated SLA turnaround days by finding the difference between request and completion dates.
* **Data Aggregation:** Filtered completed jobs and utilized `groupby()` to calculate the average turnaround time per technician.

## Repository Contents
* `deployment_analysis.py`: The complete Python script containing the dataset generation, cleaning, engineering, and aggregation logic.

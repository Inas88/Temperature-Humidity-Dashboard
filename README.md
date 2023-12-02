# Temperature-Humidity-Dashboard
## Overview

This Dash dashboard provides real-time monitoring and visualization of temperature and humidity data from an IT server room.
   * Uses Google Sheets for data storage.
   * Sends email alerts if temperature or humidity thresholds are exceeded.
*****************
![Dash - Google Chrome 11_12_2023 3_33_17 PM](https://github.com/Inas88/Temperature-Humidity-Dashboard/assets/141937875/99bfbe01-908e-4096-be23-9f6a40020c34)

************************************
![Dash - Google Chrome 11_30_2023 2_53_17 AM](https://github.com/Inas88/Temperature-Humidity-Dashboard/assets/141937875/e306e15b-a5f0-4dbd-9525-c0629f92da49)

************************************
![Dash - Google Chrome 11_30_2023 5_25_09 PM](https://github.com/Inas88/Temperature-Humidity-Dashboard/assets/141937875/349e3cb6-fdfd-4f48-a61c-3b7ea23232a2)

************************************
### Key Features
   - Real-time monitoring of temperature and humidity.
   - Email alerts for threshold exceedances.
   - Interactive visualizations with gauge figures and plots.
   - User-friendly interface with a customizable theme.


## Table of Contents

1. [Introduction](#introduction)
2. [Libraries Used](#libraries-used)
3. [Setup](#setup)
   - 3.1 [Google Sheets Credentials](31#google-sheets-credentials)
   - 3.2 [Dependencies](32#dependencies)
   - 3.3 [Dash App Setup](33#dash-app-setup)
   - 3.4 [Email Configuration](34email-configuration)
4. [Dash App Components](#dash-app-components)
   - 4.1 [Layout](#layout)
     - 4.1.1 [Title and Headings](#title-and-headings)
     - 4.1.2 [Temperature and Humidity Gauges](#temperature-and-humidity-gauges)
     - 4.1.3 [Real-Time Plot](#real-time-plot)
     - 4.1.4 [Distribution Plots](#distribution-plots)
     - 4.1.5 [User Guide](#user-guide)
   - 4.2 [Callbacks](#callbacks)
     - 4.2.1 [Update Gauges](#update-gauges)
     - 4.2.2 [Update Temperature and Humidity Plot](#update-temperature-and-humidity-plot)
     - 4.2.3 [Update Summary and Send Email Alert](#update-summary-and-send-email-alert)
6. [Troubleshooting and Deployment](#troubleshooting-and-deployment)
7. [Customization](#customization)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

This documentation provides detailed information about the Temperature and Humidity Monitoring Dashboard, including setup instructions, code explanations, and usage guidelines.

---
## Libraries Used
The following libraries are required for the dashboard:

- `gspread`: Manages Google Sheets interaction.
- `oauth2client`: Ensures secure Google Sheets access.
- `dash`: Core for web dashboard creation.
- `dash_core_components`: Adds interactive elements.
- `dash_html_components`: Structures HTML for the dashboard.
- `dash.dependencies`: Handles component interdependencies.
- `plotly.graph_objects`: Creates visual graphs and figures.
- `plotly.express`: Simplifies complex graph creation.
- `pandas`: Organizes and manages tabular data.
- `smtplib`: Sends email alerts.
- `email.mime.text, email.mime.multipart`: Formats and sends email content.
---
## Setup

### Google Sheets Credentials

To interact with Google Sheets, the script requires API credentials. Follow these steps:

1. Go to the [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Sheets API for the project.
4. Create credentials (service account key) and download the JSON file.
5. Place the JSON file in the project directory and update the `credentials.json` reference in the code.
6. Share the service account email with concerned Google Sheet.


### Dependencies

Install the required libraries using the following command:

```bash
pip install dash gspread oauth2client plotly pandas smtplib
```
### Dash App Setup
To set up the Dash app:

- Clone or download the repository to your local machine.
- Open a terminal and navigate to the project directory.

### Email Configuration
In the script, go to the "Email configuration" section and configure the SMTP server details (smtp_server, smtp_port, sender_email, recipient_email).
Uncomment and provide valid SMTP username and password if required.

---
## Dash App Components
### Layout
In Dash apps, `app.layout` acts like a blueprint, deciding how things look on the dashboard. It's like arranging furniture in a room, [Learn more](https://dash.plotly.com/layout). Here It includes various components:
#### Title and Headings
```python
html.H1("Temperature and Humidity Monitoring Dashboard"),
```
#### Temperature and Humidity Gauges
```python
dcc.Graph(id='temperature-gauge'),
dcc.Graph(id='humidity-gauge'),
```
#### Real-Time Plot
```python
dcc.Graph(id='temperature-humidity-plot'),
```
#### Distribution Plots
```python
dcc.Graph(id='temperature-distribution-plot'),
dcc.Graph(id='humidity-distribution-plot'),
```
#### User Guide
```python
dcc.Markdown('''
   دليل المستخدم: لوحة عرض درجة الحرارة والرطوبة
   =============================================
   ...
'''),
```
### Callbacks
The interactivity of the Dash app is described by "callbacks". These functions update the content of the app based on user interactions or other triggers[learn more](https://dash.plotly.com/basic-callbacks). The following are examples of key callbacks:

#### Update Gauges
```python
@app.callback(
    [Output('temperature-gauge', 'figure'),
     Output('humidity-gauge', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_gauges(n_intervals):
    # Logic to update temperature and humidity gauge figures
    # ...
    return temperature_gauge, humidity_gauge
```
#### Update Temperature and Humidity Plot
```python
@app.callback(
    Output('temperature-humidity-plot', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    # Logic to update temperature and humidity plot
    # ...
    return fig
```
#### Update Summary and Send Email Alert
```python
@app.callback(
    Output('summary-div', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_summary(n_intervals):
    # Logic to update summary and send email alert
    # ...
    return [*alert_elements]
```
---
## Troubleshooting and Deployment

When encountering errors during local execution or facing connectivity issues post-environment closure, deploying the Dash app on a company's local server or a Virtual Machine (VM) can offer a robust solution. The following outlines the considered options, the chosen approach, and the step-by-step deployment process:

**Options Considered:**

**a. Local Deployment**
   - *Issues:* Running the app locally might result in errors, especially when closing the development environment.
   - *Drawbacks:* Limited accessibility and potential connection issues.

**b. Hosted Server or Dash Enterprise**
   - *Options:* Using a hosted server or Dash Enterprise for deployment.
   - *Benefits:* Improved accessibility, reliability, and easier deployment.

**c. Company Local Server or VM**
   - *Options:* Leveraging a company's local server or a Virtual Machine.
   - *Benefits:* Increased control, accessibility within the local network, and potential for a stable deployment.

**Chosen Approach:**

Upon careful evaluation of the available options, the selected strategy involved deploying the Dash app on a company's local server utilizing a Virtual Machine (VM). Opting for a free solution, this approach is particularly well-suited for initial exploration and testing. The decision to leverage a company's local server via VM was driven by the goal of ensuring dependable access within the local network, effectively mitigating potential errors associated with local deployment.

**Deployment Steps:**

**a. Open the Dash app script (`dashboard_script.py`) and update the `host` parameter in the "Run Dash App" section with the local network IP address:**

   ``` python
   '''Section 10: Run Dash App```
   if __name__ == '__main__':
       app.run_server(debug=True, host='YOUR_LOCAL_NETWORK_IP', port=8050)
   ```
    

**b. Transfer Code and Credentials:**
   - Copy the Dash app script (`dashboard_script.py`) and the Google Sheets credentials file (`credentials.json`) to the directory on VM.

**c. Install Dependencies:**
   - Open a terminal on the server or VM, navigate to the directory containing the Dash app script, and install Python along with all required modules and dependencies:
     ```bash
     pip install -r requirements.txt
     ```

**d. Run the App:**
   - Execute the following command to run the Dash app:
     ```bash
     python dashboard_script.py
     ```

**e. Access the Dashboard:**
   - After running the app, find the displayed link in the terminal.
     Open that link in a web browser to access the Dash app from any device within the local network.

By following these structured steps, the deployment on a VM is configured, addressing potential errors and ensuring a reliable, accessible solution.

---
## Customization
Customize the dashboard layout, colors, and other settings according to your preferences:

- Adjust the layout, colors, and styling in the Dash app initialization section.
- Update the Google Sheets credentials file name and sheet name.
- Customize the email alert messages and thresholds.
----
## Troubleshooting

If you encounter issues:

- Check your internet connection and network settings.
- Verify the Google Sheets API credentials and sharing settings.
- For technical support, contact [us](mailto:enas.h.diab@gmail.com).

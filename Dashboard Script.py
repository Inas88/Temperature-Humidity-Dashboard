"""
Temperature and Humidity Monitoring Dashboard

This Dash dashboard provides real-time monitoring and visualization of temperature and humidity data from an IT server room.

- Uses Google Sheets for data storage.
- Sends email alerts if temperature or humidity thresholds are exceeded.
"""

'''Section 1: Import necessary libraries and modules'''
# Handles Google Sheets API credentials
# import dash_design_kit
# MIMEMultipart for email attachments

'''Section 2: Google Sheets Setup'''
# Set up Google Sheets credentials
# #The scope variable defines the permissions that script will have. In this case, it specifies that the script will have access to Google Sheets.
import gspread  # Allows interaction with Google Sheets
from oauth2client.service_account import ServiceAccountCredentials
import dash  # Main Dash library
from dash import dcc, html  # Components for building the dashboard layout
from dash.dependencies import Input, Output
from dash import dcc
import plotly.graph_objects as go  # Used for creating gauge figures
import plotly.express as px  # High-level interface for creating plots
import pandas as pd  # Data manipulation library
import smtplib  # Library for sending emails
from email.mime.text import MIMEText  # MIMEText for email text
from email.mime.multipart import MIMEMultipart
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]
# #This line creates credentials by loading a JSON key file and specifying the desired scope. The JSON key file contain the necessary information to authenticate as a service account.
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope)
# Authorize the script to access Google Sheets using the credentials.
# This creates a client object that can interact with Google Sheets on behalf of the service account.
client = gspread.authorize(creds)
sheet = client.open("Temp_Humid_monitoring").sheet1


'''Section 3: Dash App Initialization and Theme Configuration'''
# Create Dash application. foundation for building the web dashboard.
app = dash.Dash(__name__)

# Define custom theme for the dashboard
custom_theme = {
    'backgroundColor': '#F9F9F9',  # Background color of the entire app
    'fontFamily': 'Arial, sans-serif',
    'textColor': '#333333',  # Default text color
    'headerColor': '#3A6BAC',  # Header color
    'plotBackgroundColor': '#EFEFEF',  # Background color of plots
    'plotBorderColor': '#DDDDDD',  # Border color of plots
    'alertColor': '#F44336', }  # Color for alert messages


'''Section 4: Dashboard Layout'''
# Define Dash layout
app.layout = html.Div([
    # Div element that contain the entire layout.
    html.Div(style={'backgroundColor': custom_theme['backgroundColor']}, children=[   # Sub-sections related to dashboard components
        html.H1(children='Temperature and Humidity monitoring (IT server)', style={
            'font-family': 'Arial, sans-serif',
            'color': '#3A6BAC',
            'text-align': 'center',
            'font-size': '36px',
            'text-shadow': '2px 2px 2px #000',
            'background-color': '#F2F2F2',
            'border': '2px solid #3A6BAC',
            'padding': '10px',
            'border-radius': '10px',
            'margin': '20px'
        }),
        html.Div(id='summary-div'),
        html.Div([
            dcc.Graph(id='temperature-gauge'),
            dcc.Graph(id='humidity-gauge'),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'background-color': custom_theme['plotBackgroundColor'],
                  'border': '1px solid ' + custom_theme['plotBorderColor'],
                  'border-radius': '5px',
                  'padding': '10px',
                  'margin': '20px', }),

        dcc.Graph(id='temperature-humidity-plot',
                  style={"align": "center", "justify": "center", 'horrizontal-align': 'center', 'background-color': custom_theme['plotBackgroundColor'],
                         'border': '1px solid ' + custom_theme['plotBorderColor'],
                         'border-radius': '5px',
                         'padding': '10px',
                         'margin': '20px', }),
        dcc.Interval(
            id='interval-component',
            interval=120000,  # Interval in milliseconds (e.g., every 1 minute)
            n_intervals=0),
        html.Div([
            # Temperature Distribution Plot
            dcc.Graph(id='temperature-distribution-plot'),

            # Humidity Distribution Plot
            dcc.Graph(id='humidity-distribution-plot'),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'background-color': custom_theme['plotBackgroundColor'],
                  'border': '1px solid ' + custom_theme['plotBorderColor'],
                  'border-radius': '5px',
                  'padding': '10px',
                  'margin': '20px', }),

        dcc.Markdown('''
           
دليل المستخدم: لوحة عرض درجة الحرارة والرطوبة
=============================================

**توفر هذه اللوحة رصدًا وتصويرًا للوقت الحقيقي لبيانات درجة الحرارة والرطوبة في غرفة الخوادم.**  
  
_هذا سيساعد في التنقل وفهم اللوحة_ 

تخطيط اللوحة
------------

اللوحة مقسمة إلى الأقسام التالية:

   العنوان-
                     
   تحذيرات: تحذيرات هامة تظهر إذا كانت درجة الحرارة أو الرطوبة تتجاوز الحدود المحددة  (25  للحرارة ، 60% للرطوبة) -
   
   مخطط درجة الحرارة والرطوبة:مخطط يظهر تغيرات درجة الحرارة والرطوبة مع مرور الوقت -
                     
   التنقل: مرر فوق نقاط البيانات لعرض التفاصيل،استخدم أدوات التكبير والتمرير لاستكشاف البيانات-
                     
   دليل المستخدم -

التفاعل مع اللوحة
-----------------

   مرر فوق نقاط البيانات لعرض التفاصيل-
   استخدم أدوات التكبير والتمرير لاستكشاف البيانات-

ما تمثل البيانات
----------------

   درجة الحرارة بالدرجات مئوية (°C)-
   الرطوبة كنسبة مئوية (%)-

المشاكل
-------

إذا واجهت مشكلات، قم بالتحقق من اتصال الإنترنت الخاص بك وإعدادات الشبكة. اتصل بنا للحصول على الدعم الفني أو المساعدة [أرسل رسالة](mailto:enas.h.diab@gmail.com)  

ملاحظات
-------

نحن نقدر ملاحظاتك! يرجى إعلامنا إذا كانت لديك اقتراحات أو واجهت مشكلات مع اللوحة''',

                     style={'font-family': 'Arial, sans-serif', 'color': '#000',
                            'font-size': '16px', 'margin-top': '20px', 'text-align': 'right'},
                     ),
        html.Meta(
            name='viewport',
            content='width=device-width, initial-scale=1.0'
        )

    ])
])


'''Section 5: Email configuration'''
smtp_server = "smtp-relay.gmail.com"  # SMTP server address
smtp_port = 25
# smtp_username = ""
# smtp_password = ""

sender_email = "Dak.TempSensor@dakahlia.net"
recipient_email = "enas.h.diab@gmail.com"
subject = "Alert: Threshold Exceeded"
body = "Temperature/humidity have exceeded the threshold. Take action immediately!"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

'''Section 6: Email Alert Function'''
# # Function to send email alert


def send_email_alert():
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


temperature_threshold = 25
humidity_threshold = 60

'''Section 7: Gauge Figure Creation Function'''
# Define callback to update gauge figures


def create_gauge(value, title, threshold, unit=''):
    fig = go.Figure()

    # Define the gauge trace
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=value,
        # Include unit in the title
        title={'text': f'{title} ({value}{unit})'},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, threshold], 'tickwidth': 2, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, threshold / 2], 'color': 'lightblue'},
                {'range': [threshold / 2, threshold], 'color': 'lightcoral'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': threshold
            }
        },
        number={'font': {'size': 40, 'color': "darkblue"}, 'suffix': unit},
    ))

    # Customize layout
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=10, b=10, t=10),
    )

    return fig


'''Section 8: Dash Callbacks
Dash callbacks
Update Gauges Callback
Update Temperature and Humidity Plot Callback
Update Summary and Send Email Alert Callback
Update Temperature Distribution Plot Callback
Update Humidity Distribution Plot Callback'''


@app.callback(
    [Output('temperature-gauge', 'figure'),
     Output('humidity-gauge', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_gauges(n_intervals):
    data = sheet.get_all_records()
    most_recent_data = data[-1] if data else {}
    current_temperature = most_recent_data.get('Temperature', 'N/A')
    current_humidity = most_recent_data.get('Humidity', 'N/A')

    # Create gauge figures with units
    temperature_gauge = create_gauge(
        current_temperature, 'Temperature', temperature_threshold, '°C')
    humidity_gauge = create_gauge(
        current_humidity, 'Humidity', humidity_threshold, '%')

    return temperature_gauge, humidity_gauge


@app.callback(
    Output('temperature-humidity-plot', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    # Fetch data from  Google Sheets
    data = sheet.get_all_records()

    # Prepare the data for plotting
    df = pd.DataFrame(data)

    # Combine 'Date' and 'Time' into a single 'DateTime' column
    # df['DateTime'] =df(['Date'] + ' ' + df['Time'], format='%m/%d/%Y %I:%M:%S %p')
    df['Time'] = df['Time'].str.strip()  # Remove leading/trailing white spaces
    df['Time'] = df['Time'].str.replace(' AM', '').str.replace(
        ' PM', '')  # Remove " AM" or " PM" if present
    df['DateTime'] = pd.to_datetime(
        df['Date'] + ' ' + df['Time'], format='%m/%d/%Y %H:%M:%S')

    # Sort the data by the 'DateTime' column
    df = df.sort_values('DateTime')

    # Use 'DateTime' as the x-axis
    fig = px.line(df, x='DateTime', y=['Temperature', 'Humidity'],
                  title="Temperature and Humidity Monitoring", width=1500, height=600)
    fig.update_traces(
        hovertemplate='%{x|%Y-%m-%d %H:%M:%S}<br>%{y}')
    fig.update_layout(
        title_text="Temperature and Humidity Sensors data",
        title_font_size=24,  # Set the font size
        title_font_family='Arial, sans-serif',  # Set the font family
        title_x=0.5,  # Center the title
        title_y=0.95,  # Adjust vertical alignment
        title_xanchor='center',  # Center the title horizontally
        title_yanchor='top',  # Set the title position relative to the chart
        title_pad=dict(t=20, b=10),  # Adjust padding around the title
    )

    return fig


@app.callback(
    Output('summary-div', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_summary(n_intervals):
    data = sheet.get_all_records()
    most_recent_data = data[-1] if data else {}
    current_temperature = most_recent_data.get('Temperature', 'N/A')
    current_humidity = most_recent_data.get('Humidity', 'N/A')

    # Check thresholds and generate alert messages
    temperature_alert = (
        f"Alert: The Temperature is above the threshold of {temperature_threshold} °C!"
        if current_temperature is not None and current_temperature > temperature_threshold
        else None
    )

    humidity_alert = (
        f"Alert: The Humidity is above the threshold of {humidity_threshold}%!"
        if current_humidity is not None and current_humidity > humidity_threshold
        else None
    )

    # Send email alert if thresholds are exceeded
    if current_temperature > temperature_threshold or current_humidity > humidity_threshold:
        send_email_alert()

    # Create alert elements
    alert_elements = []
    if temperature_alert:
        alert_elements.append(
            html.P(temperature_alert, style={
                'padding': '20px',
                'background-color': '#f44336',
                'color': 'white',
                'font-size': '18px',
                'margin-top': '5px',
                'margin-bottom': '5px'
            }))

    if humidity_alert:
        alert_elements.append(html.P(humidity_alert,  style={
            'padding': '20px',
            'background-color': '#f44336',
            'color': 'white',
            'font-size': '18px',
            'margin-top': '5px',
            'margin-bottom': '5px'
        }))

      # Combine summary and alert elements
    return [*alert_elements]


@app.callback(
    Output('temperature-distribution-plot', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_temperature_distribution_plot(n_intervals):
    data = sheet.get_all_records()
    return plot_distribution(data, 'Temperature')

# Update the callback for the humidity distribution plot


@app.callback(
    Output('humidity-distribution-plot', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_humidity_distribution_plot(n_intervals):
    data = sheet.get_all_records()
    return plot_distribution(data, 'Humidity')


'''Section 9: Plot Distribution Function'''
# Define the plot_distribution function


def plot_distribution(data, variable_name):
    df = pd.DataFrame(data)
    fig = px.histogram(df, x=variable_name, nbins=20,
                       title=f'{variable_name} Distribution')
    fig.update_layout(
        title_text="Temperature and Humidity Sensors data",
        title_font_size=24,  # Set the font size
        title_font_family='Arial, sans-serif',  # Set the font family
        title_x=0.5,  # Center the title
        title_y=0.95,  # Adjust vertical alignment
        title_xanchor='center',  # Center the title horizontally
        title_yanchor='top',  # Set the title position relative to the chart
        title_pad=dict(t=20, b=10),)  # Adjust padding around the title
    return fig


'''Section 10: Run Dash App'''
if __name__ == '__main__':
    app.run_server(debug=True, host='10.1.0.29', port=8050)

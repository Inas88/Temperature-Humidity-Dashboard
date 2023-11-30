# Temperature-Humidity-Dashboard
## Overview

Welcome to the documentation for the Temperature and Humidity Monitoring Dashboard. This dashboard provides real-time monitoring of temperature and humidity data from an IT server room using Dash and Google Sheets.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
   - [Google Sheets Credentials](#google-sheets-credentials)
   - [Dependencies](#dependencies)
3. [Functions and Callbacks](#functions-and-callbacks)
   - [create_gauge Function](#create_gauge-function)
   - [Email Alert Function](#email-alert-function)
   - [Main Callbacks](#main-callbacks)
4. [Usage](#usage)
   - [Running the Dash App](#running-the-dash-app)
   - [Accessing the Dashboard](#accessing-the-dashboard)
5. [Customization](#customization)
   - [Custom Theme](#custom-theme)
   - [Layout Modification](#layout-modification)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

This documentation provides detailed information about the Temperature and Humidity Monitoring Dashboard, including setup instructions, code explanations, and usage guidelines.

---

## Setup

### Google Sheets Credentials

To interact with Google Sheets, the script requires API credentials. Follow these steps:

1. Go to the [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Sheets API for the project.
4. Create credentials (service account key) and download the JSON file.
5. Place the JSON file in the project directory and update the `credentials.json` reference in the code.

### Dependencies

Make sure to install the required Python packages using:

```bash
pip install -r requirements.txt

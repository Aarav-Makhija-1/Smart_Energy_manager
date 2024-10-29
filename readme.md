# Smart Energy Manager 💻⚡

A powerful and user-friendly application for monitoring and controlling energy usage on your computer. The **Smart Energy Manager** allows parents to set energy and time limits, monitor system performance in real-time, track applications, and provides child access management with built-in requests and permissions.

> **Note**: This project is currently in its **first prototype stage**. Feedback and contributions are highly welcome to improve functionality and stability.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Settings & Customization](#settings--customization)
- [License](#license)

---

## Project Overview

**Smart Energy Manager** is a Python-based application designed to help parents monitor and control energy usage on a computer. The program provides real-time monitoring of energy consumption, allows parents to set time and energy limits, and has a separate child interface where children can request access to specific applications. With a user-friendly design and a settings panel for customizing preferences, Smart Energy Manager is an ideal tool for balancing gaming or application usage with energy conservation.

---

## Features

### 🖥️ User Interface & Experience
- **Gradient Background**: A modern gradient background to enhance aesthetics.
- **Interactive Dashboard**: Provides an overview of energy and time limits, application monitoring, and session statistics.
- **Real-Time Monitoring**: Displays real-time energy consumption with charts and live data updates.

### 👨‍👩‍👧 Parental Control
- **Separate Parent & Child Logins**: Parents and children have separate login credentials, ensuring controlled access to the app.
- **Set Energy & Time Limits**: Allows parents to define limits for energy usage and session duration.
- **Request Management**: Children can request access to applications, which parents can approve or deny.

### 📊 Graphs & Analytics
- **Real-Time Energy Consumption Charts**: Visualize energy usage with interactive charts that update in real-time.
- **Session History Logging**: Track the start and end times of each session, allowing for better analysis of usage patterns.

### ⚙️ Settings & Customization
- **Settings Panel**: Allows customization of passwords, themes, and preferences.
- **Password Management**: Change the parent password directly from the settings panel.

---

## Installation

To install and run the **Smart Energy Manager**, follow these steps:

### Prerequisites
Ensure you have **Python 3.6+** installed. You’ll also need the following Python libraries:
- `psutil`: For system and energy monitoring
- `matplotlib`: For generating real-time graphs
- `ttkthemes`: For additional themes and enhanced UI

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/smart-energy-manager.git
    cd smart-energy-manager
    ```

2. **Install Required Libraries**:
    ```bash
    pip install psutil matplotlib ttkthemes
    ```

3. **Run the Application**:
    ```bash
    python smart_energy_manager.py
    ```

---

## Usage

After installing and running the application, follow these steps to get started:

1. **Login Screen**:
   - Choose either **Parent** or **Child** login.
   - Default credentials are:
     - **Parent**: Username: `parent`, Password: `parentpass`
     - **Child**: Username: `child`, Password: `childpass`

2. **Parent Dashboard**:
   - After logging in as a parent, set energy and time limits, view real-time charts, and manage child requests.
   - Use the **Settings Panel** to customize preferences or change passwords.

3. **Child Interface**:
   - Children can request access to specific applications, which will notify the parent for approval.

4. **Monitoring and Usage**:
   - The application will monitor energy consumption in real-time. If set limits are exceeded, it will automatically terminate specific applications.

---

## Screenshots

### Login Screen
![Login Screen](https://ibb.co/Yf7pHdT)

### Parent Dashboard
![Parent Dashboard](https://ibb.co/tJVk8y3)

### Real-Time Energy Monitoring
![Energy Monitoring](https://ibb.co/GJ39cKM)

---

## Settings & Customization

The **Settings Panel** allows you to:
- Change the **parent password**.
- Adjust **energy and time limits**.
- Customize the **theme** using additional themes provided by `ttkthemes`.

### Themes
You can easily change the theme to suit your preference

# Available themes: aquativo, black, blue, equilux, etc.
root = ThemedTk(theme="equilux")

Authors & Acknowledgments
Aarav Makhija - Initial work and code development
Special thanks to ChatGPT for assistance in generating parts of this README and code.
Issues & Support
For any issues, please open an issue on GitHub or contact me at makhijaaarav70@gmail.com

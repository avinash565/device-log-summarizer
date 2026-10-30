# Device Log Summarizer

A Python-based CLI application that cleans sensor readings, processes device telemetry data, generates device-wise summaries, and visualizes average temperatures using Matplotlib.

## Features

- Converts valid sensor readings into floating-point numbers.
- Removes `None`, negative, and invalid values.
- Clips sensor readings above 500 to 500.
- Reads device telemetry data from a CSV file.
- Groups records by device ID.
- Calculates total records, average temperature, and error count.
- Filters out devices with an average temperature above 80°C.
- Exports processed data into JSON format.
- Generates a bar chart of average device temperatures.
- Includes unit tests for Section 1.

## Tech Stack

- Python 3
- CSV
- JSON
- Matplotlib
- Unittest

## Project Structure

```text
device-log-summarizer/
│
├── data/
│   └── device_telemetry.csv
│
├── output/
│   ├── device_temperature_chart.png
│   └── summary.json
│
├── src/
│   ├── main.py
│   ├── section1_cleaning.py
│   ├── section2_processing.py
│   └── section3_visualization.py 
│
├── tests/
│   └── test_section1.py
│
├── PROMPT_LOG.md
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd device-log-summarizer
```

### 3. Install Required Library

```bash
pip3 install matplotlib
```

## How to Run

Run the complete project using:

```bash
python3 src/main.py
```

This executes all three sections:

1. Sensor Data Cleaning
2. CSV Data Processing
3. Data Visualization

## Run Unit Tests

To execute the unit tests, run:

```bash
python3 -m unittest discover -s tests -v
```

## Sample Input

The project uses `data/device_telemetry.csv` containing:

| Device ID | Status | Temperature |
|---|---|---:|
| DEV_A | ACTIVE | 65.5 |
| DEV_A | WARNING | 75.2 |
| DEV_A | ERROR | 85.7 |
| DEV_B | ACTIVE | 90.5 |
| DEV_B | ERROR | 95.8 |
| DEV_C | ACTIVE | 40.3 |
| DEV_C | ERROR | 50.6 |

## Output

The application generates:

- **summary.json:** Contains device-wise summary information.
- **device_temperature_chart.png:** Displays average temperature for each eligible device as a bar chart.

Devices with an average temperature above 80°C are excluded from the summary.

## AI Usage

AI assistance was used in Section 3 for generating and improving the Matplotlib visualization script.

The prompts, review, and improvements are documented in `PROMPT_LOG.md`.

## Author

**Avinash Kumar Yadav**
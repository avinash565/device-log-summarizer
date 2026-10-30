
from section1_cleaning import clean_sensor_readings
from section2_processing import process_device_data
from section3_visualization import generate_chart


def main():

    # Section 1: Data Cleaning
    print("\n========== SECTION 1: DATA CLEANING ==========")

    readings = [10, "20", 30.5, None, -5, "abc", 600]

    cleaned_readings = clean_sensor_readings(readings)

    print("Original Readings:", readings)
    print("Cleaned Readings:", cleaned_readings)

    # Section 2: CSV Processing
    print("\n========== SECTION 2: CSV PROCESSING ==========")

    process_device_data(
        "data/device_telemetry.csv",
        "output/summary.json"
    )

    # Section 3: Data Visualization
    print("\n========== SECTION 3: DATA VISUALIZATION ==========")

    generate_chart("output/summary.json")


if __name__ == "__main__":
    main()

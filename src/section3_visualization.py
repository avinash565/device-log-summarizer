
import json
import matplotlib.pyplot as plt


def generate_chart(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        if not data:
            print("No device data available to generate chart.")
            return

        device_ids = [item["device_id"] for item in data]
        temperatures = [item["average_temperature"] for item in data]

        plt.figure(figsize=(9, 6))

        bars = plt.bar(device_ids, temperatures)

        plt.title("Average Temperature by Device")
        plt.xlabel("Device ID")
        plt.ylabel("Average Temperature (°C)")

        plt.bar_label(bars, fmt="%.2f", padding=3)

        plt.tight_layout()

        plt.savefig("output/device_temperature_chart.png")

        print("Chart saved successfully!")

        plt.show()

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Error: Invalid JSON data - {error}")


if __name__ == "__main__":
    generate_chart("output/summary.json")


import csv
import json
from collections import defaultdict


def process_device_data(csv_file, json_file):
    devices = defaultdict(lambda: {
        "total_records": 0,
        "total_temperature": 0.0,
        "valid_temperatures": 0,
        "error_count": 0
    })

    try:
        with open(csv_file, "r", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {"device_id", "status", "temperature"}

            if not required_columns.issubset(reader.fieldnames or []):
                raise ValueError("CSV is missing required columns.")

            for row in reader:
                device_id = row["device_id"].strip()
                status = row["status"].strip().upper()

                if not device_id:
                    continue

                devices[device_id]["total_records"] += 1

                if status == "ERROR":
                    devices[device_id]["error_count"] += 1

                try:
                    temperature = float(row["temperature"])

                    if temperature < 0:
                        continue

                    devices[device_id]["total_temperature"] += temperature
                    devices[device_id]["valid_temperatures"] += 1

                except (ValueError, TypeError):
                    continue

        results = []

        for device_id, data in devices.items():

            if data["valid_temperatures"] == 0:
                continue

            average = (
                data["total_temperature"] /
                data["valid_temperatures"]
            )

            # Exclude devices with average temperature above 80.0
            if average > 80.0:
                continue

            results.append({
                "device_id": device_id,
                "total_records": data["total_records"],
                "average_temperature": round(average, 2),
                "error_count": data["error_count"]
            })

        with open(json_file, "w") as file:
            json.dump(results, file, indent=4)

        print("\nDEVICE SUMMARY")
        print("-" * 65)
        print(f"{'Device ID':<15}{'Total Records':<18}{'Avg Temp':<15}{'Errors'}")
        print("-" * 65)

        for device in results:
            print(
                f"{device['device_id']:<15}"
                f"{device['total_records']:<18}"
                f"{device['average_temperature']:<15}"
                f"{device['error_count']}"
            )

        print("-" * 65)
        print(f"\nJSON saved successfully: {json_file}")

    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_file}")

    except (ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    process_device_data(
        "data/device_telemetry.csv",
        "output/summary.json"
    )

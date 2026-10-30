
def clean_sensor_readings(readings):
    cleaned_data = []

    for value in readings:
        if value is None:
            continue

        try:
            number = float(value)

            if number < 0:
                continue

            if number > 500:
                number = 500

            cleaned_data.append(number)

        except (ValueError, TypeError):
            continue

    return cleaned_data


# Test cases
if __name__ == "__main__":
    readings = [10, "20", 30.5, None, -5, "abc", 600]

    result = clean_sensor_readings(readings)

    print("Original readings:", readings)
    print("Cleaned readings:", result)

# main.py
import csv
from convertor.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from convertor.distance import convert_distance

def convert_temperature_and_distance(input_file, output_file, target_unit_temp, target_unit_dist):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            temperature = int(row['Reading'][:-2])
            if '°C' in row['Reading']:
                converted_temp = celsius_to_fahrenheit(temperature) if target_unit_temp == 'F' else temperature
            elif '°F' in row['Reading']:
                converted_temp = fahrenheit_to_celsius(temperature) if target_unit_temp == 'C' else temperature
            else:
                converted_temp = temperature

            converted_dist = convert_distance(row['Distance'], target_unit_dist)

            row['Reading'] = f"{converted_temp}°{target_unit_temp}"
            row['Distance'] = f"{converted_dist}{target_unit_dist}"
            writer.writerow(row)

convert_temperature_and_distance('input.csv', 'output.csv', 'C', 'ft')

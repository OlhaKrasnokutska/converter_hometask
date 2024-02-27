def convert_distance(distance, target_unit):
    if 'm' in distance:
        return int(float(distance[:-1]) * 3.28084) if target_unit == 'ft' else int(distance[:-1])
    elif 'ft' in distance:
        return int(float(distance[:-2]) * 0.3048) if target_unit == 'm' else int(distance[:-2])
    else:
        return float(distance)
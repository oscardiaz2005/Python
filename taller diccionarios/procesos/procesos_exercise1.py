def meets_requirements(record):
    if (240 <= record["pedal_ground_distance"] <= 300 and
        160 <= record["crank_length"] <= 180 and
        240 <= record["saddle_length"] <= 275 and
        record["handlebar_length"] <= 50):
        return True
    else:
        return False
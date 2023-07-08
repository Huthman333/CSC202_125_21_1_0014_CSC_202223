#ADEWALE USMAN OGUNTOLA SOUND ANALYSIS
def simulate_sound_penetration_in_room(power,material,distance):
    """Calculates the intensity after attenuation"""
    attenuation = ROOM_MATERIALS[material]
    intensity = calculate_sound_intensity(power, distance)
    attenuated_intensity = intensity * (10**(-attenuation*distance))
    sound_level = calculate_sound_level(attenuated_intensity)
    return sound_level
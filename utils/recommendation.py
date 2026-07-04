def get_aqi_category(aqi):

    if aqi <= 50:
        return (
            "Good",
            "Air quality is excellent. Outdoor activities are safe."
        )

    elif aqi <= 100:
        return (
            "Satisfactory",
            "Air quality is acceptable. Sensitive people should take precautions."
        )

    elif aqi <= 200:
        return (
            "Moderate",
            "People with asthma should reduce prolonged outdoor exertion."
        )

    elif aqi <= 300:
        return (
            "Poor",
            "Wear a mask outdoors and avoid heavy exercise."
        )

    elif aqi <= 400:
        return (
            "Very Poor",
            "Stay indoors as much as possible. Use air purifiers if available."
        )

    else:
        return (
            "Severe",
            "Health emergency. Avoid going outside unless absolutely necessary."
        )
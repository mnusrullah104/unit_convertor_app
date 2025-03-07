import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

# Corrected conversion factors dictionary
conversion_factors = {
    "Length": {  # Removed space after "Length"
        "meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084
    },
    "Weight": {
        "grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
    }
}

# Conversion function
def convert_units(value, from_unit, to_unit, category):
    if category in ["Length", "Weight"]:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value
    return None

# Streamlit App UI
st.title("Unit Converter")
st.write("Convert units of Length, Weight, and Temperature easily.")

# Category selection
category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])

if category:
    units = list(conversion_factors[category].keys())  # No KeyError now
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)
    
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    
    if st.button("Convert"):
        if from_unit == to_unit:
            st.warning("Please select different units to convert.")
        else:
            result = convert_units(value, from_unit, to_unit, category)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

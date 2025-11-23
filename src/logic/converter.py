class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f, format_output=True):
        result = (f - 32) * 5 / 9
        if format_output:
            return f"{f} °F = {result:.2f} °C"
        return result
    
    @staticmethod
    def celsius_to_fahrenheit(c, format_output=True):
        result = c * 9 / 5 + 32
        if format_output:
            return f"{c} °C = {result:.2f} °F"
        return result

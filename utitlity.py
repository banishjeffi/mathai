import google.generativeai as genai

print("Google API key ==>",key)

genai.configure(api_key = "AIzaSyC6zEe1IMBGSvq5QfOrci-1KLO2Ztkc1Bk")

def load_model():
    model = genai.GenerativeModel('gemini-pro')
    return model

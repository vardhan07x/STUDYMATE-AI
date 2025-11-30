from googlegenerativeai import configure, GenerativeModel

class StudyMateAgent:

    def __init__(self, api_key):
        configure(api_key=api_key)
        self.model = GenerativeModel("gemini-1.5-flash-latest")

    def reply(self, user_text):
        response = self.model.generate_content(user_text)
        return response.text

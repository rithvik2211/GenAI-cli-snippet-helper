from dotenv import load_dotenv
import os
import sys
import google.generativeai as genai
import platform

load_dotenv()

class CustomError(Exception):   
  def __init__(self, message, code):
      self.message = message
      self.code = code
      super().__init__(self.message, self.code)

# print(os.environ["GEMINI_API_KEY"])

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)


# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

def vadlidate():
   if len(sys.argv)>3:
      print("Use:-- gen -h to know more")
      raise CustomError("Cannot pass more than 3 aruguments")

def commands():
   if sys.argv[1] == "-h":
      print("""
gen -h  --help
gen -setup  --setup your GEMINI_API_KEY
gen -i "[COMMAND]" --get explanation on your command
gen "[COMMAND]" --use to search for terminal commands 
""")
      exit()
   

def main():
    vadlidate()
    commands()


    os_name = platform.system()
    response = model.generate_content(f"give possible methods to {sys.argv[1]} without any explanation. Operating System: {os_name}")
    print("Try using follwing commands.")
    print(response.text)

if __name__ == "__main__":
    try:
      main()
    except Exception as error:
       print(error)

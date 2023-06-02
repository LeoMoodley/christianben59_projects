from googletrans import Translator, LANGUAGES
## Imports the API that will translate between languages
#Starts the translator
translator = Translator()

def translate_text(text):
    #Function responsible for converting the text between languages
    translation = translator.translate(text, dest='es')
    
    # Prints the newly translated text
    print("Original text:", text)
    print("Translated text:", translation.text)

 #Takes the users input and converts it to spanish   
def main():
    text = input("Enter text to translate to Spanish: ")
    translate_text(text)
#Starts the program
if __name__ == "__main__":
    main()

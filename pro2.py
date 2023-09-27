#Programa en python que cuenta cuanta palabras tiene la oracion.
#Autor: Ph.D. Aldo Gonzalez Vazquez
#Fecha: 27/09/2023
#Version: 1.0
#bytesroboticmx@gmail.com
import nltk
nltk.download('punkt')  # Descargar los datos necesarios para NLTK

from nltk.tokenize import word_tokenize

def tokenize_sentence(sentence):
    # Tokenizar la oración en palabras individuales
    words = word_tokenize(sentence)
    return words

# Oración de ejemplo
input_sentence = "NLTK es una biblioteca de procesamiento de lenguaje natural."

# Llamar a la función para tokenizar la oración
tokenized_words = tokenize_sentence(input_sentence)

# Contar las palabras tokenizadas
word_count = len(tokenized_words)

# Imprimir la cantidad de palabras
print(f"La oración tiene {word_count} palabras.")

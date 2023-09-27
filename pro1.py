#Programa que utiliza la biblioteca NLTK para realizar el análisis de texto simple.
#Autor: Ph.D. Aldo Gonzàlez Vàzquez
#Fecha: 20/08/2019
#Versión: 1.0
#Correo: bytesroboticmx@gmail.com
import nltk
nltk.download('punkt') #Descarga los datos necesarios para el análisis de texto

from nltk.tokenize import word_tokenize #Importa las funciones para tokenizar texto

#Crea la función para tokenizar una oración

def tokenize_sentence(sentence):
    #Tokeniza una oración en palabras individuales
    words = word_tokenize(sentence)
    return words

#oracion de ejemplo
input_sentence = "NLTK es una biblioteca de Python para el procesamiento de lenguaje natural."

#Llama la funcion para tokenizar la oración
tokenize_words = tokenize_sentence(input_sentence)

#Imprime la lista de palabras tokenizadas
print("Palabras tokenizadas: ")
for word in tokenize_words:
    print(word)



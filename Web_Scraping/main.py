import requests
import bs4
import lxml


"""
resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
print(type(resultado))
"""
#nos imprime el codigo fuente en una cadena de texto
"""
print(resultado.text)
"""
"""
#con BeautifulSoup nos permite navegar entre los elementos
sopa = bs4.BeautifulSoup(resultado.text , "lxml")

print(sopa)
"""
#Se recibe en forma de lista
"""
print(sopa.select("title"))
"""
#Nos imprime el numero de elementos que estan el la lista
"""
print(len(sopa.select("p")))
"""
#Con .getText() podemos sacar el texto sin etiquetas
"""
print(sopa.select("title")[0].getText())
"""
"""
parrafo_especial = sopa.select("p")[3].getText()
print(parrafo_especial)
"""

#Caracteres especiales
"""
" soup.select("div") : Todos los elemetos con la etiqueta "div"
# soup.select("#estolo_4") : Elementos que  contengan id="estilo_4"
. soup.select(".columna_der") : Elementos que contengan class="columna_der"
(ESPACIO) soup.select("div span") : Cualquier elemento llamado "spam" dentro de un elemento div
> soup.select("div>span") : Cualquier elemnto llamado "span" directamente dentro de un elemento "div", sin nada en medio

"""
"""
resultado2 = requests.get("https://web.archive.org/web/20211206213403/https://escueladirecta.com/blog")
print(type(resultado2))
sopa2 = bs4.BeautifulSoup(resultado2.text , "lxml")
#columna_lateral = sopa2.select(".sidebar.section")[0]

columna_lateral = sopa2.select(".content p")
print(columna_lateral)
for p in columna_lateral:
    print(p.getText())
"""
"""
resultado2 = requests.get("https://web.archive.org/web/20211206202852/https://escueladirecta.com/courses")
print(type(resultado2))
sopa2 = bs4.BeautifulSoup(resultado2.text , "lxml")
imagenes = sopa2.select(".course-box-image")
print(imagenes)

for i in imagenes:
    print(i)
"""
#imagen codificada

#Bucle para sacar todas las imagenes
"""
numero = 0
for img in imagenes:

    imagen = sopa2.select(".course-box-image")[numero]["src"]
    imagen_curso = requests.get(imagen)
    f = open(f"mi imagen{numero}.jpg" , "wb")
    print(imagen)
    f.write(imagen_curso.content)
    f.close()
    numero +=1
"""
#explorar varias paginas

url_base = "https://books.toscrape.com/catalogue/page-{}.html"
#lista de 4 o 5 estrellas
titulos_rating_alto = []

for pagina in range(1,51):
#crear sopa en cada página
    resultado2 = requests.get(url_base.format(pagina))
    sopa2 = bs4.BeautifulSoup(resultado2.text , "lxml")
    libros = sopa2.select(".product_pod")
    for libro in libros:
        #chequear que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            titulo_libro = libro.select("a")[1]["title"]
            titulos_rating_alto.append(titulo_libro)
        else:
            continue
for l in titulos_rating_alto:
    print(l)

"""
for i in range(0,51):
    resultado2 = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    print(type(resultado2))
    sopa2 = bs4.BeautifulSoup(resultado2.text , "lxml")
    stars = sopa2.select(".product_pod .star-rating Five h3")['value']
    stars_5 =
    print(imagenes)
"""
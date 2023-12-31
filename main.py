import matplotlib.pyplot as plt
import math
from numpy import linspace

# reduce(lambda x,y: x+y,liste) = sum(liste)
# Beide summiert die an Liste gehörige Elemente nacheinander.

# Mittelwert berechnen
# Bei der Mittelwertberechnung tritt im Gegensatz zu R bei Outputs eine Differenz auf, weil R Programmierungssprache berechnet den Mittelwert anders als hier gemacht wurde.
def getmw(l):
    return sum(l)/len(l)

# Varianz
def var(l):
    l = list(map(lambda x: (x-getmw(l))**2,l))
    return sum(l)/(len(l)-1)

# Kovarianz
def cov(la,lb):
    return sum( list(map(lambda a,b: (a-getmw(la))*(b-getmw(lb)),la,lb)) )/(len(la)-1)

# Regression Oberklasse, die uns ermöglicht, darin gesteckte Funktionen von Regression zu benutzen.
class Regression:
    def __init__(self,x,y,titlex=None,titley=None):
        self.x = x
        self.y = y
        self.titlex = titlex
        self.titley = titley
        self.__kontroll(self.x,self.y)
        self.b1=cov(self.x,self.y)/var(self.x)
        self.b0=getmw(self.y)-(self.b1*getmw(self.x))
    
    # Innere Funktion, die standardmäßige Kontrolle für die Benutzung der richtigen Daten durchführt.
    def __kontroll(self,x,y):
        if (not isinstance(x,list) and not all(isinstance(i,str) for i in x)) and (not isinstance(y,list) and not all(isinstance(i,str) for i in y)):
            raise TypeError()
        
        elif len(x) != len(y):
            raise IndexError()
        
    # Auf Regressiongsgerade liegenden Wert von parameterx finden
    def get_wert(self,parameterx):
        return self.b0+(self.b1*parameterx)
    
    # Quadrate von Abstände zwischen Behauptung und Realität nacheinander addieren.
    def get_residuen(self):
        return sum([math.pow(self.get_wert(i)-i,2) for i in self.y])
    
    # Alles Graphisch darstellen, man müsste am Ende diese Funkiton benutzen, um es zu visualisieren.
    def zeichnen(self):
        x = linspace(min(self.x),max(self.x))
        y = self.b0+(self.b1*x)
        plt.scatter(self.x,self.y)
        plt.plot(x,y,color="red")
        if isinstance(self.titlex,str) and isinstance(self.titley,str):
            plt.xlabel(self.titlex)
            plt.ylabel(self.titley)
        plt.show()
        

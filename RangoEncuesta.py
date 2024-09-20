class RangoEncuesta:
    
    """#
    Atributos
    #"""
    NumeroCasados = 0
    TotalOpinionCasados= 0
    NumeroSolteros = 0
    TotalOpinionSolteros = 0
    """#
    Metodo
    #""""
    
    """#
    MetodosGenerales
    #"""
    
    def darpromediorango(self):
        TotalOpiniones = (self.TotalOpnionCasados + self.TotalOpinionSolteros)
        TotalEncuestados =(self.NumeroCasados + self.NumeroSolteros)
        return TotalOpiniones/TotalEncuestados
    
    """#
    Metodos Casados
    #"""
    def AgregarOpinionCasados(self,opinion):
        self.NumeroCasados + 1
        self.TotalOpinionCasados += opinion
    
    def DarPromedioCasados(self):
        return self.NumeroCasados/self.TotalOpinionCasados
    
    def darNumeroCasados(self):
        return self.NumeroCasados
    
    def darTotalOpinionCasados(self):
        return self.TotalOpinionCasados
    
    Metodos Solteros
    def AgregarOpinionSolteros(self, opinion):
        self.numerosolteros + 1
        self.TotalOpinionSolteros +=opinion

    
    def DarPromedioSolteros(self):
        return self.NumeroSolteros/self.TotalOpinionSolteros
    
    def NumeroSolteros(self):
        return self.NumeroSolteros
    
    def TotalOpinionSolteros(self):
        return self.TotalOpinionSolteros
    
    

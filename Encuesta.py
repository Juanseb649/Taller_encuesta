from RangoEncuesta import RangoEncuesta
class Encuesta:
    
    Rango1 = RangoEncuesta()
    Rango2 = RangoEnceusta()
    Rango3 = RangoEncuesta()
    
    def AgregaropinionRango1Casado (self,Opinion):
        self.Rango1.AgregaropinionCasado(opinion)
    
    def AgregarOpinionRango2Soltero (self,opinion):
        self.Rango2.AgregarOpinionSoltero(opinion)
    
    def darpromedio(self):
        TotalRango1 = self.rango1.TotalOpinionCasados()+self.Rango1.DartotalOpinionSolteros()
        TotalRango2 = self.rango2.TotalOpinionCasados()+self.Rango2.DartotalOpinionSolteros()
        TotalRango3 = self.rango3.TotalOpinionCasados()+self.Rango3.DartotalOpinionSolteros()
    
    TotalRangos = TotalRango1+TotalRango2+TotalRango3
    
    TotalEncuestados1 = self.Rango1.TotalOpinionSolteros()+self.Rango1.DartotalopinionCasados()
    TotalEncuestados2 = self.Rango2.TotalOpinionSolteros()+self.Rango2.DartotalopinionCasados()
    TotalEncuestados3 = self.Rango3.TotalOpinionSolteros()+self.Rango3.DartotalopinionCasados()
    
    TotalEncuestados = TotalEncuestados1+TotalEncuestados2+TotalEncuestados3
    return TotalRangos/ TotalEncuestados

    def Darpromediocsados(self):
        TotalRango1= self.Rango1.TotalOpinionCasados()
        TotalRango2= self.Rango2.TotalOpinionCasados()
        TotalRango3= self.Rango3.TotalOpinionCasados()
        TotalRangoCasados = TotalRango1+TotalRango2+TotalRango3
        TotalCasados1 = self.rango1.darnumerocasados()
        TotalCasados2 = self.rango2.darnumerocasados()
        TotalCasados3 = self.rango3.darnumerocasados()
        TotalCasados = TotalCasados1+TotalCasados2+TotalCasados3
        return TotalRangoCasados/TotalCasados
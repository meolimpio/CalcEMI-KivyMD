import kivy
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 600)

class Calculator(MDApp):
    def build(self):
        return Builder.load_file('app.kv')
    
    def calcular(self, montante, pagamento_inicial, avaliacao, prazo):
        if montante.text != "" and avaliacao.text != "" and prazo.text != "":
            m = int(montante.text) - int(pagamento_inicial.text)
            a = float(avaliacao.text)/(12 * 100)
            t = float(prazo.text)*12
            emi = round(m * (a * (a + 1)**t)/((a + 1)**t - 1))
            self.root.ids.resultado.text = f"Seu resultado é {emi}"

if __name__ == '__main__':    
    Calculator().run()

from ocorrencia import Ocorrencia, Morador, Sindico, TipoDeOcorrencia
from ocorrencia_controller import OcorrenciaController

model = Ocorrencia()
controller = OcorrenciaController()
m = Morador("Nick", 123, 456, 20)
s = Sindico()
tipo = TipoDeOcorrencia("teste")
oc = Ocorrencia(1,m,s, "deu ruim", tipo)

controller.adicionar_ocorrencia(oc)
controller.busca_ocorrencias()
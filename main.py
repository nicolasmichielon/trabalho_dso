from ocorrencia import Ocorrencia, TipoDeOcorrencia
from ocorrencia_controller import OcorrenciaController
from pessoa_controller import PessoaController

model = Ocorrencia()
ocCon = OcorrenciaController()
peCon = PessoaController()
tipo = TipoDeOcorrencia("teste")
oc = Ocorrencia(1,m,s, "deu ruim", tipo)

ocCon.busca_ocorrencias()

peCon.adicionar_morador("Nick", 123, 456, 20)
peCon.adicionar_sindico("josh")
ocCon.adicionar_ocorrencia(oc)

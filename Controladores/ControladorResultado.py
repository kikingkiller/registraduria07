from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()

    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        laResultado=Resultado(self.repositorioResultado.findById(id))
        return laResultado.__dict__

    def update(self,id,infoResultado,id_mesa,id_candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.año=infoResultado["año"]
        elResultado.numeroMesa = infoResultado["numero_mesa"]
        elResultado.votosTotales=infoResultado["votos_totales"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)
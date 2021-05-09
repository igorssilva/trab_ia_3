from pyknow import *


class ClassifyAnimals(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print('O sistema é capaz de identificar os seguintes animais: baleia, morcego, ' +
              'humano, urso, cão, tubarão, arraia, baiacu, atum, jacaré, cobra, tartaruga, camaleão, pinguim, ' +
              'gavião, beija-flor, gaivota, sapo e salamandra.')
        yield Fact(ask='S')

    @Rule(Fact(ask='S'),
          NOT(Fact(classify=W())))
    def ask_identificar(self):
        self.declare(
            Fact(classify=input('Olá! Vamos identificar um animal? ')))

    @Rule(Fact(classify='N'))
    def nao_identificar(self):
        print('Tchau.')

    @Rule(Fact(classify='S'))
    def ask_branqueas(self):
        self.declare(Fact(branquea=input('O animal respira na água? ')))

    @Rule(Fact(branquea='S'))
    def ask_osso(self):
        self.declare(Fact(osseo=input('O peixe tem osso? ')))

    @Rule(Fact(branquea='S'), Fact(osseo='N'))
    def ask_peixe_achatado(self):
        self.declare(Fact(achatado=input('O peixe é achatado? ')))

    @Rule(Fact(branquea='S'), Fact(osseo='N'), Fact(achatado='S'))
    def e_arraia(self):
        print('O animal é uma arraia.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='S'), Fact(osseo='N'), Fact(achatado='N'))
    def e_tubarao(self):
        print('O animal é um tubarão.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='S'), Fact(osseo='S'))
    def ask_peixe_venenoso(self):
        self.declare(Fact(venenoso=input('O animal é venenoso? ')))

    @Rule(Fact(branquea='S'), Fact(osseo='S'), Fact(venenoso='S'))
    def e_baiacu(self):
        print('O animal é um baiacu.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='S'), Fact(osseo='S'), Fact(venenoso='N'))
    def e_atum(self):
        print('O animal é um atum.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'))
    def ask_amamenta(self):
        self.declare(Fact(amamenta=input('O animal é amamentado? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'))
    def ask_mamifero_aquatico(self):
        self.declare(Fact(aquatico=input('O animal é aquático? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='S'))
    def e_baleia(self):
        print('O animal é uma baleia.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'))
    def ask_mamifero_voa(self):
        self.declare(Fact(voa=input('O animal voa? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='S'))
    def e_morcego(self):
        print('O animal é um morcego.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='N'))
    def ask_bipede(self):
        self.declare(
            Fact(bipede=input('O animal anda primariamente sobre dois membros? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='N'), Fact(bipede='S'))
    def e_humano(self):
        print('O animal é um humano.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='N'), Fact(bipede='N'))
    def ask_domesticado(self):
        self.declare(Fact(domesticado=input('O animal é domesticado? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='N'), Fact(bipede='N'), Fact(domesticado='S'))
    def e_cao(self):
        print('O animal é um cão.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='S'), Fact(aquatico='N'), Fact(voa='N'), Fact(bipede='N'), Fact(domesticado='N'))
    def e_urso(self):
        print('O animal é um urso.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'))
    def ask_ovo_com_casca(self):
        self.declare(Fact(casca=input('O animal tem ovo com casca? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='N'))
    def ask_cauda(self):
        self.declare(Fact(cauda=input('O animal tem cauda? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='N'), Fact(cauda='S'))
    def e_salamandra(self):
        print('O animal é uma salamandra.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='N'), Fact(cauda='N'))
    def e_sapo(self):
        print('O animal é um sapo.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'))
    def ask_penas(self):
        self.declare(Fact(penas=input('O animal tem penas? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'))
    def ask_rasteja(self):
        self.declare(Fact(rasteja=input('O animal rasteja? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='S'))
    def e_cobra(self):
        print('O animal é uma cobra')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='N'))
    def ask_reptil_aquatico(self):
        self.declare(Fact(aquatico=input('O animal é aquático? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='N'), Fact(aquatico='S'))
    def e_tartaruga(self):
        print('O animal é uma tartaruga.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='N'), Fact(aquatico='N'))
    def ask_escamado(self):
        self.declare(Fact(escamado=input('O animal é escamado? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='N'), Fact(aquatico='N'), Fact(escamado='S'))
    def e_camaleao(self):
        print('O animal é uma camaleão.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='N'), Fact(rasteja='N'), Fact(aquatico='N'), Fact(escamado='N'))
    def e_jacare(self):
        print('O animal é um jacaré.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'))
    def ask_ave_voa(self):
        self.declare(Fact(voa=input('O animal voa? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='N'))
    def e_pinguim(self):
        print('O animal é um pinguim.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='S'))
    def ask_polinizador(self):
        self.declare(Fact(polinizador=input('O animal é polinizador? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='S'), Fact(polinizador='S'))
    def e_beijaflor(self):
        print('O animal é um beija-flor.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='S'), Fact(polinizador='N'))
    def ask_caca_mar(self):
        self.declare(Fact(caca_mar=input('O animal é marítimo? ')))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='S'), Fact(polinizador='N'), Fact(caca_mar='S'))
    def e_gaivota(self):
        print('O animal é uma gaivota.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(branquea='N'), Fact(amamenta='N'), Fact(casca='S'), Fact(penas='S'), Fact(voa='S'), Fact(polinizador='N'), Fact(caca_mar='N'))
    def e_gaviao(self):
        print('O animal é um gavião.')
        self.declare(Fact(aks_repeat='S'))

    @Rule(Fact(aks_repeat='S'))
    def ask_to_repeat(self):
        self.declare(Fact(repeat=input('Deseja identificar outro animal? ')))

    # Identifica outro animal
    @Rule(Fact(repeat='S'))
    def start_repeat(self):
        self.reset()
        self.declare(Fact(classify='S'))
        self.run()

    @Rule(Fact(repeat='N'))
    def end_run(self):
        print('Tchau.')


engine = ClassifyAnimals()
engine.reset()
engine.run()

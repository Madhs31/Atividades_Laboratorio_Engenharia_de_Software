class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.__notas = []

    def adicionar_nota(self, nota):
        if nota >= 0:
            self.__notas.append(nota)

    def media(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)


def test_calculo_media_aluno_sem_notas():
    aluno = Aluno("Joana")
    assert aluno.media() == 0.0

def test_calculo_media_com_notas():
    aluno = Aluno("João")
    aluno.adicionar_nota(10)
    aluno.adicionar_nota(8)
    assert aluno.media() == 9.0

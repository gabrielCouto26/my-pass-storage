from domain.constants import GET, SET


class SystemIO:
    def __init__(self) -> None:
        self.COMMAND = None
        self.KEY = None
        self.VALUE = None

    def validate_input(self):
        assert self.COMMAND, 'Comando não fornecido.'
        assert isinstance(
            self.COMMAND, str), 'Comando inválido. Use "set" ou "get".'
        assert self.COMMAND in [GET, SET], """
            Comando inválido. Use "set" ou "get"."""

        assert self.KEY, 'Chave não fornecida.'
        assert isinstance(self.KEY, str), 'Chave inválida. Use uma string.'
        assert len(self.KEY) < 10, """
            Chave inválida. Mais de 10 caracteres utilizados."""

        if self.COMMAND == 'set':
            assert self.VALUE, 'Valor não fornecido.'
            assert isinstance(self.VALUE, str)
            assert len(self.VALUE) < 50, """
                Valor inválido. Mais de 50 caracteres utilizados."""

        return self.COMMAND, self.KEY, self.VALUE

    def input(self):
        pass

    def output(self, result: str) -> None:
        if self.COMMAND == GET:
            print(f"Valor encontrado para {self.KEY}: {result}")
        elif self.COMMAND == SET:
            print(f"Valor armazenado para {self.KEY}")
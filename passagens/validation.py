def origem_destino_iguais(origem, destino, lista_erros):
    """
    Verifica se origem e destino são iguais
    :param origem: String
    :param destino: String
    :param lista_erros: Lista
    :return: lista_erros
    """
    if origem == destino:
        lista_erros['destino'] = 'Origem e destino não pode ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_erros):
    """
    Verifica se possui algum digito numerico
    :param valor_campo: String
    :param nome_campo: String
    :param lista_erros: Lista
    :return: lista_erros
    """
    if any(char.isdigit() for char in valor_campo):
        lista_erros[nome_campo] = 'Não inclua números neste campo'


def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    """
    Verifica se data de ida é maior que data de volta
    :param data_ida: String
    :param data_volta: String
    :param lista_erros: Lista
    :return: lista_erros
    """

    if data_ida > data_volta:
        lista_erros['data_volta'] = 'Data de volta não pode ser menor que a data de ida'


def data_ida_menor_data_hoje(data_ida, data_pesquisa, lista_erros):
    """
    Verifica se data de ida é maior que data de volta
    :param data_ida: String
    :param data_pesquisa: String
    :param lista_erros: Lista
    :return: lista_erros
    """

    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'Data de ida não pode ser menor que hoje'

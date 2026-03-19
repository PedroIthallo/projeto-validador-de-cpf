import re

# pymongo é opcional, suporte se instalado
try:
    import pymongo
except ImportError:  # pragma: no cover
    pymongo = None


def validar_cpf(cpf: str) -> bool:
    """Retorna True se o CPF for válido, False caso contrário.

    O argumento pode conter pontuação; apenas dígitos são considerados no
    cálculo.
    """
    cpf = re.sub(r"[^0-9]", "", cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True


# configurações do MongoDB (ajuste conforme necessário)
MONGO_URI = (
    "mongodb+srv://seu_usuario:sua_senha@cluster0.mongodb.net/"
    "?retryWrites=true&w=majority"
)
DB_NAME = "mydatabase"
COLLECTION_NAME = "usuarios"


def conectar_mongo(uri: str):
    """Retorna um cliente Mongo ou None se não for possível estabelecer.

    Se ``pymongo`` não estiver disponível, informa e retorna ``None``.
    """
    if pymongo is None:
        print("Aviso: pymongo não instalado; operação de banco será ignorada")
        return None
    try:
        return pymongo.MongoClient(uri)
    except Exception as exc:  # pragma: no cover
        print(f"Falha ao conectar ao MongoDB: {exc}")
        return None


def main():
    cpf = input("Digite o seu CPF (XXX.XXX.XXX-XX ou apenas números): ")
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return
    print("CPF válido!")

    cliente = conectar_mongo(MONGO_URI)
    if cliente:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        nome = input("Digite o seu nome de usuário: ")
        documento = {"cpf": re.sub(r"[^0-9]", "", cpf), "nome_usuario": nome}
        try:
            collection.insert_one(documento)
            print("Dados salvos no banco de dados.")
        except Exception as exc:  # pragma: no cover
            print(f"Erro ao salvar dados: {exc}")
    else:
        print("Sem conexão com banco, dados não foram salvos.")


if __name__ == "__main__":
    main()

from Startup import Startup
from StartupImpl import StartupImpl

# create
st1 = Startup('10004', 'Bom Jaboatão', 'Jaboatão')
st1.create(st1.getId(), st1.getNome(), st1.getCidade())

# read
# leitor = StartupImpl()
# print(leitor.read())

# update
# atualizador = StartupImpl()
# atualizador.update('10004', 'Boa Carpina', 'Carpina')

# delete
# deletador = StartupImpl()
# deletador.delete('10004')

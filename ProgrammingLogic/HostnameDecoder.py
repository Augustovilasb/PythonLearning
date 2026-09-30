# Desafio: Hostname Decoder
#
# O usuario digita um hostname no formato site-rackNN-srvNN
# Exemplo: dub-rack12-srv07
#
# Regra: tente sem abrir os outros exercicios. Uma etapa por vez: faz, roda, confere.
#
# ETAPAS
# 1. Entrada: peca o hostname, passe para minusculas e mostre
#    o tamanho, o primeiro e o ultimo caractere.
# 2. Quebrar: separe pelo "-". Se nao tiver exatamente 3 partes,
#    mostre "Invalid hostname!" e nao faca mais nada.
# 3. Validar: se alguma parte estiver vazia, mostre
#    "Invalid hostname! Empty part!". Use um for com bandeira.
# 4. Extrair (so se for valido):
#    - o site, em maiusculas
#    - o numero do rack, como numero (2 ultimos caracteres da segunda parte)
#    - o numero do servidor, como numero (2 ultimos caracteres da terceira parte)
# 5. Inverter e contar:
#    - o hostname invertido, feito com laco
#    - um "codigo": o invertido sem os tracos
#    - quantas vogais o hostname tem
# 6. Relatorio: mostre tudo com f-string.
#
# TESTE PRINCIPAL - digitando dub-rack12-srv07 tem que sair:
#
#   Hostname: dub-rack12-srv07
#   Length: 16
#   First: d | Last: 7
#   Site: DUB
#   Rack: 12
#   Server: 7
#   Reversed: 70vrs-21kcar-bud
#   Code: 70vrs21kcarbud
#   Vowels: 2
#
# TESTES DE ERRO
#   dub-rack12          -> Invalid hostname!
#   dub-rack12-srv07-x  -> Invalid hostname!
#   dub--srv07          -> Invalid hostname! Empty part!
#   DUB-RACK12-SRV07    -> o mesmo relatorio do teste principal
#
# EXTRA NIVEL CHEFE
#   Aceite varios hostnames separados por virgula e mostre o relatorio de cada um:
#   dub-rack12-srv07,lon-rack03-srv21


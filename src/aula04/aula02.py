class Argentina():
    def capital(self):
        print("Buenos aires e a capital da agentina")
    def lingua_oficial(self):
        print("o espanhol e a lingua oficial da argentina")
class Brasil():
    def capital(self):
        print("brasilia e a capital do brasil")
    def lingua_oficial(self):
        print("o portugues e a lingua oficial do brasil")

obj_arg = Argentina()
obj_bra = Brasil()
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()
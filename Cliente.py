from Usuario import Usuario


class Cliente(Usuario):

    def __init__(self, id, nombre, apellido, correo, contrasena,tel, direccion):
        super().__init__(id,nombre, apellido,correo, contrasena)
        self._telefono=tel
        self._direccion=direccion

    @property
    def tel(self):
     return self._tel

    @tel.setter
    def tel(self, tel):
        self._tel= tel

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self,direccion):
        self._direccion=direccion

    def registrar_usuario(self):
        super().registrar_usuario()
        self._tel=input("Ingrese el telefono del cliente")
        self._direccion=input("Ingrese la direccion del cliente")

    def ver_usuario(self):
        super().ver_usuario()
        print(f"Tel:{self._tel} Direccion:{self._direccion}")

    def iniciar_sesion(self):
        correo_val=input("Ingrese el correo registrado: ")
        contras_val=input("Ingrese la contraseña registrada:")

        if correo_val==self.correo and contras_val==self.contrasena:
            print(f"Bienvenido{self.nombre}")
            return True
        else:
            return False

    def bussiness_app (self, iniciar_sesion):
        init = iniciar_sesion()
        while init==True:
            print ("1. Calcular",
                   "2. Otra cosa: ",
                   "3. Salir")

            opc=int(input("Ingrese una opción"))

            if opc==1:
                print("Ver usuario")

            elif opc==2:
                print ("Otra cosa")
            elif opc==3:
                print ("Salir")

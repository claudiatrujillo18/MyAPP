from Cliente import Cliente

cliente1= Cliente(id=None,nombre=None,apellido=None,correo=None,contrasena=None,tel=None,direccion=None)

cliente1.registrar_usuario()

cliente1.bussiness_app(cliente1.iniciar_sesion(),cliente1.ver_usuario())

cliente1.ver_usuario()
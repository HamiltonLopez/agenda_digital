class InvalidEmailException(Exception):
    def __init__(self, message="La dirección de correo no es válida. Debe contener '@gmail.com'."):
        self.message = message
        super().__init__(self.message)

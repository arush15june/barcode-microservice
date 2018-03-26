from io import BytesIO
import pyqrcode

class IncorrectTypeException(Exception):
    pass

class CodeGenerator():
    types = ['qr']
    
    def code(self,code_type, data):
        if code_type not in self.types:
            return None
        if code_type == 'qr':
            return self.generate_qrcode(data);
                 

    @staticmethod
    def generate_qrcode(data): 
        code = pyqrcode.create(data)
        buf = BytesIO()
        code.svg(buf, scale=10)
        return buf.getvalue().decode()
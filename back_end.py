class NumberConverter:
    @staticmethod
    def dec_to_bin(dec):
        return bin(dec)[2:]

    @staticmethod
    def dec_to_hex(dec):
        return hex(dec)[2:].upper()

    @staticmethod
    def dec_to_oct(dec):
        return oct(dec)[2:]

    @staticmethod
    def bin_to_dec(bin_str):
        return int(bin_str, 2)

    @staticmethod
    def hex_to_dec(hex_str):
        return int(hex_str, 16)

    @staticmethod
    def oct_to_dec(oct_str):
        return int(oct_str, 8)
    
    @staticmethod
    def update_hex(hex_var, dec_var, oct_var, bin_var):
        try:
            dec = NumberConverter.hex_to_dec(hex_var.get())
            dec_var.set(dec)
            oct_var.set(NumberConverter.dec_to_oct(dec))
            bin_var.set(NumberConverter.dec_to_bin(dec))
        except ValueError:
            dec_var.set("")
            oct_var.set("")
            bin_var.set("")

    @staticmethod
    def update_dec(dec_var, hex_var, oct_var, bin_var):
        try:
            dec = int(dec_var.get())
            hex_var.set(NumberConverter.dec_to_hex(dec))
            oct_var.set(NumberConverter.dec_to_oct(dec))
            bin_var.set(NumberConverter.dec_to_bin(dec))
        except ValueError:
            hex_var.set("")
            oct_var.set("")
            bin_var.set("")

    @staticmethod
    def update_oct(oct_var, hex_var, dec_var, bin_var):
        try:
            dec = NumberConverter.oct_to_dec(oct_var.get())
            hex_var.set(NumberConverter.dec_to_hex(dec))
            dec_var.set(dec)
            bin_var.set(NumberConverter.dec_to_bin(dec))
        except ValueError:
            hex_var.set("")
            dec_var.set("")
            bin_var.set("")

    @staticmethod
    def update_bin(bin_var, hex_var, dec_var, oct_var):
        try:
            dec = NumberConverter.bin_to_dec(bin_var.get())
            hex_var.set(NumberConverter.dec_to_hex(dec))
            dec_var.set(dec)
            oct_var.set(NumberConverter.dec_to_oct(dec))
        except ValueError:
            hex_var.set("")
            dec_var.set("")
            oct_var.set("")


class LogicOperations:
    def __init__(self, system="BIN"):
        self.system = system

    def set_system(self, system):
        self.system = system

    def convert_to_decimal(self, value):
        """Convierte el valor ingresado a decimal desde el sistema seleccionado."""
        if self.system == "BIN":
            return NumberConverter.bin_to_dec(value)
        elif self.system == "HEX":
            return NumberConverter.hex_to_dec(value)
        elif self.system == "DEC":
            return int(value)
        elif self.system == "OCT":
            return NumberConverter.oct_to_dec(value)
        else:
            raise ValueError("Sistema no válido")

    def and_operation(self, a, b):
        """Operación lógica AND"""
        return a & b

    def or_operation(self, a, b):
        """Operación lógica OR"""
        return a | b

    def xor_operation(self, a, b):
        """Operación lógica XOR"""
        return a ^ b

    def nand_operation(self, a, b):
        """Operación lógica NAND"""
        return ~(a & b) & 0b1111  # Mantiene solo 4 bits

    def nor_operation(self, a, b):
        """Operación lógica NOR"""
        return ~(a | b) & 0b1111  # Mantiene solo 4 bits

    def not_operation(self, a):
        """Operación lógica NOT (unario)"""
        return ~a & 0b1111  # Mantiene solo 4 bits
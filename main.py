class LogicGate:

    def __init__(self, lbl):
        self.name = lbl
        self.output = None
        self.nextpin = None
        self.completedpins = False
    
    def __str__(self):
        return self.name

    def get_label(self):
        return self.name
        
    def get_output(self):
        self.output = self.perform_gate_logic()

        if self.nextpin:
            self.nextpin.get_output()
        
        if self.nextpin == None and self.completedpins:
            print(f"{self.name} Final Output is {self.output}")
        


class BinaryGate(LogicGate):

    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)

        self.pin_a = None
        self.pin_b = None
    
    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
        else:
            return self.pin_a.get_from().output

    def get_pin_b(self):
        if self.pin_b == None:
            self.completedpins = True
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
        else:
            if self.pin_b.get_from().output != None and self.pin_a.get_from().output != None and self.pin_b.get_from().completedpins:
                self.completedpins = True
            return self.pin_b.get_from().output

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print(self.output)


class AndGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
class NandGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
class XorGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
    
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a+b == 1:
            return 1 
        else:
            return 0
        
class NorGate(BinaryGate):

    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):

    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            self.completedpins = True
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            if self.pin.get_from().output != None and self.pin.get_from().completedpins:
                self.completedpins = True
            return self.pin.get_from().output

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print(self.output)


class NotGate(UnaryGate):

    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        
        fgate.nextpin = tgate
        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
    n1 = NotGate('sel')
    and1 = AndGate('and1') # sel & b

    and2 = AndGate('and2')
    c1 = Connector(n1, and2) #a
    
    or1 = OrGate('or1')
    c2 = Connector(and1, or1)
    c3 = Connector(and2, or1)
    
    n1.get_output()
    and1.get_output()

    
main()

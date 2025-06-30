class LogicGate:

    def __init__(self, lbl):
        self.name = lbl
        self.output = None
        self.nextpin = None

    def get_label(self):
        return self.name
        
    def get_output(self):
        self.output = self.perform_gate_logic()
        self.nextpin.get_output()


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
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
        else:
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
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_to().get_input()

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
    g7 = XorGate('G7') #sum1
    a1 = AndGate('A1') #carry1
    
    
    g1 = XorGate('G1(Carry Value)') #sum2 #difeern6t carry value
    a2 = AndGate('A1(Carry Value)') #carry2 #different carry value
    
    o1 = OrGate('O1') 
    
    c1 = Connector(g7,g1)
    c2 = Connector(g7,a2)
    c3 = Connector(a2,o1)
    c3 = Connector(a1,o1)
    print(f"{o1.get_output()}{g1.get_output()}")
    

main()

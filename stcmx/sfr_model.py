

class SFRModel:
    """Special Function Register Configuration Model"""

    def __init__(self, name, addr, region, def_val, desc):
        self.name = name
        self.addr = addr
        self.region = region
        self.def_val = def_val
        self.val = def_val
        self.desc = desc
        self.assignment = None

    def set_bit(self, bit, offset):
        """Set bit"""
        self.val &= 0xFF - (0B1 << offset)
        self.val |= bit << offset

    def set_bits(self, value, mask, offset):
        """Set bits in specified offset """
        self.val &= 0xFF - (mask << offset)
        self.val |= value << offset

    def get_bits(self, mask, offset):
        """Get bits in specified offset """
        tmp = self.val & (mask << offset)
        return tmp >> offset

    def output_code(self, comment = False, comment_lang = 'en', force = False):
        """Generate C code for this SFR"""
        if (self.val != self.def_val) \
                or self.assignment is not None \
                or force:
            if comment:
                print("    # [%4XH,%1d,0x%02X]: %s" % (self.addr, self.region, self.def_val, self.desc[comment_lang]))
            if self.assignment is not None:
                print("    %-10s = %s;" % (self.name, self.assignment))
            else:
                print("    %-10s = 0x%02X;" % (self.name, self.val))

    def reset(self):
        """Reset value to default"""
        self.val = self.def_val

    def is_clean(self):
        """Current value equals to default"""
        return self.val == self.def_val
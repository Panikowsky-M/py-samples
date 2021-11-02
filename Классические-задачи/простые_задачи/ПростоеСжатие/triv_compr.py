from sys import getsizeof

class CompressedGene:
    def __init__(self,gene: str) -> None:
        self._compress(gene)

    def _compress(self,gene: str) -> None:
        self.bit_string: int = 1
        for nucleotid in gene.upper():
            self.bit_string <<= 2       # Заполняем строку - складываем нуклеотид (с.6)
            if nucleotid == "A" :       # с пустой (битовой) строкой, затем сдвигаем 
                self.bit_string |= 0b00 # его в начало строки (с.4), получается 
            elif nucleotid == "C" :     # __... ^ 01  = __01 __01 << = 0100
                self.bit_string |= 0b01
            elif nucleotid == "G" :
                self.bit_string |= 0b10
            elif nucleotid == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide".format(nucleotid))
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0,self.bit_string.bit_length() - 1,2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00 :
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene == "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits".format(bits))
        return gene[::-1]
    
    def __str__(self) -> str:
        return self.decompress()
    
if __name__ == "__main__":
    original: str = "AGGACCTTCCTTAAGGCCCTTAT" * 2
    print( "original is {} bytes".format(getsizeof(original)) )
    compressed: CompressedGene  = CompressedGene(original)
    print( "compressed is {} bytes".format(getsizeof(compressed.bit_string)) )
    print(original)
    print(compressed)
    print(compressed.decompress())
    print( "original and decompressed are the same: {}".format(original == compressed.decompress()) )

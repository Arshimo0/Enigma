class CipherLogic:
    def process_text(self, text, key):
        """
        Takes text and a numeric key.
        Returns the encrypted/decrypted string using XOR.
        """
        try:
            key_int = int(key)
            result = ''.join(chr(ord(char) ^ key_int) for char in text)
            return result
            
        except ValueError:
            return None
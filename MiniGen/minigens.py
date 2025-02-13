""" Main Script for our Generators"""

import secrets
import hashlib

from itertools import chain, product
from collections import OrderedDict
from pathlib import Path


class Data:
    """Used to store our Ascii Values"""

    DEFAULT_WORDLIST = Path(__file__).parent / "assets" / "wordList.txt"
    DEFAULT_FNLIST = Path(__file__).parent / "assets" / "firstnamesList.txt"
    DEFAULT_LNLIST = Path(__file__).parent / "assets" / "lastnamesList.txt"

    def __init__(self) -> None:
        """Attributes:
        AO_AV: Ascii aA-zZ.
        DO_AV: Ascii 0-9.
        AD_AV: Ascii aA0-zZ9.
        SP_AV: Ascii Special Characters.
        Emojis: A Bunch of Ascii Emojis.
        Emojis_Plus: A Bunch of Ascii Emojis plus dingbats and extras.
        Default_Wordlist: A sample list of words.
        Default_Fnlist: A sample list of first names.
        Default_Lnlist: A sample list of last names."""

        self.alpha = self.ascii_alpha()
        self.digits = self.ascii_digits()
        self.alphadigits = self.ascii_alphadigits()
        self.special = self.ascii_special()
        self.emojis = self.ascii_emojis()
        self.emojisplus = self.ascii_emojisplus()

    @staticmethod
    def ascii_alpha() -> list:
        """Returns Ascii character values for alphabet"""
        return [chr(i) for i in chain(range(65, 91), range(97, 123))]

    @staticmethod
    def ascii_digits() -> list:
        """Returns Ascii character values for digits"""
        return [chr(i) for i in range(48, 58)]

    def ascii_alphadigits(self) -> list:
        """Since we already have the alphabet and digits well just combine them"""
        return self.alpha + self.digits

    @staticmethod
    def ascii_special() -> list:
        """Returns Ascii character values for special characters"""
        return [
            chr(i)
            for i in chain(range(33, 48), range(59, 65), range(91, 97), range(123, 127))
        ]

    @staticmethod
    def ascii_emojis() -> list:
        """Returns Ascii character values for emojis"""
        return [
            chr(i) for i in chain(range(0x1F600, 0x1F64F + 1), range(0x1F5FA, 0x1F600))
        ]

    def ascii_emojisplus(self) -> list:
        """Since we already have some emojis well just add to it"""
        return self.emojis + [
            chr(i) for i in chain(range(0x1F900, 0x1F9FF), range(0x2700, 0x27C0))
        ]

    @staticmethod
    def read_wordlist(wordlist: Path) -> list:
        """Reads our word list appending them to an empty list"""
        words = []
        try:
            with open(wordlist, "r", encoding="utf-8") as f:
                for word in f.readlines():
                    words.append(word.strip())
            return words
        except FileNotFoundError:
            raise FileNotFoundError("missing wordlist files")


class Vault(OrderedDict):
    "Small Vault to Retain Our Generated data"

    def __init__(self) -> None:
        super().__init__()
        self.vault = self

    def add_tovault(self, key: str):
        """add to the set to ensure our data will be unique"""
        self.vault[key] = None

    def to_list(self):
        """Returns a list of keys"""
        return list(self.vault.keys())

    def to_txt(self, filename: str | Path):
        """Save Vault items to txt file

        Parameter:
            filename: The filename you would like to save to"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for idx, pw in enumerate(self.vault.keys()):
                    if idx < len(self.vault.keys()) - 1:
                        f.write(pw + "\n")
                    else:
                        f.write(pw)
        except (KeyError, PermissionError) as errors:
            raise errors


class PasswordGen(Data):
    """
    Basic Password Generator
    --------------------------------------------------------
    Create passwords of various lengths, amounts and strengths
    """

    def __init__(
        self, len_password: int = 12, amount_password: int = 1, strength: int = 1
    ):
        """Attributes:
        pw_length: Length of password; Defaults 12
        pw_amount: Amount of passwords; Defaults: 1
        pw_strength: Strength of password/s; [1-3] Defaults: 1
        """

        self.pw_length = len_password
        self.pw_amount = amount_password
        self.pw_strength = strength
        self.vault = Vault()

        super().__init__()

        self.password_map = {
            "Alpha": {
                "value": self.alpha,
                "Weak": self.weak_password,
                "Medium": self.medium_password,
                "Strong": self.strong_password,
            },
            "AlphaNum": {
                "value": self.alphadigits,
                "Weak": self.weak_password,
                "Medium": self.medium_password,
                "Strong": self.strong_password,
            },
            "Special": {
                "value": self.special,
                "Weak": self.weak_password,
                "Medium": self.medium_password,
                "Strong": self.strong_password,
            },
            "Fun": {
                "value": self.emojis,
                "Weak": self.weak_password,
                "Medium": self.medium_password,
                "Strong": self.medium_password,
            },
        }

        self.pw_types = [t for t in self.password_map.keys()]
        self.strengths = list(
            OrderedDict(
                (s, None)
                for t in self.pw_types
                for s in self.password_map[t].keys()
                if s != "value"
            )
        )

    def create_password(self, pw_type: str = "Alpha") -> str | list[str]:
        """Manager function to create our passwords

        Parameters:
            pw_type: Alpha, AlphaNum, Special, Fun. Defaults to Alpha
        """
        try:
            self.password_map[pw_type]
        except KeyError:
            raise KeyError("Check your entering a valid password type")

        self.pw_choice = pw_type

        def vault_enteries(function):
            for _ in range(1, self.pw_amount + 1):
                password = function()
                self.vault.add_tovault(password)

        pw_createmap = {
            1: self.strengths[0],  # Weak
            2: self.strengths[1],  # Medium
            3: self.strengths[2],  # Strong
        }

        function_to_run = self.password_map[pw_type][pw_createmap[self.pw_strength]]
        vault_enteries(function_to_run)

        r_vault = self.vault.to_list()
        return r_vault if self.pw_amount > 1 else r_vault[0]

    # Weak Pattern Family
    def weak_password(self) -> str:
        """Returns a weak password"""
        if self.pw_choice == "Special":
            ranges = self.alphadigits + self.special
            return "".join(secrets.choice(ranges) for _ in range(1, self.pw_length + 1))

        return "".join(
            secrets.choice(self.password_map[self.pw_choice]["value"])
            for _ in range(1, self.pw_length + 1)
        )

    # Medium Pattern Family
    def medium_password(self) -> str:
        """Returns a little bit stronger password"""
        ranges = (
            self.alphadigits + self.special + self.alpha
            if self.pw_choice != "Fun"
            else self.emojis + self.emojisplus
        )

        def shuffle_secure():
            secrets.SystemRandom().shuffle(ranges)

        shuffle_secure()
        return "".join(secrets.choice(ranges) for _ in range(1, self.pw_length + 1))

    # Strong Pattern Family
    def strong_password(self) -> str:
        """Returns a password based on 50/30/20"""
        alpha_len = int(round(self.pw_length * 0.5))
        special_len = int(round(self.pw_length * 0.3))
        ascii_len = self.pw_length - alpha_len - special_len

        strong = []
        strong += "".join(secrets.choice(self.alpha) for _ in range(alpha_len))
        strong += "".join(secrets.choice(self.special) for _ in range(special_len))
        strong += "".join(secrets.choice(self.digits) for _ in range(ascii_len))

        for _ in range(self.pw_amount):
            secrets.SystemRandom().shuffle(strong)

        return "".join(strong)

    # Strictly Words Family
    def word_password(self, wordlist: None | Path | str = None):
        """By default this will change password length to 4 basically hardcoded 4

        Parameter:
            wordlist: Enter the path of your wordlist txt. Default to DEFAULT_WORDLIST
        """
        if wordlist is not None:
            words = self.read_wordlist(wordlist)
        else:
            words = self.read_wordlist(self.DEFAULT_WORDLIST)

        self.pw_length = 4

        for _ in range(1, self.pw_amount + 1):
            for _ in range(self.pw_strength):
                secrets.SystemRandom().shuffle(words)
            password = "".join(
                secrets.choice(words) for _ in range(self.pw_length)
            ).lower()
            self.vault.add_tovault(password)

        return self.vault.to_list()


# Phone Gen
class PhoneNumberGen(Data):
    """
    Basic PhoneNumber Generator
    -
    Create various amounts of phone numbers in a few different formats

    Attributes:
        Style_Map(dict): A dictionary mapping of styles to their respective phone number formats.
        Seen: Empty dict to use to make sure we only get unquie numbers

    Methods:
        new_number(amount:int=1, sep:int=0) -> str | list[str]:
            Generates a new phone number or a list of phone numbers in the specified style.
            If you don't know which separator to use, check out the style_map attribute.
            Future details in method.

    """

    def __init__(self):
        self.style_map = {
            0: "{}-{}-{}",
            1: "({}){}-{}",
            2: "({}) {}-{}",
            3: "{} {} {}",
            4: "{}{}{}",
        }
        self.seen = Vault()

        super().__init__()
        self.n_ranges = self.digits

    def new_number(
        self, amount: int = 1, sep: int = 0, areacode: None | int = None
    ) -> str | list[str]:
        """Main Function to create New Number

        Parameters:
            Amount: The amount you would wish to create.
            Sep: The format you would like to use.
            Areacode: a specific area code you would like to create in"""
        try:
            self.style_map[sep]
        except KeyError:
            raise KeyError(
                "Check your seperator choice, make sure your passing a valid key 0-4. default to 0"
            )

        def create_numbers(areacode: int | None, sep: int):
            """Helper Function to Create Phone Number in a certain Format"""

            if areacode is not None:
                numbers = self.style_map[sep].format(
                    "".join(str(areacode)),
                    "".join([secrets.choice(self.n_ranges) for _ in range(3)]),
                    "".join([secrets.choice(self.n_ranges) for _ in range(4)]),
                )
                return numbers
            else:
                numbers = self.style_map[sep].format(
                    "".join([secrets.choice(self.n_ranges) for _ in range(3)]),
                    "".join([secrets.choice(self.n_ranges) for _ in range(3)]),
                    "".join([secrets.choice(self.n_ranges) for _ in range(4)]),
                )
                return numbers

        while len(self.seen) < amount:
            try:
                for _ in range(1, amount + 1):
                    phone_num = create_numbers(areacode, sep)
                    self.seen[phone_num] = None
            except KeyboardInterrupt:
                exit()

        return self.seen.to_list()


# Email Gen
class EmailGen(Data):
    """Email Generator"""

    def __init__(self, wordlist: None | Path | str = None) -> None:
        """Parameters:
        wordlist: Pass your own path to wordlist or use the default one"""

        super().__init__()
        self.domains_map = {
            1: "gmail.com",
            2: "yahoo.com",
            3: "aol.com",
            4: "hotmail.com",
        }
        self.email_vault = Vault()
        self.word_list = wordlist if wordlist is not None else self.DEFAULT_WORDLIST

    def create_emails(self, amount: int = 1, domain_choice: int = 1):
        """Parameters:
        amount: the amount of emails you want to create
        domainChoice: enter a valid key 1-4 defaults to 1"""
        try:
            domain = self.domains_map[domain_choice]
        except KeyError:
            raise KeyError("Might want to try a valid key 1-4")

        for _ in range(amount):
            word = secrets.choice(self.read_wordlist(self.word_list))
            email = word.lower() + "@" + domain
            self.email_vault.add_tovault(email)
        return self.email_vault.to_list()


# IpAddress Gen
class IpAddressGen(Data):
    """
    Basic IpAddress Generator
    """

    def __init__(self, void: None | list = None):
        """Parameters:
        void: a list to add to already voided ip addresses"""
        super().__init__()
        self.voided = ["127.00.00.0", "192.168.1.1"]
        self.oct_range = 255
        self.ip_vault = Vault()

        if isinstance(void, list):
            self.voided + void

    def create_addresses(self, amount: int = 1, start: None | int = None):
        """Main Function to create ranges of IP addresses"""
        address = [0, 0, 0, 0]
        while len(self.ip_vault.keys()) < amount:
            for _ in range(amount):
                if start is not None:
                    address[0] = start
                else:
                    address[0] = secrets.randbelow(self.oct_range)

                address[1] = secrets.randbelow(self.oct_range)
                address[2] = secrets.randbelow(self.oct_range)
                address[3] = secrets.randbelow(self.oct_range)
                ipaddy = ".".join(str(f) for f in address)
                if ipaddy not in self.voided:
                    self.ip_vault.add_tovault(ipaddy)
        return self.ip_vault.to_list()


# Hash Gen
class HashGen:
    """Basic Hash generator

    Generates a single hash

    Methods:
        hash: A manager to pass hash type to, to hash a file or string
    """

    def __init__(self, message: None | str = None, file: None | str | Path = None):
        """Parameters:
        Message: A string that will be encoded.
        File: An absolute file path will be read and have bytes returned."""

        self.hash_map = {
            "blake2b": self.blake2_516,
            "blake2s": self.blake2_256,
            "md5": self.md5,
            "sha224": self.sha2_224,
            "sha256": self.sha2_256,
            "sha384": self.sha2_384,
            "sha512": self.sha2_512,
            "sha3_224": self.sha3_224,
            "sha3_256": self.sha3_256,
            "sha3_384": self.sha3_384,
            "sha3_512": self.sha3_512,
        }

        self.available_hashes = [f for f in self.hash_map.keys()]

        self.hash_vault = Vault()
        self.hashed_vault = Vault()

        if message and not file:
            self.message = message.encode("utf-8")

        elif file and not message:
            self.filename = file
            self.message = self.load_file(file)

        else:
            raise ValueError("You must enter a message or a file")

    def load_file(self, file: str | Path) -> list[bytes]:
        """Reads an entire file and returns lines in bytes"""
        b = b""
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    line_bytes = line.encode("utf-8")
                    b += b" " + line_bytes
                self.hash_vault.add_tovault(b)
        except (FileExistsError, FileNotFoundError, PermissionError):
            raise FileNotFoundError("try passing a valid path")

        return self.hash_vault.to_list()

    def hash(self, hashtype: str = "md5", amessage: bool = False) -> str:
        """Hash a file, or a string thats been converted into bytes
        Parameters:
            hashtype: Can check available_hashes attribute defaults to md5

        """
        try:
            function = self.hash_map[hashtype]
        except KeyError:
            return KeyError("Try entering a valid hash type")

        if amessage:
            hashed = function(self.message)
            self.hashed_vault.add_tovault(hashed)
            return "".join(self.hashed_vault.to_list())

        # when amessage is False meaning your using a file
        for m in self.message:
            hashed = function(m)
            self.hashed_vault.add_tovault(hashed)
        return "".join(self.hashed_vault.to_list())

    def md5(self, message):
        """NOT RECOMMENDED"""
        return hashlib.md5(message).hexdigest()

    def sha2_224(self, message):
        """Secure Hashing"""
        return hashlib.sha224(message).hexdigest()

    def sha2_256(self, message):
        """Secure Hashing"""
        return hashlib.sha256(message).hexdigest()

    def sha2_384(self, message):
        """Secure Hashing"""
        return hashlib.sha384(message).hexdigest()

    def sha2_512(self, message):
        """Secure Hashing"""
        return hashlib.sha512(message).hexdigest()

    def sha3_224(self, message):
        """Secure Hashing"""
        return hashlib.sha3_224(message).hexdigest()

    def sha3_256(self, message):
        """Secure Hashing"""
        return hashlib.sha3_256(message).hexdigest()

    def sha3_384(self, message):
        """Secure Hashing"""
        return hashlib.sha3_384(message).hexdigest()

    def sha3_512(self, message):
        """Secure Hashing"""
        return hashlib.sha3_512(message).hexdigest()

    def blake2_256(self, message):
        """Fast and Secure Hashing"""
        return hashlib.blake2s(message).hexdigest()

    def blake2_516(self, message):
        """Fast and Secure Hashing"""
        return hashlib.blake2b(message).hexdigest()


# Name Gen
class NameGen(Data):
    """Create test names"""

    def __init__(self, amount: int = 1) -> None:
        super().__init__()
        self.firstnames = self.read_wordlist(self.DEFAULT_FNLIST)
        self.lastnames = self.read_wordlist(self.DEFAULT_LNLIST)
        self.fn_length = len(self.firstnames)
        self.ln_length = len(self.lastnames)
        self.amount = amount
        self.name_vault = Vault()

        self.name_gmap = {
            1: self.first_only,
            2: self.last_only,
            3: self.last_first,
            4: self.first_last,
            5: self.middle,
        }
        self.len_map = len(self.name_gmap.keys())

    def create_names(self, choice: int = 1):
        """Main function to create names

        Parameters:
            choice: Enter a valid key 1-5. Defaults to 1 which is first name"""
        if choice <= self.len_map:
            try:
                function = self.name_gmap[choice]
            except KeyError:
                raise KeyError("Try enter a valid key 1-5")
            creatednames = function()
            return creatednames

    def first_only(self) -> list:
        """Creates first names only"""
        if self.amount <= self.fn_length:
            for _ in range(self.amount):
                name = secrets.choice(self.firstnames)
                self.name_vault.add_tovault(name)
            return self.name_vault.to_list()

    def last_only(self) -> list:
        """Creates last names only"""
        if self.amount <= self.ln_length:
            for _ in range(self.amount):
                name = secrets.choice(self.lastnames)
                self.name_vault.add_tovault(name)
            return self.name_vault.to_list()

    def first_last(self) -> list:
        """Creates first and last names"""
        if self.amount <= self.ln_length and self.amount <= self.fn_length:
            while len(self.name_vault.keys()) < self.amount:
                for _ in range(self.amount):
                    name = f"{secrets.choice(self.firstnames)} {secrets.choice(self.lastnames)}"
                self.name_vault.add_tovault(name)
            return self.name_vault.to_list()

    def last_first(self) -> list:
        """Creates last and first name"""
        if self.amount <= self.ln_length and self.amount <= self.fn_length:
            for _ in range(self.amount):
                name = f"{secrets.choice(self.lastnames)} {secrets.choice(self.firstnames)}"
                self.name_vault.add_tovault(name)
            return self.name_vault.to_list()

    def middle(self) -> list:
        """Creates Full names"""
        if self.amount <= self.fn_length:
            for _ in range(self.amount):
                first = secrets.choice(self.firstnames)
                middle = secrets.choice(self.firstnames)
                if first != middle:
                    last = secrets.choice(self.lastnames)
                    name = f"{first} {middle} {last}"
                    self.name_vault.add_tovault(name)
            return self.name_vault.to_list()


# Wordlist Gen
class WordlistGen(Data):
    """Basic permutation generator"""

    def __init__(self, characters: str, minL: int = 1, maxL: int = 5) -> None:
        """Parameters:
        characters: which characters you would like to use
        minL: the minimum amount of characters to use
        maxL: the maximum amount of characters to use"""
        super().__init__()
        self.characters = characters
        self.min_l = minL
        self.max_l = maxL
        self.wordlist_vault = Vault()

    def create_wordlist(self) -> list:
        """Creates a premutation from characters"""
        for i in range(self.min_l, self.max_l + 1):
            for combo in product(self.characters, repeat=i):
                word = "".join(combo)
                self.wordlist_vault.add_tovault(word)
        return self.wordlist_vault.to_list()

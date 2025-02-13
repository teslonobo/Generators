""" Script for cli interface"""
import argparse
import pathlib
from textwrap import dedent
from Helpers.createSampleLists import *
from minigens import PasswordGen, PhoneNumberGen, HashGen,\
    NameGen, EmailGen, IpAddressGen, WordlistGen

pgName = Path(__file__).parent.stem

pgmDescript = dedent('''\
                    A toolbox for generating various types of data!
                Contains several base level generators, could be extended further.''')

pwDescript = dedent('''\
                    A tool for generating various forms of passwords! ''')

ipDesript = dedent('''\
                    A tool for generating various ipAddresses! ''')

phnDescript = dedent('''\
                    A tool for generating phone numbers in various formats! ''')

emailDescript = dedent('''\
                    A tool for generating email addresses from a word list, default is provided but can pass your own!''')

hashDescript = dedent('''\
                    A tool for generating hashes from words either from a single message or txt file!
                    With the ablity to hash an entire file at once or line by line.''')

nameDescript = dedent('''\
                    A tool for generating names from default first and last name txt files!''')

wordlistDescript = dedent('''\
                    A tool for generating wordlists from characters!''')
# Main parser
parser = argparse.ArgumentParser(prog=pgName,description=pgmDescript)
subparsers = parser.add_subparsers(dest="command",title='Available Generators')

# Password parser
password_gen = subparsers.add_parser("pw", help="Password generator",description=pwDescript)
passparser = password_gen.add_argument_group(title="Password generator")
passparser.add_argument('-l', metavar='--l', help='Length of password/s: Defaults: 12', type=int, default=12)
passparser.add_argument('-a', metavar='--a', help='Amount of password/s: Defaults: 1', type=int, default=1)
passparser.add_argument('-s', metavar='--s', help='Strength of password/s: Defaults: 1', type=int, default=1)
passparser.add_argument('-t', metavar='--t', help='Type of password/s: AlphaNum, Alpha, Special, Fun, Words Defaults: AlphaNum', type=str, default='AlphaNum')
passparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
passparser.add_argument('-wl', metavar='--wl', help='Save to a text file. Defaults: None',type=pathlib.Path)
passparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# Phone number parser
phoneparser_gen = subparsers.add_parser("pn", help="Phone Number generator",description=phnDescript)
phoneparser = phoneparser_gen.add_argument_group(title="Phone Number generator")
phoneparser.add_argument('-a', metavar='--a', help='Amount of phone number/s. Defaults: 1', type=int)
phoneparser.add_argument('-t', metavar='--t', help='Styling of format output. Defaults: 0', type=int, default=0)
phoneparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
phoneparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# IP address generator
ipparser_gen = subparsers.add_parser("ipa", help="IP Address generator",description=ipDesript)
ipparser = ipparser_gen.add_argument_group(title="IP Address generator")
ipparser.add_argument('-a', help='Amount of ip addresses Defaults: 1',type=int, default=1)
ipparser.add_argument('-s', help='Choose starting range Defaults: None',type=int, default=None)
ipparser.add_argument('-v', help='Enter a list of ip address to avoid Defaults: None',type=list, default=None)
ipparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
ipparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# Email address generator
email_gen = subparsers.add_parser("email", help="Email generator",description=emailDescript)
emailparser = email_gen.add_argument_group(title="Email Address generator")
emailparser.add_argument('-f', metavar='--f', help='File path of a file with words Defaults: None', type=pathlib.Path, default=None)
emailparser.add_argument('-a', metavar='--a', help='Amount of name/s. Defaults: 1', type=int,default=1)
emailparser.add_argument('-d', metavar='--d', help='Domains: gmail.com, yahoo.com, aol.com Defaults: 1', type=int,default=1)
emailparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
emailparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# HasH Generator
hash_gen = subparsers.add_parser("hash", help="Hash generator",description=hashDescript)
hashparser = hash_gen.add_argument_group(title="Hash generator")
hashparser.add_argument('-f', metavar='--f', help='File path of a file with words Dont use together with fn: Defaults: None', type=str, default=None)
hashparser.add_argument('-m', metavar='--m', help='Enter a message you want encoded: Defaults: None', type=str, default=None)
hashparser.add_argument('-t', metavar='--t', help='Type of hashing: blake2b, blake2s, md5, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512 Defaults: md5', type=str, default='md5')
hashparser.add_argument('-w', help='Use in combination with -m : Default: False', action='store_true')
hashparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
hashparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# Name Generator
name_gen = subparsers.add_parser('names',help='Name generator',description=nameDescript)
nameparser = name_gen.add_argument_group(title='Name generator')
nameparser.add_argument('-a', metavar='--a', help='Amount of name/s. Defaults: 1', type=int,default=1)
nameparser.add_argument('-t', metavar='--t', help='Format: FirstOnly, LastOnly, LastFirst, FirstLast, Middle [1-5] Defaults: 1', type=int,default=1)
nameparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
nameparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# Wordlist Generator
wordlist_gen = subparsers.add_parser('lists',help='Wordlist generator',description=wordlistDescript)
wordlistparser = wordlist_gen.add_argument_group(title='Wordlist generator')
wordlistparser.add_argument('-c', metavar='--c', help='Characters to use Defaults: abc123', type=str,default='abc123')
wordlistparser.add_argument('-min', metavar='--min', help='Minimum length for characters to join Defaults: 1', type=int,default=1)
wordlistparser.add_argument('-max', metavar='--max', help='Maximum length for characters to join Defaults: 5', type=int,default=5)
wordlistparser.add_argument('-q', help='Quiet Printouts. Defaults: False', action='store_true')
wordlistparser.add_argument('-o', metavar='--o', help='Save to a text file. Defaults: None',type=pathlib.Path)

# Parse arguments
args = parser.parse_args()
## ===================================
if args.command == 'pw':
    password_gen = PasswordGen()
    init_attributes = {'pw_length':args.l,
                       'pw_amount':args.a,
                       'pw_strength':args.s}
    for key, value in init_attributes.items():
        setattr(password_gen, key, value)
    if args.t != 'Words':
        password_gen.create_password(args.t)
    else:
        password_gen.word_password(args.wl)

    passwords = '\n'.join(password_gen.vault.to_list())
    if args.q:
        pass
    else:
        print(passwords)
    if args.o:
        password_gen.vault.to_txt(args.o)

if args.command == 'pn':
    pnumbers = PhoneNumberGen()
    pnumbers.new_number(args.a,args.t)
    phonenumbers = '\n'.join(pnumbers.seen.to_list())
    if args.q:
        pass
    else:
        print(phonenumbers)
    if args.o:
        pnumbers.seen.to_txt(args.o)

if args.command == 'ipa':
    ip_gen = IpAddressGen()
    if args.v:
        setattr(ip_gen,'void',args.v)
    ipadresses = ip_gen.create_addresses(args.a,args.s)
    if args.q:
        pass
    else:
        print('\n'.join(ipadresses))
    if args.o:
        ip_gen.ip_vault.to_txt(args.o)

if args.command == 'hash':
    hashgen = HashGen(args.m,args.f)
    hashes = hashgen.hash(args.t,args.w)
    if args.q:
        pass
    else:
        print(hashes)
    if args.o:
        hashgen.hashed_vault.to_txt(args.o)

if args.command == 'email':
    emailgen = EmailGen(args.f)
    emails = emailgen.create_emails(args.a,args.d)
    if args.q:
        pass
    else:
        print('\n'.join(emails))
    if args.o:
        emailgen.email_vault.to_txt(args.o)

if args.command == 'names':
    namegen = NameGen(args.a)
    names = namegen.create_names(args.t)
    if args.q:
        pass
    else:
        print('\n'.join(names))
    if args.o:
        namegen.name_vault.to_txt(args.o)

if args.command == 'lists':
    wordlistgen = WordlistGen(args.c,args.min,args.max)
    words = wordlistgen.create_wordlist()
    if args.q:
        pass
    else:
        print('\n'.join(words))
    if args.o:
        wordlistgen.wordlist_vault.to_txt(args.o)
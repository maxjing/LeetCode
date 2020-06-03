class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_hex(s):
            for c in s:
                if c not in '0123456789abcdefABCDEF':
                    return False
            return True

        def is_ipv4(s):
            l = s.split('.')
            if len(l) != 4:
                return False
            for section in l:
                if not section.isdigit() or not 0 <= int(section) < 256 or (len(section) > 1 and section[0]) == '0':
                    return False
            return True

        def is_ipv6(s):
            l = s.split(':')
            if len(l) != 8:
                return False
            for section in l:

                if len(section) == 0 or len(section) > 4 or not is_hex(section):
                    return False
            return True

        if is_ipv4(IP):
            return 'IPv4'
        elif is_ipv6(IP):
            return 'IPv6'
        else:
            return 'Neither'


'''
ipv4 validator:
1. check if len(arr) == 4, arr split by .
2. check if each section is digit and 0 <= section < 256
3. check leading zero, if len(section) > 1 and section[0] == 0 which is not valid

ipv6 validator:
1. len(arr) = 8
2. each section != 0 or len(section) > 4 or section is hex

'''
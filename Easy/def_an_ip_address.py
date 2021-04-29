class Solution(object):
    def defangIPaddr(self, address):
        ip_address = []
        for i in range(len(address)):
            if address[i] == '.':
                ip_address.append('[{}]'.format(address[i]))
            else:
                ip_address.append(address[i])
        return ''.join(ip_address)
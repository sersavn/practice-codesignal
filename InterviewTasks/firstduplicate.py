lis = list()
def firstDuplicate(a):
        for elements in a:
                if elements in lis:
                        return(elements)
                        break
                else:
                        lis.append(elements)
                        continue
        return -1

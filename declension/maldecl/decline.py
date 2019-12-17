import declension.maldecl.plural
import declension.maldecl.singular


def decline(noun):
    # The pair of generators which we'll use
    decliners = {
        "Singular": None,
        "Plural": None
    }

    # Pick a generator based on the noun's shape #
    #print("decliner: noun = {0}\n\tisANStem = {1}\n\tisAMStem = {2}\n\tisRuhStem = {3}\n\tisDuhStem = {4}".format(noun, isANStem(noun), isAMStem(noun), isRuhStem(noun), isDuhStem(noun)))

    if isANStem(noun):
        decliners["Singular"] = declension.maldecl.singular.ANStem.ANStem()
        decliners["Plural"] = declension.maldecl.plural.ANStem.ANStem()

    elif isAMStem(noun):
        decliners["Singular"] = declension.maldecl.singular.AMStem.AMStem()
        decliners["Plural"] = declension.maldecl.plural.AMStem.AMStem()

    elif isRuhStem(noun):
        decliners["Singular"] = declension.maldecl.singular.RuhStem.RuhStem()
        decliners["Plural"] = declension.maldecl.plural.RuhStem.RuhStem()

    elif isDuhStem(noun):
        decliners["Singular"] = declension.maldecl.singular.DuhStem.DuhStem()
        decliners["Plural"] = declension.maldecl.plural.DuhStem.DuhStem()

    elif isALStem(noun):
        decliners["Singular"] = declension.maldecl.singular.ALStem.ALStem()
        decliners["Plural"] = declension.maldecl.plural.ALStem.ALStem()

    else: # Must be a vowel stem
        decliners["Singular"] = declension.maldecl.singular.VowelStem.VowelStem()
        decliners["Plural"] = declension.maldecl.plural.VowelStem.VowelStem()

    declensions = {
        "Singular": decliners["Singular"].decline(noun),
        "Plural": decliners["Plural"].decline(noun)
    }
    
    return declensions

def isANStem(noun):
    return ord(noun[len(noun)-1]) == 0xd7b

def isAMStem(noun):
    finalChar = noun[len(noun)-1] # Need to check the noun's final letter
    #print("isAMStem: noun[:-1] = {0}\n\tord({0}) = {1}".format(finalChar, hex(ord(finalChar))))
    return ord(finalChar) == 0xd02

def isRuhStem(noun):
    return ord(noun[len(noun)-2]) == 0x0d4d and ord(noun[len(noun)-1]) == 0x0d31

def isDuhStem(noun):
    #print("isDuhStem: second-last character = {0}, last character = {1}".format(hex(ord(noun[len(noun)-2])), hex(ord(noun[len(noun)-1]))))
    return ord(noun[len(noun)-2]) == 0x0d1f and ord(noun[len(noun)-1]) == 0x0d4d

def isALStem(noun):
    return ord(noun[len(noun)-1]) == 0x0d7e
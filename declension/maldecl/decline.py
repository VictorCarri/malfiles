import declension.maldecl.singular
import declension.maldecl.plural

def decline(noun):
    decliners = {
        "Singular": None,
        "Plural": None
    }

    # Pick a generator based on the noun's shape #

    if isANStem(noun):
        decliners["Singular"] = declension.maldecl.singular.AMStem()
        decliners["Plural"] = declension.maldecl.plural.ANStem()

    elif isAMStem(noun):
        decliners["Singular"] = declension.maldecl.singular.AMStem()
        decliners["Plural"] = declension.maldecl.plural.AMStem()

    elif isRuhStem(noun):

    elif isDuhStem(noun):

    else:

def isANStem(noun):
    return noun[:-1] == 0x0d7b

def isAMStem(noun):
    return noun[:-1] == 0x0d02

def isRuhStem(noun):
    return noun[:-2] == 0x0d4d and noun[:-1] == 0x0d31

def isDuhStem(noun):
    return noun[:-2] == 0x0d4d and noun[:-1] == 0x0d1f
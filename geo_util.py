from typing import Optional
import pgeocode

def get_interdistance(postal1:str, postal2:str)->float:
    ''' Get geographical distance in km '''
    dist = pgeocode.GeoDistance('CA')
    return round(dist.query_postal_code(postal1, postal2),2)

def get_loc_postal_code(address:str)->Optional(str):
    ''' Get postal code from an address string of format "some address XXX XXX" where XXX XXX represents postal code.
    
    If input address format does not contain valid Canadian postal code, return None
    '''
    postal_split = address.split()[-2:]
    for postal in postal_split:
        if len(postal) != 3:
            return None
    return ' '.join(postal_split)


import geocoder
import pgeocode
import re

def get_interdistance(postal1:str, postal2:str)->float:
    ''' Get geographical distance in km '''
    dist = pgeocode.GeoDistance('CA')
    return round(dist.query_postal_code(postal1, postal2),2)

def get_address_postal_code(address:str)->str:
    ''' Get canadian postal code of an addrees in canada '''
    g = geocoder.canadapost(address)
    return str(g.postal)

def postal_code_isvalid(postal_code:str)->bool:
    if re.match(r'\b(?!.{0,7}[DFIOQU])[A-VXY]\d[A-Z][^-\w\d]\d[A-Z]\d\b',postal_code):
        return True
    return False

def get_loc_postal_code(address:str)->str:
    ''' Get postal code from an address string of format "some address XXX XXX" where XXX XXX represents postal code.
    
    If input address format does not contain valid Canadian postal code, get postal code from address
    '''
    postal_split = address.split()[-2:]
    postal_code = ' '.join(postal_split)
    if postal_code_isvalid(postal_code):
        return postal_code
    else:
        return get_address_postal_code(address)


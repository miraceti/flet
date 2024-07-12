from io import StringIO
import requests
import pandas
import json

pi = 3.14159
au=1.496e11 # m 
rsun = 6.955e8 # m
G = 0.00029591220828559104 # day, AU, Msun

# keplerian semi-major axis (au)
sa = lambda m,P : (G*m*P**2/(4*pi**2) )**(1./3) 

def dataframe_to_jsonfile(dataframe, filename):
    jsondata = json.loads( dataframe.to_json(orient='table',index=False))
    with open(filename, "w") as f:
        f.write(json.dumps(jsondata['data'], indent=4))

def tap_query(base_url, query, dataframe=True):
    # table access protocol query

    # build url
    uri_full = base_url
    for k in query:
        if k != "format":
            uri_full+= "{} {} ".format(k, query[k])
    
    uri_full = uri_full[:-1] + "&format={}".format(query.get("format","csv"))
    uri_full = uri_full.replace(' ','+')
    print(uri_full)

    response = requests.get(uri_full, timeout=90)
    # TODO check status_code? 

    if dataframe:
        return pandas.read_csv(StringIO(response.text))
    else:
        return response.text

def new_scrape():

    uri_ipac_base = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    """ uri_ipac_query1 = {
        # Table columns: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
        "select"   : "pl_name,hostname,tran_flag,pl_massj,pl_radj,pl_ratdor,"
                     "pl_orbper,pl_orbpererr1,pl_orbpererr2,pl_orbeccen,"
                     "pl_orbincl,pl_orblper,pl_tranmid,pl_tranmiderr1,pl_tranmiderr2,"
                     "st_teff,st_met,st_logg,st_mass,st_rad,ra,dec",
        "from"     : "ps", # Table name
        "where"    : "tran_flag = 1 and default_flag = 1",
        "order by" : "pl_name",
        "format"   : "csv"
    } """
    
    uri_ipac_query = {
        # Table columns: https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
        "select"   : "pl_name,hostname,pl_letter,pl_bmasse,pl_bmassj,pl_rade,pl_radj,"
                     "pl_orbper,pl_dens,pl_trandur,pl_ratror,"
                     "sy_snum,sy_pnum,sy_mnum,st_mass,st_lum,st_age,st_dens,sy_dist"
                     "disc_year,disc_telescope,discoverymethod",
        "from"     : "pscomppars", # Table name
        "order by" : "pl_name",
        "format"   : "csv"
    }

    default = tap_query(uri_ipac_base, uri_ipac_query)
    print(len(default))
    print(default)
    
    # fill in missing columns
    uri_ipac_query['where'] = 'tran_flag=1'
    extra = tap_query(uri_ipac_base, uri_ipac_query)
       

    # print(default)                    
    return default

if __name__ == "__main__":
    dataframe = new_scrape()
    dataframe_to_jsonfile(dataframe, "eaConf.json")
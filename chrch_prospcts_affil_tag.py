# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:50:58 2019

@author: Guest
"""

import pandas as pd
import arda_gis_denom
fields = ['id',
          'name',
          'billing_address_street_prospect',
          'billing_address_city_prospect',
          'billing_address_state_prospect',
          'billing_address_postalcode_prospect'
          ]
renamed_dict = {'billing_address_street_prospect': "street",
                'billing_address_city_prospect': "city",
                'billing_address_state_prospect': "state",
                'billing_address_postalcode_prospect': "zipcode"}
df_prospecting = pd.read_csv("df_gpcdb_prospects.csv",
                             encoding="ISO-8859-1",
                             usecols=fields,
                             dtype="object",
                             index_col=0
                             )
keyword_affiliation = {
        "calvary chapel": "evangelical",
        "besant lodge": "no longer tax-exempt",
        "saint kevin": "catholic",
        "franciscan": "catholic",
        "association for creation truth": "korean christian",
        "eucharist": "catholic",
        "american saint hill": "scientology",
        "catholic": "catholic",
        "islam": "muslim",
        "mosque": "muslim",
        "buddh": "buddhist",
        "budda": "buddhist",
        "chokhor": "buddhist",
        "aish tamid": "jewish",
        "bezazel": "jewish",
        "vedanta": "hindu",
        "latter day": "mormon",
        "tenrikyo": "japanese new religious mvmt",
        "russian church": "russian church",
        "foursquare": "Foursquare church",
        "muslim": "muslim",
        "methodist": "methodist",
        "baptist": "baptist",
        "lutheran": "Lutheran",
        "episcop": "episcopalian",
        "el shaddai dwxi": "catholic",
        "latalmid": "jewish",
        "presbyter": "presbyterian",
        "unitarian": "unitarian",
        "greek orthodox": "greek orthodox",
        "orthodox church": "orthodox church",
        "masjid": "islam",
        "taqwa": "islam",
        "lds": "Mormon",
        "israel": "jewish",
        "rabbi": "jewish",
        "judaism": "jewish",
        "diocese": "catholic",
        "religious science": "christian religious science",
        "world for jesus": "evangelical",
        "cchr": "scientology",
        "cathedral": "catholic",
        "foundation for human rights & tolerance": "scientology",
        "ahava": "jewish",
        "judea": "jewish",
        "john the baptist": "catholic",
        "sofer": "jewish",
        "the gathering": "non-denominational christian",
        "kairos": "AMI christian",
        "bible church": "christian bible church",
        "sacred heart": "catholic",
        "coptic": "coptic orthodox",
        "nuestra senora": "hispanic catholic",
        "nuestra señora": "hispanic catholic",
        "shri ": "hindu",
        "mandir": "hindu",
        "vedic": "hindu",
        "geeta ": "hindu",
        "ramayan": "hindu",
        "vishnu": "hindu",
        "shiva": "hindu",
        "minyan": "jewish",
        "konko": "shinto",
        "transfiguration": "catholic",
        "advanced anointing": "non-denominational christian",
        "beautiful gate": "non-denominational christian",
        "padmashree": "hindu",
        "ashram": "hindu",
        "mary magdalen": "catholic",
        "sikh": "sikh",
        "the grove": "non-denominational christian",
        "hsi fang": "buddhist",
        "st. vincent": "catholic",
        "united church of christ": "united church of christ",
        "chabad": "jewish",
        "vineyard christian": "evangelical Christian",
        "evangelical": "evangelical",
        "new hope church": "non-denominational christian",
        "river of faith church": "non-denominational christian",
        "synagogue": "jewish",
        "tridentine": "catholic",
        "latin mass": "catholic",
        "pacific crossroads": "presbyterian",
        "dharma": "buddhist",
        "mitzvah": "jewish",
        "isaiah": "isaiah",
        "scientology": "scientology",
        "virgin mary": "catholic",
        "new city": "Christian Reformed Church",
        "our lady of": "catholic",
        "latter-day saints": "mormon",
        "church of the nazarene": "church of the nazarene",
        "baha'i": "baha'i faith",
        "new life christian": "non-denominational christian",
        "branch church": "Branch Church of Christ",
        "metodista": "methodist",
        "dominion center": "non-denominational christian",
        "agape house": "lutheran",
        "agape missionary": "baptist",
        "meher baba": "zoroastrian",
        "calvary faith": "non-denominational christian",
        "beth am": "jewish",
        "sephardic": "jewish",
        "people's church": "Assemblies of God",
        "elijah mountain ministries": "non-denominational christian",
        "seventh-day adventist": "seventh-day adventist",
        "horizon christian fellowship": "evangelical",
        "st augustine": "catholic",
        "hillel": "jewish",
        "wat lao": "buddhist",
        "boubpharam": "buddhist",
        "beth el ": "jewish",
        "bodhi": "buddhist",
        "geetha": "hindu",
        "self-realization fellowship": "kriya yoga",
        "magen abraham": "jewish",
        "kiryat": "jewish",
        "bethel ame": "methodist",
        "celestial church of christ": "celestial church of christ",
        "second sunday": "non denominational",
        "faith tabernacle": "evangelical",
        "free church": "non-denominational christian",
        "apostolic faith": "pentecostal",
        "pentecost": "pentecostal",
        "mijoo": "korean christian",
        "grupo getsemani": "catholic",
        "presbiter": "presbyterian",
        "church of the living god": "non-denominational christian",
        "samoan congregational": "Congregational Christian Church in Samoa",
        "god in chr": "pentecostal",
        "ame zion": "methodist",
        "ethiopian fellowship": "evangelical",
        "muhammad": "muslim",
        "st stephen": "catholic",
        "christ the king": "catholic",
        "john paul": "catholic",
        "chr-god": "pentecostal",
        "santa muerte": "hispanic church",
        "yoseff ": "jewish",
        "kahal ": "jewish",
        "saint stephen": "christian",
        "ark christian fellowship": "evangelical",
        "canvas church": "christian canvas church",
        "flood church": "non-denominational christian",
        "newbreak": "non-denominational christian",
        "centro gracia": "hispanic christian",
        "friends meeting": "quaker",
        "revival tabernacle": "pentecostal",
        "alliance church": "evangelical",
        "korean united methodist": "korean united methodist",
        "soka gakkai": "buddhist",
        "the potter's house": "christian fellowship ministries",
        "the door christian": "christian fellowship ministries",
        "al-aslam": "muslim",
        "al-rribat": "muslim",
        " a m e ": "methodist",
        "a.m.e.": "methodist",
        "kolping": "catholic",
        "leo baeck": "jewish",
        "church of the annointing": "christian",
        "living word": "pentecostal",
        "word of god": "christian",
        "blessed sacrament": "catholic",
        "christ gospel tabernacle": "pentecostal",
        "covenant church": "evangelical",
        "cogic": "pentecostal",
        "salvation army": "salvation army",
        "skyline fellowship": "evangelical",
        "messianic jewish": "messianic judaism",
        "assemblies of god": "pentecostal",
        "redemption church": "non-denominational christian",
        "assembly of god": "pentecostal",
        "church of god": "pentecostal",
        "iglesia de dios": "hispanic pentecostal",
        "gideons int": "evangelical",
        "grace city church": "non-denominational christian",
        "lighthouse bible church": "non-denominational christian",
        "madeleine": "catholic",
        "aposento alto": "hispanic christian revival",
        "comunidad cristiana": "hispanic christian",
        "iglesia de cristo": "hispanic christian",
        "nestor head start": "episcopal",
        "rccg": "pentecostal",
        "carmelite": "catholic",
        "rtla": "evangelical",
        "hebrew": "jewish",
        "recovery house": "christian",
        "redemeed christian church": "pentecostal",
        "existence church": "non-denominational christian",
        "fellowship": "evangelical",
        "krishna": "hindu",
        "spiritualist church": "christian spiritualist church",
        "catalyst church": "christian plant",
        "christian science": "christian science",
        "holy cross": "christian",
        "st michael": "catholic",
        "st. michael": "catholic",
        "st francis": "catholic",
        "ministry": "evangelical",
        "maranatha": "non-denominational christian",
        "church of christ": "churches of christ",
        "st. john bosco": "catholic",
        "new jerusalem": "baptist",
        "mission trails": "baptist",
        "seminary": "catholic",
        "armenian church": "armenian church",
        "st. francis": "catholic",
        "addiskidan": "ethiopian evangelical",
        "korean": "korean church",
        "cristiana": "hispanic christian",
        "iglesia de jesucristo": "hispanic christian",
        "jewish": "jewish",
        "koinonia": "christian",
        "ministerio cristiano": "hispanic evangelical",
        "cristiano": "hispanic christian",
        "our lady of": "catholic",
        "new life": "pentecostal",
        "tribe media corp": "jewish",
        "christ": "christian",
        "shin kenko": "japanese spiritual",
        "thai word": "thai christian",
        "gospel": "christian",
        "jesus": "christian",
        "monastery": "catholic",
        "ethiopian": "ethiopian church",
        "bethlehem": "christian",
        "core church": "christian non-denominational",
        "turning point ": "christian non-denominational",
        "torah": "jewish",
        "one church": "christian non-denominational",
        "ikar": "jewish",
        "onnuri church": "korean presbyterian",
        "st gregory": "catholic/orthodox",
        "sinai": "jewish",
        " shul": "jewish",
        "yoga": "hindu",
        "cfm": "christian family movement",
        "new hope": "christian",
        "izunome": "japanese new religious mvmt",
        "mission society church": "korean new religious mvmt",
        "zen": "buddhist",
        "choong hyun": "korean christian",
        "eckankar": "new religious movement",
        "st gerard majella": "catholic",
        "westlight": "methodist",
        "united": "methodist",
        "evangelist": "evangelical",
        "mater dei": "catholic",
        "immaculate": "catholic",
        "restoration church": "christian non-denominational",
        "holy spirit": "catholic",
        "st cyril": "catholic/orthodox",
        "rasta": "rastafarian",
        "rissho": "japanese new religious mvmt",
        "shinji": "japanese new religious mvmt",
        "the lord's word church": "korean presbyterian",
        "good news central": "korean christian",
        "ministries": "evangelical",
        "relevant church": "evangelical",
        "new creation": "christian non-denominational",
        "ministerio": "hispanic christian",
        "iglesia": "hispanic christian",
        " ame ": "methodist",
        "casa de oracion": "hispanic christian",
        "casa de dios": "hispanic christian",
        "st peter": "catholic",
        "family foundation": "family foundation",
        "deacon": "catholic",
        "christian": "christian",
        "good shepherd": "christian",
        "greater mount carmel": "baptist",
        "judaea": "jewish",
        "maha ": "buddhist",
        "asambleas de dios": "hispanic pentecostal",
        "tabernacle": "christian",
        "yahweh": "christian or jewish",
        "watanabe": "japanese church",
        "jesucristo": "hispanic christian",
        "alianza minist": "hispanic christian"
        }


def preprocess_crm_prospects(df):
    """ preprocess prospect dataframe df for join with the ARDA dataframe"""
    df = df.rename(index=str, columns=renamed_dict)
    df = df.apply(lambda x: x.str.strip())
    df = df.apply(lambda x: x.str.lower())
    return df.dropna()


def preprocess_arda(df):
    """ preprocess prospect dataframe df for join with the ARDA dataframe"""
    df = df.apply(lambda x: x.str.strip())
    df = df.apply(lambda x: x.str.lower())
    return df.dropna()


def prospect_arda_match(df_prospecting, df_arda):
    """ match prospect df with arda df"""
    left_columns = ['street',
                    'city',
                    'zipcode'
                    ]
    right_columns = ['street address',
                     'city',
                     'zip code'
                     ]
    df_arda = df_arda.drop_duplicates(subset=right_columns)
    df_prospect_merged = df_prospecting.reset_index().merge(
            df_arda,
            how='left',
            left_on=left_columns,
            right_on=right_columns
            ).set_index('id')
    return df_prospect_merged


def map_affil(church_name):
    """ determine church afilliation from church_name """
    default_val = None
    keyword_iter = (x for x in keyword_affiliation if x in church_name)
    key = next(keyword_iter, default_val)
    if key is not None:
        return keyword_affiliation[key]
    else:
        return None


def bible_to_christian(church_name):
    """determine if church contains 'bible' in name"""
    if "bible" in church_name:
        return "christian"
    else:
        return None


def bible_fill(row):
    if pd.isnull(row['filled_aux']):
        return bible_to_christian(row['name'])
    else:
        return row.denom


def get_affiliation(df, df_arda):
    """ get affiliation from a row in df. The procedure first selects
    tries to find the affiliation using map_affil, and if it isn't found,
    it proceeds to get it from the dataframe join with df_arda
    """
    df_merged = prospect_arda_match(df, df_arda)
    df_merged['denom'] = df_merged['name'].apply(map_affil)
    df_merged['filled_aux'] = df_merged['denom'].fillna(
            df_merged['denomination'])
    df_merged['filled'] = df_merged.apply(bible_fill, axis=1)
    return df_merged['filled']


def test(df_prospect, city_test):
    df_arda = arda_gis_denom.create_df_city(city_test)
    print(len(df_arda))
    df_prospect = preprocess_crm_prospects(df_prospect)
    print(len(df_prospect))
    df_arda_fields = ['church name',
                      'city',
                      'state',
                      'street address',
                      'zip code']
    df_arda[df_arda_fields] = preprocess_arda(df_arda[df_arda_fields])
    print(len(df_arda))
    df_arda = df_arda[df_arda['city'] == city_test]
    print(len(df_arda))

    df_prospect = df_prospect[df_prospect['city'] == city_test]
    print(len(df_prospect))
    df_prospect2 = df_prospect.copy()
    df_prospect2['affili'] = get_affiliation(df_prospect, df_arda)
    return df_prospect2


def create_arda_csvs(top_cities2):
    """create a csv for every city in top_cities2"""
    for city in top_cities2:
        csv_name = "ardachurches_{}.csv".format(city)
        df_arda = arda_gis_denom.create_df_city(city)
        df_arda.to_csv(csv_name)

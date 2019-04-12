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
        "bread of life": "christian",
        "quaker meeting": "quaker",
        "pan de ": "hispanic cristian",
        "virgen de guadalupe": "hispanic christian",
        "tenrikyo": "japanese new religious mvmt",
        "russian church": "russian church",
        "foursquare": "Foursquare church",
        "shevet": "jewish",
        "tapuz": "jewish",
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
        "scottish rite": "freemasonry",
        "free mason": "freemasonry",
        "freemason": "freemasonry",
        "masons": "freemasonry",
        "masonic": "freemasonry",
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
        "yiddish": "jewish",
        "john the baptist": "catholic",
        "sofer": "jewish",
        "the gathering": "christian non-denominational",
        "kairos": "AMI christian",
        "bible church": "christian bible church",
        "sacred heart": "catholic",
        "coptic": "coptic orthodox",
        "st thomas the hermit": "coptic orthodox",
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
        "cordero de dios": "hispanic christian",
        "transfiguration": "catholic",
        "advanced anointing": "christian non-denominational",
        "beautiful gate": "christian non-denominational",
        "padmashree": "hindu",
        "ashram": "hindu",
        "mary magdalen": "catholic",
        "sikh": "sikh",
        "the grove": "christian non-denominational",
        "hsi fang": "buddhist",
        "st. vincent": "catholic",
        "united church of christ": "united church of christ",
        "chabad": "jewish",
        "vineyard christian": "evangelical Christian",
        "evangelical": "evangelical",
        "new hope church": "christian non-denominational",
        "river of faith church": "christian non-denominational",
        "synagogue": "jewish",
        "tridentine": "catholic",
        "latin mass": "catholic",
        "pacific crossroads": "presbyterian",
        "dharma": "buddhist",
        "mitzvah": "jewish",
        "isaiah": "jewish",
        "taslimi": "baha'i faith",
        "vincent de paul": "catholic",
        "syro malabar": "catholic",
        "scientology": "scientology",
        "virgin mary": "catholic",
        " tich ": "buddhist",
        "new city": "Christian Reformed Church",
        "our lady of": "catholic",
        "latter-day saints": "mormon",
        "church of the nazarene": "church of the nazarene",
        "baha'i": "baha'i faith",
        "bahai": "baha'i faith",
        "new life christian": "christian non-denominational",
        "branch church": "Branch Church of Christ",
        "metodista": "methodist",
        "dominion center": "christian non-denominational",
        "agape house": "lutheran",
        "agape missionary": "baptist",
        "meher baba": "zoroastrian",
        "agapa": "christian",
        "mikvah": "jewish",
        "missionary sister": "catholic",
        "rey de reyes": "christian",
        "golden circle church": "christian religious science",
        "calvary faith": "christian non-denominational",
        "beth am": "jewish",
        "sephardic": "jewish",
        "de lestonnac": "catholic",
        "people's church": "Assemblies of God",
        "elijah mountain ministries": "christian non-denominational",
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
        " beth ": "jewish",
        "shalom": "jewish",
        "bethel ame": "methodist",
        "celestial church of christ": "celestial church of christ",
        "second sunday": "non denominational",
        "faith tabernacle": "evangelical",
        "free church": "christian non-denominational",
        "apostolic faith": "pentecostal",
        "pentecost": "pentecostal",
        "mijoo": "korean christian",
        "grupo getsemani": "catholic",
        "presbiter": "presbyterian",
        "church of the living god": "christian non-denominational",
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
        "kolel": "jewish",
        "ixthus": "christian",
        "resplendent light": "christian non-denominational",
        "calvario": "hispanic christian",
        "crossway": "christian non-denominational",
        "saint stephen": "christian",
        "ark christian fellowship": "evangelical",
        "canvas church": "christian canvas church",
        "flood church": "christian non-denominational",
        "newbreak": "christian non-denominational",
        "centro gracia": "hispanic christian",
        "friends meeting": "quaker",
        "revival tabernacle": "pentecostal",
        "alliance church": "evangelical",
        "korean united methodist": "korean united methodist",
        "soka gakkai": "buddhist",
        "sgi-usa": "buddhist",
        "the potter's house": "christian fellowship ministries",
        "the door christian": "christian fellowship ministries",
        "al-aslam": "muslim",
        "al-rribat": "muslim",
        "lighthill": "christian non-denominational",
        " a m e ": "methodist",
        "a.m.e.": "methodist",
        "kolping": "catholic",
        "leo baeck": "jewish",
        "agnus dei": "catholic",
        "world ark mission": "christian",
        "most precious blood": "catholic",
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
        "light of zion": "messianic judaism",
        "assemblies of god": "pentecostal",
        "redemption church": "christian non-denominational",
        "assembly of god": "pentecostal",
        "church of god": "pentecostal",
        "iglesia de dios": "hispanic pentecostal",
        "gideons int": "evangelical",
        "grace city church": "christian non-denominational",
        "lighthouse bible church": "christian non-denominational",
        "madeleine": "catholic",
        "dawn mission": "korean christian",
        "aposento alto": "hispanic christian revival",
        "comunidad cristiana": "hispanic christian",
        "iglesia de cristo": "hispanic christian",
        "nestor head start": "episcopal",
        "rccg": "pentecostal",
        "carmelite": "catholic",
        "rtla": "evangelical",
        "hebrew": "jewish",
        "quang": "buddhist",
        "sunnataram": "buddhist",
        "recovery house": "christian",
        "redemeed christian church": "pentecostal",
        "existence church": "christian non-denominational",
        "fellowship": "evangelical",
        "krishna": "hindu",
        "gayatri": "hindu",
        "pariwar": "hindu",
        "saddleback church": "baptist",
        "congregational church": "christian congregational church",
        "spiritualist church": "christian spiritualist church",
        "catalyst church": "christian plant",
        "christian science": "christian science",
        "holy cross": "christian",
        "st michael": "catholic",
        "st. michael": "catholic",
        "st francis": "catholic",
        "st timothy": "catholic/orthodox",
        "ministry": "evangelical",
        "kehillat": "jewish",
        "ma'arav": "jewish",
        "maranatha": "christian non-denominational",
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
        "yaseen": "muslim",
        "new life": "pentecostal",
        "tribe media corp": "jewish",
        "christ": "christian",
        "shin kenko": "japanese spiritual",
        "thai word": "thai christian",
        "gospel": "christian",
        "jesus": "christian",
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
        "chosen people": "jewish",
        "victory outreach": "christian",
        "st luke": "catholic",
        "st ephrem": "catholic",
        "united reformed church": "presbyterian",
        "jacobite church": "orthodox church",
        "fraternal order": "fraternal order",
        "choong hyun": "korean christian",
        "eckankar": "new religious movement",
        "st gerard majella": "catholic",
        "westlight": "methodist",
        "nueva jerusalem": "hispanic christian",
        "templo": "hispanic christian",
        "evangelist": "evangelical",
        "mater dei": "catholic",
        "immaculate": "catholic",
        "reliance church": "christian non-denominational",
        "saint rose ": "catholic",
        "crosspoint": "christian non-denominational",
        "restoration church": "christian non-denominational",
        "holy spirit": "catholic",
        "st cyril": "catholic/orthodox",
        "knights of columbus": "catholic",
        "rasta": "rastafarian",
        "rissho": "japanese new religious mvmt",
        "shinji": "japanese new religious mvmt",
        "the lord's word church": "korean presbyterian",
        "good news central": "korean christian",
        "ministries": "evangelical",
        "adventist": "adventist",
        "healing wings": "christian",
        "samaritan": "christian",
        "spectrum church": "christian non-denominational",
        "relevant church": "evangelical",
        "new creation": "christian non-denominational",
        "ministerio": "hispanic christian",
        "iglesia": "hispanic christian",
        " ame ": "methodist",
        "casa de oracion": "hispanic christian",
        "casa de dios": "hispanic christian",
        "st peter": "catholic",
        "corssroads": "christian non-denominational",
        "family foundation": "family foundation",
        "deacon": "catholic",
        "faith harbor": "christian",
        "sword of the spirit": "christian",
        "christian": "christian",
        "community church": "christian",
        "come-unity": "christian",
        "grace renewal": "christian",
        "order of elks": "fraternal order",
        "good shepherd": "christian",
        "greater mount carmel": "baptist",
        "judaea": "jewish",
        "maha ": "buddhist",
        "asamblea de dios": "hispanic pentecostal",
        "asamblea": "hispanic pentecostal",
        "tabernacle": "christian",
        "calvary chapel": "christian",
        "yahweh": "christian or jewish",
        "watanabe": "japanese church",
        "alianza minist": "hispanic christian",
        "international house": "evangelical",
        "cristo": "hispanic christian",
        "alpha omega": "christian",
        "risen church": "christian non-denominational",
        "whole life": "methodist",
        "hope church": "christian",
        "scholarship foundation": "scholarship foundation",
        "chaldean": "iraqi",
        " sda": "seventh-day adventist",
        "eagles wings": "christian",
        "jehovah's witnes": "christian jehovah's witnesses",
        "the rock": "christian non-denominational",
        "lamb of god": "christian",
        "monastery": "catholic/buddhist monastery",
        "sanctuary church": "christian non-denominational",
        }
# maybe add again later:"united": "methodist",


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

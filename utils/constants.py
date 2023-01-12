import pandas as pd
from country_list import countries_for_language
from dotenv import load_dotenv
import os

load_dotenv()

df_companies = pd.read_csv('./data/yc_top_companies.csv')
df_universities = pd.read_csv('./data/10_top_universities.csv')

TOP_COMPANIES = df_companies.company_name.values.tolist()
TOP_UNIVERSITIES = df_universities.university.values.tolist()

COUNTRIES = dict(countries_for_language('en'))
COUNTRIES_CODES = [k for k,v in COUNTRIES.items()]

HFApiKey = os.environ.get('HFApiKey')

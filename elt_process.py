import pandas as pd
import psycopg2
from psycopg2 import sql

# DBconnection config
DB_CONFIG = {
    "host": "localhost",        
    "port": 5432,               
    "database": "testdb",     
    "user": "user",             
    "password": "password"      
}

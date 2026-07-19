from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

from urllib.parse import quote_plus

ca_path = quote_plus(r"C:\Users\91860\Downloads\isrgrootx1 (1).pem")

DATABASE_URL = (

"mysql+pymysql://4M1rjhCyPLnDA3G.root:WIxm8QmTNCMb5ch8"

"@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"

f"?ssl_ca={ca_path}"

"&ssl_verify_cert=true"

"&ssl_verify_identity=true"

)

engine = create_engine(

DATABASE_URL,

pool_pre_ping=True,

echo=True

)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
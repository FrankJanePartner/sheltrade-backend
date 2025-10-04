import os
from supabase import create_client, Client
from supabase.client import ClientOptions


from supabase import create_client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")

# supabase: Client = create_client(
#     url,
#     key,
#     options=ClientOptions(
#         postgrest_client_timeout=10,
#         storage_client_timeout=10,
#         schema="public",
#     )
# )
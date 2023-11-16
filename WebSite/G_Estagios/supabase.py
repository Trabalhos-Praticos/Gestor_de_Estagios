import os
from supabase import create_client, Client

url: str = os.environ.get("https://rxpmviaksgbicuyrxqtr.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4cG12aWFrc2diaWN1eXJ4cXRyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5OTg2OTkwMywiZXhwIjoyMDE1NDQ1OTAzfQ.vE4o4iq3Y9bMPEcP8WFLlEVy6oUyqg7JhDLoK9hAOYI")
supa: Client = create_client(url, key)
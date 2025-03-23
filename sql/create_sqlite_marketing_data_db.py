import sqlite3
import random
import datetime
from utils.event_utils import generate_delayed_random_event_time


connection = sqlite3.connect("marketing_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing_email_sent (
    campaign_id INTEGER,
    user_id INTEGER,
    event_time TIMESTAMP,
    UNIQUE(campaign_id, user_id)
)
""")

try:
    cursor.execute("DELETE FROM marketing_email_sent")
    print("Existing entries removed from marketing_email_sent table.")
except:
    pass

## Ensuring that only unqiue (campaign_id, user_id) pairs are inserted
number_of_campaigns = 25
number_of_users = 800
size_of_sample = 10000
campaign_ids = range(1, number_of_campaigns)
user_ids = range(1, number_of_users)
all_pairs = [(campaign_id, user_id) for campaign_id in campaign_ids for user_id in user_ids]
selected_pairs = random.sample(all_pairs, size_of_sample)
entries = []
for campaign_id, user_id in selected_pairs:
    random_days = random.randint(0, 365)
    random_time = datetime.datetime.now() - datetime.timedelta(days=random_days)
    event_time = random_time.strftime('%Y-%m-%d %H:%M:%S')
    entries.append((campaign_id, user_id, event_time))

cursor.executemany("INSERT INTO marketing_email_sent (campaign_id, user_id, event_time) VALUES (?, ?, ?)", entries)
print("Successfully populated marketing_data.db")

# Verify sample data
cursor.execute("SELECT COUNT(*) FROM marketing_email_sent")
row_count = cursor.fetchone()[0]
print(f"Total rows in the marketing_email_sent table: {row_count}")

cursor.execute("SELECT * FROM marketing_email_sent LIMIT 3")
rows = cursor.fetchall()
print("Sample data:")
for row in rows:
    print(row)

connection.commit()

# Code section for marketing_email_opened
try:
    cursor.execute("DELETE FROM marketing_email_opened")
    print("Existing entries removed from marketing_email_opened table.")
except:
    pass

cursor.execute("""
    CREATE TABLE IF NOT EXISTS marketing_email_opened (
        campaign_id INTEGER,
        user_id INTEGER,
        event_time TEXT
    )
""")

cursor.execute("SELECT * FROM marketing_email_sent")
all_entries = cursor.fetchall()

# Decide the random percentage (between 30% and 70%)
percentage = random.uniform(0.3, 0.7)
number_to_copy = int(len(all_entries) * percentage)

# Randomly select entries to be copied
entries_to_copy = random.sample(all_entries, number_to_copy)

# Create the new entries for email_opened with adjusted event_time
email_opened_entries = [
    (campaign_id, user_id, generate_delayed_random_event_time(event_time))
    for campaign_id, user_id, event_time in entries_to_copy
]

cursor.executemany("INSERT INTO marketing_email_opened (campaign_id, user_id, event_time) VALUES (?, ?, ?)", email_opened_entries)

connection.commit()
connection.close()

print(f"{len(email_opened_entries)} entries were copied to 'email_opened' ({percentage*100:.2f}%).")

print("marketing_data.db created with tables: marketing_email_sent and marketing_email_opened")
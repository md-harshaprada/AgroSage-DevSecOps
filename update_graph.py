import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://SRISAILA:saila1410@cluster0.jnllygb.mongodb.net/?retryWrites=true&w=majority')

db = client.get_database('AgroSage')
collection = db["persons"]

# Query all data, including 'count', and convert 'Date' to string
cursor = collection.find({}, {'Date': {'$dateToString': {'format': '%Y-%m-%d', 'date': '$Date'}}, 'count': 1})

# Convert the cursor to a DataFrame
df = pd.DataFrame(list(cursor))

# Create the bar graph
plt.bar(df['Date'], df['count'])  # Use plt.bar() for bar graph
plt.xlabel('Date')
plt.ylabel('No of persons who visited website')
plt.title('Graph')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout for better spacing
plt.savefig('graph.png') 

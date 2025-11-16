# Lab 4 — Wikimedia Streaming Pipeline (Databricks)

This lab reads real-time data from the Wikimedia “recent change” stream, saves the raw events in Databricks, processes them, and creates two Delta tables: one for aggregated analytics and one for alerts. A cleanup notebook removes old raw data. The pipeline was also set up as a Databricks Job.

### What happens in the lab
- A notebook connects to the live Wikimedia stream and saves the incoming JSON events in a Unity Catalog volume.
- A second notebook processes these events: it creates a table that counts edits every 5 minutes (bot vs. human), and a second table that detects very large human edits (alerts).
- A cleanup notebook deletes old daily raw data to free space.
- A Databricks Job is created to run the 3 steps in order: **ingest → process → cleanup**.

### Serverless problem
Our Databricks workspace only gives us **Serverless compute**, and Serverless jobs stay stuck in the “Queued” state, so the Job cannot start.  
The notebooks themselves run correctly when executed manually.  
This is a Databricks limitation, not a code error.

### Notebooks included
- `Lab4_Wikimedia_ingest.ipynb` — reads the live stream and stores raw events
- `Lab4_Wikimedia_processing.ipynb` — creates the gold table and alerts table
- `Lab4_Wikimedia_cleanup.ipynb` — deletes old raw volumes

### Team
- Abdel Moughit BERAMI EL IDRISSI  
- Fares Boukasba

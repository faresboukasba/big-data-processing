This script tracks live Wikipedia edits for five IMDB-related entities: Inception, The Dark Knight, Christopher Nolan, Leonardo DiCaprio, and Comedy (genre).

It connects to the Wikimedia RecentChange stream, counts edits per entity, and stores them in wiki_events.jsonl. An alert system triggers when an entity reaches a certain number of edits (ALERT_THRESHOLD=3) and writes these alerts to wiki_alerts.jsonl.

This demonstrates real-time monitoring, metrics tracking, and alerting, as required by the project. Since edits are live, the number of events depends on Wikipedia activity during execution.
SHOW FIELDS IN gdelt_historical;

# Get data to test merge MIDS and GDELT, May 2005
SELECT * FROM gdelt_historical
	WHERE
	MonthYear="200505";

# Get stories data for the Polity project, Brazil Dec 2012
SELECT @Brazil_id := `actor_id` FROM dict_actors
	WHERE name="Brazil" AND
	is_country=1;

SHOW FIELDS FROM events;
SELECT @story_id := `story_id` FROM events
	WHERE
	(source_actor_id=@Brazil_id OR
	target_actor_id=@Brazil_id) AND
	YEAR(event_date)=2012;

CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (SELECT DISTINCT story_id FROM events
	WHERE
	(source_actor_id=@Brazil_id OR
	target_actor_id=@Brazil_id) AND
	YEAR(event_date)=2012);

SELECT * FROM temp_table;
SELECT * FROM stories, temp_table
	WHERE
	stories.StoryID = temp_table.story_id;
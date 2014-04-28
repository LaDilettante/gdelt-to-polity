SHOW FIELDS IN gdelt_historical;

# Get stories data for the Polity project, Brazil Dec 2012

## Get the id of Brazil
SELECT @Brazil_id := `actor_id` FROM dict_actors
	WHERE name="Brazil" AND
	is_country=1;

## Get all events that have actor_id of Brazil
SHOW FIELDS FROM events;
SELECT @story_id := `story_id` FROM events
	WHERE
	(source_actor_id=@Brazil_id OR
	target_actor_id=@Brazil_id) AND
	YEAR(event_date)=2012;

## Get the story_id of all the events above
CREATE TEMPORARY TABLE IF NOT EXISTS temp_table AS (SELECT DISTINCT story_id FROM events
	WHERE
	(source_actor_id=@Brazil_id OR
	target_actor_id=@Brazil_id) AND
	YEAR(event_date)=2012);

## Get the text of stories with the story_id above
SELECT * FROM temp_table;
SELECT * FROM stories, temp_table
	WHERE
	stories.StoryID = temp_table.story_id;
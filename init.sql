CREATE TABLE IF NOT EXISTS sensor_data (
	dt 			TIMESTAMP NOT NULL DEFAULT NOW(),
	temp_c		NUMERIC(5, 2),
	temp_f		NUMERIC(5, 2),
	humidity	NUMERIC(5, 2),
	sensor_id	int
);
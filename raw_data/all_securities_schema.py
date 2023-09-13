create_table = "CREATE TABLE IF NOT EXISTS all_securities \
	        (      	     	    	   \
		 display_name String, 	   \
		 code String,  		   \
		 start_date Date,	   \
		 end_date Date, 		   \
		 type String		   \
		)			   \
		ENGINE = ReplacingMergeTree() \
		PRIMARY KEY (code) 	      \
		ORDER BY (code)"

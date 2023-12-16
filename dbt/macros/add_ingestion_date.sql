-- {% macro add_ingestion_date() %}
--     ALTER TABLE {{ this }} ADD COLUMN ingestion_date current_timestamp() TIMESTAMP 
-- {% endmacro %}


-- {% if is_incremental() %}
--   where event_time > (select max(event_time) from {{ this }})
-- {% endif %}


-- {{ dbt_date.now() }}
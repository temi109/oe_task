with src_races as (
    select * from {{ source('FORMULA_1_SOURCE', 'races') }}
),

stg_races as (
    select RACEID as race_id,
    YEAR,
    ROUND,
    CIRCUITID::VARCHAR as circuit_id,
    NAME,
    DATE,
    TIME,
    {{ dbt_date.now() }} as ingestion_date from src_races
)

select * from stg_races
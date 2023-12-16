with src_results as (
    select * from {{ source('FORMULA_1_SOURCE', 'results') }}
),

stg_results as (
    select RESULTID as result_id,
    RACEID as race_id,
    DRIVERID as driver_id,
    CONSTRUCTORID as constructor_id,
    NUMBER,
    GRID,
    POSITION,
    POSITIONTEXT as position_txt,
    POSITIONORDER as positon_order,
    POINTS,
    LAPS,
    TIME,
    MILLISECONDS,
    RANK,
     {{ dbt_date.now() }} as ingestion_date from src_results
)

select * from stg_results
with src_circuits as (
    select * from {{ source('FORMULA_1_SOURCE', 'circuits') }}
),

stg_circuits as (
    select circuitId as circuit_id,
    circuitRef as circuit_ref,
    name,
    location,
    country,
    lat as latitude,
    lng as longititude,
    alt,
    {{ dbt_date.now() }} as ingestion_date from src_circuits
)

select * from stg_circuits
with src_constructors as (
    select * from {{ source('FORMULA_1_SOURCE', 'constructors') }}
),

stg_constructors as (
    select CONSTRUCTORID as constructor_id,
    CONSTRUCTORREF as constructor_ref,
    NAME,
    NATIONALITY,
    {{ dbt_date.now() }} as ingestion_date from src_constructors
)

select * from stg_constructors
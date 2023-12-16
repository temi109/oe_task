with race_results as (
    SELECT * FROM {{ref('race_results')}}
    ),

constructors as (
    SELECT * FROM {{ref('stg_formula_1__constructors')}}
),

circuits as (
    SELECT * FROM {{ref('stg_formula_1__circuits')}}
)

SELECT rr.race_id, rr.race_year, rr.constructor_id, rr.points, rr.end_position,
circ.country, crs.name, crs.nationality,
 {{ dbt_date.now() }} as created_date FROM constructors crs 
INNER JOIN race_results rr ON crs.constructor_id = rr.constructor_id
INNER JOIN circuits circ ON rr.circuit_id = circ.circuit_id
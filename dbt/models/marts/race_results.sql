
with races as (
    SELECT * FROM {{ref('stg_formula_1__races')}}
),

results as (
    SELECT * FROM {{ref('stg_formula_1__results')}}
)

SELECT races.race_id, 
races.year as race_year, 
races.name as races_name,
races.circuit_id,
races.date as race_date, 
results.constructor_id,
results.position as end_position,
results.points,
results.laps as no_of_laps from results
inner join races
on results.race_id = races.race_id
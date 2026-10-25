-- Вежбa 2 — досије клуба
-- Изаберите један клуб и анализирајте његову сезону 2024/25. Сваки упит почните истим кораком, тако да за други клуб мењате само име:
-- WITH club AS (


-- SELECT team_id FROM teams WHERE team_name = 'Elmsworth Wanderers'
-- )
-- SELECT ...

-- 1. Сезона у бројевима: утакмице, победе, нерешене, порази, дати и примљени голови, бодови.
-- Dosije kluba Elmsworth Wanderers (ELW, team_id = 8) iz grada Elmsworth, osnovan 1894. godine, igra na travnatom stadionu bez krova (stadium_id = 8) Elmsworth Lane u istoimenom gradu, kapaciteta 24000 koji docekuje gledaoce od 1931.

SELECT count (*) AS matches,
    season
FROM matches 
WHERE (home_team_id = 8 
    OR away_team_id = 8)
    AND season = '2024/25'
GROUP BY season; -- 38 meceva

-- svi mecevi/all_matches:
SELECT -- tim kao domacin
    m.season,
    m.match_id,
    t.team_name,
    m.home_goals AS goals_for,
    m.away_goals AS goals_against
FROM matches m
JOIN teams t ON t.team_id = m.home_team_id 
WHERE m.status = 'played'
AND m.season = '2024/25'

UNION ALL

SELECT -- tim kao gost
    m.season,
    m.match_id,
    t.team_name,
    m.away_goals AS goals_for,
    m.home_goals AS goals_against
FROM matches m
JOIN teams t ON t.team_id = m.away_team_id 
WHERE m.status = 'played'
AND m.season = '2024/25'
;

WITH all_matches AS (
                SELECT -- tim kao domacin
                    m.match_id,
                    t.team_name,
                    m.home_goals AS goals_for,
                    m.away_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.home_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'

                UNION ALL

                SELECT -- tim kao gost
                    m.match_id,
                    t.team_name,
                    m.away_goals AS goals_for,
                    m.home_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.away_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'
)
SELECT
    -- team_name,
    sum (goals_for) AS goals_for, -- 61
    sum (goals_against) AS goals_against, --54
    sum (CASE 
            WHEN goals_for > goals_against THEN 1
            ELSE 0
        END) AS wins, -- sve pobede tima - 15

    sum (CASE 
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS ties, -- sve neresene utakmice tima 4
    sum (CASE 
            WHEN goals_for < goals_against THEN 1
            ELSE 0
        END) AS losses, -- sve izgubljene utakmice tima 19
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM all_matches
WHERE team_name = 'Elmsworth Wanderers'
;


-- goals_for	goals_against	wins	ties	losses  points
-- 61	            54	           15	   4	19          49

-- cela tabela bodova: (Elmsworth Wanderers je u sredini, na 12 mestu od 20 timova )


WITH all_matches AS (
                SELECT -- tim kao domacin
                    m.match_id,
                    t.team_name,
                    m.home_goals AS goals_for,
                    m.away_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.home_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'

                UNION ALL

                SELECT -- tim kao gost
                    m.match_id,
                    t.team_name,
                    m.away_goals AS goals_for,
                    m.home_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.away_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'
) 
SELECT
    team_name,
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM all_matches
GROUP BY team_name
ORDER BY points DESC
;


-------------------------------

-- SELECT * 
-- FROM stadiums 
-- WHERE stadium_id = 8;

-- 2. Код куће и у гостима: исти бројеви, одвојено за домаће и гостујуће утакмице.


-- kao domacin:
WITH home_matches AS (
                SELECT -- tim kao domacin
                    m.match_id,
                    t.team_name,
                    m.home_goals AS goals_for,
                    m.away_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.home_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'

)
SELECT
    -- team_name,
    sum (goals_for) AS goals_for, 
    sum (goals_against) AS goals_against,
    sum (CASE 
            WHEN goals_for > goals_against THEN 1
            ELSE 0
        END) AS wins, 

    sum (CASE 
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS ties,
    sum (CASE 
            WHEN goals_for < goals_against THEN 1
            ELSE 0
        END) AS losses,
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM home_matches
WHERE team_name = 'Elmsworth Wanderers'
;

-- kod kuce:

-- goals_for	goals_against	wins	ties	losses	points
-- 37	            24	            9	    2	    8	    29

-- kao gost:

WITH away_matches AS (
                
                SELECT -- tim kao gost
                    m.match_id,
                    t.team_name,
                    m.away_goals AS goals_for,
                    m.home_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.away_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'
)
SELECT
    -- team_name,
    sum (goals_for) AS goals_for, -- 61
    sum (goals_against) AS goals_against, --54
    sum (CASE 
            WHEN goals_for > goals_against THEN 1
            ELSE 0
        END) AS wins, -- sve pobede tima - 15

    sum (CASE 
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS ties, -- sve neresene utakmice tima 4
    sum (CASE 
            WHEN goals_for < goals_against THEN 1
            ELSE 0
        END) AS losses, -- sve izgubljene utakmice tima 19
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM away_matches
WHERE team_name = 'Elmsworth Wanderers'
;

-- goals_for	goals_against	wins	ties	losses	points
--  24	            30	            6	    2	    11	    20


-- 3. Стрелци: три најбоља стрелца клуба и најбољи асистент.

SELECT 
    count (*) as event_type_count,
    e.event_type
FROM match_events e
JOIN matches m ON m.match_id = e.match_id
WHERE   e.team_id = 8
    AND m.season = '2024/25'
GROUP BY e.event_type
;

-- event_type_count	        event_type
--       6                   penalty_goal
--      61                   yellow_card
--      53	                 goal
--       2	                 own_goal
--       2	                 red_card
--       1	                 second_yellow
--     154	                 substitution

SELECT 
    count (e.event_id) AS goals_scored,
    concat (p.first_name, ' ', p.last_name) AS player
FROM match_events e
JOIN matches m ON m.match_id = e.match_id
JOIN players p ON p.player_id = e.player_id
WHERE   e.team_id = 8
    AND m.season = '2024/25'
    AND event_type IN ('penalty_goal', 'goal')
GROUP BY e.player_id, player
ORDER BY goals_scored DESC
;

-- najbolji strelci:
-- 17	Marko Stanković
-- 7	Iñigo López
-- 6	Raphaël Lefèvre

-- najbolji asistent:

SELECT 
    count (e.event_id) AS assistances,
    concat (p.first_name, ' ', p.last_name) AS player
FROM match_events e
JOIN matches m ON m.match_id = e.match_id
JOIN players p ON p.player_id = e.related_player_id
WHERE   e.team_id = 8
    AND m.season = '2024/25'
    AND event_type IN ('penalty_goal', 'goal')
GROUP BY e.related_player_id, player
ORDER BY assistances DESC
;

-- -- najbolji asistent:
-- 4	Marko Stanković
-- 4	Mathis Lefèvre
-- 4	Kylian Lefèvre

-- po match_events, tim je dao 53+6 golova, sto ynaci da su 2 "dobili" na poklon od protivnika, kao autogolove.

-- 4. Дисциплина: картони клуба по утакмици у поређењу са просеком лиге по тиму по утакмици.

-- kartoni kluba ukupno za sezonu
SELECT 
    count (*) as event_type_count,
    e.event_type
FROM match_events e
JOIN matches m ON m.match_id = e.match_id
WHERE   e.team_id = 8
    AND m.season = '2024/25'
    AND e.event_type IN ('yellow_card', 'second_yellow', 'red_card')
GROUP BY e.event_type
;

-- 61	yellow_card
-- 2	red_card
-- 1	second_yellow

-- kartoni po utakmicama
SELECT 
    count (*) as event_type_count,
    e.match_id
FROM match_events e
JOIN matches m ON m.match_id = e.match_id
WHERE   m.season = '2024/25'
    AND e.event_type IN ('yellow_card', 'second_yellow', 'red_card')
GROUP BY e.match_id
ORDER BY event_type_count DESC
;

-- izracunat prosek kartona po utakmici za celu sezonu
WITH match_cards AS (
        SELECT 
            count (*) as event_type_count,
            e.match_id
        FROM match_events e
        JOIN matches m ON m.match_id = e.match_id
        WHERE   m.season = '2024/25'
            AND e.event_type IN ('yellow_card', 'second_yellow', 'red_card')
        GROUP BY e.match_id
        ORDER BY event_type_count DESC
)
SELECT avg (event_type_count) --(3,66)
FROM match_cards
;

-- ukupan prosek kartona u odnosu na prosek lige

WITH match_cards AS (
        SELECT 
            count (*) as event_type_count,
            e.match_id
        FROM match_events e
        JOIN matches m ON m.match_id = e.match_id
        WHERE   m.season = '2024/25'
            AND e.team_id = 8
            AND e.event_type IN ('yellow_card', 'second_yellow', 'red_card')
        GROUP BY e.match_id
        ORDER BY event_type_count DESC
)
SELECT avg (event_type_count) --(3,66 liga vs 2.29)
FROM match_cards
;

-- Tim je u ovoj sezoni igrao znacajnije cistije u odnosu na ostale timove, sa samo 2.29 kartona po utakmici u poredjenju sa prosekom lige od 3.66




-- 5. Тренери: ко је водио клуб у сезони и са колико бодова по утакмици.

SELECT * 
FROM manager_spells
WHERE team_id = 8
; 



-- Tim je i tokom ove cele sezone vodio Holandjanin Erik ten Hag (sa timom od 18.juna 2021.), sa 1,29 bodova po utakmici

--point

WITH all_matches AS (
                SELECT -- tim kao domacin
                    m.match_id,
                    t.team_name,
                    m.home_goals AS goals_for,
                    m.away_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.home_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'

                UNION ALL

                SELECT -- tim kao gost
                    m.match_id,
                    t.team_name,
                    m.away_goals AS goals_for,
                    m.home_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.away_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'
)
SELECT
    -- team_name,
    sum (goals_for) AS goals_for, -- 61
    sum (goals_against) AS goals_against, --54
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM all_matches
WHERE team_name = 'Elmsworth Wanderers'
;

-------- PROSEK golova i poena po utakmici

WITH points AS
(WITH all_matches AS (
                SELECT -- tim kao domacin
                    m.match_id,
                    t.team_name,
                    m.home_goals AS goals_for,
                    m.away_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.home_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'

                UNION ALL

                SELECT -- tim kao gost
                    m.match_id,
                    t.team_name,
                    m.away_goals AS goals_for,
                    m.home_goals AS goals_against
                FROM matches m
                JOIN teams t ON t.team_id = m.away_team_id 
                WHERE m.status = 'played'
                AND m.season = '2024/25'
)
SELECT
    -- team_name,
    count (all_matches.match_id) AS count,
    sum (goals_for) AS goals_for, -- 61
    sum (goals_against) AS goals_against, --54
    sum (CASE 
            WHEN goals_for > goals_against THEN 3
            WHEN goals_for = goals_against THEN 1
            ELSE 0
        END) AS points

FROM all_matches
WHERE team_name = 'Elmsworth Wanderers')

SELECT 

    goals_for/count AS goals_for_per_match,
    goals_against/count AS goals_against_per_match,
    points/count AS points_per_match
FROM points
;




-- 6. Највећа победа и најтежи пораз.

SELECT 
    m.match_id,
    (CASE 
        WHEN ht.team_id = 8 THEN m.home_goals - m.away_goals
        WHEN awt.team_id = 8 THEN m.away_goals - m.home_goals
    END) AS goal_diff

FROM matches m
JOIN teams ht ON ht.team_id = m.home_team_id
JOIN teams awt ON awt.team_id = m.away_team_id
WHERE m.season = '2024/25'
    AND (m.away_team_id = 8
    OR m.home_team_id = 8)
ORDER BY goal_diff
;

SELECT *
FROM matches
WHERE match_id = 2378 -- GOAL_DIFF -3
OR match_id = 2324 -- +6
;

SELECT
    concat (ht.team_name, ' - ', awt.team_name) AS played,
    concat (m.home_goals, ' : ', m.away_goals) AS result,
    CASE 
        WHEN m.match_id = 2378 THEN 'worst defeat'
        WHEN m.match_id = 2324 THEN 'greatest win'
        ELSE ' '
    END AS comment
FROM matches m
JOIN teams ht ON ht.team_id = m.home_team_id
JOIN teams awt ON awt.team_id = m.away_team_id
WHERE ht.team_id = 8 or awt.team_id = 8
--m.match_id = 2378 -- najtezi poraz
;

-- Najveca pobeda Elmsworth Wanderers je u gostima kod Pemberton United sa fantasticnih 1:7, dok je najtezi poraz po broju golova mnogo blazi, 3:0, ponovo u gostima, ali ovaj put kod tima Oakfield Town.


-- 7. Публика: просечна посета и попуњеност на домаћим утакмицама, и колико утакмица нема податак о посети.

SELECT avg (m.attendance)
FROM matches m
WHERE m.home_team_id = 8
AND m.season = '2024/25'
; --21745,5

SELECT 
    s.stadium_name,
    s.capacity 
FROM stadiums s
JOIN teams t ON t.stadium_id = s.stadium_id
WHERE team_id = 8
; -- 24000

SELECT count (m.match_id)
FROM matches m
WHERE m.home_team_id = 8
AND m.season = '2024/25'
AND m.attendance IS NULL
; 

SELECT 
    s.capacity AS capacity,
    m.attendance/capacity*100 AS attendance_percentage
FROM matches m
JOIN stadiums s ON s.stadium_id = m.stadium_id
WHERE m.home_team_id = 8
AND m.season = '2024/25'
ORDER BY attendance_percentage
; 

SELECT 
    avg (s.capacity) AS capacity,
    avg (m.attendance/capacity*100) AS attendance_percentage
FROM matches m
JOIN stadiums s ON s.stadium_id = m.stadium_id
WHERE m.home_team_id = 8
AND m.season = '2024/25'
;
-- Dok jedna poseta u sezoni 2024/25 nije zabelezena, prosecna poseta u sezoni je iznosila 21745,5, sto je vrlo visoko u odnosu na kapacitet Elmsworth Lane stadiona od 24000. 
-- Po utakmicama, osim nezabelezena posete, najmanja popunjenost je bila 78,93%, a isla je cak do 99,7%. Prosecna popunjenost za celu sezonu je 90,61%.


-- Све упите сачувајте у један SQL фајл, на пример workshop/dossier.sql, и пошаљите га у свој репозиторијум sql-bootcamp (commit и push). На крају припремите један најзанимљивији налаз о свом клубу.


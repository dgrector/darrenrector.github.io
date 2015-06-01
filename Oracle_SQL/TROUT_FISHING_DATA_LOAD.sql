-------------------------------------------------------------------------------
--
--Name: Darren Rector
--
--
--Purpose: A script that populates and then manipulates the data in the trout 
--         table.
--
--
-------------------------------------------------------------------------------
-----------------------------------------------
--DATA LOAD
-----------------------------------------------
INSERT INTO DGR_FISH (SPECIES_ID, FISH_NAME, LAKE_ID, FLY_USED, FISH_LENGTH, LINE_WEIGHT) VALUES(1, 'RAINBOW', 1, 'STONE', 18, 4);
INSERT INTO DGR_FISH (SPECIES_ID, FISH_NAME, LAKE_ID, FLY_USED, FISH_LENGTH, LINE_WEIGHT) VALUES(3, 'BROWN', 4, 'GREEN DRAKE', 14, 5);
--
INSERT INTO DGR_FLIES(FLY_ID, FLY_NAME, FLY_SIZE, FLY_TYPE, FISH_NAME, SPECIES_ID) VALUES(4, 'STONE', 3, 'DRY', 'RAINBOW', 1);
INSERT INTO DGR_FLIES(FLY_ID, FLY_NAME, FLY_SIZE, FLY_TYPE, FISH_NAME, SPECIES_ID) VALUES(5, 'GREEN DRAKE', 4, 'WET', 'BROWN', 3);
--
INSERT INTO DGR_LAKE(LAKE_ID, LOCATION_NAME, FISH_NAME, MONTH, LOC_TIME) VALUES(1, 'PENNINGTON', 'RAINBOW', 'MARCH', 'NIGHT');
INSERT INTO DGR_LAKE(LAKE_ID, LOCATION_NAME, FISH_NAME, MONTH, LOC_TIME) VALUES(4, 'YAWKEY', 'BROWN', 'JULY', 'AFTERNOON');
--
COMMIT;

-----------------------------------------------
--SUCCESSFUL UPDATE
-----------------------------------------------
--
UPDATE DGR_LAKE----------CHANGE MONTH FROM 'JULY' TO 'JUNE'
SET MONTH = 'JUNE'
WHERE LAKE_ID = 4;

-----------------------------------------------
--SUCCESSFUL DELETE
-----------------------------------------------
--
DELETE FROM DGR_LAKE-----GET PENNINGTON OUT OF LAKE TABLE
WHERE LAKE_ID = 1
AND LOCATION_NAME = 'PENNINGTON'

-----------------------------------------------
COMMIT;
-----------------------------------------------
--UNSUCCESSFUL INSERTS
-----------------------------------------------
INSERT INTO DGR_FLIES
(SPECIES_ID, FISH_NAME, LAKE_ID, FLY_USED, FISH_LENGTH, LINE_WEIGHT)-----MISSING SELECT WORD
(1, 'SHARK', 1, 'STONE', 18, 4);
-----------------------------------------------
--UNSUCCESSFUL DELETES
-----------------------------------------------
DELETE FROM DGR_FISH
WHERE FISH_ID = 12;
----------------------------------------------
-----I HOPE FOR ALL THAT IS HOLY THAT THIS IS EVEN REMOTELY CLOSE TO WHAT YOU'RE LOOKING FOR!!!!!!!!!!!












































































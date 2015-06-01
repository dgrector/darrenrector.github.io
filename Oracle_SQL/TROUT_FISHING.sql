--------------------------------------------------
--Name : Darren Rector
--
--Purpose: This script creates a set of objects
--         that will be used to store information
--         about my fishing trips
--------------------------------------------------
--Darren goes fishing on various mine pits stocked
--with different trout species and he goes fishing with 
--different flies at different times of the day.
--
--
--Trout are caught using one or more different flies
--Flies can catch one or more different fish


DROP TABLE DGR_FISH            CASCADE CONSTRAINTS PURGE;
DROP TABLE DGR_FLIES           CASCADE CONSTRAINTS PURGE;
DROP TABLE DGR_LAKE            CASCADE CONSTRAINTS PURGE;



CREATE TABLE DGR_FISH
 (
    SPECIES_ID     NUMBER   (10),
    FISH_NAME      VARCHAR2 (30)  NOT NULL,
    LAKE_ID        NUMBER   (10)  NOT NULL,
    FLY_USED       VARCHAR2 (30)  NOT NULL,
    FISH_LENGTH    NUMBER   (3)   NOT NULL,      
    LINE_WEIGHT    NUMBER   (3,2) NOT NULL,
    CONSTRAINT     DGR_FISH_PK
     PRIMARY KEY (SPECIES_ID)
 );
 
----------------------------------------------
 
CREATE TABLE DGR_FLIES
(
    FLY_ID         NUMBER   (10)   NOT NULL,
    FLY_NAME       VARCHAR2 (30)   NOT NULL,
    FLY_SIZE       NUMBER   (4)    NOT NULL,    
    FLY_TYPE       VARCHAR2 (30)   NOT NULL,  
    FISH_NAME	   VARCHAR2 (50)   NOT NULL,
    SPECIES_ID     NUMBER   (10)   NOT NULL,
    CONSTRAINT    DGR_FLIES_PK
        PRIMARY KEY (FLY_ID)
);

----------------------------------------------

CREATE TABLE DGR_LAKE
(
    LAKE_ID        NUMBER   (10)   NOT NULL,
    LOCATION_NAME  VARCHAR2 (30)   NOT NULL,
    FISH_NAME      VARCHAR2 (50)   NOT NULL,
    MONTH          VARCHAR2 (10)   NOT NULL,
    LOC_TIME       VARCHAR2 (30)   NOT NULL,
    CONSTRAINT    DGR_LAKE_ID_PK
        PRIMARY KEY (LAKE_ID)
);

----------------------------------------------
--Foreign Keys
----------------------------------------------
ALTER TABLE DGR_FISH
ADD CONSTRAINTS DGR_FISH_FK
FOREIGN KEY (LAKE_ID)
REFERENCES DGR_LAKE (LAKE_ID);

----------------------------------------------
ALTER TABLE DGR_FLIES
ADD CONSTRAINTS DGR_FLIES_FK
FOREIGN KEY (SPECIES_ID)
REFERENCES  DGR_FISH (SPECIES_ID);

----------------------------------------------
--Business Logic
----------------------------------------------
--Unique Constraint
----------------------------------------------

ALTER TABLE DGR_FLIES --FLY NAMES MUST BE UNIQUE
ADD CONSTRAINT DGR_FLIES_U
UNIQUE (FLY_NAME);

----------------------------------------------
--Check Constraint
----------------------------------------------

ALTER TABLE DGR_FISH --FISH NAME MUST BE ONE OF THE LISTED NAMES
ADD CONSTRAINT DGR_FISH_CK
CHECK (FISH_NAME IN ('BROWN', 'RAINBOW', 'NORTHERN', 'WALLEYE', 'CRAPPIE', 'BASS'))

----------------------------------------------
CREATE OR REPLACE VIEW fish_view AS
   SELECT      f.species_id, f.fish_name, l.lake_id
   FROM     dgr_fish f, dgr_lake l, dgr_flies fl
   WHERE    f.lake_id = l.lake_id
   AND      fl.species_id = f.species_id;
----------------------------------------------


















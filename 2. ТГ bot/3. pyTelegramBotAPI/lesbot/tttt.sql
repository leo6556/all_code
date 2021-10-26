BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"id"	INTEGER NOT NULL UNIQUE,
	"file_id"	TEXT NOT NULL,
	"right_answ"	TEXT NOT NULL,
	"wrong"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "music" VALUES (1,'AwACAgIAAxkDAAMhYSBXiRnBs5b4-ESfnRgAARe06YzBAAImDwAC4_QJScCzYfscuBbUIAQ','toto - to','popo - po, lolo - lo, gogo - go');
INSERT INTO "music" VALUES (2,'AwACAgIAAxkDAAMjYSBXir4GsZXZhdhfNZULBHEqPikAAicPAALj9AlJJDoorIAdDbcgBA','popo - po','toto - to, lolo - lo, gogo - go');
INSERT INTO "music" VALUES (3,'AwACAgIAAxkDAAMlYSBXjM_Nonwhvpxtwi65Rlx84aYAAigPAALj9AlJ1W3uLtMutLQgBA','ruru - ru','toto - to, lolo - lo, gogo - go');
COMMIT;

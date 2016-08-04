CREATE TABLE pitching (playerID TEXT, yearID INTEGER, stint INTEGER, teamID TEXT, lgID TEXT, w INTEGER, l INTEGER, g INTEGER,
gs INTEGER, cg INTEGER, sho INTEGER, sv INTEGER, ipouts INTEGER, h INTEGER, er INTEGER, hr INTEGER, bb INTEGER, so INTEGER,
baopp INTEGER, era INTEGER, ibb INTEGER, wp INTEGER, hbp INTEGER, bk INTEGER, bfp INTEGER, gf INTEGER, r INTEGER, sh INTEGER, sf INTEGER,
g_idp INTEGER);
.separator ","
.import pitching.csv pitching

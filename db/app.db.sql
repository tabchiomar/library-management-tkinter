BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"rank"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Exemplaire" (
	"idExemplaire"	INTEGER NOT NULL UNIQUE,
	"idlivre"	INTEGER,
	"disponibilite"	INTEGER,
	FOREIGN KEY("idlivre") REFERENCES "LIVRE"("idlivre"),
	PRIMARY KEY("idExemplaire")
);
CREATE TABLE IF NOT EXISTS "ADHERENT" (
	"idadherent"	INTEGER NOT NULL UNIQUE,
	"CIN"	TEXT NOT NULL,
	"nom"	TEXT NOT NULL,
	"datead"	TEXT,
	"prenom"	TEXT NOT NULL,
	"email"	TEXT,
	"datenaissance"	TEXT,
	"iduser"	TEXT NOT NULL,
	FOREIGN KEY("iduser") REFERENCES "Users"("id"),
	PRIMARY KEY("idadherent" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Biblio" (
	"idbiblio"	INTEGER NOT NULL UNIQUE,
	"CIN"	TEXT NOT NULL,
	"nom"	TEXT NOT NULL,
	"daterecr"	TEXT,
	"prenom"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"datenaissance"	TEXT,
	"iduser"	TEXT NOT NULL,
	PRIMARY KEY("idbiblio" AUTOINCREMENT),
	FOREIGN KEY("iduser") REFERENCES "Users"("id")
);
CREATE TABLE IF NOT EXISTS "Admin" (
	"idadmin"	INTEGER NOT NULL UNIQUE,
	"iduser"	TEXT NOT NULL,
	"nom"	TEXT NOT NULL,
	"prenom"	TEXT NOT NULL,
	PRIMARY KEY("idadmin" AUTOINCREMENT),
	FOREIGN KEY("iduser") REFERENCES "Users"("id")
);
CREATE TABLE IF NOT EXISTS "Livre" (
	"idlivre"	INTEGER NOT NULL UNIQUE,
	"titre"	TEXT NOT NULL,
	"categorie"	TEXT,
	"auteur"	TEXT NOT NULL,
	"description"	TEXT,
	"annee_pub"	INTEGER,
	"rayon"	TEXT,
	PRIMARY KEY("idlivre" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pret" (
	"idpret"	INTEGER NOT NULL UNIQUE,
	"idadherent"	INTEGER NOT NULL,
	"idbiblio"	INTEGER NOT NULL,
	"idlivre"	INTEGER NOT NULL,
	"datepret"	TEXT NOT NULL,
	"dateretour"	TEXT NOT NULL,
	"dateretoureffectif"	TEXT,
	"etat"	INTEGER,
	PRIMARY KEY("idpret" AUTOINCREMENT),
	FOREIGN KEY("idbiblio") REFERENCES "Biblio"("idbiblio"),
	FOREIGN KEY("idadherent") REFERENCES "ADHERENT"("idadherent"),
	FOREIGN KEY("idlivre") REFERENCES "Livre"("idlivre")
);
CREATE TABLE IF NOT EXISTS "contact" (
	"id"	INTEGER NOT NULL UNIQUE,
	"Etat"	INTEGER,
	"username"	TEXT,
	"contact"	TEXT,
	"sujet"	TEXT,
	"datecontacat"	TEXT,
	"datecharge"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sanction" (
	"idsanction"	INTEGER NOT NULL UNIQUE,
	"iduser"	INTEGER UNIQUE,
	"av1"	TEXT,
	"av2"	TEXT,
	"av3"	TEXT,
	PRIMARY KEY("idsanction" AUTOINCREMENT),
	FOREIGN KEY("iduser") REFERENCES "Users"("id")
);
INSERT INTO "Users" VALUES (0,'admin','admin','admin');
INSERT INTO "Users" VALUES (1,'aaa','aaa','aaa');
INSERT INTO "Users" VALUES (2,'omar','omar','bibliothecaire');
INSERT INTO "Users" VALUES (15,'adherent','123','Adherent');
INSERT INTO "Users" VALUES (16,'uhi','hiu','Adherent');
INSERT INTO "Users" VALUES (17,'uhigfd','hiu','Adherent');
INSERT INTO "Users" VALUES (24,'u','hu','Adherent');
INSERT INTO "Users" VALUES (25,'jioj','mj','Adherent');
INSERT INTO "Users" VALUES (26,'jio','mj','Adherent');
INSERT INTO "Users" VALUES (27,'gfdgfdgfdg','gfdgfd','Adherent');
INSERT INTO "Users" VALUES (32,'mehdi','mehdi','Adherent');
INSERT INTO "Exemplaire" VALUES (1,5,1);
INSERT INTO "Exemplaire" VALUES (4,2,1);
INSERT INTO "Exemplaire" VALUES (5,2,1);
INSERT INTO "Exemplaire" VALUES (6,2,1);
INSERT INTO "Exemplaire" VALUES (8,2,1);
INSERT INTO "Exemplaire" VALUES (9,2,1);
INSERT INTO "Exemplaire" VALUES (10,1,1);
INSERT INTO "Exemplaire" VALUES (11,1,1);
INSERT INTO "Exemplaire" VALUES (12,1,1);
INSERT INTO "Exemplaire" VALUES (13,1,1);
INSERT INTO "Exemplaire" VALUES (14,2,1);
INSERT INTO "Exemplaire" VALUES (15,2,1);
INSERT INTO "Exemplaire" VALUES (16,2,1);
INSERT INTO "Exemplaire" VALUES (17,2,1);
INSERT INTO "Exemplaire" VALUES (22,4,1);
INSERT INTO "Exemplaire" VALUES (23,4,1);
INSERT INTO "Exemplaire" VALUES (24,4,1);
INSERT INTO "Exemplaire" VALUES (25,4,1);
INSERT INTO "Exemplaire" VALUES (26,5,1);
INSERT INTO "Exemplaire" VALUES (27,5,1);
INSERT INTO "Exemplaire" VALUES (28,5,1);
INSERT INTO "Exemplaire" VALUES (29,5,1);
INSERT INTO "Exemplaire" VALUES (30,6,1);
INSERT INTO "Exemplaire" VALUES (31,6,1);
INSERT INTO "Exemplaire" VALUES (32,6,1);
INSERT INTO "Exemplaire" VALUES (33,6,1);
INSERT INTO "Exemplaire" VALUES (38,8,1);
INSERT INTO "Exemplaire" VALUES (39,8,1);
INSERT INTO "Exemplaire" VALUES (40,8,1);
INSERT INTO "Exemplaire" VALUES (41,8,1);
INSERT INTO "Exemplaire" VALUES (42,9,1);
INSERT INTO "Exemplaire" VALUES (43,9,1);
INSERT INTO "Exemplaire" VALUES (44,9,1);
INSERT INTO "Exemplaire" VALUES (45,9,1);
INSERT INTO "Exemplaire" VALUES (50,11,1);
INSERT INTO "Exemplaire" VALUES (51,11,1);
INSERT INTO "Exemplaire" VALUES (52,11,1);
INSERT INTO "Exemplaire" VALUES (53,11,1);
INSERT INTO "Exemplaire" VALUES (90,1,1);
INSERT INTO "Exemplaire" VALUES (91,1,1);
INSERT INTO "Exemplaire" VALUES (92,1,1);
INSERT INTO "Exemplaire" VALUES (93,1,1);
INSERT INTO "Exemplaire" VALUES (94,2,1);
INSERT INTO "Exemplaire" VALUES (95,2,1);
INSERT INTO "Exemplaire" VALUES (96,2,1);
INSERT INTO "Exemplaire" VALUES (97,2,1);
INSERT INTO "Exemplaire" VALUES (102,4,1);
INSERT INTO "Exemplaire" VALUES (103,4,1);
INSERT INTO "Exemplaire" VALUES (104,4,1);
INSERT INTO "Exemplaire" VALUES (105,4,1);
INSERT INTO "Exemplaire" VALUES (106,5,1);
INSERT INTO "Exemplaire" VALUES (107,5,1);
INSERT INTO "Exemplaire" VALUES (108,5,1);
INSERT INTO "Exemplaire" VALUES (109,5,1);
INSERT INTO "Exemplaire" VALUES (110,6,1);
INSERT INTO "Exemplaire" VALUES (111,6,1);
INSERT INTO "Exemplaire" VALUES (112,6,1);
INSERT INTO "Exemplaire" VALUES (113,6,1);
INSERT INTO "Exemplaire" VALUES (118,8,1);
INSERT INTO "Exemplaire" VALUES (119,8,1);
INSERT INTO "Exemplaire" VALUES (120,8,1);
INSERT INTO "Exemplaire" VALUES (121,8,1);
INSERT INTO "Exemplaire" VALUES (122,9,1);
INSERT INTO "Exemplaire" VALUES (123,9,1);
INSERT INTO "Exemplaire" VALUES (124,9,1);
INSERT INTO "Exemplaire" VALUES (125,9,1);
INSERT INTO "Exemplaire" VALUES (130,11,1);
INSERT INTO "Exemplaire" VALUES (131,11,1);
INSERT INTO "Exemplaire" VALUES (132,11,1);
INSERT INTO "Exemplaire" VALUES (133,11,1);
INSERT INTO "Exemplaire" VALUES (134,3,0);
INSERT INTO "Exemplaire" VALUES (135,3,1);
INSERT INTO "Exemplaire" VALUES (136,3,1);
INSERT INTO "Exemplaire" VALUES (137,3,1);
INSERT INTO "Exemplaire" VALUES (138,3,0);
INSERT INTO "Exemplaire" VALUES (139,3,0);
INSERT INTO "Exemplaire" VALUES (140,3,1);
INSERT INTO "Exemplaire" VALUES (141,3,1);
INSERT INTO "Exemplaire" VALUES (142,3,1);
INSERT INTO "Exemplaire" VALUES (143,3,1);
INSERT INTO "Exemplaire" VALUES (144,3,1);
INSERT INTO "Exemplaire" VALUES (145,3,1);
INSERT INTO "Exemplaire" VALUES (146,3,1);
INSERT INTO "Exemplaire" VALUES (147,3,1);
INSERT INTO "Exemplaire" VALUES (148,3,1);
INSERT INTO "Exemplaire" VALUES (149,3,1);
INSERT INTO "Exemplaire" VALUES (150,3,1);
INSERT INTO "Exemplaire" VALUES (151,3,1);
INSERT INTO "Exemplaire" VALUES (152,3,1);
INSERT INTO "Exemplaire" VALUES (153,3,1);
INSERT INTO "Exemplaire" VALUES (154,3,1);
INSERT INTO "Exemplaire" VALUES (155,3,1);
INSERT INTO "ADHERENT" VALUES (12,'omar','omar','31/05/2023','omar','omar','omar','15');
INSERT INTO "ADHERENT" VALUES (13,'ih','gfd','31/05/2023','huh','ih','hiu','16');
INSERT INTO "ADHERENT" VALUES (14,'ih','gfd','31/05/2023','huh','ih','hiu','17');
INSERT INTO "ADHERENT" VALUES (21,'h','fgfdga','02/06/2023','gfdh','uh','uh','24');
INSERT INTO "ADHERENT" VALUES (22,'jiji','jii','02/06/2023','ji','oiji','ojm','25');
INSERT INTO "ADHERENT" VALUES (23,'jiji','jii','02/06/2023','ji','oiji','ojm','26');
INSERT INTO "ADHERENT" VALUES (24,'gfd','dfgfd','02/06/2023','gfd','gfd','gfd','27');
INSERT INTO "ADHERENT" VALUES (25,'gfd','fdgfdg','02/06/2023','gfd','gfd','gfd','28');
INSERT INTO "ADHERENT" VALUES (26,'omar','omaaar','02/02/2023','omar','omar','omar','30');
INSERT INTO "ADHERENT" VALUES (27,'gfdijiu','omar','02/06/2023','omar','huuhu','uhi','31');
INSERT INTO "ADHERENT" VALUES (28,'mehdi','mehdi','02/01/2023','mehdi','mehdi','mehdi','32');
INSERT INTO "Biblio" VALUES (1,'A','gfdg','15/11/2002','gfdgfd','gfdgfd@gmail.com','gfddgf','2');
INSERT INTO "Admin" VALUES (1,'0','OMAR','TABCHI');
INSERT INTO "Livre" VALUES (2,'Harry Potter à l’école des sorciers','Fantasy','J.K. Rowling','La découverte du monde des sorciers',1997,'1');
INSERT INTO "Livre" VALUES (3,'1984','Science-fiction','George Orwel','Un roman dystopique



',1949,'1');
INSERT INTO "Livre" VALUES (4,'Le Seigneur des anneaux','Fantasy','J.R.R. Tolkien','Une épopée fantastique',1954,'1');
INSERT INTO "Livre" VALUES (5,'Orgueil et Préjugés','Romance','Jane Austen','Une histoire d''amour classique',1813,'1');
INSERT INTO "Livre" VALUES (8,'Cien años de soledad','FictionK','Gabriel García Márquez','Un chef-d''œuvre de la littérature latino-américaine
',1967,'1');
INSERT INTO "Livre" VALUES (11,'Le Nom de la Rose','Mystère','Umberto Eco','Un roman historique captivant',1980,'1');
INSERT INTO "pret" VALUES (1,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (2,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (3,5,2,1,'30/05/2023','14/06/2023',NULL,1);
INSERT INTO "pret" VALUES (4,5,2,1,'30/05/2023','14/06/2023',NULL,1);
INSERT INTO "pret" VALUES (5,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (6,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (7,5,2,3,'30/05/2023','14/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (8,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (9,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (10,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (11,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (12,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (13,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (14,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (15,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (16,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (17,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (18,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (19,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (20,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (21,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (22,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (23,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (24,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (25,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (26,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (27,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (28,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (29,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (30,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (31,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (32,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (33,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (34,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (35,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (36,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (37,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (38,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (39,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (40,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (41,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (42,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (43,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (44,5,2,1,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (45,5,2,3,'30/05/2023','14/06/2023','30/05/2023',1);
INSERT INTO "pret" VALUES (46,5,2,1,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (47,15,2,3,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (48,15,2,3,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (49,15,2,3,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (50,15,2,3,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (51,15,2,3,'31/05/2023','15/06/2023','31/05/2023',1);
INSERT INTO "pret" VALUES (52,15,2,3,'02/06/2023','17/06/2023','02/06/2023',1);
INSERT INTO "pret" VALUES (53,15,2,3,'02/06/2023','17/06/2023','02/06/2023',1);
INSERT INTO "pret" VALUES (54,15,2,3,'01/06/2023','02/06/2023','03/06/2023',1);
INSERT INTO "pret" VALUES (55,32,2,3,'01/06/2023','02/06/2023','03/06/2023',1);
INSERT INTO "pret" VALUES (56,15,0,3,'03/06/2023','18/06/2023','03/06/2023',1);
INSERT INTO "pret" VALUES (57,15,0,3,'03/06/2023','18/06/2023','03/06/2023',1);
INSERT INTO "pret" VALUES (58,15,2,3,'03/06/2023','18/06/2023',NULL,0);
INSERT INTO "contact" VALUES (1,1,'wiiiw','wiwwiwi','waaw','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (2,1,'omarrr','gfgd','gfdg','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (3,1,'hjghjjh','jhgjhg','jhgjhgj','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (4,1,'ghhgfa²','gfd','fgdg','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (5,1,'ghhgfa²','gfd','fgdg','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (6,1,'ghhgfa²','gfd','fgdg','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (7,1,'ghhgfa²','gfd','fgdg','31/05/2023','31/05/2023');
INSERT INTO "contact" VALUES (8,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (9,1,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','31/05/2023');
INSERT INTO "contact" VALUES (10,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (11,1,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','31/05/2023');
INSERT INTO "contact" VALUES (12,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (13,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (14,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (15,1,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','31/05/2023');
INSERT INTO "contact" VALUES (16,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (17,1,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','31/05/2023');
INSERT INTO "contact" VALUES (18,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (19,1,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','31/05/2023');
INSERT INTO "contact" VALUES (20,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (21,1,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','31/05/2023');
INSERT INTO "contact" VALUES (22,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (23,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (24,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (25,1,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','31/05/2023');
INSERT INTO "contact" VALUES (26,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (27,1,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','31/05/2023');
INSERT INTO "contact" VALUES (28,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (29,1,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','31/05/2023');
INSERT INTO "contact" VALUES (30,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (31,1,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','31/05/2023');
INSERT INTO "contact" VALUES (32,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (33,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (34,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (35,1,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','31/05/2023');
INSERT INTO "contact" VALUES (36,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (37,1,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','31/05/2023');
INSERT INTO "contact" VALUES (38,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (39,1,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','31/05/2023');
INSERT INTO "contact" VALUES (40,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (41,1,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','31/05/2023');
INSERT INTO "contact" VALUES (42,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (43,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (44,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (45,1,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','31/05/2023');
INSERT INTO "contact" VALUES (46,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (47,1,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','31/05/2023');
INSERT INTO "contact" VALUES (48,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (49,1,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','31/05/2023');
INSERT INTO "contact" VALUES (50,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (51,1,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','31/05/2023');
INSERT INTO "contact" VALUES (52,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (53,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (54,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (55,1,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','31/05/2023');
INSERT INTO "contact" VALUES (56,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (57,1,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','23/06/2023');
INSERT INTO "contact" VALUES (58,1,'JohnDoe','johndoe@example.com','Question','2023-05-01','2023-05-02');
INSERT INTO "contact" VALUES (59,0,'JaneSmith','janesmith@example.com','Problème technique','2023-05-03','2023-05-04');
INSERT INTO "contact" VALUES (60,1,'MikeJohnson','mikejohnson@example.com','Demande d''assistance','2023-05-05','2023-05-06');
INSERT INTO "contact" VALUES (61,0,'EmilyBrown','emilybrown@example.com','Réclamation','2023-05-07','2023-05-08');
INSERT INTO "contact" VALUES (62,1,'DavidWilson','davidwilson@example.com','Demande d''information','2023-05-09','2023-05-10');
INSERT INTO "contact" VALUES (63,1,'SarahDavis','sarahdavis@example.com','Problème de livraison','2023-05-11','31/05/2023');
INSERT INTO "contact" VALUES (64,1,'MichaelSmith','michaelsmith@example.com','Demande de remboursement','2023-05-13','2023-05-14');
INSERT INTO "contact" VALUES (65,0,'JenniferJohnson','jenniferjohnson@example.com','Problème de connexion','2023-05-15','2023-05-16');
INSERT INTO "contact" VALUES (66,1,'ChristopherBrown','christopherbrown@example.com','Demande de devis','2023-05-17','2023-05-18');
INSERT INTO "contact" VALUES (67,0,'JessicaWilson','jessicawilson@example.com','Problème de facturation','2023-05-19','2023-05-20');
INSERT INTO "sanction" VALUES (1,16,'0','0','0');
INSERT INTO "sanction" VALUES (2,27,'0','0','0');
INSERT INTO "sanction" VALUES (6,32,'0','0','0');
COMMIT;

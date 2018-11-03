INSERT INTO leagues (name) VALUES ('NBA'), ('NHL');
INSERT INTO teams (name, league_id) VALUES ('lakers', 1),
                                      ('New York Knicks', 1),
                                      ('New York Rangers', 2),
                                      ('canucks', 2);
INSERT INTO players (name, team_id) VALUES ('player1', 1),
                                      ('playerr2', 2),
                                      ('playerrr3', 3),
                                      ('playerrrr4', 4);
INSERT INTO games (date, location) VALUES ('2018-11-02', 'NYC'),
                                          ('2018-11-03', 'BOS'),
                                          ('2018-11-04', 'SFO');
INSERT INTO team_games (team_id, game_id, score) VALUES (1, 1, 4),
                                                        (2, 1, 3),
                                                        (3, 2, 4),
                                                        (4, 2, 5),
                                                        (1, 3, 2),
                                                        (4, 3, 3);

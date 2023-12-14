-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users ADD total_weighted_score INT NOT NULL;
    ALTER TABLE users ADD total_weight INT NOT NULL;

    UPDATE users
    INNER JOIN (
        SELECT user_id, SUM(corrections.score * projects.weight) AS total_weighted_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        GROUP BY user_id
    ) AS weighted_scores ON users.id = weighted_scores.user_id
    SET users.total_weighted_score = weighted_scores.total_weighted_score;

    UPDATE users
    INNER JOIN (
        SELECT user_id, SUM(projects.weight) AS total_weight
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        GROUP BY user_id
    ) AS total_weights ON users.id = total_weights.user_id
    SET users.total_weight = total_weights.total_weight;

    UPDATE users
    SET average_score = IF(total_weight = 0, 0, total_weighted_score / total_weight);

    ALTER TABLE users DROP COLUMN total_weighted_score;
    ALTER TABLE users DROP COLUMN total_weight;
END $$
DELIMITER ;

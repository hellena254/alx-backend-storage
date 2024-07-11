-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
-- 101-average_weighted_score.sql
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;

    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the weighted average score for the current user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;

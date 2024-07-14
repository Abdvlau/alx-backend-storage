# 0x00. MySQL Advanced

## Description

This project focuses on advanced MySQL concepts including creating tables with constraints, optimizing queries using indexes, and implementing stored procedures, views, and triggers. The goal is to enhance database management and efficiency by leveraging these advanced features.

## Learning Objectives

By the end of this project, you should be able to:

- Create tables with constraints.
- Optimize queries by adding indexes.
- Implement stored procedures and functions in MySQL.
- Create and manage views in MySQL.
- Implement triggers in MySQL.

## Project Tasks

### Task 0: We are all unique!
- **File:** `0-uniq_users.sql`
- **Description:** Create a table `users` with unique constraints on the `email` field.

### Task 1: In and not out
- **File:** `1-country_users.sql`
- **Description:** Create a table `users` with an enumeration type for `country` field.

### Task 2: Best band ever!
- **File:** `2-fans.sql`
- **Description:** Rank country origins of bands by the number of (non-unique) fans.

### Task 3: Old school band
- **File:** `3-glam_rock.sql`
- **Description:** List bands with Glam rock as their main style, ranked by their longevity.

### Task 4: Buy buy buy
- **File:** `4-store.sql`
- **Description:** Create a trigger to decrease the quantity of an item after adding a new order.

### Task 5: Email validation to sent
- **File:** `5-valid_email.sql`
- **Description:** Create a trigger to reset the attribute `valid_email` only when the email has been changed.

### Task 6: Add bonus
- **File:** `6-bonus.sql`
- **Description:** Create a stored procedure `AddBonus` that adds a new correction for a student.

### Task 7: Average score
- **File:** `7-average_score.sql`
- **Description:** Create a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.

### Task 8: Optimize simple search
- **File:** `8-index.sql`
- **Description:** Create an index `idx_name_first` on the table `names` and the first letter of `name`.

## Usage

To execute the SQL scripts, follow these steps:

1. **Start MySQL Server:**
    ```bash
    $ service mysql start
    ```

2. **Run a script:**
    ```bash
    $ cat script.sql | mysql -uroot -p database_name
    ```

3. **Connect to MySQL:**
    ```bash
    $ mysql -uroot -p
    ```

4. **Run queries within MySQL:**
    ```sql
    mysql> SOURCE script.sql;
    ```

## Requirements

- MySQL 5.7 (version 5.7.30)
- Ubuntu 18.04 LTS



CREATE TABLE my_table (
    Age INT,
    Gender TEXT,
    City TEXT,
    Position TEXT,
    Years_worked FLOAT,
    Seniority TEXT,
    Technology TEXT,
    Salary FLOAT
    
);

COPY my_table FROM 'C:/Users/user/Desktop/Bootcamp/IT2020.csv' DELIMITER ',' CSV HEADER;



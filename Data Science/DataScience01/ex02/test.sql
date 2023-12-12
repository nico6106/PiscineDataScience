--create table tmp
CREATE TABLE cust_tmp (
    event_time timestamp NOT NULL,
    event_type VARCHAR(255),
    product_id int,
    price float,
    user_id bigint,
    user_session uuid)

--insert into tmp table
INSERT INTO cust_tmp (event_time, event_type, product_id, price, user_id, user_session)
SELECT T1.event_time, T1.event_type, T1.product_id, T1.price, T1.user_id, T1.user_session
FROM customers T1
WHERE EXISTS (
    SELECT 1
    FROM customers T2
    WHERE T1.event_type = T2.event_type
      AND T1.product_id = T2.product_id
      AND T1.price = T2.price
      AND T1.user_id = T2.user_id
      AND T1.user_session = T2.user_session
      AND ABS(EXTRACT(EPOCH FROM (T1.event_time - T2.event_time))) <= 60
      AND T1.event_time <> T2.event_time
);

--delete doublons
DELETE
FROM customers T1
WHERE  EXISTS (SELECT *
            FROM   customers T2
            WHERE  T1.event_type = T2.event_type
			AND T1.product_id = T2.product_id
			AND T1.price = T2.price
			AND T1.user_id = T2.user_id
			AND T1.user_session = T2.user_session
			AND ABS(EXTRACT(EPOCH FROM (T1.event_time - T2.event_time))) <= 60
            GROUP BY event_time, event_type, product_id, price, user_id, user_session
            HAVING COUNT(*) > 1)


--alter customers with new column 
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE customers
ADD COLUMN coluid UUID;

UPDATE customers
SET coluid = uuid_generate_v4();

--nb null
SELECT * FROM customers WHERE user_session IS NULL;

--delete
DELETE
FROM   customers T1
WHERE  T1.coluid < ANY
   (SELECT coluid
    FROM   customers T2
    WHERE  T1.coluid <> T2.coluid
    	AND  T1.event_type = T2.event_type
		AND T1.product_id = T2.product_id
		AND T1.price = T2.price
		AND T1.user_id = T2.user_id
		AND T1.user_session = T2.user_session
		AND ABS(EXTRACT(EPOCH FROM (T1.event_time - T2.event_time))) <= 60)

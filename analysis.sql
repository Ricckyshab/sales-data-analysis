
-- 1. Calculate total revenue
SELECT SUM(quantity * unit_price) AS total_revenue
FROM sales;

-- 2. Calculate revenue by product
SELECT
    product,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- 3. Calculate monthly revenue
SELECT
    SUBSTR(order_date, 1, 7) AS sales_month,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY sales_month;